### Assumptions
- We assume there is only one method in a program file. By specifying an index, you can target your required method if there are more than one methods present in your file. We process only one method per file.
- Any conditional statements provided in the file must be in the form of inequalities on dafny integer/float variables.
- Variable updates must be linear in the set of variables.
- The file should not declare variables with names which happen to be existing python classes and constructs.
- You may add multiple files.
- ITEs should be formatted in a nested manner instead of shortening syntax.
- Make sure there is a line seperating the `while <condition>` declaration and the curly braces that begin the loop body. In other words, avoid the [K&R or Ratliff](https://en.wikipedia.org/wiki/Indentation_style) indentation styles.
- Make sure there are no internal brackets inside a condition.

### How to run
- Run the following command from the root directory:
    ```
    python -m week7.dafny_check [<path_to_file_1>.dfy <path_to_file_2>.dfy]... --[arguments]
    ```
- Arguments include:
    - `-d <int>` or `--degree <int>` for the degree of the invariant inequality polynomial, defaults to 2.
    - `-m <int>` or `--method <int>` for the index of the method to check for, defaults to 0 (first method in the program).
    - `-r` or `--real` to assume real numbers (floats) instead of integers.
    - `-c` or `--combos` to take combinations of the parameter variables(s) as terms of the invariant polynomial
    - `-t <float>` or `--threshold <float>` to specify the similarity of synthesised invariant. To avoid redundancy, make sure it's between 0 and 1.

