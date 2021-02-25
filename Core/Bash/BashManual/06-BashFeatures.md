- [6 Bash Features](#6-bash-features)
  - [6.1 Invoking Bash](#61-invoking-bash)
  - [6.2 Bash Startup Files](#62-bash-startup-files)
    - [Invoked as an interactive login shell, or with --login](#invoked-as-an-interactive-login-shell-or-with---login)
  - [Invoked as an interactive non-login shell](#invoked-as-an-interactive-non-login-shell)
    - [Invoked non-interactively](#invoked-non-interactively)
    - [Invoked with name sh](#invoked-with-name-sh)
    - [Invoked in POSIX mode](#invoked-in-posix-mode)
    - [Invoked by remote shell daemon](#invoked-by-remote-shell-daemon)
    - [Invoked with unequal effective and real UID/GIDs](#invoked-with-unequal-effective-and-real-uidgids)
  - [6.3 Interactive Shells](#63-interactive-shells)
    - [6.3.1 What is an Interactive Shell?](#631-what-is-an-interactive-shell)
    - [6.3.2 Is this Shell Interactive?](#632-is-this-shell-interactive)
    - [6.3.3 Interactive Shell Behavior](#633-interactive-shell-behavior)
  - [6.4 Bash Conditional Expressions](#64-bash-conditional-expressions)
    - [-a file](#-a-file)
    - [-b file](#-b-file)
    - [-c file](#-c-file)
    - [-d file](#-d-file)
    - [-e file](#-e-file)
    - [-f file](#-f-file)
    - [-g file](#-g-file)
    - [-h file](#-h-file)
    - [-k file](#-k-file)
    - [-p file](#-p-file)
    - [-r file](#-r-file)
    - [-s file](#-s-file)
    - [-t fd](#-t-fd)
    - [-u file](#-u-file)
    - [-w file](#-w-file)
    - [-x file](#-x-file)
    - [-G file](#-g-file-1)
    - [-L file](#-l-file)
    - [-N file](#-n-file)
    - [-O file](#-o-file)
    - [-S file](#-s-file-1)
    - [file1 -ef file2](#file1--ef-file2)
    - [file1 -nt file2](#file1--nt-file2)
    - [file1 -ot file2](#file1--ot-file2)
    - [-o optname](#-o-optname)
    - [-v varname](#-v-varname)
    - [-R varname](#-r-varname)
    - [-z string](#-z-string)
    - [-n string](#-n-string)
    - [string](#string)
    - [string1 == string2](#string1--string2)
    - [string1 = string2](#string1--string2-1)
    - [string1 != string2](#string1--string2-2)
    - [string1 < string2](#string1--string2-3)
    - [string1 > string2](#string1--string2-4)
    - [arg1 OP arg2](#arg1-op-arg2)
  - [6.5 Shell Arithmetic](#65-shell-arithmetic)
  - [6.6 Aliases](#66-aliases)
  - [6.7 Arrays](#67-arrays)
    - [Indexed Array vs Associative Array](#indexed-array-vs-associative-array)
      - [Creating numerically indexed arrays](#creating-numerically-indexed-arrays)
      - [Creating associative arrays](#creating-associative-arrays)
    - [Array Operations](#array-operations)
      - [Reference Elements](#reference-elements)
  - [6.8 The Directory Stack](#68-the-directory-stack)
    - [dirs](#dirs)
    - [popd](#popd)
    - [pushd](#pushd)
  - [6.9 Controlling the Prompt](#69-controlling-the-prompt)
  - [6.10 The Restricted Shell](#610-the-restricted-shell)
  - [6.11 Bash POSIX Mode](#611-bash-posix-mode)
  - [6.12 Shell Compatibility Mode](#612-shell-compatibility-mode)


# 6 Bash Features

## 6.1 Invoking Bash

```
bash [long-opt] [-ir] [-abefhkmnptuvxdBCDHP] [-o option]
    [-O shopt_option] [argument …]
bash [long-opt] [-abefhkmnptuvxdBCDHP] [-o option]
    [-O shopt_option] -c string [argument …]
bash [long-opt] -s [-abefhkmnptuvxdBCDHP] [-o option]
    [-O shopt_option] [argument …]
```

All of the single-character options used with the `set` builtin can be used as options when the shell is invoked. In addition, there are several multi-character options that you can use. These options must appear on the command line before the single-character options to be recognized.

--debugger
Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see The Shopt Builtin for a description of the extdebug option to the shopt builtin).

--dump-po-strings
A list of all double-quoted strings preceded by ‘$’ is printed on the standard output in the GNU gettext PO (portable object) file format. Equivalent to -D except for the output format.

--dump-strings
Equivalent to -D.

--help
Display a usage message on standard output and exit successfully.

--init-file filename
--rcfile filename
Execute commands from filename (instead of ~/.bashrc) in an interactive shell.

--login
Equivalent to -l.

--noediting
Do not use the GNU Readline library (see Command Line Editing) to read command lines when the shell is interactive.

--noprofile
Don’t load the system-wide startup file /etc/profile or any of the personal initialization files ~/.bash_profile, ~/.bash_login, or ~/.profile when Bash is invoked as a login shell.

--norc
Don’t read the ~/.bashrc initialization file in an interactive shell. This is on by default if the shell is invoked as sh.

--posix
Change the behavior of Bash where the default operation differs from the POSIX standard to match the standard. This is intended to make Bash behave as a strict superset of that standard. See Bash POSIX Mode, for a description of the Bash POSIX mode.

--restricted
Make the shell a restricted shell (see The Restricted Shell).

--verbose
Equivalent to -v. Print shell input lines as they’re read.

--version
Show version information for this instance of Bash on the standard output and exit successfully.

There are several single-character options that may be supplied at invocation which are not available with the set builtin.

-c
Read and execute commands from the first non-option argument command_string, then exit. 
- If there are arguments after the command_string, the first argument is assigned to `$0` and any remaining arguments are assigned to the positional parameters. 
- The assignment to `$0` sets the name of the shell, which is used in warning and error messages.

-i
Force the shell to run interactively. Interactive shells are described in Interactive Shells.

-l
Make this shell act as if it had been directly invoked by login. 
- When the shell is interactive, this is equivalent to starting a login shell with ‘exec -l bash’. 
- When the shell is not interactive, the login shell startup files will be executed. 
- ‘exec bash -l’ or ‘exec bash --login’ will replace the current shell with a Bash login shell. See Bash Startup Files, for a description of the special behavior of a login shell.

-r
Make the shell a restricted shell (see The Restricted Shell).

-s
If this option is present, or if no arguments remain after option processing, then commands are read from the standard input. 
- This option allows the positional parameters to be set when invoking an interactive shell or when reading input through a pipe.

-D
A list of all double-quoted strings preceded by ‘$’ is printed on the standard output. These are the strings that are subject to language translation when the current locale is not C or POSIX (see Locale Translation). This implies the -n option; no commands will be executed.

`[-+]O [shopt_option]`
shopt_option is one of the shell options accepted by the `shopt` builtin. 
- If `shopt_option` is present, `-O` sets the value of that option; +O unsets it. 
- If `shopt_option` is not supplied, the names and values of the shell options accepted by `shopt` are printed on the standard output. 
- If the invocation option is `+O`, the output is displayed in a format that may be reused as input.

--
A -- signals the end of options and disables further option processing. 
- Any arguments after the -- are treated as filenames and arguments.

A **login shell** is one whose first character of argument zero is ‘-’, or one invoked with the `--login` option.
- (A login shell is a shell given to a user upon login into their user account. This is initiated by using the -l or --login option, or placing a dash as the initial character of the command name, for example invoking `bash` as `-bash`.)

An **interactive shell** is one started without non-option arguments, unless -s is specified, without specifying the -c option, and whose input and output are both connected to terminals (as determined by isatty(3)), or one started with the -i option. 

If arguments remain after option processing, and neither the -c nor the -s option has been supplied, the first argument is assumed to be the name of a file containing shell commands (see Shell Scripts). 
- When Bash is invoked in this fashion, `$0` is set to the name of the file, and the positional parameters are set to the remaining arguments. 
- Bash reads and executes commands from this file, then exits. 
- Bash’s exit status is the exit status of the last command executed in the script. 
- If no commands are executed, the exit status is `0`.

## 6.2 Bash Startup Files

If any of the files exist but cannot be read, Bash reports an error. Tildes are expanded in filenames.

### Invoked as an interactive login shell, or with --login

- When Bash is invoked as an interactive login shell, or as a non-interactive shell with the --login option, it first reads and executes commands from the file `/etc/profile`, if that file exists. 
- After reading that file, it looks for `~/.bash_profile`, `~/.bash_login`, and `~/.profile`, in that order, and reads and executes commands from the first one that exists and is readable. 
- The `--noprofile` option may be used when the shell is started to inhibit this behavior.

- When an interactive login shell exits, or a non-interactive login shell executes the `exit` builtin command, Bash reads and executes commands from the file `~/.bash_logout`, if it exists.

## Invoked as an interactive non-login shell

- When an interactive shell that is not a login shell is started, Bash reads and executes commands from `~/.bashrc`, if that file exists. 
- This may be inhibited by using the `--norc` option. The `--rcfile file` option will force Bash to read and execute commands from `file` instead of `~/.bashrc`.

So, typically, your `~/.bash_profile` contains the line
```bash
if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
```
after (or before) any login-specific initializations.


### Invoked non-interactively

When Bash is started non-interactively, to run a shell script, for example, it looks for the variable **BASH_ENV** in the environment, expands its value if it appears there, and uses the expanded value as the name of a file to read and execute. Bash behaves as if the following command were executed:
```bash
if [ -n "$BASH_ENV" ]; then . "$BASH_ENV"; fi
```
but the value of the `PATH` variable is not used to search for the filename.

As noted above, if a non-interactive shell is invoked with the `--login` option, Bash attempts to read and execute commands from the login shell startup files.

### Invoked with name sh

If Bash is invoked with the name `sh`, it tries to mimic the startup behavior of historical versions of sh as closely as possible, while conforming to the POSIX standard as well.

- When invoked as an interactive login shell, or as a non-interactive shell with the `--login` option, it first attempts to read and execute commands from `/etc/profile` and `~/.profile`, in that order. 
- The `--noprofile` option may be used to inhibit this behavior. 
- When invoked as an interactive shell with the name `sh`, Bash looks for the variable ENV, expands its value if it is defined, and uses the expanded value as the name of a file to read and execute. 
- Since a shell invoked as `sh` does not attempt to read and execute commands from any other startup files, the `--rcfile` option has no effect. 
- A non-interactive shell invoked with the name `sh` does not attempt to read any other startup files.

When invoked as `sh`, Bash enters POSIX mode after the startup files are read.

### Invoked in POSIX mode

When Bash is started in POSIX mode, as with the `--posix` command line option, it follows the POSIX standard for startup files. 
- In this mode, interactive shells expand the ENV variable and commands are read and executed from the file whose name is the expanded value. 
- No other startup files are read.

### Invoked by remote shell daemon

Bash attempts to determine when it is being run with its standard input connected to a network connection, as when executed by the remote shell daemon, usually `rshd`, or the secure shell daemon `sshd`. 
- If Bash determines it is being run in this fashion, it reads and executes commands from `~/.bashrc`, if that file exists and is readable. 
- It will not do this if invoked as `sh`. 
- The `--norc` option may be used to inhibit this behavior, and the `--rcfile` option may be used to force another file to be read, but neither `rshd` nor `sshd` generally invoke the shell with those options or allow them to be specified.

### Invoked with unequal effective and real UID/GIDs

If Bash is started with the effective user (group) id not equal to the real user (group) id, and the -p option is not supplied, **no startup files are read**, shell functions are not inherited from the environment, the SHELLOPTS, BASHOPTS, CDPATH, and GLOBIGNORE variables, if they appear in the environment, are ignored, and the effective user id is set to the real user id. If the -p option is supplied at invocation, the startup behavior is the same, but the effective user id is not reset.


## 6.3 Interactive Shells

### 6.3.1 What is an Interactive Shell?

An interactive shell is one started without non-option arguments, unless -s is specified, without specifying the -c option, and whose input and error output are both connected to terminals (as determined by isatty(3)), or one started with the -i option.

- An interactive shell generally reads from and writes to a user’s terminal.

- The -s invocation option may be used to set the positional parameters when an interactive shell is started.

### 6.3.2 Is this Shell Interactive?

To determine within a startup script whether or not Bash is running interactively, test the value of the ‘-’ special parameter. It contains `i` when the shell is interactive. For example:
```bash
case "$-" in
*i*)	echo This shell is interactive ;;
*)	echo This shell is not interactive ;;
esac
```
Alternatively, startup scripts may examine the variable `PS1`; it is unset in non-interactive shells, and set in interactive shells. Thus:
```bash
if [ -z "$PS1" ]; then
        echo This shell is not interactive
else
        echo This shell is interactive
fi
```

### 6.3.3 Interactive Shell Behavior

When the shell is running interactively, it changes its behavior in several ways.

1. Startup files are read and executed as described in Bash Startup Files.
2. Job Control is enabled by default. When job control is in effect, Bash ignores the keyboard-generated job control signals SIGTTIN, SIGTTOU, and SIGTSTP.
3. Bash expands and displays PS1 before reading the first line of a command, and expands and displays PS2 before reading the second and subsequent lines of a multi-line command. 
   - Bash expands and displays PS0 after it reads a command but before executing it. See Controlling the Prompt, for a complete list of prompt string escape sequences.
4. Bash executes the values of the set elements of the PROMPT_COMMAND array variable as commands before printing the primary prompt, `$PS1`.
5. `Readline` is used to read commands from the user’s terminal.
6. Bash inspects the value of the `ignoreeof` option to `set -o` instead of exiting immediately when it receives an EOF on its standard input when reading a command.
7. Command `history` and history expansion (see History Interaction) are enabled by default. 
   - Bash will save the command history to the file named by $HISTFILE when a shell with history enabled exits.
8. Alias expansion is performed by default.
9. In the absence of any traps, Bash ignores SIGTERM.
10. In the absence of any traps, SIGINT is caught and handled. SIGINT will interrupt some shell builtins.
11. An interactive login shell sends a SIGHUP to all jobs on exit if the huponexit shell option has been enabled.
12. The -n invocation option is ignored, and ‘set -n’ has no effect.
13. Bash will check for mail periodically, depending on the values of the MAIL, MAILPATH, and MAILCHECK shell variables.
14. Expansion errors due to references to unbound shell variables after ‘set -u’ has been enabled will not cause the shell to exit.
15. The shell will not exit on expansion errors caused by `var` being unset or null in `${var:?word}` expansions.
16. Redirection errors encountered by shell builtins will not cause the shell to exit.
17. When running in POSIX mode, a special builtin returning an error status will not cause the shell to exit.
18. A failed `exec` will not cause the shell to exit.
19. Parser syntax errors will not cause the shell to exit.
20. Simple spelling correction for directory arguments to the `cd` builtin is enabled by default (see the description of the `cdspell` option to the `shopt` builtin).
21. The shell will check the value of the TMOUT variable and exit if a command is not read within the specified number of seconds after printing `$PS1`.

## 6.4 Bash Conditional Expressions

Conditional expressions are used by the `[[` compound command and the `test` and `[` builtin commands. The `test` and `[` commands determine their behavior based on the number of arguments.

Expressions may be unary or binary, and are formed from the following **primaries**. 
- Unary expressions are often used to examine the **status of a file**. 
- There are string operators and numeric comparison operators as well. 
- Bash handles several filenames specially when they are used in expressions. 
  - If the operating system on which Bash is running provides these special files, Bash will use them; 
  - otherwise it will emulate them internally with this behavior: 
    - If the file argument to one of the primaries is of the form `/dev/fd/N`, then file descriptor N is checked. 
    - If the file argument to one of the primaries is one of `/dev/stdin, /dev/stdout, or /dev/stderr`, file descriptor 0, 1, or 2, respectively, is checked.

When used with `[[`, the ‘<’ and ‘>’ operators sort lexicographically using the current locale. The `test` command uses **ASCII ordering**.

Unless otherwise specified, primaries that operate on files follow symbolic links and operate on the target of the link, rather than the link itself.

### -a file
True if file exists.

### -b file
True if file exists and is a block special file.

### -c file
True if file exists and is a character special file.

### -d file
True if file exists and is a directory.

### -e file
True if file exists.

### -f file
True if file exists and is a regular file.

### -g file
True if file exists and its set-group-id bit is set.

### -h file
True if file exists and is a symbolic link.

### -k file
True if file exists and its "sticky" bit is set.

### -p file
True if file exists and is a named pipe (FIFO).

### -r file
True if file exists and is readable.

### -s file
True if file exists and has a size greater than zero.

### -t fd
True if file descriptor fd is open and refers to a terminal.

### -u file
True if file exists and its set-user-id bit is set.

### -w file
True if file exists and is writable.

### -x file
True if file exists and is executable.

### -G file
True if file exists and is owned by the effective group id.

### -L file
True if file exists and is a symbolic link.

### -N file
True if file exists and has been modified since it was last read.

### -O file
True if file exists and is owned by the effective user id.

### -S file
True if file exists and is a socket.

### file1 -ef file2
True if file1 and file2 refer to the same device and inode numbers.

### file1 -nt file2
True if file1 is newer (according to modification date) than file2, or if file1 exists and file2 does not.

### file1 -ot file2
True if file1 is older than file2, or if file2 exists and file1 does not.

### -o optname
True if the shell option `optname` is enabled. The list of options appears in the description of the `-o` option to the `set` builtin.

### -v varname
True if the shell variable varname is set (has been assigned a value).

### -R varname
True if the shell variable varname is set and is a name reference.

### -z string
True if the length of string is zero.

### -n string
### string
True if the length of string is non-zero.

### string1 == string2
### string1 = string2
True if the strings are equal. When used with the `[[` command, this performs pattern matching as described above (see Conditional Constructs).

‘=’ should be used with the `test` command for POSIX conformance.

### string1 != string2
True if the strings are not equal.

### string1 < string2
True if string1 sorts before string2 lexicographically.

### string1 > string2
True if string1 sorts after string2 lexicographically.

### arg1 OP arg2
`OP` is one of ‘-eq’, ‘-ne’, ‘-lt’, ‘-le’, ‘-gt’, or ‘-ge’. 
- These arithmetic binary operators return true if `arg1` is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to `arg2`, respectively. 
- Arg1 and arg2 may be positive or negative integers. 
- When used with the `[[` command, Arg1 and Arg2 are evaluated as arithmetic expressions (see Shell Arithmetic).

## 6.5 Shell Arithmetic

The shell allows arithmetic expressions to be evaluated, as one of the shell expansions or by using the `((` compound command, the `let` builtin, or the `-i` option to the `declare` builtin.

- Evaluation is done in fixed-width integers with no check for overflow, though division by 0 is trapped and flagged as an error. 
- The operators and their precedence, associativity, and values are the same as in the C language. 
- The following list of operators is grouped into levels of equal-precedence operators. The levels are listed in order of decreasing precedence.

`id++ id--`
variable post-increment and post-decrement

`++id --id`
variable pre-increment and pre-decrement

`- +`
unary minus and plus

`! ~`
logical and bitwise negation

`**`
exponentiation

`* / %`
multiplication, division, remainder

`+ -`
addition, subtraction

`<< >>`
left and right bitwise shifts

`<= >= < >`
comparison

`== !=`
equality and inequality

`&`
bitwise AND

`^`
bitwise exclusive OR

`|`
bitwise OR

`&&`
logical AND

`||`
logical OR

`expr ? expr : expr`
conditional operator

`= *= /= %= += -= <<= >>= &= ^= |=`
assignment

`expr1 , expr2`
comma

Shell variables are allowed as operands; parameter expansion is performed before the expression is evaluated. 
- Within an expression, shell variables may also be referenced by name without using the parameter expansion syntax. 
- A shell variable that is null or unset evaluates to `0` when referenced by name without using the parameter expansion syntax. 
- The value of a variable is evaluated as an arithmetic expression when it is referenced, or when a variable which has been given the integer attribute using ‘declare -i’ is assigned a value. 
- A null value evaluates to `0`. 
- A shell variable need not have its integer attribute turned on to be used in an expression.

Integer constants follow the C language definition, without suffixes or character constants. 
- Constants with a leading `0` are interpreted as octal numbers. 
- A leading ‘0x’ or ‘0X’ denotes hexadecimal. 
- Otherwise, numbers take the form `[base#]n`, where the optional `base` is a decimal number between 2 and 64 representing the arithmetic base, and `n` is a number in that base. 
- If `base#` is omitted, then base `10` is used. 
- When specifying `n`, if a non-digit is required, the digits greater than 9 are represented by the lowercase letters, the uppercase letters, ‘@’, and ‘_’, in that order. 
- If base is less than or equal to 36, lowercase and uppercase letters may be used interchangeably to represent numbers between 10 and 35.

Operators are evaluated in order of precedence. Sub-expressions in parentheses are evaluated first and may override the precedence rules above.

## 6.6 Aliases

Aliases allow a string to be substituted for a word when it is used as the first word of a simple command. The shell maintains a list of aliases that may be set and unset with the `alias` and `unalias` builtin commands.

The first word of each simple command, if unquoted, is checked to see if it has an alias. 
- If so, that word is replaced by the text of the alias. 
- The characters ‘/’, ‘$’, ‘`’, ‘=’ and any of the shell metacharacters or quoting characters listed above may not appear in an alias name. 
- The replacement text may contain any valid shell input, including shell metacharacters. 
- The first word of the replacement text is tested for aliases, but a word that is identical to an alias being expanded is not expanded a second time. 
  - This means that one may alias ls to "ls -F", for instance, and Bash does not try to recursively expand the replacement text. 
- If the last character of the alias value is a blank, then the next command word following the alias is also checked for alias expansion.

There is no mechanism for using arguments in the replacement text, as in csh. If arguments are needed, a shell function should be used.

**Aliases are not expanded when the shell is not interactive**, unless the `expand_aliases` shell option is set using `shopt`.

The rules concerning the definition and use of aliases are somewhat confusing. 
- Bash always reads at least one complete line of input, and all lines that make up a compound command, before executing any of the commands on that line or the compound command. 
- **Aliases are expanded when a command is read**, not when it is executed. 
- Therefore, an alias definition appearing on the same line as another command does not take effect until the next line of input is read. 
- The commands following the alias definition on that line are not affected by the new alias. 
- This behavior is also an issue when functions are executed. 
- Aliases are expanded when a function definition is read, not when the function is executed, because a function definition is itself a command. 
- As a consequence, aliases defined in a function are not available until after that function is executed. 
- To be safe, always put alias definitions on a separate line, and do not use `alias` in compound commands.

For almost every purpose, **shell functions** are preferred over **aliases**.

## 6.7 Arrays

Bash provides one-dimensional indexed and associative array variables. 
- Any variable may be used as an indexed array; 
- the `declare` builtin will explicitly declare an array. 
- There is no maximum limit on the size of an array, nor any requirement that members be indexed or assigned contiguously. 
- Indexed arrays are referenced using integers (including arithmetic expressions) and are zero-based; associative arrays use arbitrary strings. 
- Unless otherwise noted, indexed array indices must be non-negative integers.

An indexed array is created automatically if any variable is assigned to using the syntax
```bash
name[subscript]=value
```

The `subscript` is treated as an **arithmetic expression** that must evaluate to a number. To explicitly declare an array, use

```bash
declare -a name
```

The syntax
```bash
declare -a name[subscript]
```
is also accepted; the `subscript` is ignored.

Associative arrays are created using
```bash
declare -A name
```
Attributes may be specified for an array variable using the `declare` and `readonly` builtins. Each attribute applies to all members of an array.

Arrays are assigned to using compound assignments of the form
```bash
name=(value1 value2 … )
```

where each value may be of the form `[subscript]=string`. 
- Indexed array assignments do not require anything but **string**. 
- When assigning to indexed arrays, if the optional subscript is supplied, that index is assigned to; otherwise the index of the element assigned is the last index assigned to by the statement plus one. 
- Indexing starts at zero.

Each value in the list undergoes all the shell expansions described above.

When assigning to an associative array, 
- the words in a compound assignment may be either assignment statements, for which the **subscript** is required, 
- or a list of words that is interpreted as a sequence of alternating keys and values: `name=(key1 value1 key2 value2 … )`. 
  - These are treated identically to `name=( [key1]=value1 [key2]=value2 … )`. 
  - The first word in the list determines how the remaining words are interpreted; 
  - all assignments in a list must be of the same type. 
  - When using `key/value` pairs, the keys may not be missing or empty; a final missing value is treated like the empty string.

This syntax is also accepted by the `declare` builtin. Individual array elements may be assigned to using the `name[subscript]=value` syntax introduced above.

When assigning to an indexed array, if name is subscripted by a negative number, that number is interpreted as relative to one greater than the maximum index of name, so negative indices count back from the end of the array, and **an index of -1 references the last element**.

Any element of an array may be referenced using `${name[subscript]}`. 
- The braces are required to avoid conflicts with the shell’s filename expansion operators. 
- If the subscript is `‘@’` or `‘*’`, the word expands to all members of the array name. These subscripts differ only when the word appears within double quotes. 
  - If the word is double-quoted, `${name[*]}` expands to a single word with the value of each array member separated by the first character of the **IFS** variable, and `${name[@]}` expands each element of name to a separate word. 
  - When there are no array members, `${name[@]}` expands to nothing. 
  - If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the beginning part of the original word, and the expansion of the last parameter is joined with the last part of the original word. 
  - This is analogous to the expansion of the special parameters `‘@’` and `‘*’`. `${#name[subscript]}` expands to the length of `${name[subscript]}`. 
  - If subscript is `‘@’` or `‘*’`, the expansion is the number of elements in the array. 
- If the `subscript` used to reference an element of an indexed array evaluates to a number less than zero, it is interpreted as relative to one greater than the maximum index of the array, so negative indices count back from the end of the array, and an index of -1 refers to the last element.

Referencing an array variable without a subscript is equivalent to referencing with a subscript of `0`. Any reference to a variable using a valid subscript is legal, and bash will create an array if necessary.

An array variable is considered set if a subscript has been assigned a value. The null string is a valid value.

It is possible to obtain the keys (indices) of an array as well as the values. 
- `${!name[@]}` and `${!name[*]}` expand to the indices assigned in array variable name. 
- The treatment when in double quotes is similar to the expansion of the special parameters `‘@’` and `‘*’` within double quotes.

The `unset` builtin is used to destroy arrays. 
- `unset name[subscript]` destroys the array element at index subscript. 
- Negative subscripts to indexed arrays are interpreted as described above. 
- Unsetting the last element of an array variable does not `unset` the variable. 
- `unset name`, where name is an array, removes the entire array. 
- A subscript of `‘*’` or `‘@’` also removes the entire array.

When using a variable name with a subscript as an argument to a command, such as with `unset`, without using the word expansion syntax described above, the argument is subject to the shell’s `filename expansion`. If filename expansion is not desired, the argument should be quoted.

- The `declare`, `local`, and `readonly` builtins each accept a `-a` option to specify an indexed array and a `-A` option to specify an associative array. 
- If both options are supplied, `-A` takes precedence. 
- The `read` builtin accepts a `-a` option to assign a list of words read from the standard input to an array, and can read values from the standard input into individual array elements. 
- The `set` and `declare` builtins display array values in a way that allows them to be reused as input.

### Indexed Array vs Associative Array

- Bash supports one-dimensional numerically indexed and associative arrays types. 
- Numerical arrays are referenced using integers, and associative are referenced using strings.

- Numerically indexed arrays can be accessed from the end using negative indices, the index of -1 references the last element. The indices do not have to be contiguous.

- Unlike most of the programming languages, Bash array elements don’t have to be of the same data type. You can create an array that contains both strings and numbers.

- Bash does not support multidimensional arrays, and you can’t have array elements that are also arrays.

- There is no limit on the maximum number of elements that can be stored in an array.

#### Creating numerically indexed arrays

Bash variables are untyped, any variable can be used as an indexed array without declaring it.

To explicitly declare an array, use the declare builtin:
```bash
declare -a array_name
```
One way to create an indexed array is by using the following form:
```bash
array_name[index_1]=value_1
array_name[index_2]=value_2
array_name[index_n]=value_n
```
Where `index_*` is a positive integer.

Another way to create a numeric array is to specify the list of the elements within parentheses, separated by empty space:
```bash
array_name=( element_1 element_2 element_N )
```
When the array is created using the form above, indexing starts at zero i.e. the first element have an index of 0.

#### Creating associative arrays

Unlike numerically indexed, the associative arrays must be declared before they can be used.

To declare an associative array use the declare builtin with the `-A` (uppercase) option:
```bash
declare -A array_name
```
Associative arrays can be created using the following form:
```bash
declare -A array_name

array_name[index_foo]=value_foo
array_name[index_bar]=value_bar
array_name[index_xyz]=value_xyz
```
Where `index_*` can be any string.

You can also create an associative array using the form below:
```bash
declare -A array_name

array_name=( 
  [index_foo]=value_foo 
  [index_bar]=value_bar 
  [index_xyz]=value_xyz 
)
```

### Array Operations

#### Reference Elements
To reference a single element, you need to know the element index.
Any element can be referenced using the following syntax:
```bash
${array_name[index]}
```
If you use `@` or `*` as an index, the word expands to all members of the array. 

The only difference between `@` and `*` is when the form `${my_array[x]}` is surrounded with **double-quotes**. 
- In this case, `*` expands to a single word where array elements are separated with space. 
- `@` expands each array element to a separate word. 

To print the keys of the array add the ! operator before the array name:
```bash
${!array_name[index]}
```

**Array Length**
To get the length of an array, use the following form:
```bash
${#array_name[@]}
```

**Loop through the array**
```bash
declare -a my_array=( "Hydrogen" "Helium" "Lithium" "Beryllium" )

## Array Loop
for i in "${my_array[@]}"
do 
  echo "$i"
done
```

Here is an example of how to print all keys and values:
```bash
declare -a my_array=( "Hydrogen" "Helium" "Lithium" "Beryllium" )

## Array Loop
for i in "${!my_array[@]}"
do
  echo "$i" "${my_array[$i]}"
done
```
```
0 Hydrogen
1 Helium
2 Lithium
3 Beryllium
```
Another way to loop through an array is to get the length of the array and use the C style loop:
```bash
declare -a my_array=( "Hydrogen" "Helium" "Lithium" "Beryllium" )

# Length of the array
length=${#my_array[@]}

# Array Loop
for (( i=0; i < ${length}; i++ ))
do
  echo $i ${my_array[$i]}
done
```
**Add a new element**
To add a new element to a bash array and specify its index use the following form:
```bash
my_array[index_n]="New Element"
```
Another way of adding a new element to an array without specifying the index is by using the += operator. You can add one or multiple elements:
```bash
declare -a my_array=( "Hydrogen" "Helium" "Lithium" "Beryllium" )

## add new elements
my_array+=( Cobalt Nickel )
```

**Delete an element**
To delete a single element, you’ll need to know the element index. An element can be removed using the unset command:

unset my_array[index]



## 6.8 The Directory Stack

The directory stack is a list of recently-visited directories. 
- The `pushd` builtin adds directories to the stack as it changes the current directory, 
- and the `popd` builtin removes specified directories from the stack and changes the current directory to the directory removed. 
- The `dirs` builtin displays the contents of the directory stack. 
- The current directory is always the "top" of the directory stack.

The contents of the directory stack are also visible as the value of the `DIRSTACK` shell variable.

### dirs

```bash
dirs [-clpv] [+N | -N]
```
Display the list of currently remembered directories. Directories are added to the list with the `pushd` command; the `popd` command removes directories from the list. The current directory is always the first directory in the stack.

-c
Clears the directory stack by deleting all of the elements.

-l
Produces a listing using full pathnames; the default listing format uses a tilde to denote the home directory.

-p
Causes dirs to print the directory stack with one entry per line.

-v
Causes dirs to print the directory stack with one entry per line, prefixing each entry with its index in the stack.

+N
Displays the Nth directory (counting from the left of the list printed by dirs when invoked without options), starting with zero.

-N
Displays the Nth directory (counting from the right of the list printed by dirs when invoked without options), starting with zero.

### popd

```bash
popd [-n] [+N | -N]
```

When no arguments are given, popd removes the top directory from the stack and performs a `cd` to the new top directory. The elements are numbered from 0 starting at the first directory listed with dirs; that is, `popd` is equivalent to `popd +0`.

-n
Suppresses the normal change of directory when removing directories from the stack, so that only the stack is manipulated.

+N
Removes the Nth directory (counting from the left of the list printed by dirs), starting with zero.

-N
Removes the Nth directory (counting from the right of the list printed by dirs), starting with zero.

### pushd

```bash
pushd [-n] [+N | -N | dir]
```

Save the current directory on the top of the directory stack and then cd to dir. With no arguments, pushd exchanges the top two directories and makes the new top the current directory.

-n
Suppresses the normal change of directory when rotating or adding directories to the stack, so that only the stack is manipulated.

+N
Brings the Nth directory (counting from the left of the list printed by dirs, starting with zero) to the top of the list by rotating the stack.

-N
Brings the Nth directory (counting from the right of the list printed by dirs, starting with zero) to the top of the list by rotating the stack.

dir
Makes dir be the top of the stack, making it the new current directory as if it had been supplied as an argument to the cd builtin.

## 6.9 Controlling the Prompt

Bash examines the value of the array variable PROMPT_COMMAND just before printing each primary prompt. If any elements in PROMPT_COMMAND are set and non-null, Bash executes each value, in numeric order, just as if it had been typed on the command line.

In addition, the following table describes the special characters which can appear in the prompt variables PS0, PS1, PS2, and PS4:

`\a`
A bell character.

`\d`
The date, in "Weekday Month Date" format (e.g., "Tue May 26").

`\D{format}`
The format is passed to `strftime(3)` and the result is inserted into the prompt string; an empty format results in a locale-specific time representation. The braces are required.

`\e`
An escape character.

`\h`
The hostname, up to the first ‘.’.

`\H`
The hostname.

`\j`
The number of jobs currently managed by the shell.

`\l`
The basename of the shell’s terminal device name.

`\n`
A newline.

`\r`
A carriage return.

`\s`
The name of the shell, the basename of $0 (the portion following the final slash).

`\t`
The time, in 24-hour HH:MM:SS format.

`\T`
The time, in 12-hour HH:MM:SS format.

`\@`
The time, in 12-hour am/pm format.

`\A`
The time, in 24-hour HH:MM format.

`\u`
The username of the current user.

`\v`
The version of Bash (e.g., 2.00)

`\V`
The release of Bash, version + patchlevel (e.g., 2.00.0)

`\w`
The current working directory, with `$HOME` abbreviated with a tilde (uses the `$PROMPT_DIRTRIM` variable).

`\W`
The basename of `$PWD`, with `$HOME` abbreviated with a tilde.

`\!`
The history number of this command.

`\#`
The command number of this command.

`\$`
If the effective uid is 0, #, otherwise $.

`\nnn`
The character whose ASCII code is the octal value nnn.

`\\`
A backslash.

`\[`
Begin a sequence of non-printing characters. This could be used to embed a terminal control sequence into the prompt.

`\]`
End a sequence of non-printing characters.

```
$ PROMPT_COMMAND="date +%H%M"
1103
ubuntu@primary:~/effectivec$ 
1104
ubuntu@primary:~/effectivec$
```

The command number and the history number are usually different: 
- the history number of a command is its position in the history list, which may include commands restored from the history file (see Bash History Facilities), 
- while the command number is the position in the sequence of commands executed during the current shell session.

After the string is decoded, it is expanded via parameter expansion, command substitution, arithmetic expansion, and quote removal, subject to the value of the `promptvars` shell option (see The Shopt Builtin). This can have unwanted side effects if escaped portions of the string appear within command substitution or contain characters special to word expansion.

## 6.10 The Restricted Shell

If Bash is started with the name `rbash`, or the `--restricted` or `-r` option is supplied at invocation, the shell becomes restricted. A restricted shell is used to set up an environment more controlled than the standard shell. A restricted shell behaves identically to bash with the exception that the following are disallowed or not performed:

- Changing directories with the cd builtin.
- Setting or unsetting the values of the SHELL, PATH, HISTFILE, ENV, or BASH_ENV variables.
- Specifying command names containing slashes.
- Specifying a filename containing a slash as an argument to the `.` builtin command.
- Specifying a filename containing a slash as an argument to the `history` builtin command.
- Specifying a filename containing a slash as an argument to the `-p` option to the `hash` builtin command.
- Importing function definitions from the shell environment at startup.
- Parsing the value of SHELLOPTS from the shell environment at startup.
- Redirecting output using the ‘>’, ‘>|’, ‘<>’, ‘>&’, ‘&>’, and ‘>>’ redirection operators.
- Using the `exec` builtin to replace the shell with another command.
- Adding or deleting builtin commands with the `-f` and `-d` options to the enable builtin.
- Using the `enable` builtin command to enable disabled shell builtins.
- Specifying the `-p` option to the `command` builtin.
- Turning off restricted mode with ‘set +r’ or ‘set +o restricted’.
- These restrictions are enforced after any startup files are read.

When a command that is found to be **a shell script** is executed, `rbash` turns off any restrictions in the shell spawned to execute the script.

The restricted shell mode is only one component of a useful restricted environment. 
- It should be accompanied by setting PATH to a value that allows execution of only a few verified commands (commands that allow shell escapes are particularly vulnerable), leaving the user in a non-writable directory other than his home directory after login, not allowing the restricted shell to execute shell scripts, and cleaning the environment of variables that cause some commands to modify their behavior (e.g., VISUAL or PAGER).

Modern systems provide more secure ways to implement a restricted environment, such as `jails`, `zones`, or `containers`.

## 6.11 Bash POSIX Mode

Starting Bash with the `--posix` command-line option or executing ‘set -o posix’ while Bash is running will cause Bash to conform more closely to the POSIX standard by changing the behavior to match that specified by POSIX in areas where the Bash default differs.

When invoked as `sh`, Bash enters POSIX mode after reading the startup files.

The following list is what’s changed when ‘POSIX mode’ is in effect:

1. Bash ensures that the POSIXLY_CORRECT variable is set.
2. When a command in the hash table no longer exists, Bash will re-search `$PATH` to find the new location. This is also available with ‘shopt -s checkhash’.
3. Bash will not insert a command without the execute bit set into the command hash table, even if it returns it as a (last-ditch) result from a `$PATH` search.
4. The message printed by the job control code and builtins when a job exits with a non-zero status is ‘Done(status)’.
5. The message printed by the job control code and builtins when a job is stopped is ‘Stopped(signame)’, where signame is, for example, SIGTSTP.
6. Alias expansion is always enabled, even in non-interactive shells.
7. Reserved words appearing in a context where reserved words are recognized do not undergo alias expansion.
8. The POSIX PS1 and PS2 expansions of ‘!’ to the history number and ‘!!’ to ‘!’ are enabled, and parameter expansion is performed on the values of PS1 and PS2 regardless of the setting of the promptvars option.
9. The POSIX startup files are executed (`$ENV`) rather than the normal Bash files.
10. Tilde expansion is only performed on assignments preceding a command name, rather than on all assignment statements on the line.
11. The default history file is `~/.sh_history` (this is the default value of `$HISTFILE`).
12. Redirection operators do not perform filename expansion on the word in the redirection unless the shell is interactive.
13. Redirection operators do not perform word splitting on the word in the redirection.
14. Function names must be valid shell names. That is, they may not contain characters other than letters, digits, and underscores, and may not start with a digit. Declaring a function with an invalid name causes a fatal syntax error in non-interactive shells.
15. Function names may not be the same as one of the POSIX special builtins.
16. POSIX special builtins are found before shell functions during command lookup.
17. When printing shell function definitions (e.g., by `type`), Bash does not print the `function` keyword.
18. Literal tildes that appear as the first character in elements of the PATH variable are not expanded as described above under Tilde Expansion.
19. The `time` reserved word may be used by itself as a command. When used in this way, it displays timing statistics for the shell and its completed children. The TIMEFORMAT variable controls the format of the timing information.
20. When parsing and expanding a `${…}` expansion that appears within double quotes, single quotes are no longer special and cannot be used to quote a closing brace or other special character, unless the operator is one of those defined to perform **pattern removal**. In this case, they do not have to appear as matched pairs.
21. The parser does not recognize `time` as a reserved word if the next token begins with a ‘-’.
22. The ‘!’ character does not introduce history expansion within a double-quoted string, even if the `histexpand` option is enabled.
23. If a POSIX special builtin returns an error status, a non-interactive shell exits. The fatal errors are those listed in the POSIX standard, and include things like passing incorrect options, redirection errors, variable assignment errors for assignments preceding the command name, and so on.
24. A non-interactive shell exits with an error status if a variable assignment error occurs when no command name follows the assignment statements. A variable assignment error occurs, for example, when trying to assign a value to a readonly variable.
25. A non-interactive shell exits with an error status if a variable assignment error occurs in an assignment statement preceding a special builtin, but not with any other simple command.
26. A non-interactive shell exits with an error status if the iteration variable in a for statement or the selection variable in a select statement is a readonly variable.
27. Non-interactive shells exit if filename in `. filename` is not found.
28. Non-interactive shells exit if a syntax error in an arithmetic expansion results in an invalid expression.
29. Non-interactive shells exit if a parameter expansion error occurs.
30. Non-interactive shells exit if there is a syntax error in a script read with the `.` or `source` builtins, or in a string processed by the `eval` builtin.
31. While variable indirection is available, it may not be applied to the ‘#’ and ‘?’ special parameters.
32. When expanding the `‘*’` special parameter in a pattern context where the expansion is double-quoted does not treat the `$*` as if it were double-quoted.
33. Assignment statements preceding POSIX special builtins persist in the shell environment after the builtin completes.
34. The `command` builtin does not prevent builtins that take assignment statements as arguments from expanding them as assignment statements; when not in POSIX mode, assignment builtins lose their assignment statement expansion properties when preceded by `command`.
35. The `bg` builtin uses the required format to describe each job placed in the background, which does not include an indication of whether the job is the current or previous job.
36. The output of ‘kill -l’ prints all the signal names on a single line, separated by spaces, without the ‘SIG’ prefix.
37. The kill builtin does not accept signal names with a ‘SIG’ prefix.
38. The `export` and `readonly` builtin commands display their output in the format required by POSIX.
39. The `trap` builtin displays signal names without the leading SIG
40. The `trap` builtin doesn’t check the first argument for a possible signal specification and revert the signal handling to the original disposition if it is, unless that argument consists solely of digits and is a valid signal number. If users want to reset the handler for a given signal to the original disposition, they should use ‘-’ as the first argument.
41. `trap -p` displays signals whose dispositions are set to SIG_DFL and those that were ignored when the shell started.
42. The `.` and `source` builtins do not search the current directory for the filename argument if it is not found by searching PATH.
43. Enabling POSIX mode has the effect of setting the `inherit_errexit` option, so subshells spawned to execute command substitutions inherit the value of the `-e` option from the parent shell. When the `inherit_errexit` option is not enabled, Bash clears the `-e` option in such subshells.
44. Enabling POSIX mode has the effect of setting the `shift_verbose` option, so numeric arguments to `shift` that exceed the number of positional parameters will result in an error message.
45. When the `alias` builtin displays alias definitions, it does not display them with a leading ‘alias ’ unless the `-p` option is supplied.
46. When the `set` builtin is invoked without options, it does not display shell function names and definitions.
47. When the `set` builtin is invoked without options, it displays variable values without quotes, unless they contain shell metacharacters, even if the result contains nonprinting characters.
48. When the `cd` builtin is invoked in logical mode, and the pathname constructed from `$PWD` and the directory name supplied as an argument does not refer to an existing directory, `cd` will fail instead of falling back to physical mode.
49. When the `cd` builtin cannot change a directory because the length of the pathname constructed from `$PWD` and the directory name supplied as an argument exceeds PATH_MAX when all symbolic links are expanded, `cd` will fail instead of attempting to use only the supplied directory name.
50. The `pwd` builtin verifies that the value it prints is the same as the current directory, even if it is not asked to check the file system with the `-P` option.
51. When listing the history, the `fc` builtin does not include an indication of whether or not a history entry has been modified.
52. The default editor used by `fc` is `ed`.
53. The `type` and `command` builtins will not report a non-executable file as having been found, though the shell will attempt to execute such a file if it is the only so-named file found in `$PATH`.
54. The `vi` editing mode will invoke the `vi` editor directly when the ‘v’ command is run, instead of checking `$VISUAL` and `$EDITOR`.
55. When the `xpg_echo` option is enabled, Bash does not attempt to interpret any arguments to `echo` as options. Each argument is displayed, after escape characters are converted.
56. The `ulimit` builtin uses a block size of 512 bytes for the `-c` and `-f` options.
57. The arrival of SIGCHLD when a trap is set on SIGCHLD does not interrupt the `wait` builtin and cause it to return immediately. The `trap` command is run once for each child that exits.
58. The `read` builtin may be interrupted by a signal for which a trap has been set. If Bash receives a trapped signal while executing `read`, the trap handler executes and `read` returns an exit status greater than 128.
59. Bash removes an exited background process’s status from the list of such statuses after the `wait` builtin is used to obtain it.

There is other POSIX behavior that Bash does not implement by default even when in POSIX mode. Specifically:

1. The `fc` builtin checks `$EDITOR` as a program to edit history entries if FCEDIT is unset, rather than defaulting directly to `ed`. `fc` uses `ed` if EDITOR is unset.
2. As noted above, Bash requires the `xpg_echo` option to be enabled for the `echo` builtin to be fully conformant.

Bash can be configured to be POSIX-conformant by default, by specifying the `--enable-strict-posix-default` to configure when building (see Optional Features).

## 6.12 Shell Compatibility Mode

Bash-4.0 introduced the concept of a ‘shell compatibility level’, specified as a set of options to the `shopt` builtin (compat31, compat32, compat40, compat41, and so on). 
- There is only one current compatibility level – each option is mutually exclusive. 
- The compatibility level is intended to allow users to select behavior from previous versions that is incompatible with newer versions while they migrate scripts to use current features and behavior. 
- It’s intended to be a temporary solution.

This section does not mention behavior that is standard for a particular version.

If a user enables, say, compat32, it may affect the behavior of other compatibility levels up to and including the current compatibility level. 
- The idea is that each compatibility level controls behavior that changed in that version of Bash, but that behavior may have been present in earlier versions. 
  - For instance, the change to use locale-based comparisons with the `[[` command came in bash-4.1, and earlier versions used ASCII-based comparisons, so enabling compat32 will enable ASCII-based comparisons as well. 
  - That granularity may not be sufficient for all uses, and as a result users should employ compatibility levels carefully. 

Bash-4.3 introduced a new shell variable: **BASH_COMPAT**. 
- The value assigned to this variable (a decimal version number like 4.2, or an integer corresponding to the compatNN option, like 42) determines the compatibility level.

Starting with bash-4.4, Bash has begun deprecating older compatibility levels. 
- Eventually, the options will be removed in favor of BASH_COMPAT.

Bash-5.0 is the final version for which there will be an individual `shopt` option for the previous version. 
- Users should use BASH_COMPAT on bash-5.0 and later versions.

The following table describes the behavior changes controlled by each compatibility level setting. 
- The **compatNN** tag is used as shorthand for setting the compatibility level to `NN` using one of the following mechanisms. 
- For versions prior to bash-5.0, the compatibility level may be set using the corresponding `compatNN` `shopt` option. 
- For bash-4.3 and later versions, the BASH_COMPAT variable is preferred, and it is required for bash-5.1 and later versions.

compat31
- quoting the `rhs` of the `[[` command’s regexp matching operator (=~) has no special effect

compat32
- interrupting a command list such as "a ; b ; c" causes the execution of the next command in the list (in bash-4.0 and later versions, the shell acts as if it received the interrupt, so interrupting one command in a list aborts the execution of the entire list)

 compat40
- the ‘<’ and ‘>’ operators to the [[ command do not consider the current locale when comparing strings; they use ASCII ordering. Bash versions prior to bash-4.1 use ASCII collation and strcmp(3); bash-4.1 and later use the current locale’s collation sequence and strcoll(3).

compat41
- in posix mode, time may be followed by options and still be recognized as a reserved word (this is POSIX interpretation 267)
- in posix mode, the parser requires that an even number of single quotes occur in the word portion of a double-quoted ${…} parameter expansion and treats them specially, so that characters within the single quotes are considered quoted (this is POSIX interpretation 221)

compat42
- the replacement string in double-quoted pattern substitution does not undergo quote removal, as it does in versions after bash-4.2
- in posix mode, single quotes are considered special when expanding the word portion of a double-quoted ${…} parameter expansion and can be used to quote a closing brace or other special character (this is part of POSIX interpretation 221); in later versions, single quotes are not special within double-quoted word expansions

compat43
- the shell does not print a warning message if an attempt is made to use a quoted compound assignment as an argument to declare (declare -a foo=’(1 2)’). Later versions warn that this usage is deprecated
- word expansion errors are considered non-fatal errors that cause the current command to fail, even in posix mode (the default behavior is to make them fatal errors that cause the shell to exit)
- when executing a shell function, the loop state (while/until/etc.) is not reset, so break or continue in that function will break or continue loops in the calling context. Bash-4.4 and later reset the loop state to prevent this

compat44
- the shell sets up the values used by BASH_ARGV and BASH_ARGC so they can expand to the shell’s positional parameters even if extended debugging mode is not enabled
- a subshell inherits loops from its parent context, so break or continue will cause the subshell to exit. Bash-5.0 and later reset the loop state to prevent the exit
- variable assignments preceding builtins like export and readonly that set attributes continue to affect variables with the same name in the calling environment even if the shell is not in posix mode

compat50 (set using BASH_COMPAT)
- Bash-5.1 changed the way $RANDOM is generated to introduce slightly more randomness. If the shell compatibility level is set to 50 or lower, it reverts to the method from bash-5.0 and previous versions, so seeding the random number generator by assigning a value to RANDOM will produce the same sequence as in bash-5.0
- If the command hash table is empty, Bash versions prior to bash-5.1 printed an informational message to that effect, even when producing output that can be reused as input. Bash-5.1 suppresses that message when the -l option is supplied.















