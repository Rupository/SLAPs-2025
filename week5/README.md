- Install Java 25 from OpenJDK

- Install [ANTLR Tool (Java Target)](https://www.antlr.org/download.html)

- Copy `dafny.g4` from the [dafny-antlr](https://github.com/fuzz-d/dafny-antlr) parsing library.

- Create a directory for the python parser "library" we'll build ('dfyPyParse') using ANTLR and run the following inside it:
    ```powershell
    dfyPyParse> java -jar ..\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener ..\dafny.g4
    ```