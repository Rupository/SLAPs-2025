
#### Current Working Environment:

- IDE: VSCode
- Dafny Extension (for intellisense and other useful highlights)
- NuGet (Binary) installation of Dafny to access `dafny verify <filename>.dfy`
- Microsoft .NET framwork, added to path
- Z3 full installation, added to path
- z3-solver library added to python

```
PS C:\Users\Tintu\Documents\Obsidian\Notes\Academics\Ashoka\Semester 5\SLAPs\Code\SLAPs-2025> dafny verify test.dfy

Dafny program verifier finished with 1 verified, 0 errors
PS C:\Users\Tintu\Documents\Obsidian\Notes\Academics\Ashoka\Semester 5\SLAPs\Code\SLAPs-2025> dafny verify week1\examples\example1.dfy

Dafny program verifier finished with 2 verified, 0 errors
PS C:\Users\Tintu\Documents\Obsidian\Notes\Academics\Ashoka\Semester 5\SLAPs\Code\SLAPs-2025> dafny verify week1\examples\example2.dfy

Dafny program verifier finished with 3 verified, 0 errors
PS C:\Users\Tintu\Documents\Obsidian\Notes\Academics\Ashoka\Semester 5\SLAPs\Code\SLAPs-2025> dafny verify week1\examples\example3.dfy

Dafny program verifier finished with 3 verified, 0 errors
```

#### Issues encountered:

1. Accessing `dafny verify` through the command line as instructed in the setup:
	- This was (somewhat expectedly) not available through the Dafny extension, or the manual download.
	- Solution
		- Required installing the latest Microsoft .NET SDK release on my Windows system
			- This then needed to be added to the system PATH, which required restarting the system. Even when added to PATH, VSCode (and presumably applications other than Command Prompt and Powershell) would update their internal references to PATH only after a full restart.
		- After this, ran ` dotnet tool install --global dafny ` to install Dafny

2. Integrating Dafny and Z3:
	- Z3 is not bundled with Dafny when installing through Microsoft .NET, leading to an error on calling `dafny verify`
	- Solution
		- Required installing the latest Z3 release on my Windows system
			- This then needed to be added to the system PATH, which required restarting the system. Even when added to PATH, VSCode (and presumably applications other than Command Prompt and Powershell) would update their internal references to PATH only after a full restart.
		- After this, ran`dafny verify <filename>.dfy` without issue