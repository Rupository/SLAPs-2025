### Assumptions
- We assume there is only one method in a program file. By specifying an index, you can target your required method if there are more than one methods present in your file. We process only one method per file.
- Any conditional statements provided in the file must be in the for of inequalities of dafny integer/float variables.
- Variable updates must be linear in the set of variables.
- The file should not declare variables with names which happen to be existing python classes and constructs.

### How to run
- Run the following command from the root directory:
    ```bash
    python -m week6.invariant_synthesis <path_to_your_file>.dfy --[arguments]
    ```
- Arguments include:
    - `-d <int>` or `--degree <int>` for the degree of the invariant inequality polynomial, defaults to 2.
    - `-m <int>` or `--method <int>` for the index of the method to check for, defaults to 0 (first method in the program).
    - `-r` or `--real` to assume real numbers (floats) instead of integers.
    - `-c` or `--combos` to take combinations of the parameter variables(s) as terms of the invariant polynomial
    - `-t <float>` or `--threshold <float>` to specify the similarity of synthesised invariant. To avoid redundancy, make sure it's between 0 and 1.

