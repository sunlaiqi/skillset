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


Compound commands are the shell programming language constructs. Each construct be- gins with a reserved word or control operator and is terminated by a corresponding reserved word or operator.

Any redirections associated with a compound command apply to all commands within that compound command unless ex- plicitly overridden.

Bash provides looping constructs, conditional commands, and mechanisms to group commands and execute them as a unit.

#### 3.2.5.1 Looping Constructs














