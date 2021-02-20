- [3 Basic Shell Features](#3-basic-shell-features)
  - [3.1 Shell Syntax](#31-shell-syntax)
    - [3.1.1 Shell Operation](#311-shell-operation)
    - [3.1.2 Quoting](#312-quoting)
      - [3.1.2.1 Escape Character](#3121-escape-character)
      - [3.1.2.2 Single Quotes](#3122-single-quotes)
      - [3.1.2.3 Double Quotes](#3123-double-quotes)
      - [3.1.2.4 ANSI-C Quoting](#3124-ansi-c-quoting)
      - [3.1.2.5 Locale-Specific Translation](#3125-locale-specific-translation)
    - [3.1.3 Comments](#313-comments)
  - [3.2 Shell Commands](#32-shell-commands)
    - [3.2.1 Reserved Words](#321-reserved-words)
    - [3.2.2 Simple Commands](#322-simple-commands)
    - [3.2.3 Pipelines](#323-pipelines)
    - [3.2.4 Lists of Commands](#324-lists-of-commands)
    - [3.2.5 Compound Commands](#325-compound-commands)
      - [3.2.5.1 Looping Constructs](#3251-looping-constructs)
      - [3.2.5.2 Conditional Constructs](#3252-conditional-constructs)
      - [3.2.5.3 Grouping Commands](#3253-grouping-commands)
    - [3.2.6 Coprocesses](#326-coprocesses)
    - [3.2.7 GNU Parallel](#327-gnu-parallel)
  - [3.3 Shell Functions](#33-shell-functions)
  - [3.4 Shell Parameters](#34-shell-parameters)
    - [nameref](#nameref)
    - [3.4.1 Positional Parameters](#341-positional-parameters)
    - [3.4.2 Special Parameters](#342-special-parameters)
      - [`*` `($*)`](#-)
      - [`@` `($@)`](#--1)
      - [`#` `($#)`](#--2)
      - [`? ($?)`](#--3)
      - [`- ($-, a hyphen.)`](#----a-hyphen)
      - [`$ ($$)`](#--4)
      - [`! ($!)`](#--5)
      - [`0 ($0)`](#0-0)
  - [3.5 Shell Expansions](#35-shell-expansions)
    - [3.5.1 Brace Expansion](#351-brace-expansion)
    - [3.5.2 Tilde Expansion](#352-tilde-expansion)
    - [3.5.3 Shell Parameter Expansion](#353-shell-parameter-expansion)


# 3 Basic Shell Features

## 3.1 Shell Syntax

When the shell reads input, it proceeds through a sequence of operations. If the input indicates the beginning of a comment, the shell ignores the comment symbol (‘#’), and the rest of that line.

Otherwise, roughly speaking, the shell reads its input and divides the input into words and operators, employing the quoting rules to select which meanings to assign various words and characters.

The shell then parses these tokens into commands and other constructs, removes the special meaning of certain words or characters, expands others, redirects input and output as needed, executes the specified command, waits for the command’s exit status, and makes that exit status available for further inspection or processing.

### 3.1.1 Shell Operation

The following is a brief description of the shell’s operation when it reads and executes a command. Basically, the shell does the following:

1. Reads its input from a file, from a string supplied as an argument to the `-c` invocation optio, or from the user’s terminal.
2. Breaks the input into **words** and **operators**, obeying the quoting rules described in Section 3.1.2 [Quoting]. These **tokens** are separated by metacharacters. Alias expansion is performed by this step.
3. Parses the **tokens** into simple and compound commands.
4. Performs the various shell expansions, breaking the expanded tokens into lists of **filenames**, and **commands** and **arguments**.
5. Performs any necessary redirections, and removes the redirection operators and their operands from the argument list.
6. Executes the command.
7. Optionally waits for the command to complete and collects its exit status.


### 3.1.2 Quoting

Quoting is used to remove the special meaning of certain characters or words to the shell.

There are three quoting mechanisms: the **escape character**, **single quotes**, and **double quotes**.

#### 3.1.2.1 Escape Character

A non-quoted backslash ‘\’ is the Bash escape character. It preserves the **literal value** of the next character that follows, with the exception of newline. If a `\newline` pair appears, and the backslash itself is not quoted, the `\newline` is treated as a line continuation (that is, it is removed from the input stream and effectively ignored).

#### 3.1.2.2 Single Quotes

Enclosing characters in single quotes (‘’’) preserves the literal value of each character within the quotes. A single quote may not occur between single quotes, even when preceded by a backslash.

#### 3.1.2.3 Double Quotes

Enclosing characters in double quotes (‘"’) preserves the literal value of all characters within the quotes, with the exception of `‘$’, ‘‘’, ‘\’`, and, when history expansion is enabled, ‘!’. When the shell is in posix mode, the `‘!’` has no special meaning within double quotes, even when history expansion is enabled. The characters `‘$’` and `‘‘’` retain their special meaning within double quotes. 

The backslash retains its special meaning only when followed by one of the following characters: `‘$’, ‘‘’, ‘"’, ‘\’`, or `newline`. Within double quotes, backslashes that are followed by one of these characters are removed. Backslashes preceding characters without a special meaning are left unmodified. A double quote may be quoted within double quotes by preceding it with a backslash. If enabled, history expansion will be performed unless an `‘!’` appearing in double quotes is escaped using a backslash. The backslash preceding the `‘!’` is not removed.

The special parameters `‘*’` and `‘@’` have special meaning when in double quotes.

#### 3.1.2.4 ANSI-C Quoting

Words of the form `$’string’` are treated specially. The word expands to string, with backslash-escaped characters replaced as specified by the ANSI C standard. Backslash escape sequences, if present, are decoded as follows:
```
\a      alert (bell)
\b      backspace
\e
\E      an escape character (not ANSI C)
\f      form feed
\n      newline
\r      carriage return
\t      horizontal tab
\v      vertical tab
\\      backslash
\’      single quote
\"      double quote
\?      question mark
\nnn    the eight-bit character whose value is the octal value nnn (one to three octal digits)
\xHH    the eight-bit character whose value is the hexadecimal value HH (one or two hex digits)
\uHHHH  the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value HHHH (one to four hex digits)
\UHHHHHHHH
        the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value HHHHHHHH (one to eight hex digits)
\cx     a control-x character
```
The expanded result is single-quoted, as if the dollar sign had not been present.

#### 3.1.2.5 Locale-Specific Translation

A double-quoted string preceded by a dollar sign (`‘$’`) will cause the string to be translated according to the current locale. The **gettext** infrastructure performs the message catalog lookup and translation, using the `LC_MESSAGES` and `TEXTDOMAIN` shell variables. If the current locale is `C` or `POSIX`, or if there are no translations available, the dollar sign is ignored. If the string is translated and replaced, the replacement is double-quoted.

If you use the `TEXTDOMAIN` variable, you may need to set the `TEXTDOMAINDIR` variable to the location of the message catalog files. Still others use both variables in this fashion: `TEXTDOMAINDIR/LC_MESSAGES/LC_MESSAGES/TEXTDOMAIN.mo`.

### 3.1.3 Comments

In a non-interactive shell, or an interactive shell in which the **interactive_comments** option to the `shopt` builtin is enabled, a word beginning with `‘#’` causes that word and all remaining characters on that line to be ignored.

The `interactive_comments` option is on by default in interactive shells.

## 3.2 Shell Commands

### 3.2.1 Reserved Words

The following words are recognized as reserved when unquoted and the **first word** of a command
```
if then elif else fi
for in 
case esac 
{       }
time 
until while do done 
coproc 
select 
function
[[      ]] 
!
```
**in** is recognized as a reserved word if it is the **third word** of a **case** or **select** command. **in** and **do** are recognized as reserved words if they are the **third word** in a **for** command.

### 3.2.2 Simple Commands

The return status of a simple command is its exit status as provided by the posix 1003.1 `waitpid` function, or `128+n` if the command was terminated by `signal n`.

### 3.2.3 Pipelines

A pipeline is a sequence of one or more commands separated by one of the control operators `‘|’` or `‘|&’`.

The format for a pipeline is
```bash
[time [-p]] [!] command1 [ | or |& command2 ] ...
```
This connection is performed before any redirections specified by the command.

If `‘|&’` is used, command1’s standard error, in addition to its standard output, is connected to command2’s standard input through the pipe; it is shorthand for `2>&1 |`. This implicit redirection of the standard error to the standard output is performed after any redirections specified by the command.

The reserved word **time** causes timing statistics to be printed for the pipeline once it finishes. The statistics currently consist of **elapsed (wall-clock)** time and **user** and **system** time consumed by the command’s execution. The `-p` option changes the output format to that specified by posix. When the shell is in posix mode, it does not recognize `time` as a reserved word if the next token begins with a `‘-’`. The `TIMEFORMAT` variable may be set to a format string that specifies how the timing information should be displayed. The use of `time` as a reserved word permits the timing of shell builtins, shell functions, and pipelines. **An external time command** cannot time these easily.


When the shell is in posix mode, `time` may be followed by a `newline`. In this case, the shell displays the `total user` and `system` time consumed by the shell and its children. The `TIMEFORMAT` variable may be used to specify the format of the time information.

If the pipeline is not executed asynchronously, the shell waits for all commands in the pipeline to complete.

**Each command in a pipeline is executed in its own subshell, which is a separate process**.

If the `lastpipe` option is enabled using the `shopt` builtin, the last element of a pipeline may be run by the shell process.

The exit status of a pipeline is the exit status of the last command in the pipeline, unless the `pipefail` option is enabled. If `pipefail` is enabled, the pipeline’s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully. If the reserved word `‘!’` precedes the pipeline, the exit status is the logical negation of the exit status as described above. The shell waits for all commands in the pipeline to terminate before returning a value.

### 3.2.4 Lists of Commands

A `list` is a sequence of one or more pipelines separated by one of the operators `‘;’, ‘&’, ‘&&’, or ‘||’`, and optionally terminated by one of `‘;’, ‘&’`, or a newline.

Of these list operators, `‘&&’` and `‘||’` have equal precedence, followed by `‘;’` and `‘&’`, which have equal precedence.

A sequence of one or more `newlines` may appear in a list to delimit commands, equivalent to a `semicolon`.

If a command is terminated by the control operator `‘&’`, the shell executes the command **asynchronously** in a subshell. This is known as executing the command in the **background**, and these are referred to as **asynchronous commands**. The shell does not wait for the command to finish, and the **return status is 0 (true)**. When job control is not active, the standard input for asynchronous commands, in the absence of any explicit redirections, is redirected from `/dev/null`.

Commands separated by a `‘;’` are executed sequentially; the shell waits for each command to terminate in turn. The return status is the exit status of the last command executed.

`AND` and `OR` lists are sequences of one or more pipelines separated by the control operators `‘&&’` and `‘||’`, respectively. `AND` and `OR` lists are executed with **left associativity**.

An `AND` list has the form 
```bash
command1 && command2
```
`command2` is executed if, and only if, `command1` returns an exit status of zero (success). 

An `OR` list has the form
```bash
command1 || command2
```
`command2` is executed if, and only if, `command1` returns a non-zero exit status.

The return status of `AND` and `OR` lists is the exit status of the last command executed in the list.

### 3.2.5 Compound Commands

Compound commands are the shell programming language constructs. Each construct begins with a reserved word or control operator and is terminated by a corresponding reserved word or operator.

Any redirections associated with a compound command apply to all commands within that compound command unless explicitly overridden.

Bash provides looping constructs, conditional commands, and mechanisms to group commands and execute them as a unit.

#### 3.2.5.1 Looping Constructs

The syntax of the **until** command is:
```bash
until test-commands; do consequent-commands; done
```

The syntax of the **while** command is:
```bash
while test-commands; do consequent-commands; done
```

The syntax of the **for** command is:
```bash
for name [ [in [words ...] ] ; ] do commands; done
```
If ‘in words’ is not present, the `for` command executes the commands once for each positional parameter that is set, as if ‘in "$@"’ had been specified.

An alternate form of the `for` command is also supported:
```bash
for (( expr1 ; expr2 ; expr3 )) ; do commands ; done
```
- First, the arithmetic expression `expr1` is evaluated according to the rules described below. 
- The arithmetic expression `expr2` is then evaluated repeatedly until it evaluates to zero. 
- Each time `expr2` evaluates to a non-zero value, commands are executed and the arithmetic expression `expr3` is evaluated. 
- If any expression is omitted, it behaves as if it evaluates to 1.

The **break** and **continue** builtins may be used to control loop execution.

#### 3.2.5.2 Conditional Constructs

**if** 

The syntax of the `if` command is:

```bash
if test-commands; then 
  consequent-commands;
[elif more-test-commands; then 
  more-consequents;]
[else alternate-consequents;] 
fi
```

**case** 

The syntax of the case command is:

```bash
case word in
  [ [(] pattern [| pattern]...) command-list ;;]...
esac
```

- If the `nocasematch` shell option is enabled, the match is performed without regard to the case of alphabetic characters. The ‘|’ is used to separate multiple patterns, and the ‘)’ operator terminates a pattern list. A list of patterns and an associated command-list is known as a **clause**.
- Each clause must be terminated with ‘;;’, ‘;&’, or ‘;;&’.
- The `word` undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal before matching is attempted.
- Each `pattern` undergoes tilde expansion, parameter expansion, command substitution, and arithmetic expansion.
- The first pattern that matches determines the command-list that is executed.
- It’s a common idiom to use ‘*’ as the final pattern to define the default case, since that pattern will always match.
- If the ‘;;’ operator is used, no subsequent matches are attempted after the first pattern match.
- Using ‘;&’ in place of ‘;;’ causes execution to continue with the command-list associated with the next `clause`, if any.
- Using ‘;;&’ in place of ‘;;’ causes the shell to test the patterns in the next `clause`, if any, and execute any associated command-list on a successful match, continuing the case statement execution as if the pattern list had not matched.
- The return status is zero if no pattern is matched. Otherwise, the return status is the exit status of the command-list executed.

**select**

The `select` construct allows the easy generation of menus. It has almost the same syntax as the `for` command:
```bash
select name [in words ...]; do commands; done
```

- The list of words following in is expanded, generating a list of items. 
- The set of expanded `words` is printed on the standard error output stream, each preceded by a number. 
- If the ‘in words’ is omitted, the positional parameters are printed, as if ‘in "$@"’ had been specified.
- The PS3 prompt is then displayed and a line is read from the standard input.
- If the line consists of a number corresponding to one of the displayed words, then the value of name is set to that word.
- If the line is empty, the words and prompt are displayed again.
- If `EOF` is read, the select command completes.
- Any other value read causes name to be set to `null`. 
- The line read is saved in the variable `REPLY`.
- The `commands` are executed after each selection until a `break` command is executed, at which point the `select` command completes.

Here is an example that allows the user to pick a filename from the current directory, and displays the name and index of the file selected.
```bash
     select fname in *;
     do
     echo you picked $fname \($REPLY\)
     break;
     done
```
Execute it on Ubuntu:
```
ubuntu@primary:~/effectivec$ bash select.sh 
1) atoi			      6) copying.c	        11) feature_test_macros	    16) grep.c		    21) testgrub.sh
2) atoi.c		      7) count_array	      12) feature_test_macros.c	  17) hello		      22) wc
3) constants		  8) count_array.c	    13) fsize.c		              18) hello.c		    23) wc.c
4) constants.c		9) execl_eg		        14) gmon.out		            19) hellogp
5) copying		    10) execl_eg.c	      15) grep			              20) select.sh
#? 1
you picked atoi (1)
```

**`(( expression ))`**

- The arithmetic expression is evaluated according to the rules described below (same as in the C language). 
- If the value of the expression is non-zero, the return status is 0; otherwise the return status is 1. This is exactly equivalent to 
```bash
let "expression"
```

**`[[ expression ]]`**

- Return a status of 0 or 1 depending on the evaluation of the conditional expression expression.
- Expressions are composed of the primaries
- Word splitting and filename expansion are not performed on the words between the `[[` and `]]`;
- tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution, and quote removal are performed.
- Conditional operators such as ‘-f’ must be unquoted to be recognized as primaries.
- When used with `[[`, the ‘<’ and ‘>’ operators sort lexicographically using the current locale.
- When the ‘==’ and ‘!=’ operators are used, the string to the right of the operator is considered a pattern and matched according to the rules described in Pattern Matching as if the `extglob` shell option were enabled.
- The ‘=’ operator is identical to ‘==’.
- If the `nocasematch` shell option is enabled, the match is performed without regard to the case of alphabetic characters. 
- The return value is 0 if the string matches (‘==’) or does not match (‘!=’) the pattern, and 1 otherwise. 
- Any part of the pattern may be quoted to force the quoted portion to be matched as a string.
- An additional binary operator, ‘=~’ (regular expression match), is available, with the same precedence as ‘==’ and ‘!=’.
  - When it is used, the string to the right of the operator is considered a posix extended regular expression and matched accordingly (using the posix `regcomp` and `regexec` interfaces usually described in regex(3)).
  - If the regular expression is syntactically incorrect, the conditional expression’s return value is 2.
  - If the `nocasematch` shell option is enabled, the match is performed without regard to the case of alphabetic characters. 
  - Any part of the pattern may be quoted to force the quoted portion to be matched as a string.
  - If the pattern is stored in a shell variable, quoting the variable expansion forces the entire pattern to be matched as a string.
  - The pattern will match if it matches any part of the string. 
  - Anchor the pattern using the ‘^’ and ‘$’ regular expression operators to force it to match the entire string. 
  - The array variable `BASH_REMATCH` records which parts of the string matched the pattern. The element of `BASH_REMATCH` with index 0 contains the portion of the string matching the entire regular expression. Substrings matched by parenthesized subexpressions within the regular expression are saved in the remaining `BASH_REMATCH` indices. The element of `BASH_REMATCH` with index n is the portion of the string matching the nth parenthesized subexpression.

- It is sometimes difficult to specify a regular expression literally without using quotes, or to keep track of the quoting used by regular expressions while paying attention to the shell’s quote removal. Using a shell variable to store the pattern decreases these problems. For example, the following is equivalent to the above:
```bash
     pattern=’[[:space:]]*(a)?b’
     [[ $line =~ $pattern ]]
```

- If you want to match a character that’s special to the regular expression grammar, it has to be quoted to remove its special meaning.
This means that in the pattern ‘xxx.txt’, the ‘.’ matches any character in the string (its usual regular expression meaning), but in the pattern ‘"xxx.txt"’ it can only match a literal ‘.’.

- Shell programmers should take special care with backslashes, since back- slashes are used both by the shell and regular expressions to remove the special meaning from the following character. The following two sets of commands are not equivalent:
```bash

     pattern=’\.’

     [[ . =~ $pattern ]]
     [[ . =~ \. ]]

     [[ . =~ "$pattern" ]]
     [[ . =~ ’\.’ ]]
```
The first two matches will succeed, but the second two will not, because in the second two the backslash will be part of the pattern to be matched. In the first two examples, the backslash removes the special meaning from ‘.’, so the literal ‘.’ matches. If the string in the first examples were anything other than ‘.’, say ‘a’, the pattern would not match, because the quoted ‘.’ in the pattern loses its special meaning of matching any single character.

Expressions may be combined using the following operators, listed in decreasing order of precedence:
```bash
( expression )
```
Returns the value of expression. This may be used to override the normal precedence of operators.
```bash
! expression
```
True if expression is false.
```bash
expression1 && expression2
```
True if both `expression1` and `expression2` are true.
```bash
expression1 || expression2
```
True if either `expression1` or `expression2` is true.

The `&&` and `||` operators do not evaluate `expression2` if the value of `expression1` is sufficient to determine the return value of the entire conditional expression.

#### 3.2.5.3 Grouping Commands


**Bash provides two ways to group a list of commands to be executed as a unit.** When commands are grouped, redirections may be applied to the entire command list. For example, the output of all the commands in the list may be redirected to a single stream.

**`()`**    `( list )`
Placing a list of commands between parentheses causes a **subshell** environment to be created, and each of the commands in list to be executed in that subshell. Since the list is executed in a subshell, variable assignments do not remain in effect after the subshell completes.

**`{}`**    `{ list; }`
Placing a list of commands between curly braces causes the list to be executed in the **current shell context**. No subshell is created. The **semicolon** (or newline) following list is required.

- The **braces** are **reserved words**, so they must be separated from the list by blanks or other shell metacharacters. 
- The **parentheses** are **operators**, and are recognized as separate tokens by the shell even if they are not separated from the list by whitespace.
- The **exit status** of both of these constructs is the exit status of list.

### 3.2.6 Coprocesses

A **coprocess** is a shell command preceded by the **coproc** reserved word. A coprocess is executed asynchronously in a subshell, as if the command had been terminated with the ‘&’ control operator, with a two-way pipe established between the executing shell and the coprocess.

The format for a coprocess is:
```bash
coproc [NAME] command [redirections]
```
This creates a coprocess named `NAME`. If NAME is not supplied, the default name is `COPROC`. NAME must not be supplied if command is a simple command; otherwise, it is interpreted as the first word of the simple command.

When the coprocess is executed, the shell creates an array variable (see Arrays) named `NAME` in the context of the executing shell. 
- The standard output of command is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to `NAME[0]`. 
- The standard input of command is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to `NAME[1]`. 
- This pipe is established before any redirections specified by the command (see Redirections). The file descriptors can be utilized as arguments to shell commands and redirections using standard word expansions. 
- Other than those created to execute command and process substitutions, the file descriptors are not available in subshells.

The process ID of the shell spawned to execute the coprocess is available as the value of the variable `NAME_PID`. The `wait` builtin command may be used to wait for the coprocess to terminate.

Since the coprocess is created as an asynchronous command, the `coproc` command always returns success. The return status of a coprocess is the exit status of command.

If no name is given in the `coproc` command so by default `COPROC` is the name of the array.

```bash
coproc (echo $(whoami))                                   
echo "The coprocess array is ${COPROC[@]}"         
echo "The PID of the coprocess is ${COPROC_PID}"                                 
read -r o <&"${COPROC[0]}"
echo "The user is $o which is the output of the coprocess"
```
The result would look like this:
```
The coprocess array is 63 60
The PID of the coprocess is 12236
The user is ubuntu which is the output of the coprocess
```

For non simple commands.

```bash
$ coproc testproc (echo 1          Start a named coprocess
> read aline ; echo $aline)        in the background
[1] 5090
$ echo ${testproc[@]}              Show the file descriptors
63 60
$ echo $testproc_PID               Show the coprocess PID
5090
$ read out <&${testproc[0]}        Read the first line of coprocess
$ echo $out                        output and show it
1
$ echo foo >&${testproc[1]}        Send coprocess some input
$ read out2 <&${testproc[0]}       Read second output line
[1]+ Done  coproc testproc (echo 1; read aline; echo $aline)
$ echo $out2                       Show the second output line
foo
```
The first line is equal to `coproc testproc (echo 1 ; read aline ; echo $aline)`


### 3.2.7 GNU Parallel

There are ways to run commands in parallel that are not built into Bash. GNU Parallel is a tool to do just that.

Parallel can replace `xargs` or `feed` commands from its input sources to several different instances of Bash.

For example, it is easy to replace `xargs` to gzip all html files in the current directory and its subdirectories:
```bash
find . -type f -name '*.html' -print | parallel gzip
```
If you need to protect special characters such as newlines in file names, use find’s `-print0` option and parallel’s `-0` option.

You can use Parallel to move files from the current directory when the number of files is too large to process with one mv invocation:
```bash
printf '%s\n' * | parallel mv {} destdir
```

As you can see, the `{}` is replaced with each line read from standard input. While using `ls` will work in most instances, it is not sufficient to deal with all filenames. `printf` is a shell builtin, and therefore is not subject to the kernel’s limit on the number of arguments to a program, so you can use ‘*’. If you need to accommodate special characters in filenames, you can use
```bash
printf '%s\0' * | parallel -0 mv {} destdir
```
as alluded to above.

This will run as many mv commands as there are files in the current directory. You can emulate a parallel xargs by adding the -X option:
```bash
printf '%s\0' * | parallel -0 -X mv {} destdir
```

Finally, Parallel can be used to run a sequence of shell commands in parallel, similar to ‘cat file | bash’. It is not uncommon to take a list of filenames, create a series of shell commands to operate on them, and feed that list of commands to a shell. Parallel can speed this up. Assuming that file contains a list of shell commands, one per line,
```bash
parallel -j 10 < file
```
will evaluate the commands using the shell (since no explicit command is supplied as an argument), in blocks of ten shell jobs at a time.

## 3.3 Shell Functions

Shell functions are executed in the **current shell context**; no new process is created to interpret them.

Functions are declared using this syntax:
```bash
  fname () compound-command [ redirections ] 
or
  function fname [()] compound-command [ redirections ]
```
- The body of the function is the compound command compound-command.
  - That command is usually a list enclosed between { and }, but may be any compound command listed above, with one exception: If the `function` reserved word is used, but the parentheses are not supplied, the braces are required. 

- In default mode, a function name can be any unquoted shell word that does not contain ‘$’.
- Any redirections associated with the shell function are performed when the function is executed.
- A function definition may be deleted using the `-f` option to the `unset` builtin.
- The exit status of a **function definition** is zero unless a syntax error occurs or a readonly function with the same name already exists.
- When **executed**, the exit status of a function is the exit status of the last command executed in the body.
- In the most common usage the **curly braces** that surround the body of the function must be separated from the body by **blanks** or **newlines**. This is because the braces are **reserved words** and are only recognized as such when they are separated from the command list by whitespace or another shell metacharacter.
  - Also, when using the braces, the list must be terminated by a semicolon, a ‘&’, or a newline.

When a function is executed:
- The special parameter ‘#’ that expands to the number of positional parameters is updated to reflect the change.
- Special parameter 0 is unchanged.
- The first element of the `FUNCNAME` variable is set to the name of the function while the function is executing.

All other aspects of the shell execution environment are identical between a function and its caller with these exceptions: 
- the `DEBUG` and `RETURN` traps are not inherited unless the function has been given the `trace` attribute using the `declare` builtin or the `-o functrace` option has been enabled with the `set` builtin, (in which case all functions inherit the DEBUG and RETURN traps), 
- and the `ERR` trap is not inherited unless the `-o errtrace` shell option has been enabled.

The `FUNCNEST` variable, if set to a numeric value greater than 0, defines a maximum function nesting level.
- By default, no limit is placed on the number of recursive calls.

When a function completes, the values of the positional parameters and the special parameter ‘#’ are restored to the values they had prior to the function’s execution.

If a numeric argument is given to `return`, that is the function’s `return` status; otherwise the function’s `return` status is the exit status of the last command executed before the `return`.

Variables local to the function may be declared with the `local` builtin. 
- These variables are visible only to the function and **the commands it invokes**. This is particularly important when a shell function calls other functions.
- Local variables "shadow" variables with the same name declared at previous scopes.
- The shell uses **dynamic scoping** to control a variable’s visibility within functions.
  - For example, if a variable `var` is declared as local in function `func1`, and `func1` calls another function `func2`, references to `var` made from within `func2` will resolve to the local variable `var` from `func1`, shadowing any global variable named `var`.
- The `unset` builtin also acts using **the same dynamic scope**: 
  - if a variable is local to the current scope, unset will unset it;
  - otherwise the unset will refer to the variable found in any calling scope as described above.
  - If a variable at the current local scope is unset, it will remain so until it is reset in that scope or until the function returns

Function names and definitions may be listed with the `-f` option to the `declare` (typeset) builtin command.

The `-F` option to `declare` or `typeset` will list the function names only (and optionally the source file and line number, if the extdebug shell option is enabled).

Functions may be exported so that subshells automatically have them defined with the `-f` option to the `export` builtin.

## 3.4 Shell Parameters

A parameter is an entity that stores values. It can be a name, a number, or one of the special characters listed below. 
A variable is a parameter denoted by a name. A variable has a value and zero or more attributes. 
Attributes are assigned using the `declare` builtin command.

A parameter is set if it has been assigned a value. The `null` string is a valid value. Once a variable is set, it may be unset only by using the `unset` builtin command.

A variable may be assigned to by a statement of the form
```bash
name=[value]
```
If value is not given, the variable is assigned the `null string`.
All values undergo tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, and quote removal (detailed below).
If the variable has its `integer` attribute set, then value is evaluated as an **arithmetic expression** even if the `$((...))` expansion is not used.
Word splitting is not performed, with the exception of "$@".
Filename expansion is not performed.
Assignment statements may also appear as arguments to the `alias`, `declare`, `typeset`, `export`, `readonly`, and `local` builtin commands (declaration commands).

In the context where an assignment statement is assigning a value to a `shell variable` or `array index`, the ‘+=’ operator can be used to append to or add to the variable’s previous value.
This includes arguments to builtin commands such as `declare` that accept assignment statements (declaration commands).
- When ‘+=’ is applied to a variable for which the **integer attribute** has been set, value is evaluated as an arithmetic expression and added to the variable’s current value, which is also evaluated. 
- When ‘+=’ is applied to an **array variable** using compound assignment, the variable’s value is **not unset** (as it is when using ‘=’), and new values are appended to the array beginning at one greater than the array’s maximum index (for indexed arrays), or added as additional key-value pairs in an associative array. 
- When applied to a **string-valued** variable, value is expanded and appended to the variable’s value.

### nameref

A variable can be assigned the **nameref** attribute using the `-n` option to the `declare` or `local` builtin commands to create a `nameref`, or a reference to another variable.
- This allows variables to be manipulated indirectly. Whenever the `nameref` variable is referenced, assigned to, unset, or has its attributes modified (other than using or changing the `nameref` attribute itself), the operation is actually performed on the variable specified by the `nameref` variable’s value. 
- A `nameref` is commonly used within shell functions to refer to a variable whose name is passed as an argument to the function. 
  - For instance, if a variable name is passed to a shell function as its first argument, running
  ```bash
     declare -n ref=$1
  ```
  inside the function creates a `nameref` variable `ref` whose value is the variable name passed as the first argument. References and assignments to ref, and changes to its attributes, are treated as references, assignments, and attribute modifications to the variable whose name was passed as $1.

- If the control variable in a `for` loop has the `nameref` attribute, the list of words can be a list of shell variables, and a name reference will be established for each word in the list, in turn, when the loop is executed. 
- **Array variables** cannot be given the `nameref` attribute. However, `nameref` variables can reference array variables and subscripted array variables. 
- Namerefs can be unset using the `-n` option to the `unset` builtin. Otherwise, if `unset` is executed with the name of a `nameref` variable as an argument, the variable referenced by the `nameref` variable will be unset.

### 3.4.1 Positional Parameters

- A positional parameter is a parameter denoted by **one or more digits**, other than the single digit 0. 
- Positional parameters are assigned from the shell’s arguments when it is invoked, and may be reassigned using the `set` builtin command. 
- Positional parameter N may be referenced as `${N}`, or as `$N` when N consists of a single digit. 
- Positional parameters may not be assigned to with assignment statements. 
- The `set` and `shift` builtins are used to set and unset them. 
- The positional parameters are temporarily replaced when a shell function is executed.
- When a positional parameter consisting of more than a single digit is expanded, it must be enclosed in **braces**.

### 3.4.2 Special Parameters

#### `*` `($*)`
  
`($*)` Expands to the positional parameters, starting from **one**. 
- When the expansion is not within double quotes, each positional parameter expands to a separate word. 
  - In contexts where it is performed, those words are subject to further word splitting and filename expansion. 
- When the expansion occurs within double quotes, it expands to a single word with the value of each parameter separated by the first character of the IFS special variable. 
  - That is, `"$*"` is equivalent to `"$1c$2c..."`, where `c` is the first character of the value of the IFS variable. 
  - If IFS is unset, the parameters are separated by `spaces`. 
  - If IFS is null, the parameters are joined without intervening separators.


#### `@` `($@)`

`($@)` Expands to the positional parameters, starting from one. 
- In contexts where word splitting is performed, this expands each positional parameter to a separate word; if not within double quotes, these words are subject to word splitting. 
- In contexts where word splitting is not performed, this expands to a single word with each positional parameter separated by a space. 
  - When the expansion occurs within double quotes, and word splitting is performed, each parameter expands to a separate word. 
    - That is, `"$@"` is equivalent to `"$1" "$2" ….` If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the beginning part of the original word, and the expansion of the last parameter is joined with the last part of the original word. When there are no positional parameters, `"$@"` and `$@` expand to nothing (i.e., they are removed).


```bash
for arg in $@; do 
echo "$arg"
done   ## output "a\nb\nc"

for arg in "$@"; do
echo "$arg"
done  ## output "a\nb\nc" -- I don't know why

for arg in $*; do
echo "$arg"
done  ##    output "a\nb\nc"

for arg in "$*"; do
echo "$arg"
done    ## output "abc"
```
result:
```
a
b
c
a
b
c
a
b
c
a b c
```

#### `#` `($#)`

`($#)` Expands to the number of positional parameters in decimal.

#### `? ($?)`
`($?)` Expands to the exit status of the most recently executed foreground pipeline.



#### `- ($-, a hyphen.)`
`($-, a hyphen.)` Expands to the current option flags as specified upon invocation, by the `set` builtin command, or those set by the shell itself (such as the `-i` option).

#### `$ ($$)`
`($$)` Expands to the process ID of the shell. In a `()` subshell, it expands to the process ID of the **invoking shell**, not the subshell.

#### `! ($!)`
`($!)` Expands to the process ID of the job most recently placed **into the background**, whether executed as an asynchronous command or using the `bg` builtin

#### `0 ($0)`
`($0)` Expands to the name of the shell or shell script. This is set at shell initialization. 
- If Bash is invoked with a file of commands, `$0` is set to the name of that file. 
- If Bash is started with the `-c` option, then `$0` is set to the first argument after the string to be executed, if one is present. Otherwise, it is set to the filename used to invoke Bash, as given by argument zero.

## 3.5 Shell Expansions

Expansion is performed on the command line after it has been split into `tokens`. There are **seven** kinds of expansion performed:
```
- Brace Expansion	  	          Expansion of expressions within braces.
- Tilde Expansion	  	          Expansion of the `~` character.
- Shell Parameter Expansion	  	How Bash expands variables to their values.
- Command Substitution	  	    Using the output of a command as an argument.
- Arithmetic Expansion	  	    How to use arithmetic in shell expansions.
- Process Substitution	  	    A way to write and read to and from a command.
- Word Splitting	  	          How the results of expansion are split into separate arguments.
- Filename Expansion	  	      A shorthand for specifying filenames matching patterns.
- Quote Removal	  	            How and when quote characters are removed from words.
```
The **order of expansions** is: brace expansion; tilde expansion, parameter and variable expansion, arithmetic expansion, and command substitution (done in a left-to-right fashion); word splitting; and filename expansion.

On systems that can support it, there is an additional expansion available: **process substitution**. This is performed at the same time as tilde, parameter, variable, and arithmetic expansion and command substitution.

After these expansions are performed, quote characters present in the original word are removed unless they have been quoted themselves (quote removal).

Only brace expansion, word splitting, and filename expansion can increase the number of words of the expansion; other expansions expand a single word to a single word. The only exceptions to this are the expansions of `"$@"` and `$*` (see Special Parameters), and `"${name[@]}"` and `${name[*]}` (see Arrays).

After all expansions, quote removal (see Quote Removal) is performed.

### 3.5.1 Brace Expansion

- Patterns to be brace expanded take the form of an optional **preamble**, followed by either a series of **comma-separated** strings or a sequence expression between a pair of braces, followed by an optional **postscript**.
- The preamble is prefixed to each string contained within the braces, and the postscript is then appended to each resulting string, expanding left to right.
- Brace expansions may be nested. The results of each expanded string are not sorted; left to right order is preserved. For example,
```bash
bash$ echo a{d,c,b}e
ade ace abe
```

A sequence expression takes the form `{x..y[..incr]}`, where x and y are either integers or single characters, and `incr`, an optional increment, is an integer. 
- When integers are supplied, the expression expands to each number between x and y, **inclusive**. 
  - Supplied integers may be prefixed with ‘0’ to force each term to have the same width. 
  - When either x or y begins with a zero, the shell attempts to force all generated terms to contain the same number of digits, zero-padding where necessary. 
- When characters are supplied, the expression expands to each character lexicographically between x and y, inclusive, using the default `C` locale. 
  - Note that both x and y must be of the same type. 
- When the increment is supplied, it is used as the difference between each term. The default increment is 1 or -1 as appropriate.

```bash
$ echo 0{a..h}0
0a0 0b0 0c0 0d0 0e0 0f0 0g0 0h0
$ echo 0{a..h..2}0
0a0 0c0 0e0 0g0
$ echo a{0..20..2}a
a0a a2a a4a a6a a8a a10a a12a a14a a16a a18a a20a
$ for i in {0..20..2}; do echo $i; done 
0
2
4
6
8
10
12
14
16
18
20
$ for i in {20..0..-2}; do echo $i; done 
20
18
16
14
12
10
8
6
4
2
0

```

Brace expansion is performed before any other expansions, and any characters special to other expansions are preserved in the result. It is strictly textual. Bash does not apply any syntactic interpretation to the context of the expansion or the text between the braces.
A `{` or ‘`,`’ may be quoted with a backslash to prevent its being considered part of a brace expression. To avoid conflicts with parameter expansion, the string ‘`${`’ is not considered eligible for brace expansion, and inhibits brace expansion until the closing ‘`}`’.

This construct is typically used as shorthand when the common prefix of the strings to be generated is longer than in the above example:
```bash
mkdir /usr/local/src/bash/{old,new,dist,bugs}
```
or
```bash
chown root /usr/{ucb/{ex,edit},lib/{ex?.?*,how_ex}}
```

### 3.5.2 Tilde Expansion

- If a word begins with an unquoted tilde character (‘`~`’), all of the characters up to the first unquoted **slash(/)** (or all characters, if there is no unquoted slash) are considered a `tilde-prefix`. 
- If none of the characters in the tilde-prefix are quoted, the characters in the tilde-prefix following the tilde are treated as a possible login name. 
- If this login name is the null string, the tilde is replaced with the value of the `HOME` shell variable. 
- If HOME is unset, the home directory of the user executing the shell is substituted instead. Otherwise, the tilde-prefix is replaced with the home directory associated with the specified login name.

- If the tilde-prefix is ‘`~+`’, the value of the shell variable PWD replaces the tilde-prefix. 
- If the tilde-prefix is ‘`~-`’, the value of the shell variable OLDPWD, if it is set, is substituted.

- If the characters following the tilde in the tilde-prefix consist of a number N, optionally prefixed by a ‘+’ or a ‘-’, the tilde-prefix is replaced with the corresponding element from the **directory stack**, as it would be displayed by the `dirs` builtin invoked with the characters following tilde in the tilde-prefix as an argument (see The Directory Stack). If the tilde-prefix, sans the tilde, consists of a number without a leading ‘+’ or ‘-’, ‘+’ is assumed.

The following table shows how Bash treats unquoted tilde-prefixes:
```
~
The value of $HOME

~/foo
$HOME/foo

~fred/foo
The subdirectory foo of the home directory of the user fred

~+/foo
$PWD/foo

~-/foo
${OLDPWD-'~-'}/foo

~N
The string that would be displayed by ‘dirs +N’

~+N
The string that would be displayed by ‘dirs +N’

~-N
The string that would be displayed by ‘dirs -N’

```

### 3.5.3 Shell Parameter Expansion








