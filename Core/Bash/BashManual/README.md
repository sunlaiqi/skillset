

Bash Reference Manual

Chet Ramey, Case Western Reserve University Brian Fox, Free Software Foundation

Reference Documentation for Bash Edition 5.1, for Bash Version 5.1. December 2020

- [How to find info about a command?](#how-to-find-info-about-a-command)
- [compound command](#compound-command)
  - [Documentation](#documentation)



# How to find info about a command?

```
$ type command
```
Find out the type of the command, builtin? or external command.
```
nobody@primary:~$ type uname
uname is /usr/bin/uname
nobody@primary:~$ type cd
cd is a shell builtin
nobody@primary:~$ type ls
ls is aliased to `ls --color=auto'
nobody@primary:~$ 
```

If no man page for a command, use help.
```
$ help command
```

```
command -V command
```

# compound command

Bash distinguishes between simple commands and compound commands:

1. **Simple commands** are a single command with optional arguments and redirections. For example:
```
$ echo Hello
Hello
```

2. **Compound commands** combine one or more simple commands into something that functions as a single unit. For example:
```
$ { echo Hello; date; }
Hello
Sun Aug 28 23:16:03 PDT 2016
```

One useful feature of compound commands is that redirections applied to the compound command are applied to every command that it contains. For example:
```
$ { echo info1; echo info2; } >logfile
$ cat logfile
info1
info2
```
According to man bash, there are **four types of compound commands**:

1. **Group: {...;}**, as illustrated above can be used to group simple commands together to form a compound command.

2. **Subshell: (...)** is similar to a group except that the commands are run in subshell environment. This means that variable assignments do not survive after the subshell completes. As an example:
```
$ a=0; (a=10; echo "inside=$a"); echo "outside=$a"
inside=10
outside=0
```
3. **Arithmetic Expression: ((...))**: Inside double-parens, a series of **comma-separated** arithmetic calculations may be performed. For example:
```
$ ((a=2, a=10*a, a+=2)); echo "a=$a"
a=22
```
4. **Test Command**: Bash's advanced form of the `test` command, `[[...]]`, can include several tests. Tests are separated by `&&` or `||`:
```
$ [[ a == b || 3 -gt 2 && 4 -gt 3 ]]; echo $?
0
```

## Documentation

From man bash:

Compound Commands

A compound command is one of the following. In most cases a list in a command's description may be separated from the rest of the command by one or more newlines, and may be followed by a newline in place of a semicolon.

`(list)`

list is executed in a subshell environment (see COMMAND EXECUTION ENVIRONMENT below). Variable assignments and builtin commands that affect the shell's environment do not remain in effect after the command completes. The return status is the exit status of list.

`{ list; }`

list is simply executed in the current shell environment. list must be terminated with a newline or semicolon. This is known as a group command. The return status is the exit status of list. Note that unlike the metacharacters ( and ), { and } are reserved words and must occur where a reserved word is permitted to be recognized. Since they do not cause a word break, they must be separated from list by whitespace or
another shell metacharacter.

`((expression))`

The expression is evaluated according to the rules described below under ARITHMETIC EVALUATION. If the value of the expression is non-zero, the return status is 0; otherwise the return status is 1. This is exactly equivalent to let "expression".

`[[ expression ]]`

Return a status of 0 or 1 depending on the evaluation of the conditional expression expression. Expressions are composed of the primaries described below under CONDITIONAL EXPRESSIONS. Word splitting and pathname expansion are not performed on the words between the `[[` and `]]`; tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution, and quote removal are performed. Conditional operators such as -f must be unquoted to be recognized as primaries.

When used with `[[`, the `<` and `>` operators sort lexicographically using the current locale.






