- [Exit code](#exit-code)
- [positional arguments](#positional-arguments)
- [Debugging on the entire script](#debugging-on-the-entire-script)
- [Regular Expression operators](#regular-expression-operators)
- [Single and double quotes](#single-and-double-quotes)
- [Arithmetic expansion](#arithmetic-expansion)
- [Conditional statements](#conditional-statements)
- [String comparisons](#string-comparisons)
  - [No exit?](#no-exit)
- [Boolean operations AND OR](#boolean-operations-and-or)
- [Using case statements](#using-case-statements)
- [escape sequence in echo](#escape-sequence-in-echo)
- [Catching user input](#catching-user-input)
- [Redirection and file descriptors](#redirection-and-file-descriptors)
  - [Using /dev/fd](#using-devfd)
- [Here documents](#here-documents)
- [Repetitive tasks](#repetitive-tasks)
  - [For loop](#for-loop)
  - [While loop](#while-loop)
  - [The until loop](#the-until-loop)
  - [Break and continue](#break-and-continue)
  - [Making menus with the select built-in](#making-menus-with-the-select-built-in)
- [I/O redirection and loops](#io-redirection-and-loops)
- [WHAT IS FILE GLOBBING IN LINUX?](#what-is-file-globbing-in-linux)
- [The shift built-in](#the-shift-built-in)
- [exec {} vs xargs](#exec--vs-xargs)
- [More on variables](#more-on-variables)
  - [Using the declare built-in](#using-the-declare-built-in)
  - [Constants](#constants)
  - [Array variables](#array-variables)
  - [Operations on variables](#operations-on-variables)
  - [Transformations of variables](#transformations-of-variables)
    - [Substitution](#substitution)
  - [Removing substrings](#removing-substrings)
  - [Replacing parts of variable names](#replacing-parts-of-variable-names)
- [Functions](#functions)
  - [Positional parameters in functions](#positional-parameters-in-functions)
  - [Export function](#export-function)
- [Catching signals](#catching-signals)
  - [Traps](#traps)
  - [Detecting when a variable is used](#detecting-when-a-variable-is-used)


# Exit code

-  0    successful
-  1    general error
-  2    built-in error
-  126  permission issue
-  127  could not invoke requested command
-  128  invalide argument
-  128+n    fatal error with signal n
-  130  terminate prog with ctrl+c
-  255  out of range

# positional arguments

- $#    number of arguments
- $*    all the arguments in a string "$1 $2..."
- $@    all the arguments in a seperate quotes "$1" "$2" ...


Other special symbol

- $$    parent pid of current instance
- $!    pid of most recent background command
- $_    absolute file name of the script

# Debugging on the entire script

Bash provides extensive debugging features. The most common is to start up the subshell with the `-x `option, which will run the entire script in debug mode. Traces of each command plus its arguments are printed to standard output after the commands have been expanded but before they are executed.

Using the set Bash built-in you can run in normal mode those portions of the script of which you are sure they are without fault, and display debugging information only for troublesome zones.
`set -x` # activate debugging from here

`set +x` # stop debugging from here

Use the -o option to set to display all shell options: 
```
willy:~> set -o
```

# Regular Expression operators

- .	replaces any character
- ^	matches start of string
- $	matches end of string
- *	matches up zero or more times the preceding character
- \	Represent special characters
- ()	Groups regular expressions
- ?	Matches up exactly one character
- + one or more times
- {N}   exactly N times
- {N,}  N or more times


# Single and double quotes

Single quotes
Single quotes ('') are used to preserve the literal value of each character enclosed within the quotes. 

Double quotes
Using double quotes the literal value of all characters enclosed is preserved, except for the dollar sign, the backticks (backward single quotes, ``) and the backslash.


# Arithmetic expansion

```bash
$(( EXPRESSION ))

(( VAR++ ))
(( VAR-- ))
(( VAR1 + VAR2 ))
```

Wherever possible, Bash users should try to use the syntax with square brackets:
```bash
$[ EXPRESSION ]
echo $[365*24]
8760
```

# Conditional statements

if TEST-COMMANDS; then CONSEQUENT-COMMANDS; fi

- [ -a FILE ]   True if FILE exists.
- [ -e FILE ]   True if FILE exists.
- [ -f FILE ]   True if FILE exists and is a regular file.
- [ -z STRING ] True of the length if “STRING” is zero.
- [ -n STRING ] or [ STRING ]   True if the length of “STRING” is non-zero.
- [ STRING1 == STRING2 ]    True if the strings are equal. “=“ may be used instead of “==“ for strict POSIX compliance.
- [ STRING1 != STRING2 ]    True if the strings are not equal.
- [ ARG1 OP ARG2 ]
“OP” is one of -eq, -ne, -lt, -le, -gt or -ge. These arithmetic binary operators return true if “ARG1” is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to “ARG2”, respectively. “ARG1” and “ARG2” are integers.
- [ ! EXPR ]    True if EXPR is false.
- [ EXPR1 -a EXPR2 ]    True if both EXPR1 and EXPR2 are true.
- [ EXPR1 -o EXPR2 ]    True if either EXPR1 or EXPR2 is true.

# String comparisons

```bash

if [ "$(whoami)" != 'root' ]; then
echo "You have no permission to run $0 as non-root user." 
exit 1;
fi
```
Notice: a space is must between “[“ and “$(whoami)”

With Bash, you can shorten this type of construct. The compact equivalent of the above test is as follows:

```bash
 [ "$(whoami)" != 'root' ] && ( echo you are using a non-privileged account; exit 1 )
```

Regular expressions may also be used in comparisons:
```bash
gender="female"
if [[ "$gender" == f* ]]
then 
echo "Pleasure to meet you, Madame."
fi
```

## No exit?

If you invoke the exit in a subshell, it will not pass variables to the parent. Use { and } instead of ( and ) if you do not want Bash to fork a subshell.

# Boolean operations AND OR

The above script can be shortened using the Boolean operators "AND" (&&) and "OR" (||).

# Using case statements
```bash
case EXPRESSION in 
CASE1) 
COMMAND-LIST
;; 
CASE2) 
COMMAND-LIST
;;
...
CASEN) 
COMMAND-LIST
;;
esac
```

# escape sequence in echo

- \a    Alert(bell)
- \b    backspace
- \c    suppress trailing newline
- \e    escape
- \f    form feed
- \n    new line
- \r    carriage return
- \t    horizontal tab
- \v    vertical tab
- \\    backslash


# Catching user input

```bash
read [options] NAME1 NAME2 ... NAMEN

```

# Redirection and file descriptors

These numeric values are known as file descriptors. The best known file descriptors are stdin, stdout and stderr, with file descriptor numbers 0, 1 and 2, respectively.

`&> FILE`
This is the equivalent of > `FILE 2>&1`

## Using /dev/fd

The /dev/fd directory contains entries named 0, 1, 2, and so on. Opening the file /dev/fd/N is equivalent to duplicating file descriptor N. If your system provides /dev/stdin, /dev/stdout and /dev/stderr, you will see that these are equivalent to /dev/fd/0, /dev/fd/1 and /dev/ fd/2, respectively.


# Here documents

```bash
echo "These are the web browsers on this system:"
# Start here document
cat << BROWSERS
mozilla
links
konqueror
opera
netscape
BROWSERS
# End here document
echo -n "Which is your favorite? " 
read browser
echo "Starting $browser, please wait..." 
$browser &
```

This is an example that installs a package automatically, eventhough you should normally confirm:

```bash
#!/bin/bash
 # This script installs packages automatically, using yum.
if [ $# -lt 1 ]; then
 echo "Usage: $0 package."
exit 1
fi
yum install << CONFIRM
y
CONFIRM

```

# Repetitive tasks

## For loop

```bash
for NAME [in LIST ]; do COMMANDS; done
```

Odd characters
You will run into problems if the list expands to file names containing spaces and other irregular characters. A more ideal construct to obtain the list would be to use the shell's **globbing** feature, like this:
```bash

for i in $PATHNAME/*; do
        commands
done
```

## While loop

```bash
while CONTROL-COMMAND; do CONSEQUENT-COMMANDS; done
```

```bash
#!/bin/bash
# This script opens 4 terminal windows. i="0"
while [ $i -lt 4 ]
do
# xterm & 
i=$[$i+1] 
echo $i 
done
```

## The until loop

The until loop is very similar to the while loop, except that the loop executes until the TEST-COMMAND executes successfully. As long as this command fails, the loop continues. The syntax is the same as for the while loop:
```bash
until TEST-COMMAND; do CONSEQUENT-COMMANDS; done
```
## Break and continue

Mind that `break` exits the loop, not the script.
In nested loops, `break` allows for specification of which loop to exit.
The `continue` statement resumes iteration of an enclosing for, `while, until or select` loop.
When used in a `for` loop, the controlling variable takes on the value of the next element in the list. When used in a `while or until` construct, on the other hand, execution resumes with `TEST-COMMAND` at the top of the loop.

## Making menus with the select built-in

The select construct allows easy menu generation. The syntax is quite similar to that of the for loop:
```bash
select WORD [in LIST]; do RESPECTIVE-COMMANDS; done
```
- LIST is expanded, generating a list of items. 
- The expansion is printed to standard error; each item is preceded by a number. 
- If in LIST is not present, the positional parameters are printed, as if in `$@` would have been specified. 
- LIST is only printed once.
- The read line is saved in the `REPLY` variable.
- The `RESPECTIVE-COMMANDS` are executed after each selection until the number representing the break is read. This exits the loop.

```bash
#!/bin/bash
echo "This script can make any of the files in this directory private."
echo "Enter the number of the file you want to protect:"
select FILENAME in *;
do
echo "You picked $FILENAME ($REPLY), it is now only accessible to you." 
chmod go-rwx "$FILENAME"
done
```

Improved version:

```bash
#!/bin/bash
echo "This script can make any of the files in this directory private." 
echo "Enter the number of the file you want to protect:"
PS3="Your choice: "
QUIT="QUIT THIS PROGRAM - I feel safe now."
touch "$QUIT"
select FILENAME in *;
do
case $FILENAME in 
"$QUIT")
echo "Exiting." 
break
;;
*)
echo "You picked $FILENAME ($REPLY)" 
chmod go-rwx "$FILENAME"
;;
esac 
done
rm "$QUIT"
```

# I/O redirection and loops

Instead of controlling a loop by testing the result of a command or by user input, you can specify a file from which to read input that controls the loop. In such cases, `read` is often the controlling command. As long as input lines are fed into the loop, execution of the loop commands continues. As soon as all the input lines are read the loop exits.

Since the loop construct is considered to be one command structure (such as while `TEST-COMMAND; do CONSEQUENT-COMMANDS; done`), the redirection should occur after the done statement, so that it complies with the form
```bash
command < file
```
This kind of redirection also works with other kinds of loops.
```bash
find . -name "*.sh" >temp 
while read lig
do
echo $lig 
done < temp 
rm temp
```






# WHAT IS FILE GLOBBING IN LINUX?

File globbing is a feature provided by the UNIX/Linux shell to represent multiple filenames by using special characters called wildcards with a single file name. A wildcard is essentially a symbol which may be used to substitute for one or more characters. Therefore, we can use wildcards for generating the appropriate combination of file names as per our requirement.
TYPES OF AVAILABLE FILE GLOBBING:
The bash shell provides three characters to use as wildcards:
- Asterisk (*) to represent 0 or more characters
- Question mark (?) to represent exactly one character
- Square brackets ([]) to represent and match for the character enclosed within the square brackets.


# The shift built-in

- This command takes one argument, a number.
- The positional parameters are shifted to the left by this number, N. 
- The positional parameters from `N+1` to `$#` are renamed to variable names from `$1` to `$# - N+1`.
  - Say you have a command that takes `10` arguments, and `N` is `4`, then `$4` becomes `$1`, `$5` becomes `$2` and so on. `$10` becomes `$7` and the original `$1`, `$2` and `$3` are thrown away.
- If `N` is zero or greater than `$#`, the positional parameters are not changed (the total number of arguments) and the command has no effect. 
- If N is not present, it is assumed to be 1.
- The return status is `zero` unless N is greater than `$#` or less than zero; otherwise it is non-zero.

Use shift:

- A `shift` statement is typically used when the number of arguments to a command is not known in advance, for instance when users can give as many arguments as they like. 
- In such cases, the arguments are usually processed in a `while` loop with a test condition of `(( $# ))`. 
- This condition is `true` as long as the number of arguments is greater than `zero`.
- The `$1` variable and the `shift` statement process each argument. 
- The number of arguments is reduced each time `shift` is executed and eventually becomes `zero`, upon which the `while` loop exits.

The number of arguments is reduced each time shift is executed and eventually becomes zero, upon which the while loop exits.

```bash
#!/bin/bash

echo $1
shift
echo $1
shift
echo $1
```
```bash
MacBook-Air:tests michael$ ./bash.sh 1 2 3
1
2
3
```

A real example:

```bash
#!/bin/bash
# Scan directories for old files (over 365 days) and ls them.
USAGE="Usage: $0 dir1 dir2 dir3 ..."
if [ "$#" == "0" ]; then                      # If zero arguments were supplied,
  echo "Error: no directory names provided."
  echo "$USAGE"                               # display a help message
  exit 1                                      # and return an error.
fi
while (( "$#" )); do        # While there are arguments still to be shifted...
  while IFS= read -r -d $'\0' file; do
    echo "Removing $file..."
    ls $file
  done < <(find "$1" -type f -atime +365 -print0)
  shift
done
echo "Done."
exit 0
```
Explain:
- The expressions `(( "$#" ))` and `[ "$#" != "0" ]` give equivalent results, and are functionally interchangeable.
- `while IFS= read -r -d $'\0' file; do` 
  - This line says: while items remain to be read that are delimited `( -d )` by a null character `( $'\0' )`, read one item into the variable `file`, then perform the commands inside the loop.
  - The Internal Field Separator (IFS) that is used for word splitting after expansion and to split lines into words with the read builtin command. IFS variable is commonly used with read command, parameter expansions and command substitution. The default value is <space><tab><newline>. 
- `done < <(find "$1" -type f -atime +365 -print0)` This line says: 
  - find all files, beginning the search in the directory `dir1` (in positional parameter `$1`), that were last accessed (`-atime`) more than `( + ) 365` days ago. Delimit the list of matching file names with null characters (`-print0`).
  - The find command is enclosed in `<( … )`, which uses process substitution to treat the output as if it's a file.
  - The contents of this "file" are redirected ( < ) to the inner while loop.
  - There, read interprets everything up to a null character as the next file name, and assigns this name to the variable file. 
- `shift` shifts the positional parameters, so that dir2 ($2) is now dir1 ($1).


# exec {} vs xargs

`FIND -EXEC VS. FIND | XARGS`
Which one is more efficient over a very large set of files and should be used?
`find . -exec cmd {} +`
or
`find . | xargs cmd`

- When you use `-exec` to do the work you run a **separate** instance of the called program for each element of input. So if find comes up with 10,000 results, you run exec 10,000 times. 
- With `xargs` , you build up the input into bundles and run them through the command as few times as possible, which is often just once.


# More on variables

## Using the declare built-in
The syntax for declare is the following: 
```bash
declare OPTION(s) VARIABLE=value 
```
Options to the declare built-in:

- -a  Variable is an array
- -f  Use function names only
- -i  The variable is to be treated as an integer; arithmetic evaluation is performed when the variable is assigned a value
- -p  Display the attributes and values of each variable. When -p is used, additional options are ignored.
- -r  Make variables read-only. These variables cannot then be assigned values by subsequent assignment statements, nor can the be unset.
- -t  Give each variable the trace attribute
- -x  Mark each variable for export to subsequent commands via the environment.

Using + instead of - turns off the attribute instead. When used in a function, declare creates local variables.
```bash
[bob in ~] declare -i VARIABLE=12
[bob in ~] VARIABLE=string
[bob in ~] echo $VARIABLE 0
[bob in ~] declare -p VARIABLE
declare -i VARIABLE="0"
[bob in ~] OTHERVAR=blah
[bob in ~] declare -p OTHERVAR
declare -- OTHERVAR="blah"
```

## Constants
The syntax is:
```bash
readonly OPTION VARIABLE(s)
```
- If the `-f` option is given, each variable refers to a shell function; 
- If `-a` is specified, each variable refers to an array of variables. 
- If no arguments are given, or if `-p` is supplied, a list of all read-only variables is displayed. 
- Using the `-p` option, the output can be reused as input.

## Array variables

Indirect declaration is done using the following syntax to declare a variable:
```bash
ARRAY[INDEXNR]=value
```
The `INDEXNR` is treated as an arithmetic expression that must evaluate to a positive number. 
Explicit declaration of an array is done using the declare built-in:
```bash
declare -a ARRAYNAME
```
Array variables may also be created using compound assignments in this format:
```bash
ARRAY=(value1 value2 ... valueN)
```
Remember that the `read` built-in provides the `-a` option, which allows for reading and assigning values for member variables of an array.
```bash
$ declare -a arr
$ read -a arr
one two three
$ echo $arr
one
$ echo ${arr[*]}
one two three
$ echo ${#arr[*]}
3
$ echo ${arr[*]#one}
two three
echo ${arr[*]#t}
one wo hree
$ echo ${arr[*]#t*}
one wo hree
$ echo ${arr[*]##t*}
one
```
In order to refer to the content of an item in an array, use **curly braces**. This is necessary, as you can see from the following example, to bypass the shell
interpretation of expansion operators. If the index number is `@` or `*`, all members of an array are referenced.
```bash
[bob in ~] ARRAY=(one two three) 
[bob in ~] echo ${ARRAY[*]}
one two three
[bob in ~] echo $ARRAY[*]
one[*]
[bob in ~] echo ${ARRAY[2]}
three
[bob in ~] ARRAY[3]=four
[bob in ~] echo ${ARRAY[*]}
one two three four
```
Referring to the content of a member variable of an array without providing an index number is the same as referring to the content of the **first element**, the one referenced with **index number zero**.

**Deleting array variables**

The `unset` built-in is used to destroy arrays or member variables of an array:

## Operations on variables
Using the `${#VAR}` syntax will calculate the number of characters in a variable. If VAR is "`*`" or "`@`", this value is substituted with the number of positional parameters or number of elements in an array in general.
```bash 
[bob in ~] echo $SHELL 
/bin/bash
[bob in ~] echo ${#SHELL} 
9
[bob in ~] ARRAY=(one two three)
[bob in ~] echo ${#ARRAY} 
3
```

## Transformations of variables

### Substitution
```bash
${VAR:-WORD}
```
If `VAR` is not defined or null, the expansion of `WORD` is substituted; otherwise the value of `VAR` is substituted:
```bash
[bob in ~] echo ${TEST:-test} 
test
[bob in ~] echo $TEST
[bob in ~] export TEST=a_string
[bob in ~] echo ${TEST:-test} 
a_string
[bob in ~] echo ${TEST2:-$TEST} 
a_string
[ -z "${COLUMNS:-}" ] && COLUMNS=80

```
If the hyphen (-) is replaced with the equal sign (=), the value is assigned to the parameter if it does not exist:

```bash
[bob in ~] echo $TEST2
[bob in ~] echo ${TEST2:=$TEST}
a_string
[bob in ~] echo $TEST2
a_string
```

The following syntax tests the existence of a variable. If it is not set, the expansion of WORD is printed to standard out and non-interactive shells quit. A demonstration:
```bash
 echo ${TESTVAR:?"There's so much I still wanted to do..."}
 echo "TESTVAR is set, we can proceed."
```

Using "+" instead of the exclamation mark sets the variable to the expansion of WORD; if it does not exist, nothing happens.

```bash
MacBook-Air:scripting michael$ echo $TEST2
aaaaa
MacBook-Air:scripting michael$ echo ${TEST2:+bbb}
bbb
MacBook-Air:scripting michael$ echo $TEST2
aaaaa
```

## Removing substrings
To strip a number of characters, equal to `OFFSET`, from a variable, use this syntax: 
```bash
${VAR:OFFSET:LENGTH}
```
```bash
[bob in ~] export STRING="thisisaverylongname" 
[bob in ~] echo ${STRING:4}
isaverylongname
[bob in ~] echo ${STRING:6:5} 
avery
```

`${VAR#WORD} and ${VAR##WORD}`

```bash
[bob in ~] echo ${ARRAY[*]} 
one two one three one four
[bob in ~] echo ${ARRAY[*]#one} 
two three four
[bob in ~] echo ${ARRAY[*]#t} 
one wo one hree one four
[bob in ~] echo ${ARRAY[*]#t*} 
one wo one hree one four
[bob in ~] echo ${ARRAY[*]##t*} 
one one one four
```

The opposite effect is obtained using "%" and "%%", as in this example below. WORD should match a trailing portion of string:

```bash
[bob in ~] echo $STRING 
thisisaverylongname
[bob in ~] echo ${STRING%name} 
thisisaverylong
```

## Replacing parts of variable names
This is done using the
```bash
${VAR/PATTERN/STRING}
```
or 
```bash
${VAR//PATTERN/STRING}
```

- The first form replaces only the **first match**, 
- the second replaces all matches of PATTERN with STRING:
```bash
[bob in ~] echo ${STRING/name/string} 
thisisaverylongstring
```


# Functions

Functions either use the syntax
```bash
function FUNCTIONNAME { COMMANDS; }
```
or
```bash
FUNCTIONNAME () { COMMANDS; }
```
**Common mistakes**
- The curly braces must be separated from the body by spaces, otherwise they are interpreted in the wrong way.
- The body of a function should end in a **semicolon** or **a newline**.

## Positional parameters in functions
However, the positional parameters passed to a function are not the same as the ones passed to a command or script.

The special parameter `#` that expands to the number of positional parameters is updated to reflect the change. Positional parameter `0` is unchanged. The Bash variable `FUNCNAME` is set to the name of the function, while it is executing.

If the `return` built-in is executed in a function, the function completes and execution resumes with the next command after the function call. When a function completes, the values of the positional parameters and the special parameter `#` are restored to the values they had prior to the function's execution. If a numeric argument is given to return, that status is returned.

```bash
#!/bin/bash
echo "This script demonstrates function arguments."
echo
echo "Positional parameter 1 for the script is $1."
echo
test ()
{
echo "Positional parameter 1 in the function is $1." 
RETURN_VALUE=$?
echo "The exit code of this function is $RETURN_VALUE." 
}
echo "Print return value in function:"
echo
echo $RETURN_VALUE
echo
test other_param
```
```
MacBook-Air:tests michael$ ./bash.sh arg1
This script demonstrates function arguments.

Positional parameter 1 for the script is arg1.

Print return value in function:



Positional parameter 1 in the function is other_param.
The exit code of this function is 0.
```

## Export function
```bash
$ fn(){ echo “Hello World”;} 
$ export -f fn
$ fn
Hello World
```

# Catching signals

Signal names can be found using `kill -l`.

- 1     SIGHUP  Hangup
- 2     SIGINT  Interrupt from keyboard
- 9     SIGKILL Kill signal
- 15    SIGTERM Termination signal (default)
- 17,19, 23 SIGSTO  Stop the process


## Traps

The syntax for the trap statement is straightforward: 
```bash
trap [COMMANDS] [SIGNALS]
```

- This instructs the trap command to catch the listed `SIGNALS`, which may be signal names with or without the SIG prefix, or signal numbers. 
- If a signal is `0 or EXIT`, the COMMANDS are executed when the shell exits. 
- If one of the signals is `DEBUG`, the list of COMMANDS is executed after every simple command. 
- A signal may also be specified as `ERR`; in that case COMMANDS are executed each time a simple command exits with a non-zero status. 
  - Note that these commands will not be executed when the non-zero exit status comes from part of an `if` statement, or from a `while` or `until` loop. 
  - Neither will they be executed if a logical `AND (&&)` or `OR (||)` result in a non-zero exit code, or when a command's return status is inverted using the `!` operator.
- The return status of the `trap` command itself is zero unless an invalid signal specification is encountered.

Here is a very simple example, catching `Ctrl+C `from the user, upon which a message is printed. When you try to kill this program without specifying the KILL signal, nothing will happen:

```bash
#!/bin/bash # traptest.sh
trap "echo Booh!" SIGINT SIGTERM
echo "pid is $$"
while : # This is the same as "while true".
do
    sleep 60 # This script is not really doing anything.
done
```

## Detecting when a variable is used

When debugging longer scripts, you might want to give a variable the trace attribute and `trap DEBUG` messages for that variable. Normally you would just declare a variable using an assignment like `VARIABLE=value`. Replacing the declaration of the variable with the following lines might provide valuable information about what your script is doing:

```bash
#!/bin/bash # traptest.sh
declare -t VARIABLE=value
trap "echo VARIABLE is being used here." DEBUG

echo $VARIABLE

while true; do
echo "Enter the while loop"
sleep 6
echo "Exit the while loop"
done

```
```
MacBook-Air:tests michael$ bash -x bash.sh 
+ declare -t VARIABLE=value
+ trap 'echo VARIABLE is being used here.' DEBUG
++ echo VARIABLE is being used here.
VARIABLE is being used here.
+ echo value
value
++ echo VARIABLE is being used here.
VARIABLE is being used here.
+ true
++ echo VARIABLE is being used here.
VARIABLE is being used here.
+ echo 'Enter the while loop'
Enter the while loop
++ echo VARIABLE is being used here.
VARIABLE is being used here.
+ sleep 6
```

