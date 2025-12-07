
### How to replicate environment

- Install Java 25 from OpenJDK

- Install [ANTLR Tool (Java Target)](https://www.antlr.org/download.html) into `/installs`.

- Copy `dafny.g4` from the [dafny-antlr](https://github.com/fuzz-d/dafny-antlr) parsing library into `/installs`.

-  Edit the forLoop syntax in `dafny.g4` to include invariants:
    ```antlr
    forLoop: FOR identifier ':=' expression TO expression (verifierAnnotation)* '{' sequence '}';
    ```

- Create a directory for the python parser module we'll build (`dfyPyParse`) using ANTLR and run the following:
    ```bash
    java -jar installs/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener -o dfyPyParse installs/dafny.g4
    ```
    Add an `__init.py__` to configure the directory as a module.

- Install the ANTLR python package:
    ```bash
    pip install antlr4-python3-runtime
    ```

### How to run

- Run the following command:
    ```bash
    python parser.py <your_file>.dfy
    ```
    You may use more than one file