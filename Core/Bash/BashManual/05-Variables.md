- [5 Shell Variables](#5-shell-variables)
  - [5.1 Bourne Shell Variables](#51-bourne-shell-variables)
    - [CDPATH](#cdpath)
    - [HOME](#home)
    - [IFS (Internal Field Separator)](#ifs-internal-field-separator)
    - [MAIL](#mail)
    - [MAILPATH](#mailpath)
    - [OPTARG](#optarg)
    - [OPTIND](#optind)
    - [PATH](#path)
    - [PS1](#ps1)
    - [PS2](#ps2)
  - [5.2 Bash Variables](#52-bash-variables)
    - [_](#_)
    - [BASH](#bash)
    - [BASHOPTS](#bashopts)
    - [BASHPID](#bashpid)
    - [BASH_ALIASES](#bash_aliases)
    - [BASH_ARGC](#bash_argc)
    - [BASH_ARGV](#bash_argv)
    - [BASH_ARGV0](#bash_argv0)
    - [BASH_CMDS](#bash_cmds)
    - [BASH_COMMAND](#bash_command)
    - [BASH_COMPAT](#bash_compat)
    - [BASH_ENV](#bash_env)
    - [BASH_EXECUTION_STRING](#bash_execution_string)
    - [BASH_LINENO](#bash_lineno)
    - [BASH_LOADABLES_PATH](#bash_loadables_path)
    - [BASH_REMATCH](#bash_rematch)
    - [BASH_SOURCE](#bash_source)
    - [BASH_SUBSHELL](#bash_subshell)
    - [BASH_VERSINFO](#bash_versinfo)
    - [BASH_VERSION](#bash_version)
    - [BASH_XTRACEFD](#bash_xtracefd)
    - [CHILD_MAX](#child_max)
    - [COLUMNS](#columns)
    - [COMP_CWORD](#comp_cword)
    - [COMP_LINE](#comp_line)
    - [COMP_POINT](#comp_point)
    - [COMP_TYPE](#comp_type)
    - [COMP_KEY](#comp_key)
    - [COMP_WORDBREAKS](#comp_wordbreaks)
    - [COMP_WORDS](#comp_words)
    - [COMPREPLY](#compreply)
    - [COPROC](#coproc)
    - [DIRSTACK](#dirstack)
    - [EMACS](#emacs)
    - [ENV](#env)
    - [EPOCHREALTIME](#epochrealtime)
    - [EPOCHSECONDS](#epochseconds)
    - [EUID](#euid)
    - [EXECIGNORE](#execignore)
    - [FCEDIT](#fcedit)
    - [FIGNORE](#fignore)
    - [FUNCNAME](#funcname)
    - [FUNCNEST](#funcnest)
    - [GLOBIGNORE](#globignore)
    - [GROUPS](#groups)
    - [histchars](#histchars)
    - [HISTCMD](#histcmd)
    - [HISTCONTROL](#histcontrol)
    - [HISTFILE](#histfile)
    - [HISTFILESIZE](#histfilesize)
    - [HISTIGNORE](#histignore)
    - [HISTSIZE](#histsize)
    - [HISTTIMEFORMAT](#histtimeformat)
    - [HOSTFILE](#hostfile)
    - [HOSTNAME](#hostname)
    - [HOSTTYPE](#hosttype)
    - [IGNOREEOF](#ignoreeof)
    - [INPUTRC](#inputrc)
    - [INSIDE_EMACS](#inside_emacs)
    - [LANG](#lang)
    - [LC_ALL](#lc_all)
    - [LC_COLLATE](#lc_collate)
    - [LC_CTYPE](#lc_ctype)
    - [LC_MESSAGES](#lc_messages)
    - [LC_NUMERIC](#lc_numeric)
    - [LC_TIME](#lc_time)
    - [LINENO](#lineno)
    - [LINES](#lines)
    - [MACHTYPE](#machtype)
    - [MAILCHECK](#mailcheck)
    - [MAPFILE](#mapfile)
    - [OLDPWD](#oldpwd)
    - [OPTERR](#opterr)
    - [OSTYPE](#ostype)
    - [PIPESTATUS](#pipestatus)
    - [POSIXLY_CORRECT](#posixly_correct)
    - [PPID](#ppid)
    - [PROMPT_COMMAND](#prompt_command)
    - [PROMPT_DIRTRIM](#prompt_dirtrim)
    - [PS0](#ps0)
    - [PS3](#ps3)
    - [PS4](#ps4)
    - [PWD](#pwd)
    - [RANDOM](#random)
    - [READLINE_LINE](#readline_line)
    - [READLINE_MARK](#readline_mark)
    - [READLINE_POINT](#readline_point)
    - [REPLY](#reply)
    - [SECONDS](#seconds)
    - [SHELL](#shell)
    - [SHELLOPTS](#shellopts)
    - [SHLVL](#shlvl)
    - [SRANDOM](#srandom)
    - [TIMEFORMAT](#timeformat)
    - [TMOUT](#tmout)
    - [TMPDIR](#tmpdir)
    - [UID](#uid)


# 5 Shell Variables

## 5.1 Bourne Shell Variables

Bash uses certain shell variables in the same way as the Bourne shell. In some cases, Bash assigns a default value to the variable.

### CDPATH
A colon-separated list of directories used as a search path for the cd builtin command.

### HOME
The current user’s home directory; the default for the cd builtin command. The value of this variable is also used by tilde expansion.

### IFS (Internal Field Separator)

A list of characters that separate fields; used when the shell splits words as part of expansion.

The default value is `<space><tab><newline>`.

### MAIL
If this parameter is set to a filename or directory name and the MAILPATH variable is not set, Bash informs the user of the arrival of mail in the specified file or Maildir-format directory.

### MAILPATH
A colon-separated list of filenames which the shell periodically checks for new mail. Each list entry can specify the message that is printed when new mail arrives in the mail file by separating the filename from the message with a ‘?’. When used in the text of the message, `$_` expands to the name of the current mail file.

### OPTARG
The value of the last option argument processed by the `getopts` builtin.

### OPTIND
The index of the last option argument processed by the `getopts` builtin.

### PATH
A colon-separated list of directories in which the shell looks for commands. A zero-length (null) directory name in the value of PATH indicates the current directory. A null directory name may appear as two adjacent colons, or as an initial or trailing colon.

### PS1
The primary prompt string. The default value is ‘\s-\v\$ ’. See Controlling the Prompt, for the complete list of escape sequences that are expanded before PS1 is displayed.

### PS2
The secondary prompt string. The default value is ‘> ’. PS2 is expanded in the same way as PS1 before being displayed.

## 5.2 Bash Variables

These variables are set or used by Bash, but other shells do not normally treat them specially.

A few variables used by Bash are described in different chapters: variables for controlling the job control facilities (see Job Control Variables).

### _

($_, an underscore.) 
- At shell startup, set to the pathname used to invoke the shell or shell script being executed as passed in the environment or argument list. 
  - if the `_` variable was in the environment that bash received, then bash leaves it untouched.

    In particular, if that bash shell was invoked by another bash shell (though zsh, yash and some ksh implementations also do it), then that bash shell will have set the _ environment variable to **the path of the command being executed**. For instance, if bash is invoked to interpret a script as a result of another bash shell interpreting:
    ```
    bash-script some args
    ```
    That bash will have passed `_=/path/to/bash-scrip` in the environment given to bash-script, and that's what the initial value of the `$_` bash variable will be in the bash shell that interprets that script.
    ```
    $ env -i _=whatever bash -c 'echo "$_"'
    whatever
    ```
  - Now, if the invoking application doesn't pass a _ environment variable, the invoked bash shell will initialise `$_` to the `argv[0]` it receives itself which could be bash, or `/path/to/bash` or `/path/to/some-script` or anything else (in the example above, that would be `/bin/bash` if the she-bang of the script was `#!/bin/bash` or `/path/to/bash-script` depending on the system).

    So that text is misleading as it describes the behaviour of the caller which bash has no control over. The application that invoked bash may very well not set `$_` at all (in practice, only some shells and a few rare interactive applications do, `execlp()` doesn't for instance), or it could use it for something completely different (for instance `ksh93` sets it to `*pid*/path/to/command`).
    ```
    $ env bash -c 'echo "$_"'
    /usr/bin/env   (env did not set it to /bin/bash, so the value we
               get is the one passed to env by my interactive shell
               _=/usr/bin/env (on Ubuntu20))
    $ ksh93 -c 'bash -c "echo \$_"'
    *20042*/bin/bash
    $ ksh -c 'bash -c "echo \$_"' (on MacOS)
    *66379*/usr/local/bin/bash
    ```

- Subsequently, expands to the last argument to the previous simple command executed in the foreground, after expansion. 
  - In the case of an interactive shell, that will be on the first simple command interpreted from /etc/bash.bashrc for instance.

    For instance, at the prompt of an interactive shell:
    ```
    $ echo "$_"
    ]      (the last arg of the last command from my ~/.bashrc)
    $ f() { echo test; }
    $ echo "$_"
    ]      (the command-line before had no simple command, so we get
            the last argument of that previous echo commandline)
    $ (: test)
    $ echo "$_"
    ]      (simple command, but in a sub-shell environment)
    $ : test
    $ echo "$_"
    test
    ```
  - For a non-interactive shell, it would be the first command in `$BASH_ENV` or of the code fed to that shell if `$BASH_ENV` is not set.
- Also set to the full pathname used to invoke each command executed and placed in the environment exported to that command. 
  - bash, like a few other shells will pass a _ environment variable to commands it executes that contains the path that bash used as the first argument to the execve() system calls.
    ```
    $ env | grep '^_'
    _=/usr/bin/env
    ```
- When checking mail, this parameter holds the name of the mail file.
    Example:
    ```
    $ MAILCHECK=1 MAILPATH='/tmp/a?New mail in <$_>' bash
    bash$ echo test >> /tmp/a
    New mail in </tmp/a>
    ```

### BASH
The full pathname used to execute the current instance of Bash.

### BASHOPTS
A colon-separated list of enabled shell options. Each word in the list is a valid argument for the -s option to the `shopt` builtin command. The options appearing in BASHOPTS are those reported as ‘on’ by ‘shopt’. If this variable is in the environment when Bash starts up, each shell option in the list will be enabled before reading any startup files. This variable is readonly.

### BASHPID
Expands to the process ID of the current Bash process. This differs from `$$` under certain circumstances, such as subshells that do not require Bash to be re-initialized. Assignments to BASHPID have no effect. If BASHPID is unset, it loses its special properties, even if it is subsequently reset.

### BASH_ALIASES
An associative array variable whose members correspond to the internal list of aliases as maintained by the `alias` builtin. Elements added to this array appear in the alias list; however, unsetting array elements currently does not cause aliases to be removed from the alias list. If BASH_ALIASES is unset, it loses its special properties, even if it is subsequently reset.

### BASH_ARGC
An array variable whose values are the number of parameters in each frame of the current bash execution **call stack**. 
- The number of parameters to the current subroutine (shell function or script executed with `.` or `source`) is at the top of the stack. 
- When a subroutine is executed, the number of parameters passed is pushed onto BASH_ARGC. 
- The shell sets BASH_ARGC only when in extended debugging mode (see The Shopt Builtin for a description of the `extdebug` option to the shopt builtin). 
- Setting extdebug after the shell has started to execute a script, or referencing this variable when extdebug is not set, may result in inconsistent values.

### BASH_ARGV
An array variable containing all of the parameters in the current bash execution **call stack**. 
- The final parameter of the last subroutine call is at the top of the stack; the first parameter of the initial call is at the bottom. 
- When a subroutine is executed, the parameters supplied are pushed onto BASH_ARGV. 
- The shell sets BASH_ARGV only when in extended debugging mode (see The Shopt Builtin for a description of the `extdebug` option to the shopt builtin). 
- Setting extdebug after the shell has started to execute a script, or referencing this variable when extdebug is not set, may result in inconsistent values.

### BASH_ARGV0
When referenced, this variable expands to the name of the shell or shell script (identical to `$0`). 
- Assignment to BASH_ARGV0 causes the value assigned to also be assigned to `$0`. 
- If BASH_ARGV0 is unset, it loses its special properties, even if it is subsequently reset.

### BASH_CMDS
An associative array variable whose members correspond to the internal **hash table** of commands as maintained by the `hash` builtin. 
- Elements added to this array appear in the hash table; 
- however, unsetting array elements currently does not cause command names to be removed from the hash table. 
- If BASH_CMDS is unset, it loses its special properties, even if it is subsequently reset.

### BASH_COMMAND
The command currently being executed or about to be executed, unless the shell is executing a command as the result of a trap, in which case it is the command executing at the time of the trap. 
- If BASH_COMMAND is unset, it loses its special properties, even if it is subsequently reset.

### BASH_COMPAT
The value is used to set the shell’s compatibility level. 
- See Shell Compatibility Mode, for a description of the various compatibility levels and their effects. 
- The value may be a decimal number (e.g., 4.2) or an integer (e.g., 42) corresponding to the desired compatibility level. 
- If BASH_COMPAT is unset or set to the empty string, the compatibility level is set to the default for the current version. 
- If BASH_COMPAT is set to a value that is not one of the valid compatibility levels, the shell prints an error message and sets the compatibility level to the default for the current version. 
- The valid values correspond to the compatibility levels described below (see Shell Compatibility Mode). 
  - For example, 4.2 and 42 are valid values that correspond to the `compat42` `shopt` option and set the compatibility level to 42. 
  - The current version is also a valid value.

### BASH_ENV
If this variable is set when Bash is invoked to execute a shell script, its value is expanded and used as the name of a startup file to read before executing the script. See Bash Startup Files.

### BASH_EXECUTION_STRING
The command argument to the -c invocation option.

### BASH_LINENO
An array variable whose members are the line numbers in source files where each corresponding member of FUNCNAME was invoked. 
- `${BASH_LINENO[$i]}` is the line number in the source file (`${BASH_SOURCE[$i+1]}`) where `${FUNCNAME[$i]}` was called (or `${BASH_LINENO[$i-1]}` if referenced within another shell function). 
- Use LINENO to obtain the current line number.

### BASH_LOADABLES_PATH
A colon-separated list of directories in which the shell looks for dynamically loadable builtins specified by the `enable` command.

### BASH_REMATCH
An array variable whose members are assigned by the ‘=~’ binary operator to the `[[` conditional command. 
- The element with index `0` is the portion of the string matching the entire regular expression. 
- The element with index `n` is the portion of the string matching the `nth` parenthesized subexpression.

### BASH_SOURCE
An array variable whose members are the source filenames where the corresponding shell **function names** in the FUNCNAME array variable are defined. 
- The shell function `${FUNCNAME[$i]}` is defined in the file `${BASH_SOURCE[$i]}` and called from `${BASH_SOURCE[$i+1]}`

### BASH_SUBSHELL
Incremented by one within each subshell or subshell environment when the shell begins executing in that environment. 
- The initial value is `0`. 
- If BASH_SUBSHELL is unset, it loses its special properties, even if it is subsequently reset.

### BASH_VERSINFO
A readonly array variable (see Arrays) whose members hold version information for this instance of Bash. The values assigned to the array members are as follows:

- `BASH_VERSINFO[0]`
The major version number (the release).

- `BASH_VERSINFO[1]`
The minor version number (the version).

- `BASH_VERSINFO[2]`
The patch level.

- `BASH_VERSINFO[3]`
The build version.

- `BASH_VERSINFO[4]`
The release status (e.g., beta1).

- `BASH_VERSINFO[5]`
The value of MACHTYPE.

```
$ echo ${BASH_VERSINFO[@]}
5 0 17 1 release x86_64-pc-linux-gnu
```

### BASH_VERSION
The version number of the current instance of Bash.

### BASH_XTRACEFD
- If set to an integer corresponding to a valid file descriptor, Bash will write the trace output generated when ‘set -x’ is enabled to that file descriptor. 
- This allows tracing output to be separated from diagnostic and error messages. 
- The file descriptor is closed when BASH_XTRACEFD is unset or assigned a new value. 
- Unsetting BASH_XTRACEFD or assigning it the empty string causes the trace output to be sent to the standard error. 
- Note that setting BASH_XTRACEFD to 2 (the standard error file descriptor) and then unsetting it will result in the standard error being closed.

### CHILD_MAX
Set the number of exited child status values for the shell to remember. 
- Bash will not allow this value to be decreased below a POSIX-mandated minimum, and there is a maximum value (currently 8192) that this may not exceed. The minimum value is system-dependent.

### COLUMNS
Used by the `select` command to determine the terminal width when printing selection lists. 
- Automatically set if the `checkwinsize` option is enabled (see The Shopt Builtin), or in an interactive shell upon receipt of a SIGWINCH.

### COMP_CWORD
An index into `${COMP_WORDS}` of the word containing the current cursor position. 
- This variable is available only in shell functions invoked by the programmable completion facilities (see Programmable Completion).

### COMP_LINE
The current command line. 
- This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see Programmable Completion).

### COMP_POINT
The index of the current cursor position relative to the beginning of the current command. 
- If the current cursor position is at the end of the current command, the value of this variable is equal to `${#COMP_LINE}`. 
- This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see Programmable Completion).

### COMP_TYPE
Set to an integer value corresponding to the type of completion attempted that caused a completion function to be called: 
- TAB, for normal completion, 
- ‘?’, for listing completions after successive tabs, 
- ‘!’, for listing alternatives on partial word completion, 
- ‘@’, to list completions if the word is not unmodified, 
- or ‘%’, for menu completion. 

This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see Programmable Completion).

### COMP_KEY
The key (or final key of a key sequence) used to invoke the current completion function.

### COMP_WORDBREAKS
The set of characters that the Readline library treats as word separators when performing word completion. 
- If COMP_WORDBREAKS is unset, it loses its special properties, even if it is subsequently reset.

### COMP_WORDS
An array variable consisting of the individual words in the current command line. 
- The line is split into words as Readline would split it, using COMP_WORDBREAKS as described above. 
- This variable is available only in shell functions invoked by the programmable completion facilities (see Programmable Completion).

### COMPREPLY
An array variable from which Bash reads the possible completions generated by a shell function invoked by the programmable completion facility (see Programmable Completion). Each array element contains one possible completion.

### COPROC
An array variable created to hold the file descriptors for output from and input to an `unnamed coprocess` (see Coprocesses).

### DIRSTACK
An array variable containing the current contents of the **directory stack**. 
- Directories appear in the stack in the order they are displayed by the `dirs` builtin. 
- Assigning to members of this array variable may be used to modify directories already in the stack, but the `pushd` and `popd` builtins must be used to add and remove directories. 
- Assignment to this variable will not change the current directory. 
- If DIRSTACK is unset, it loses its special properties, even if it is subsequently reset.

### EMACS
If Bash finds this variable in the environment when the shell starts with value ‘t’, it assumes that the shell is running in an Emacs shell buffer and disables line editing.

### ENV
Expanded and executed similarlty to BASH_ENV (see Bash Startup Files) when an interactive shell is invoked in POSIX Mode (see Bash POSIX Mode).

### EPOCHREALTIME
Each time this parameter is referenced, it expands to the number of seconds since the Unix Epoch as a floating point value with micro-second granularity (see the documentation for the C library function time for the definition of Epoch). 
- Assignments to EPOCHREALTIME are ignored. 
- If EPOCHREALTIME is unset, it loses its special properties, even if it is subsequently reset.

### EPOCHSECONDS
Each time this parameter is referenced, it expands to the number of seconds since the Unix Epoch (see the documentation for the C library function time for the definition of Epoch). 
- Assignments to EPOCHSECONDS are ignored. 
- If EPOCHSECONDS is unset, it loses its special properties, even if it is subsequently reset.

### EUID
The numeric effective user id of the current user. This variable is readonly.

### EXECIGNORE
A colon-separated list of shell patterns (see Pattern Matching) defining the list of filenames to be ignored by command search using PATH. 
- Files whose full pathnames match one of these patterns are not considered executable files for the purposes of completion and command execution via PATH lookup. 
- This does not affect the behavior of the `[`, `test`, and `[[` commands. 
- Full pathnames in the command hash table are not subject to EXECIGNORE. 
- Use this variable to ignore shared library files that have the executable bit set, but are not executable files. 
- The pattern matching honors the setting of the `extglob` shell option.

### FCEDIT
The editor used as a default by the `-e` option to the `fc` builtin command.

### FIGNORE
A colon-separated list of suffixes to ignore when performing filename completion. 
- A filename whose suffix matches one of the entries in FIGNORE is excluded from the list of matched filenames. 
- A sample value is ‘.o:~’

### FUNCNAME
An array variable containing the names of all shell functions currently in the execution **call stack**. 
- The element with index `0` is the name of any currently-executing shell function. 
- The bottom-most element (the one with the highest index) is "main". 
- This variable exists only when a shell function is executing. 
- Assignments to FUNCNAME have no effect. 
- If FUNCNAME is unset, it loses its special properties, even if it is subsequently reset.

This variable can be used with BASH_LINENO and BASH_SOURCE. 
- Each element of FUNCNAME has corresponding elements in BASH_LINENO and BASH_SOURCE to describe the call stack. 
- For instance, `${FUNCNAME[$i]}` was called from the file `${BASH_SOURCE[$i+1]}` at line number `${BASH_LINENO[$i]}`. 
- The `caller` builtin displays the current call stack using this information.

### FUNCNEST
If set to a numeric value greater than `0`, defines a maximum function nesting level. 
- Function invocations that exceed this nesting level will cause the current command to abort.

### GLOBIGNORE
A colon-separated list of patterns defining the set of file names to be ignored by filename expansion. 
- If a file name matched by a filename expansion pattern also matches one of the patterns in GLOBIGNORE, it is removed from the list of matches. 
- The pattern matching honors the setting of the `extglob` shell option.

### GROUPS
An array variable containing the list of groups of which the current user is a member. 
- Assignments to GROUPS have no effect. 
- If GROUPS is unset, it loses its special properties, even if it is subsequently reset.

### histchars
Up to three characters which control history expansion, quick substitution, and tokenization (see History Interaction). 
- The first character is the history expansion character, that is, the character which signifies the start of a history expansion, normally ‘!’. 
- The second character is the character which signifies ‘quick substitution’ when seen as the first character on a line, normally ‘^’. 
- The optional third character is the character which indicates that the remainder of the line is a comment when found as the first character of a word, usually ‘#’. 
  - The history comment character causes history substitution to be skipped for the remaining words on the line. It does not necessarily cause the shell parser to treat the rest of the line as a comment.

### HISTCMD
The history number, or index in the history list, of the current command. 
- Assignments to HISTCMD are ignored. 
- If HISTCMD is unset, it loses its special properties, even if it is subsequently reset.

### HISTCONTROL
A colon-separated list of values controlling how commands are saved on the history list. 
- If the list of values includes ‘ignorespace’, lines which begin with a space character are not saved in the history list. 
- A value of ‘ignoredups’ causes lines which match the previous history entry to not be saved. 
- A value of ‘ignoreboth’ is shorthand for ‘ignorespace’ and ‘ignoredups’. 
- A value of ‘erasedups’ causes all previous lines matching the current line to be removed from the history list before that line is saved. 
- Any value not in the above list is ignored. 
- If HISTCONTROL is unset, or does not include a valid value, all lines read by the shell parser are saved on the history list, subject to the value of HISTIGNORE. 
- The second and subsequent lines of a multi-line compound command are not tested, and are added to the history regardless of the value of HISTCONTROL.

### HISTFILE
The name of the file to which the command history is saved. The default value is `~/.bash_history`.

### HISTFILESIZE
The maximum number of lines contained in the history file. 
- When this variable is assigned a value, the history file is truncated, if necessary, to contain no more than that number of lines by removing the oldest entries. 
- The history file is also truncated to this size after writing it when a shell exits. 
- If the value is 0, the history file is truncated to zero size. 
- Non-numeric values and numeric values less than zero inhibit truncation. 
- The shell sets the default value to the value of HISTSIZE after reading any startup files.

### HISTIGNORE
A colon-separated list of patterns used to decide which command lines should be saved on the history list. 
- Each pattern is anchored at the beginning of the line and must match the complete line (no implicit ‘*’ is appended). 
- Each pattern is tested against the line after the checks specified by HISTCONTROL are applied. 
- In addition to the normal shell pattern matching characters, 
  - ‘&’ matches the previous history line. ‘&’ may be escaped using a backslash; 
  - the backslash is removed before attempting a match. 
- The second and subsequent lines of a multi-line compound command are not tested, and are added to the history regardless of the value of HISTIGNORE. 
- The pattern matching honors the setting of the `extglob` shell option.

HISTIGNORE subsumes the function of HISTCONTROL. 
- A pattern of ‘&’ is identical to `ignoredups`, and a pattern of `‘[ ]*’` is identical to `ignorespace`. 
- Combining these two patterns, separating them with a colon, provides the functionality of `ignoreboth`.

### HISTSIZE
The maximum number of commands to remember on the history list. 
- If the value is `0`, commands are not saved in the history list. 
- Numeric values less than zero result in every command being saved on the history list (there is no limit). 
- The shell sets the default value to 500 after reading any startup files.

### HISTTIMEFORMAT
If this variable is set and not null, its value is used as a format string for `strftime` to print the time stamp associated with each history entry displayed by the `history` builtin. 
- If this variable is set, time stamps are written to the history file so they may be preserved across shell sessions. 
- This uses the history comment character to distinguish timestamps from other history lines.

### HOSTFILE
Contains the name of a file in the same format as `/etc/hosts` that should be read when the shell needs to complete a hostname. 
- The list of possible hostname completions may be changed while the shell is running; 
- the next time hostname completion is attempted after the value is changed, Bash adds the contents of the new file to the existing list. 
- If HOSTFILE is set, but has no value, or does not name a readable file, Bash attempts to read `/etc/hosts` to obtain the list of possible hostname completions. 
- When HOSTFILE is unset, the hostname list is cleared.

### HOSTNAME
The name of the current host.

### HOSTTYPE
A string describing the machine Bash is running on.
```
$ echo $HOSTTYPE
x86_64
```

### IGNOREEOF
Controls the action of the shell on receipt of an EOF character as the sole input. 
- If set, the value denotes the number of consecutive EOF characters that can be read as the first character on an input line before the shell will exit. 
- If the variable exists but does not have a numeric value, or has no value, then the default is 10. 
- If the variable does not exist, then EOF signifies the end of input to the shell. 
- This is only in effect for interactive shells.

### INPUTRC
The name of the Readline initialization file, overriding the default of `~/.inputrc`.

### INSIDE_EMACS
If Bash finds this variable in the environment when the shell starts, it assumes that the shell is running in an Emacs shell buffer and may disable line editing depending on the value of TERM.

### LANG
Used to determine the locale category for any category not specifically selected with a variable starting with `LC_`.

### LC_ALL
This variable overrides the value of LANG and any other LC_ variable specifying a locale category.

### LC_COLLATE
This variable determines the collation order used when sorting the results of filename expansion, and determines the behavior of range expressions, equivalence classes, and collating sequences within filename expansion and pattern matching (see Filename Expansion).

### LC_CTYPE
This variable determines the interpretation of characters and the behavior of character classes within filename expansion and pattern matching (see Filename Expansion).

### LC_MESSAGES
This variable determines the locale used to translate double-quoted strings preceded by a ‘$’ (see Locale Translation).

### LC_NUMERIC
This variable determines the locale category used for number formatting.

### LC_TIME
This variable determines the locale category used for data and time formatting.

### LINENO
The line number in the script or shell function currently executing. 
- If LINENO is unset, it loses its special properties, even if it is subsequently reset.

### LINES
Used by the `select` command to determine the column length for printing selection lists. 
- Automatically set if the `checkwinsize` option is enabled (see The Shopt Builtin), or in an interactive shell upon receipt of a SIGWINCH.

### MACHTYPE
A string that fully describes the system type on which Bash is executing, in the standard GNU cpu-company-system format.
```
$ echo $MACHTYPE
x86_64-pc-linux-gnu
```

### MAILCHECK
How often (in seconds) that the shell should check for mail in the files specified in the MAILPATH or MAIL variables. 
- The default is 60 seconds. 
- When it is time to check for mail, the shell does so before displaying the primary prompt. 
- If this variable is unset, or set to a value that is not a number greater than or equal to zero, the shell disables mail checking.

### MAPFILE
An array variable created to hold the text read by the `mapfile` builtin when no variable name is supplied

### OLDPWD
The previous working directory as set by the `cd` builtin.

### OPTERR
If set to the value 1, Bash displays error messages generated by the `getopts` builtin command.

### OSTYPE
A string describing the operating system Bash is running on.
```
$ echo $OSTYPE
linux-gnu
```

### PIPESTATUS
An array variable (see Arrays) containing a list of exit status values from the processes in the most-recently-executed foreground pipeline (which may contain only a single command).

### POSIXLY_CORRECT
If this variable is in the environment when Bash starts, the shell enters POSIX mode (see Bash POSIX Mode) before reading the startup files, as if the `--posix` invocation option had been supplied. 
- If it is set while the shell is running, Bash enables POSIX mode, as if the command
    ```
    set -o posix
    ```
    had been executed. 
- When the shell enters POSIX mode, it sets this variable if it was not already set.

### PPID
The process ID of the shell’s parent process. This variable is readonly.

### PROMPT_COMMAND
If this variable is set, and is an array, the value of each set element is interpreted as a command to execute before printing the primary prompt ($PS1). 
- If this is set but not an array variable, its value is used as a command to execute instead.

### PROMPT_DIRTRIM
If set to a number greater than zero, the value is used as the number of trailing directory components to retain when expanding the `\w` and `\W` prompt string escapes (see Controlling the Prompt). Characters removed are replaced with an ellipsis.

### PS0
The value of this parameter is expanded like PS1 and displayed by interactive shells after reading a command and before the command is executed.

### PS3
The value of this variable is used as the prompt for the `select` command. 
- If this variable is not set, the select command prompts with ‘#? ’

### PS4
The value of this parameter is expanded like PS1 and the expanded value is the prompt printed before the command line is echoed when the `-x` option is set. 
- The first character of the expanded value is replicated multiple times, as necessary, to indicate multiple levels of indirection. 
- The default is ‘+ ’.

### PWD
The current working directory as set by the cd builtin.

### RANDOM
Each time this parameter is referenced, it expands to a random integer between 0 and 32767. 
- Assigning a value to this variable seeds the random number generator. 
- If RANDOM is unset, it loses its special properties, even if it is subsequently reset.

### READLINE_LINE
The contents of the Readline line buffer, for use with ‘bind -x’.

### READLINE_MARK
The position of the mark (saved insertion point) in the Readline line buffer, for use with ‘bind -x’ (see Bash Builtins). 
- The characters between the insertion point and the mark are often called the **region**.

### READLINE_POINT
The position of the insertion point in the Readline line buffer, for use with ‘bind -x’ (see Bash Builtins).

### REPLY
The default variable for the read builtin.

### SECONDS
This variable expands to the number of seconds since the shell was started. 
- Assignment to this variable resets the count to the value assigned, and the expanded value becomes the value assigned plus the number of seconds since the assignment. 
- The number of seconds at shell invocation and the current time is always determined by querying the system clock. 
- If SECONDS is unset, it loses its special properties, even if it is subsequently reset.

### SHELL
This environment variable expands to the full pathname to the shell. If it is not set when the shell starts, Bash assigns to it the full pathname of the current user’s login shell.

### SHELLOPTS
A colon-separated list of enabled shell options. 
- Each word in the list is a valid argument for the `-o` option to the `set` builtin command. 
- The options appearing in SHELLOPTS are those reported as ‘on’ by ‘set -o’. 
- If this variable is in the environment when Bash starts up, each shell option in the list will be enabled before reading any startup files. 
- This variable is readonly.

### SHLVL
Incremented by one each time a new instance of Bash is started. This is intended to be a count of how deeply your Bash shells are nested.

### SRANDOM
This variable expands to a 32-bit pseudo-random number each time it is referenced. 
- The random number generator is not linear on systems that support `/dev/urandom` or `arc4random`, so each returned number has no relationship to the numbers preceding it. 
- The random number generator cannot be seeded, so assignments to this variable have no effect. 
- If SRANDOM is unset, it loses its special properties, even if it is subsequently reset.

### TIMEFORMAT
The value of this parameter is used as a format string specifying how the timing information for pipelines prefixed with the `time` reserved word should be displayed. 
- The ‘%’ character introduces an escape sequence that is expanded to a time value or other information. 
- The escape sequences and their meanings are as follows; the braces denote optional portions.

- `%%`
A literal `‘%’`.

- `%[p][l]R`
The elapsed time in seconds.

- `%[p][l]U`
The number of CPU seconds spent in user mode.

- `%[p][l]S`
The number of CPU seconds spent in system mode.

- `%P`
The CPU percentage, computed as `(%U + %S) / %R`.

The optional `p` is a digit specifying the precision, the number of fractional digits after a decimal point. 
- A value of `0` causes no decimal point or fraction to be output. 
- At most three places after the decimal point may be specified; values of p greater than 3 are changed to 3. 
- If p is not specified, the value 3 is used.

The optional `l` specifies a longer format, including minutes, of the form `MMmSS.FFs`. 
- The value of p determines whether or not the fraction is included.

If this variable is not set, Bash acts as if it had the value
    ```
    $'\nreal\t%3lR\nuser\t%3lU\nsys\t%3lS'
    ```
If the value is null, no timing information is displayed. A trailing newline is added when the format string is displayed.

### TMOUT
If set to a value greater than zero, TMOUT is treated as the default timeout for the `read` builtin. 
- The `select` command (see Conditional Constructs) terminates if input does not arrive after TMOUT seconds when input is coming from a terminal.

In an interactive shell, the value is interpreted as the number of seconds to wait for a line of input after issuing the primary prompt. - Bash terminates after waiting for that number of seconds if a complete line of input does not arrive.

### TMPDIR
If set, Bash uses its value as the name of a directory in which Bash creates temporary files for the shell’s use.

### UID
The numeric real user id of the current user. This variable is readonly.









