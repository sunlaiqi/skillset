- [Tools](#tools)
  - [wc](#wc)
  - [cut](#cut)
  - [paste](#paste)
  - [sed](#sed)
  - [tr](#tr)
  - [grep](#grep)
  - [sort](#sort)
  - [uniq](#uniq)
- [Variables](#variables)
  - [Built-in Integer Arithmetic](#built-in-integer-arithmetic)
  - [The Double Quote](#the-double-quote)
  - [The Backslash](#the-backslash)
  - [The $(...)](#the-)
  - [The expr Command](#the-expr-command)
  - [The test Command](#the-test-command)
    - [Parentheses](#parentheses)
  - [`$*` vs `$@`](#-vs-)
- [The `for` Without the List](#the-for-without-the-list)
- [redirection](#redirection)
- [getopts](#getopts)
- [basename](#basename)
- [$$](#)
- [export -p](#export--p)
- [The exec Command](#the-exec-command)
- [The (...) and { ...; } Constructs](#the--and----constructs)
- [Another Way to Pass Variables to a Subshell](#another-way-to-pass-variables-to-a-subshell)
- [The TZ Variable](#the-tz-variable)
- [Parameter Substitution](#parameter-substitution)
- [Pattern Matching Constructs](#pattern-matching-constructs)
- [The set Command](#the-set-command)
- [The unset Command](#the-unset-command)
- [The eval Command](#the-eval-command)
- [The $! Variable](#the--variable)
- [Ignoring Signals](#ignoring-signals)
- [Resetting Traps](#resetting-traps)
- [In-line Input Redirection (here document)](#in-line-input-redirection-here-document)
- [Removing a Function Definition](#removing-a-function-definition)
- [The ENV File](#the-env-file)
- [Command-Line Editing](#command-line-editing)
- [Shell initialization files](#shell-initialization-files)
- [Special Characters](#special-characters)


# Tools

## wc
```
$ wc names 
5 7 27 names 
```

## cut 

```
$ who | cut –c1-8 # Extract the first 8 characters 
```


## paste 
The paste command is the inverse of cut 

## sed 

The `ed` utility is a line-oriented text editor. It is used to create, display, modify and otherwise manipulate text files. 
`sed` is a program used for editing data in a pipe or command sequence. It stands for `stream editor`. Unlike `ed`, `sed` cannot be used interactively, though its commands are similar. The general form of the sed command issed command file
```
# echo "intro Substitute Unix with UNIX"|sed 's/Unix/UNIX/'
intro Substitute UNIX with UNIX
```

## tr 

The `tr` filter is used to translate characters from standard input. The general form of the command is
```
tr from-chars to-chars 
```
The following shows how `tr` can be used to translate all letter `e’s` to `x’s`: 
```
# echo "hello world. She love him" | tr e x 
hxllo world. Shx lovx him
```
## grep 

`grep` allows you to search one or more files for a pattern you specify. The general format of this command is 
```
grep pattern files
```
```
$ grep -l 'Move_history' *.c List the files that contain Move_history 
$ grep -n 'Move_history' testch.c Precede matches with line numbers 
$ grep -v 'UNIX' intro Print all lines that don't contain UNIX 
```

## sort 

At its most basic, the `sort` command is really easy to understand: give it lines of input and it’ll sort them alphabetically, with the result appearing as its output:
```
$ sort names 
```
The `-u` option tells `sort` to eliminate duplicate lines from the output. 
```
$ sort -u names 
```

## uniq 

The `uniq` command is useful when you need to find or remove duplicate **lines** in a file. The basic format of the command is
```
uniq in_file out_file 
```
```
$ sort names | uniq -d # List duplicate lines
$ sort names | uniq –c # Count line occurrences 
```

# Variables and Parameters 

## Variable Substitution 

If `variable1` is the name of a variable, then `$variable1` is a **reference** to its value, the data item it contains. 

The only times a variable appears "naked" -- without the `$ prefix` -- is 
- when declared or assigned, 
- when unset, 
- when exported, 
- in an arithmetic expression within double parentheses `(( ... ))`, or 
- in the special case of a variable representing a signal. 
- Assignment may be with an `=` (as in `var1=27`), in a read statement, and 
- at the head of a loop `(for var2 in 1 2 3)`. 

Partial quoting vs Full quoting

- Enclosing a referenced value in double quotes (`" ... "`) does not interfere with variable substitution. This is called `partial quoting`, sometimes referred to as "`weak quoting`." 
- Using single quotes (`' ... '`) causes the variable name to be used literally, and no substitution will take place. This is `full quoting`, sometimes referred to as '`strong quoting`.' 

```bash
hello="A B C D"
# It is permissible to set multiple variables on the same line, 
#+ if separated by white space.
# Caution, this may reduce legibility, and may not be portable. 
var1=21 var2=22 var3=$V3
# Note that setting a variable to a null value is not the same as 
#+ unsetting it, although the end result is the same (see below). 
# Declaring, but not initializing it -- 
#+ same as setting it to a null value, 
# Escaping the whitespace also works. 
mixed_bag=2\ ---\ Whatever
#           ^    ^ Space after escape (\). 
echo "$mixed_bag" # 2 --- Whatever 
```
An uninitialized variable has a "null" value -- no assigned value at all (not zero!). 
```bash
if [ -z "$unassigned" ] 
then 
	echo "\$unassigned is NULL." 
fi # $unassigned is NULL. 
```
Using a variable before assigning a value to it may cause problems. It is nevertheless possible to perform arithmetic operations on an uninitialized variable. 
```bash
echo "$uninitialized" 		# (blank line)
let "uninitialized += 5" 	# Add 5 to it.
echo "$uninitialized" 		# 5

# Conclusion:
# An uninitialized variable has no value,
#+ however it evaluates as 0 in an arithmetic operation. 
```

## Variable Assignment 

`=`	the assignment operator (no space before and after)
Do not confuse this with `=` and `-eq`, which test, rather than assign!
Note that `=` can be either an assignment or a test operator, depending on context. 
```bash
# Assignment using 'let'let a=16+5
# In a 'for' loop (really, a type of disguised assignment):
echo -n "Values of \"a\" in the loop are: " 
for a in 7 8 9 11
do 
	echo -n "$a " 
done 
# In a 'read' statement (also a type of assignment): 
echo -n "Enter \"a\" "
read a
echo "The value of \"a\" is now $a." 
a=`echo Hello!` # Assigns result of 'echo' command to 'a' ...
echo $a
# Note that including an exclamation mark (!) within a
#+ command substitution construct will not work from the command-line, 
#+ since this triggers the Bash "history mechanism." 
# Inside a script, however, the history functions are disabled by default. 
```
```bash
# a=`echo Hello!`
-bash: !`: event not found
```


## Bash Variables Are Untyped 

Essentially, Bash variables are **character strings**, but, depending on context, Bash permits arithmetic operations and comparisons on variables. **The determining factor is whether the value of a variable contains only digits.** 
```bash
a=2334
let "a += 1" 
echo "a = $a " 	# a = 2335
b=${a/23/BB} 	# Substitute "BB" for “23".
				# This transforms $b into a string.
echo "b = $b" 	# b = BB35
declare -i b 	# Declaring it an integer doesn't help. 
echo "b = $b" 	# b = BB35 
let "b += 1" 	# BB35 + 1
echo "b = $b"	# b = 1			
                # Bash sets the "integer value" of a string to 0. 
c=BB34
echo "c = $c" 	# c = BB34 
d=${c/BB/23} 	# Substitute "23" for “BB".
				# This makes $d an integer.
echo "d = $d" 	# d = 2334
let "d += 1" 	# 2334 + 1
echo "d = $d"  	#d = 2335

# What about null variables?
e=''			# ... Or e="" ... Or e=
echo "e = $e" 	#e =
let "e += 1" 	# Arithmetic operations allowed on a null variable?
echo "e = $e" 	#e= 1
echo 			# Null variable transformed into an integer.

# What about undeclared variables?
echo "f = $f" 	#f =
let "f += 1" 	# Arithmetic operations allowed?
echo "f = $f" 	#f= 1
echo 			# Undeclared variable transformed into an integer.
#
# However ...
let "f /= $undecl_var" 	# Divide by zero?
#let: f /= : syntax error: operand expected (error token is " ") 
#Syntax error! Variable $undecl_var is not set to zero here! 
#
# But still …
let "f /= 0"
# let: f /= 0: division by 0 (error token is "0") 
# Expected behavior. 
```

## Special Variable Types 
```bash
args=$#     # Number of args passed. 
lastarg=${!args}    # Note: This is an *indirect reference* to $args ... 
# Or: 
lastarg=${!#} 
# This is an *indirect reference* to the $# variable.
# Note that lastarg=${!$#} doesn't work. 
```
If a script expects a command-line parameter but is invoked without one, this may cause a null variable assignment, generally an undesirable result. One way to prevent this is to append an extra character to both sides of the assignment statement using the expected positional parameter. 

```bash
variable1_=$1_ # Rather than variable1=$1
# This will prevent an error, even if positional parameter is absent. 
critical_argument01=$variable1_ 
# The extra character can be stripped off later, like so. variable1=${variable1_/_/}
# A more straightforward way of dealing with this is
#+ to simply test whether expected positional parameters have been passed. 
if [ -z $1 ]then 
exit $E_MISSING_POS_PARAM 
fi 
# However, as Fabian Kreutz points out,
#+ the above method may have unexpected side-effects. 
# A better method is parameter substitution:
# 	${1:-$DefaultVal}
```



# Variables 

## Built-in Integer Arithmetic 
The format for arithmetic expansion is 
```bash
$((expression)) 
```

where `expression` is an arithmetic expression using shell variables and operators. 
- Valid shell variables are those that contain numeric values (**leading and trailing whitespace is allowed**). 
- Valid operators are taken from the C programming language 
```bash
$ echo $(( 8#100 )) #100 octal (base 8) 64
```

## The Double Quote 

Double quotes work similarly to single quotes, except they’re less protective of their content: 
- single quotes tell the shell to ignore all enclosed characters, 
- double quotes say to ignore most. In particular, the following three characters are not ignored inside double quotes: 
  - Dollar signs ︎ 
  - Back quotes ︎ 
  - Backslashes 

## The Backslash 
Functionally, the backslash (used as a prefix) is equivalent to placing single quotes around a single character, though with a few minor exceptions. The backslash escapes the character that immediately follows it. The general format is 
`\c` where `c` is the character you want to quote. Any special meaning normally attached to thatcharacter is removed. Here is an example:
```
$ echo >
syntax error: 'newline or ;' unexpected 
$  echo \> 
>
$ echo "\^"
\^

```
**The Backslash Inside Double Quotes** 

If the backslash precedes any other character inside double quotes, the backslash is ignored by the shell and passed on to the program: 
```
$ echo "\$x"$x
$ echo "\ is the backslash character" 
```

`\` is the backslash character 
```
$ x=5
$ echo "The value of x is \"$x\"
"The value of x is "5"$ 
```

## The $(...) 

Constructused to replace back quote \`date\`
```
now=$(date) 
```

## The expr Command 
```
$ expr 1 + 23
```

note: each operator and operand given to `expr` must be separated by spaces to be properly understood. 
```
$ expr 1+2 
1+2
$ expr 17 * 6
expr: syntax error $
$ expr 17 \* 6
102
$ expr 4 / 2
2
```

## The test Command 

String Operators 
```
test "$name" = julio 
```
(Note `$name` must be quoted by “”) 

Note that test must see all operands (`$name` and `julio`) and operators (=) as separate arguments, meaning that they must be delimited by one or more whitespace characters. 

In fact, you can replace “=“ with “==“, but you don’t need space before and after “==“
```
test $name==julio
```
And it seems you don’t need to quote variables using “”.

An Alternative Format for test  

This can also be expressed in the alternative format as `[ expression ]`
Spaces must appear after the `[` and before the `]`. 

The Logical AND Operator `–a` 
The Logical OR Operator `–o` 

### Parentheses 

You can use parentheses in a `test` expression to alter the order of evaluation as needed; just make sure that the parentheses themselves are quoted because they have a special meaning to the shell. So to translate the earlier example into a `test` command, you would write 
```
[ \( "$count" -ge 0 \) -a \( "$count" -lt 10 \) ]
```

## `$*` vs `$@`

The shell replaces the value of `$*` with `$1, $2, ...` , but if you instead use the special shell variable "`$@`" the values will be passed with `"$1", "$2", ...` . The key difference is the **double quotes** around the `$@`: without them this variable behaves just like `$*`. 

# The `for` Without the List 

A special notation is recognized by the shell when writing `for` commands. If you omit the `in` element and its subsequent list 
```
for var 
do 
    command 
    command 
    ... 
done 
```

the shell automatically sequences through all the arguments typed on the command line, just as if you had written
```
for var in "$@" 
do 
	command 
	command 
	... 
done 
```

# redirection
```
grep da * 1>&2 
```

Here, the stdout portion of the command is sent to stderr, you may notice that in differen ways.
```
grep * 2>&1
```
        
Here, the stderr portion of the command is sent to stdout

This will place every output of a program to a file.
```
rm -f $(find / -name core) &> /dev/null 
```
```
command >&2 
```
The notation `>&` specifies output redirection to a file associated with the file descriptor that follows. 
Bash allows for both standard output and standard error to be redirected to the file whose name is the result of the expansion of FILE with this construct: 
```
&> FILE
```
This is the equivalent of `> FILE 2>&1` 

`<&-` and `>&-`

The sequence `>&-` has the effect of closing standard output. If preceded by a file descriptor, the associated file is closed instead. So writing
```
ls >&- 
```
causes the output from `ls` to go nowhere because standard output is closed by the shell before `ls` is executed. 

# getopts 

```bash
# process command options 
while getopts “:mt:n”: option 
do 
	case "$option" 
	in 
		m) mailopt=TRUE;;		
        t) interval=$OPTARG;;		
        n) num=$OPTARG;;		
        \?) echo "Usage: waitfor [-m] [-t n] user" 
			echo " -m means to be informed by mail" 					echo " -t means check every n secs."			
            exit 1;; 
	esac 
done 
# Make sure a user name was specified 
if [ "$OPTIND" -gt "$#" ]; then 
	echo "Missing user name!" 
	exit 2 
fi 
# OPTIND is the Option index, pointing to next argument
shiftcount=$((OPTIND – 1)) 
shift $shiftcount
user=$1 
```

`OPTIND` is initially set to 1 and is updated each time `getopts` returns to reflect the number of the next command line argument to be processed. 

# basename 

When `basename` is given a pathname, it will delete any prefix up to the last slash character and return the result. 
```
$ basename /Users/michael/Downloads/Resume-Michael-Sun.pdf
Resume-Michael-Sun.pdf 
```
# $$
Is the `PID`

# export -p

If you type `export -p`, you’ll get a list of the variables and their values exported by your shell 


# The exec Command 

Because the exec’ed program replaces the current one, there’s one less process hanging around, which helps the system run quickly. The startup time of an exec’ed program is quicker too, due to how Unix systems execute processes.

If you use `exec` to reassign standard input and later want to reassign it someplace else, you can simply invoke `exec` again. To reassign standard input back to the terminal, you would write
```
exec < /dev/tty
```

# The (...) and { ...; } Constructs 

Sometimes you want to group a set of commands together. For example, you may want to push a `sort` followed by your plot data program into the background. Not connected with a pipe; just two commands one after the other. 

It turns out that you can group a set of commands together by enclosing them in **parentheses** or **braces**. 
- The first form causes the commands to be executed by a subshell, 
- the latter form by the current shell. 

# Another Way to Pass Variables to a Subshell 
```
$ DBHOME=/uxn2/data DBID=452 dbrun 
```
Places the variables `DBHOME` and `DBID`, and their indicated values, into the environment of `dbrun`, then `dbrun` gets executed. These variables will not be known to the current shell, however, because they are only created for the execution of `dbrun`.

# The TZ Variable 
```
TZ="America/Tijuana" 
date
```
will show the current time in Tijuana, Mexico. 
```
$ TZ=GMT date
Fri Aug 20 15:15:36 GMT 2010
```

# Parameter Substitution 

**${parameter}**

`${parameter:-value}`
use the value of parameter if it is not null 

`${parameter:=value}` 
if `parameter` is null, not only is `value` used, but it is also assigned to parameter as well 

`${parameter:?value}` 
If parameter is not null, the shell substitutes its value; otherwise, the shell writes `value` to standard error and then exits 

`${parameter:+value}` 
This one substitutes `value` if parameter is not null; otherwise, it substitutes nothing.

# Pattern Matching Constructs 
```bash
$ var=testcase 
$ echo $var
testcase
$ echo ${var%e} # Remove e from right 
testcas
$ echo $var	# Variable is unchanged
testcase
$ echo ${var%s*e}
testca
$ echo ${var%%s*e}
te
$ echo ${var#?e}
stcase
$ echo ${var#*s}
tcase
$ echo ${var##*s}
e
$ echo ${var#test}
case
$ echo ${var#teas}
testcase
$
```

# The set Command 

The shell’s `set` command also serves two purposes: 
- it’s used both to set various shell options and 
- to reassign the positional parameters $1, $2, and so on... . 

**set -x**

You can turn off trace mode at any time simply by executing `set` with the `+x` option 

**set a b c**

- will assign `a to $1`, `b to $2`, and `c to $3`. 
- `$#` also gets set to 3 as appropriate for the new argument count. 

```bash
$ set one two three four 
$ echo $1:$2:$3:$4 
one:two:three:four
```

# The unset Command

Sometimes you may want to remove the definition of a variable from your environment. 

# The eval Command 

Its format is as follows: 
```bash
eval command-line 
```
where `command-line` is a normal command line that you would type at the terminal. When you put `eval` in front of it, however, the effect is that the shell scans the command line **twice** before executing it, which can be very useful if the script is building a command that needs to be invoked, among other purposes. 

But consider the following example without the use of `eval`: 
```bash
$ pipe="|"
$ ls $pipe wc -l
|: No such file or directory 
wc: No such file or directory 
-1: No such file or directory 
$ 
$ eval ls $pipe wc –l 
16 
```

# The $! Variable 

If you have only one process running in the background, then `wait` with no argument suffices. However, if you’re running more than one background command and you want to wait on the most recently launched, you can access the process ID of the most recent background command as the special variable `$!`. So the command 
```bash
wait $!
```


# Ignoring Signals 
```bash
trap "" SIGINT
```

- If you ignore a signal, all subshells also ignore that signal. 
- If you specify a signal handler action, however, all subshells will automatically take the default action on receipt of that signal, not the new code sequence. 

# Resetting Traps 

After you’ve changed the default action to be taken on receipt of a signal, you can change it back again with trap if you simply omit the first argument; so 
```bash
trap HUP INT 
```

# In-line Input Redirection (here document)

If the `<<` characters follow a command in the format command `<<word`, the shell uses the lines that follow as the input for command, until a line that contains just `word` is found.

**In-line input redirection—also referred to as here documents** 

To side-step all the issues with the shell interpreting the contents of the lines, use **backslash** on the end-of-document `word` instead:(following commands won’t be executed)
```bash
$ cat <<\FOOBAR
> \\\\ 
> `date`
> $HOME 
> FOOBAR 
\\\\ 
`date` 
$HOME 
$ 
```
You now know about the `<<\` sequence, but there’s another one that most modern shells understand: If the first character that follows the `<<` is a dash (-), any leading tab characters in the input will be removed by the shell. 


# Removing a Function Definition 

To remove the definition of a function from the shell, use the `unset` command with the `–f` option. 
```bash
$ unset –f nu 
```

# The ENV File 
  
When you start the shell, one of the first things it does is look in your environment for a variable called `ENV`. If it finds it and it’s non-null, the file specified by ENV will be executed, much like the `.profile` is executed when logging in.

# Command-Line Editing 

To turn on a line edit mode, use the `set` command with the `-o mode` option, where mode is either `vi` or `emacs`:
```bash
$ set -o vi 
```
Turn on vi mode

```bash
$ echo $0 
/bin/bash
```

To find the PID of the current instance of shell: 
```bash
echo "$$"
```

# Shell initialization files 

System-wide configuration files 
```
/etc/profile 
/etc/bashrc (bash specific)
```
Individual user configuration files 
```
~/.bash_profile 
```
This is the preferred configuration file for configuring user environments individually. 
```
~/.bash_login 
```
This file contains specific settings that are normally only executed when you log in to the system. 
```
~/.profile 
```
In the absence of `~/.bash_profile` and `~/.bash_login`, `~/.profile` is read. 
```
~/.bashrc 
```
use a non-login shell 
```
~/.bash_logout 
```


Array variables 
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


The opposite effect is obtained using "`%`" and "`%%`", as in this example below. `WORD` should match a trailing portion of string: 


# Special Characters 

What makes a character special? If it has a meaning beyond its literal meaning, a meta-meaning, then we refer to it as a special character. 
- `;`	**Command separator** [semicolon]. Permits putting two or more commands on the same line. 
- `;;`	**Terminator** in a case option [double semicolon]. 
- `;;&, ;&` 	**Terminators** in a case option (version 4+ of Bash).
- `“`	**partial quoting** [double quote]. "STRING" preserves (from interpretation) most of the special characters within STRING. 
- `‘`	**full quoting** [single quote]. 'STRING' preserves all special characters within STRING. This is a stronger form of quoting than "STRING". 
- `,`	**comma operator**. The comma operator links together a series of arithmetic operations. All are evaluated, but only the last one is returned. 
    ```bash
    let "t2 = ((a = 9, 15 / 3))"# Set "a = 9" and "t2 = 15 / 3" 
    ```
    The `comma` operator can also concatenate strings. 
    ```bash
    for file in /{,usr/}bin/*calc
    #.            ^ Find all executable files ending in "calc" 
    #.              in /bin and /usr/bin directories. 
    ```

- `,, ,` 	**Lowercase conversion** in parameter substitution (added in version 4 of Bash). 
- `\`	**escape** [backslash]. A quoting mechanism for single characters. 
- `\X` **escapes the character** `X`. This has the effect of "quoting" X, equivalent to 'X'. The \ may be used to quote " and ', so they are expressed literally. 
- \` 	**command substitution**. The \`command\` construct makes available the output of command for assignment to a variable. This is also known as backquotes or backticks. 
- `:`	**null command** [colon]. This is the shell equivalent of a "NOP" (no op, a do-nothing operation). It may be considered a synonym for the shell builtin true. The ":" command is itself a Bash builtin, and its exit status is true (0). 
    ```bash
    :
    echo $? 
    # 0 
    ```
    - **Endless loop**: 
        ```bash
        while : 
        do 
        operation-1 
        operation-2 
        ... 
        operation-n 
        done 
        ```
    - Provide a placeholder where a binary operation is expected. 
        ```bash
        : ${username=`whoami`}
        # ${username=`whoami`} Gives an error without the leading :
        # unless "username" is a command or builtin... 
        : ${1?"Usage: $0 ARGUMENT"} 
        # bash: 1: Usage: /bin/bash ARGUMENT
        ```
    - Provide a placeholder where a command is expected in a `here document`. 
    - Evaluate string of variables using parameter substitution 
        ```bash
        : ${HOSTNAME?} ${USER?} ${MAIL?}# Prints error message
        #+ if one or more of essential environmental variables not set. 
        # eg: bash: MAIL: parameter null or not set
        ```
    - **Variable expansion / substring replacement**. In combination with the `>` redirection operator, truncates a file to zero length, without changing its permissions. If the file did not previously exist, creates it. 
        ```bash
        : > data.xxx # File "data.xxx" now empty. 
        # Same effect as cat /dev/null >data.xxx
        # However, this does not fork a new process, since ":" is a builtin. 
        ```
        In combination with the `>>` redirection operator, has no effect on a pre-existing target file `(: >> target_file)`. If the file did not previously exist, creates it. 
    - A colon is acceptable as a **function name**.   
        ```bash
        :() { 
        echo "The name of this function is "$FUNCNAME" " 
        # Why use a colon as a function name?# It's a way of obfuscating your code. 
        }
        :
        # The name of this function is :
        ```
        This is not portable behavior, and therefore not a recommended practice. In fact, more recent releases of Bash do not permit this usage. An underscore `_` works, though. 
- !	**reverse (or negate)** the sense of a test or exit status [bang]. The `!` operator inverts the exit status of the command to which it is applied. It also inverts the meaning of a test operator. This can, for example, change the sense of equal ( `=` ) to not-equal ( `!=` ). The `!` operator is a Bash keyword. 
In a different context, the `!` also appears in *indirect variable references*. 
The actual notation is `\$$var`, usually preceded by an `eval` (and sometimes an `echo`). This is called an indirect reference. 
In yet another context, from the command line, the `!` invokes the Bash history mechanism. Note that within a script, the history mechanism is disabled. 
- ?	**test operator**. Within certain expressions, the ? indicates a test for a condition. In a double-parentheses construct, the ? can serve as an element of a C-style *trinary operator*. 
    ```bash
    (( condition?result-if-true:result-if-false ))
    ```
    Notice the whitespaces after and before the double-parentheses.
    In a parameter substitution expression, the ? tests whether a variable has been set. 
- `$`	**end-of-line**. In a regular expression, a "`$`" addresses the end of a line of text. 
    - `${ }`	Parameter substitution
    - `$' ... '`	Quoted string expansion. This construct expands single or multiple escaped octal or hex values into ASCII or Unicode characters. 
    - `$*`	All of the positional parameters, seen as a single word. `"$*"` must be quoted. 
    - `$@` 	Same as `$*`, but each parameter is a quoted string, that is, the parameters are passed on intact, without interpretation or expansion. This means, among other things, that each parameter in the argument list is seen as a separate word. Of course, `"$@"` should be quoted.
    - `$$` 	process ID variable. The `$$` variable holds the process ID of the script in which it appears. 
- ( )	
  - **command group**. 
    ```bash
    (a=hello; echo $a) 
    # It doesn’t matter if there is whitespace next to parentheses 
    ```
    A listing of commands within parentheses starts a subshell. 
    Variables inside parentheses, within the subshell, are not visible to the rest of the script. The parent process, the script, cannot read variables created in the child process, the subshell. 
  - **array initialization**. 
    ```bash
    Array=(element1 element2 element3) 
    ```
- {xxx,yyy,zzz,...} 	**Brace expansion**. 
    ```bash
    echo \"{These,words,are,quoted}\"   # " prefix and suffix
    # "These" "words" "are" "quoted"
    cat {file1,file2,file3} > combined_file# Concatenates the files file1, file2, and file3 into combined_file. 
    cp file22.{txt,backup}# Copies "file22.txt" to "file22.backup" 
    ```
    - A command may act upon a comma-separated list of file specs within braces. Filename expansion (globbing) applies to the file specs between the braces. 
    - No spaces allowed within the braces unless the spaces are quoted or escaped. 
        ```bash
        echo {file1,file2}\ :{\ A," B",' C'}
        # file1 : A file1 : B file1 : C file2 : A file2 : B file2 : C 
        ```
- {a..z} 	**Extended Brace expansion**. 
    ```bash
    echo {a..z} # a b c d e f g h i j k l m n o p q r s t u v w x y z # Echoes characters between a and z. 
    echo {0..3} # 0 1 2 3# Echoes characters between 0 and 3. 
    base64_charset=( {A..Z} {a..z} {0..9} + / = )# Initializing an array, using extended brace expansion. # From vladz's "base64.sh" example script. 
    ```
- {} 	**Block of code** [curly brackets]. Also referred to as an inline group, this construct, in effect, creates **an anonymous function** (a function without a name). However, unlike in a "standard" function, the variables inside a code block remain **visible** to the remainder of the script. 
Unlike a command group within `(parentheses)`, as above, a code block enclosed by `{braces}` will not normally launch a subshell. 
    ```bash
    bash$ { local a; a=123; } 
    bash: local: can only be used in a function

    a=123
    { a=321; }
    echo "a = $a" # a = 321 (value inside code block) 
    ```
    - The code block enclosed in braces may have I/O redirected to and from it. 
        ```bash
        File=/etc/fstab 
        {
        read line1
        read line2
        } < $File

        {
        Command1
        Command2
        …
        Commando
        } > $AFILE # Redirects outputs of everything in the block to file
        ```
    - placeholder for text. Used after `xargs -i` (replace strings option). The `{}` double curly brackets are a placeholder for output text. 
        ```bash
        ls . | xargs -i -t cp ./{} $1 
        #            ^^         ^^ 
        ```
- `{} \;`	**pathname**. Mostly used in find constructs. This is not a shell builtin. 
The "`;`" ends the `-exec` option of a find command sequence. It needs to be escaped to protect it from interpretation by the shell. 
- `[ ]` 	**test**. Test expression between `[ ]`. Note that `[` is part of the shell builtin test (and a synonym for it), not a link to the external command `/usr/bin/test`. 
- `[[ ]]` 	**test**. Test expression between `[[ ]]`. More flexible than the single-bracket `[ ]` test, this is a shell keyword. 
- `$[ ... ]` 	**integer expansion**. Evaluate integer expression between `$[ ]`. 
- `(( ))` 		**integer expansion**. Expand and evaluate integer expression between `(( ))`. 
- `> &> >& >> < <>` 	**redirection**. 
    - `command &>filename` redirects both the stdout and the stderr of command to filename. 
    - `command >&2` redirects stdout of command to stderr.
    - `[i]<>filename` opens file filename for reading and writing, and assigns file descriptor `i` to it. If filename does not exist, it is created. 
- **process substitution**. 
    ```bash
    (command)> 
    <(command) 
    ```
    Piping the stdout of a command into the stdin of another is a powerful technique. But, what if you need to pipe the stdout of multiple commands? This is where process substitution comes in. 
    Process substitution feeds the output of a process (or processes) into the stdin of another process.
  - **Template** 
    Command list enclosed within parentheses 
    ```bash
    >(command_list) 
    <(command_list) 
    ```
    Process substitution uses `/dev/fd/<n>` files to send the results of the process(es) within parentheses to another process. There is no space between the the "<" or ">" and the parentheses. 
- `<<` 	redirection used in a here document. 
- `<<<` 	redirection used in a here string. 
- `<, >` 	ASCII comparison. 
- `\<, \>` 	word boundary in a regular expression. 
- **pipe**. Passes the output (stdout) of a previous command to the input (stdin) of the next one, or to the shell. This is a method of chaining commands together. a classic method of interprocess communication, 
The stdout of each process in a pipe must be read as the stdin of the next. If this is not the case, the data stream will block, and the pipe will not behave as expected. 
    ```bash
    cat file1 file2 | ls -l | sort
    # The output from "cat file1 file2" disappears. 
    ```
    A pipe runs as a child process, and therefore cannot alter script variables. 
- `>|` 	**force redirection** (even if the noclobber option is set). This will forcibly overwrite an existing file. 
- `-`	**option, prefix**. Option flag for a command or filter. Prefix for an operator. Prefix for a default parameter in parameter substitution. 
- `--`	**The double-dash** `--` prefixes long (verbatim) options to commands.Used with a Bash builtin, it means the end of options to that particular command. 
This provides a handy means of removing files whose names begin with a dash. 
    ```bash
    bash$ ls -l-rw-r--r-- 1 bozo bozo 0 Nov 25 12:29 -badname 
    bash$ rm -- -badname 
    bash$ ls -l 
    total 0 
    ```
    The double-dash is also used in conjunction with `set`. 
    ```bash
    set -- $variable
    ```
- `-`	**redirection from/to stdin or stdout** [dash]. 
    ```bash
    bash$ cat - abc
    abc 
    ... 
    Ctl-D 
    ```
    Use `-` in `tar` command
    ```
    $ tar -cf - . |  (cd ../dest/directory; tar xpvf -)
    ```
    `tar cf - .`
    The 'c' option 'tar' archiving command creates a new archive, the 'f' (file) option, followed by '-' designates the target file as stdout, and do it in current directory tree ('.'). 
    `tar xpvf -`
    Unarchive ('x'), preserve ownership and file permissions ('p'), and send verbose messages to stdout ('v'),reading data from stdin ('f' followed by '-'). 
    Note that in this context the "-" is not itself a Bash operator, but rather an option recognized by certain UNIX utilities that write to stdout, such as `tar`, `cat`, etc. 
    By itself on the command-line, file fails with an error message. 
    Add a "-" for a more useful result. This causes the shell to await user input. 
    ```bash
    $ file -
    abc
    /dev/stdin: ASCII text
    ```

- `~+` 	**current working directory**. This corresponds to the `$PWD` internal variable. 
    ```bash
    $echo ~+ # (no $ prefix)
    ```
- `~-` 	**previous working directory**. This corresponds to the `$OLDPWD` internal variable. 
- `=~` 	**regular expression match**. This operator was introduced with version 3 of Bash. 
- `^, ^^` 	Uppercase conversion in parameter substitution (added in version 4 of Bash). 
    ```bash
    var=veryMixedUpVariable 
    echo ${var}		# veryMixedUpVariable
    echo ${var^}		# VeryMixedUpVariable
    #         *		First char --> uppercase. 


    echo ${var^^}		# VERYMIXEDUPVARIABLE 
    #         **	All chars --> uppercase. 
    echo ${var,}		# veryMixedUpVariable 
    #         *		First char --> lowercase. 
    echo ${var,,}		# verymixedupvariable 
    #         **		All chars --> lowercase. 
    ```
- **Whitespace**		functions as a separator between commands and/or variables. Whitespace consists of either `spaces`, `tab`s, `blank lines`, or any combination thereof. 
    - **Definition**: A field is a discrete chunk of data expressed as a string of consecutive characters. Separating each field from adjacent fields is either whitespace or some other designated character (often determined by the **$IFS**). In some contexts, a field may be called a record. 
    UNIX filters can target and operate on whitespace using the POSIX character class `[:space:]`. 
    `[:space:]` matches whitespace characters (space and horizontal tab).

# Quoting 

## Quoting Variables 

When referencing a variable, it is generally advisable to enclose its name in double quotes. 
```bash
List="one two three" 
for a in $List	# Splits the variable in parts at whitespace. 

do
  echo "$a"
done
# one
# two
# three
echo "---" 
for a in "$List"	# Preserves whitespace in a single variable. 
do #     ^     ^
  echo "$a"
done
# one two three

variable2="" # Empty. 
COMMAND $variable2 $variable2 $variable2
# Executes COMMAND with no arguments. 
COMMAND "$variable2" "$variable2" "$variable2"
# Executes COMMAND with 3 empty arguments. 
COMMAND "$variable2 $variable2 $variable2"
# Executes COMMAND with 1 argument (2 spaces). 
IFS='\' 
echo $var 	# '(] {}$"	\ converted to space. Why? 
echo "$var" 	# '(]\{}$"
```

## Escaping 

Escaping is a method of **quoting single characters**. The escape (`\`) preceding a character tells the shell to interpret that character literally. 
The `$' ... '` quoted string-expansion construct is a mechanism that uses escaped octal or hex values to assign ASCII characters to variables, e.g., `quote=$'\042'`. 
```bash
echo "\v\v\v\v" # Prints \v\v\v\v literally.
# Use the -e option with 'echo' to print escaped characters. 
echo "VERTICAL TABS"
echo -e "\v\v\v\v" # Prints 4 vertical tabs. 
echo "QUOTATION MARK"
echo -e "\042" # Prints " (quote, octal ASCII character 42). 
# The $'\X' construct makes the -e option unnecessary. 
echo; echo "NEWLINE and (maybe) BEEP" echo $'\n' # Newline.
echo $'\a' # Alert (beep). 
# May only flash, not beep, depending on terminal. 
# Assigning ASCII characters to a variable.
# ----------------------------------------
quote=$'\042' # " assigned to a variable.
echo "$quote Quoted string $quote and this lies outside the quotes." 
# " Quoted string " and this lies outside the quotes.
# Concatenating ASCII chars in a variable. 
triple_underline=$'\137\137\137'	# 137 is octal ASCII code for '_'. 
echo "$triple_underline UNDERLINE $triple_underline" 
# ___ UNDERLINE ___
ABC=$'\101\102\103\010' # 101, 102, 103 are octal A, B, C. 
echo $ABC 
# ABC
echo "\" 	# Invokes secondary prompt from the command-line. 
> 
# In a script, gives an error message. 

variable=\
echo "$variable" 
	#  Will not work - gives an error message: 
	#  test.sh: : command not found 
	#  A "naked" escape cannot safely be assigned to a variable.
```


# Exit and Exit Status 
When a script ends with an exit that has no parameter, the exit status of the script is the exit status of the last command executed in the script (previous to the exit). 

The equivalent of a bare `exit` is `exit $?` or even just omitting the exit. 
The `!`, the logical not qualifier, reverses the outcome of a test or command, and this affects its exit status. 
```bash
true # The "true" builtin.
echo "exit status of \"true\" = $?" # 0 
! true
echo "exit status of \"! true\" = $?" # 1
# Note that the "!" needs a space between it and the command.
# !true leads to a "command not found" error
#
# The '!' operator prefixing a command invokes the Bash history mechanism. 
true
!true
# No error this time, but no negation either. 
# It just repeats the previous command (true). 
```

# Tests 

Again, note that the exit status of an arithmetic expression is not an error value. 
```bash
var=-2 && (( var+=2 ))
echo $? # 1 
var=-2 && (( var+=2 )) && echo $var
# Will not echo $var! 
```
```
if [ -x "$filename" ]; then 
```
The `if test condition-true` construct is the exact equivalent of if `[ condition-true ]`. 
As it happens, the left bracket, `[` , is a token which invokes the `test` command. The closing right bracket, `]` , in an if/test should not therefore be strictly necessary, however newer versions of Bash require it. 

The `test` command is a Bash builtin which tests file types and compares strings. Therefore, in a Bash script, `test` does not call the external `/usr/bin/test` binary, which is part of the sh-utils package. Likewise, `[` does not call `/usr/bin/[`, which is linked to `/usr/bin/test`. 
```bash
bash$ type test
test is a shell builtin 
bash$ type '['
[ is a shell builtin 
bash$ type '[['
[[ is a shell keyword 
bash$ type ']]'
]] is a shell keyword 
bash$ type ']'
bash: type: ]: not found 
```

**No filename expansion** or word splitting takes place between `[[` and `]]`, but there is parameter expansion and command substitution. 
```bash
file=/etc/passwd 
if [[ -e $file ]] 
then 
	echo "Password file exists." 
fi 
```
- Using the `[[ ... ]]` test construct, rather than `[ ... ]` can prevent many logic errors in scripts. For example, the `&&`, `||`, `<`, and `>` operators work within a `[[ ]]` test, despite giving an error within a `[ ]` construct. 
- Arithmetic evaluation of `octal / hexadecimal` constants takes place automatically within a `[[ ... ]]` construct. 
- Following an `if`, neither the `test` command nor the test brackets ( `[ ]` or `[[ ]]` ) are strictly necessary. 
- The "`if COMMAND`" construct returns the exit status of `COMMAN`D. 
- The `(( ))` construct expands and evaluates an arithmetic expression. If the expression evaluates as **zero**, it returns an **exit status of 1**, or "false". A non-zero expression returns an exit status of 0, or "true". This is in marked contrast to using the `test` and `[ ]` constructs previously discussed. 
- 

## Other Comparison Operators 

- `<`	is less than (within double parentheses) 
	`(("$a" < "$b"))`

- string comparison 
    - `=`   is equal to 
        ```bash
        if [ "$a" = "$b" ]
        ```
        Note the whitespace framing the =. 
        ```bash
        if [ "$a"="$b" ] 
        ```
        is not equivalent to the above. 
    - `==`  is equal to
        ```bash
        if [ "$a" == "$b" ]
        ```
        This is a synonym for `=`. 

    - `<` 	is less than, in ASCII alphabetical order
        ```bash
        if [[ "$a" < "$b" ]]
        if [ "$a" \< "$b" ] 
        ```
    - `-z` 	string is null, that is, has zero length 
    - `-n`	string is not null. 
- compound comparison 
    - -a
    logical **and** 
        ```bash
        exp1 -a exp2 
        ```
        returns `true` if both exp1 and exp2 are `true`.
    - -o 
    logical **or**
        ```bash
        exp1 -o exp2 
        ```
        returns `true` if either exp1 or exp2 is `true`. 

These are similar to the Bash comparison operators `&&` and `||`, used within double brackets. 
`[[ condition1 && condition2 ]]` 

# Operations and Related Topics 

## Operators 

Bash does not understand floating point arithmetic. It treats numbers containing a decimal point as strings. 

```bash
$ a=1.5 
$ let "b = $a + 1.3" # Error.
-bash: let: b = 1.5 + 1.3: syntax error: invalid arithmetic operator (error token is ".5 + 1.3")
$ echo "b = $b"
b = 
```

**bitwise operators**. 
The bitwise operators seldom make an appearance in shell scripts. Their chief use seems to be manipulating and testing values read from ports or sockets. "Bit flipping" is more relevant to compiled languages, such as C and C++, which provide direct access to system hardware. 
bitwise operators 

- `<<`	bitwise left shift (multiplies by 2 for each shift position) 
- `<<=`  	left-shift-equal 
    ```bash
    let "var <<= 2" 
    ``
    results in `var` left-shifted 2 bits (multiplied by 4) 
- `>>` 	bitwise right shift (divides by 2 for each shift position) 
- `>>=` 	right-shift-equal (inverse of <<=) 
- `&`	bitwise AND 
- `&=`	bitwise AND-equal 
- `|`   bitwise OR 
- `|=`	bitwise OR-equal 
- `~`   bitwise NOT 
- `^`   bitwise XOR 
- `^=`	bitwise XOR-equal 

**logical (boolean) operators**

- `!`	NOT 
    ```bash
    if [ ! -f $FILENAME ] 
    then 
    ... 
    ```
- `&&`	AND 
    ```bash
    if [ $condition1 ] && [ $condition2 ]
    # Same as: 
    if [ $condition1 -a $condition2 ]
    # Returns true if both condition1 and condition2 hold true... 
    if [[ $condition1 && $condition2 ]] 
    # Also works.
    # Note that && operator not permitted inside brackets 
    #+ of [ ... ] construct. 
    ```

- `||`	OR 
    ```bash
    if [ $condition1 ] || [ $condition2 ]
    # Same as: 
    if [ $condition1 -o $condition2 ]
    # Returns true if either condition1 or condition2 holds true... 
    if [[ $condition1 || $condition2 ]] 
    # Also works.
    # Note that || operator not permitted inside brackets 
    #+ of a [ ... ] construct. 
    ```

The `&&` and `||` operators also find use in an arithmetic context.
```bash 
bash$ echo $(( 1 && 2 )) $((3 && 0)) $((4 || 0)) $((0 || 0)) 
1 01 0 
```

**miscellaneous operators** 

- `,`	Comma operator
  The comma operator chains together two or more arithmetic operations. All the operations are evaluated (with possible side effects. 
    ```bash
    let "t1 = ((5 + 3, 7 - 1, 15 - 4))"
    echo "t1 = $t1" ^^^^^^ 
    # t1 = 11
    # Here t1 is set to the result of the last operation. Why? 
    let "t2 = ((a = 9, 15 / 3))" 
    # Set "a" and calculate "t2". 
    echo "t2 = $t2 a = $a" 
    # t2 = 5 a = 9 
    ```

## Numerical Constants 

- A shell script interprets a number as **decimal (base 10)**, unless that number has a special prefix or notation. 
- A number preceded by a `0` is **octal (base 8)**. 
- A number preceded by `0x` is **hexadecimal (base 16)**. 
- A number with an embedded `#` evaluates as `BASE#NUMBER` (with range and notational restrictions). 
    ```bash
    # Octal: numbers preceded by '0' (zero) 
    let "oct = 032"
    echo "octal number = $oct"	
    # 26
    # Expresses result in decimal. 
    # Hexadecimal: numbers preceded by '0x' or '0X' 
    let "hex = 0x32"
    echo "hexadecimal number = $hex" 
    # 50 
    echo $((0x9abc)) 
    # 39612
    # Other bases: BASE#NUMBER
    #  BASE between 2 and 64. 
    #  NUMBER must use symbols within the BASE range, see below. 
    let "bin = 2#111100111001101" 
    echo "binary number = $bin" 	
    # 31181 
    let "b32 = 32#77"
    echo "base-32 number = $b32" 	
    # 231 
    let "b64 = 64#@_"
    echo "base-64 number = $b64"	
    # 4031
    # This notation only works for a limited range (2 - 64) of ASCII characters. 
    # 10 digits + 26 lowercase characters + 26 uppercase characters + @ + _ 
    ```

## The Double-Parentheses Construct 
Similar to the `let` command, the `(( ... ))` construct permits arithmetic expansion and evaluation. In its simplest form, `a=$(( 5 + 3 ))` would set `a` to `5 + 3`, or `8`. However, this double-parentheses construct is also a mechanism for allowing C-style manipulation of variables in Bash, for example, `(( var++ ))`. 
```bash
(( t = a<45?7:11 )) # C-style trinary operator. 
```

