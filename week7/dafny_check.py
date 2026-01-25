import os
import subprocess
import sys
import argparse
import time
from week6 import invariant_synthesis

def get_file_info(filename:str, method_id = 0):
    params, preconditions, loops = invariant_synthesis.load_data(filename, method_id)
    insertion_pts = [loop.get('insertion_pt') for loop in loops]
    return params, preconditions, loops, insertion_pts

def get_path_invariant_string(path_guards, invariant_strs):
    hypothesis = ''
    if path_guards != []:
        hypothesis = path_guards
    else:
        hypothesis = 'true'
    
    path_inv_str = f'invariant {hypothesis} ==>'

    counter = len(invariant_strs) 
    for inv_str in invariant_strs:
        path_inv_str += f" {inv_str}"
        counter -= 1
        if counter > 0:
            path_inv_str += " &&"
        else:
            pass

    return path_inv_str

def write_to_file(filename: str, path_inv_str, insertion_pt):
    if not path_inv_str:
        return
    
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        id = int(insertion_pt) - 1

        if 0 <= id < len(lines):
            current_line = lines[id].rstrip()
            lines[id] = f"{current_line} {path_inv_str}\n"

            with open(filename, "w") as f:
                f.writelines(lines)

    except Exception as e:
        print(f"Error writing to file: {e}")

def process_all(filename:str, params, preconditions, loops, insertion_pts, degree, assume_int = True, method_id = 0):
    start_time = time.time()
    loop_count = 0
    for loop in loops:
        insertion_pt = insertion_pts[loop_count]
        print(f"> Analyzing Loop {loop_count}...")
        loop_conditions = loop.get("conditions")
        paths = loop.get('paths')
        path_count = 0
        for loop_path in paths:
            print(f"\t>> Analyzing Path {path_count}...")
            print()
            path_guards = loop_path.get('guards')
            vars_sym, vars_init, vars_trans = invariant_synthesis.parse_vars(loop_path)
            path_setup = invariant_synthesis.constraints_and_setup(vars_sym, 
                                             vars_init, 
                                             vars_trans, 
                                             params, 
                                             preconditions,
                                             loop_conditions,
                                             path_guards,
                                             degree,
                                             assume_int)
            found_floats = invariant_synthesis.solve(*path_setup)
            invariant_strs = invariant_synthesis.analyze_invariants(found_floats, preconditions, loop_conditions, loop_path,
                               vars_sym, vars_init, vars_trans, params, assume_int)
            
            path_inv_str = get_path_invariant_string(path_guards, invariant_strs)
            write_to_file(filename, path_inv_str, insertion_pt)

            path_count += 1
            print()
        
        loop_count += 1
        print()
    
    end_time = time.time()
    print(f"> Finished in {format(end_time - start_time, '.2f')}s")
    print()

def run_verification(filename):
    print()
    print(f"> Running Dafny Verification...")

    try:
        subprocess.run(["dafny", "verify", filename])
    except FileNotFoundError:
        print("Error: 'dafny' executable not found in PATH.")
    except Exception as e:
        print(f"An error occurred while running dafny: {e}")

def main():
    # [AI DISCLOSURE] Commandline boilerplate
    parser = argparse.ArgumentParser(description="Dafny Invariant Checker & Injector")
    parser.add_argument("files", nargs='+', help="Path to the .dfy file(s)")
    parser.add_argument("-d", "--degree", type=int, default=2, help="Polynomial degree (default: 2)")
    parser.add_argument("-m", "--method", type=int, default=0, help="Method to analyze (default: 0th)")
    parser.add_argument("--assume_real", action="store_true", help="Assume real variables instead of integers")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    assume_int = not args.assume_real

    for filename in args.files:
        print(f"> Processing File: {filename}")
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            continue

        try:
            params, preconditions, loops, insertion_pts = get_file_info(filename, method_id=args.method)
            process_all(
                filename, 
                params, 
                preconditions, 
                loops, 
                insertion_pts, 
                degree=args.degree, 
                assume_int=assume_int, 
                method_id=args.method
            )
            
            run_verification(filename)
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()