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
