
**Shell programming in Unix Linux OSX 4th***

- [Basics](#basics)
  - [Filename Substitution](#filename-substitution)
  - [Standard Input/Output, and I/O Redirection](#standard-inputoutput-and-io-redirection)
  - [Regular expression](#regular-expression)
- [Tools](#tools)
  - [wc](#wc)
  - [cut](#cut)
  - [paste](#paste)
  - [sed](#sed)
  - [tr](#tr)
  - [grep](#grep)
  - [sort](#sort)
  - [uniq](#uniq)
    - [The -d Option](#the--d-option)
- [Variables](#variables)
  - [Built-in Integer Arithmetic](#built-in-integer-arithmetic)
    - [$(( )) Operators](#--operators)
  - [quote characters](#quote-characters)
    - [The Single Quote](#the-single-quote)
    - [The Double Quote](#the-double-quote)
    - [The Backslash](#the-backslash)
  - [Command Substitution](#command-substitution)
    - [The Back Quote](#the-back-quote)
    - [The $(...) Construct](#the--construct)
    - [The expr Command](#the-expr-command)
- [Passing Arguments](#passing-arguments)
  - [${n}](#n)
  - [The shift Command](#the-shift-command)
- [Decisions, Decisions](#decisions-decisions)
  - [The test Command](#the-test-command)
  - [An Alternative Format for test](#an-alternative-format-for-test)
    - [The Logical Negation Operator !](#the-logical-negation-operator-)
    - [The Logical AND Operator –a](#the-logical-and-operator-a)
    - [Parentheses](#parentheses)
    - [The Logical OR Operator –o](#the-logical-or-operator-o)
- [The Null Command :](#the-null-command-)
- [The && and || Constructs](#the--and--constructs)
- [Loops](#loops)
  - [The for Command](#the-for-command)
    - [The $@ Variable](#the--variable)
    - [The for Without the List](#the-for-without-the-list)
  - [The while Command](#the-while-command)
  - [The until Command](#the-until-command)
  - [More on Loops](#more-on-loops)
    - [Breaking Out of a Loop](#breaking-out-of-a-loop)
    - [Skipping the Remaining Commands in a Loop](#skipping-the-remaining-commands-in-a-loop)
    - [Executing a Loop in the Background](#executing-a-loop-in-the-background)
    - [I/O Redirection on a Loop](#io-redirection-on-a-loop)
    - [Piping Data into and out of a Loop](#piping-data-into-and-out-of-a-loop)
- [The getopts Command](#the-getopts-command)
- [Reading and Printing Data](#reading-and-printing-data)
  - [The read Command](#the-read-command)
    - [The $$ Variable and Temporary Files](#the--variable-and-temporary-files)
    - [The Exit Status from read](#the-exit-status-from-read)
  - [The printf Command](#the-printf-command)
- [Your Environment](#your-environment)
  - [Exported Variables](#exported-variables)
    - [export -p](#export--p)
    - [CDPATH](#cdpath)
  - [More on Subshells](#more-on-subshells)
    - [The . Command](#the--command)
    - [The exec Command](#the-exec-command)
    - [The (...) and { ...; } Constructs](#the--and----constructs)
    - [Another Way to Pass Variables to a Subshell](#another-way-to-pass-variables-to-a-subshell)
- [More on Parameters](#more-on-parameters)
  - [Parameter Substitution](#parameter-substitution)
    - [${parameter:-value}](#parameter-value)
    - [${parameter:=value}](#parametervalue)
    - [${parameter:?value}](#parametervalue-1)
    - [${parameter:+value}](#parametervalue-2)
  - [Pattern Matching Constructs](#pattern-matching-constructs)
    - [${variable%pattern}](#variablepattern)
    - [${variable%%pattern}](#variablepattern-1)
    - [${variable#pattern}](#variablepattern-2)
    - [${variable##pattern}](#variablepattern-3)
- [The set Command](#the-set-command)
  - [The -x Option](#the--x-option)
  - [set with No Arguments](#set-with-no-arguments)
  - [Using set to Reassign Positional Parameters](#using-set-to-reassign-positional-parameters)
  - [The -- Option](#the----option)
- [The IFS Variable](#the-ifs-variable)
  - [The readonly Command](#the-readonly-command)
  - [The unset Command](#the-unset-command)
- [MISC Commands](#misc-commands)
  - [The eval Command](#the-eval-command)
  - [The wait Command](#the-wait-command)
  - [The trap Command](#the-trap-command)
    - [trap with No Arguments](#trap-with-no-arguments)
    - [Ignoring Signals](#ignoring-signals)
    - [Resetting Traps](#resetting-traps)
  - [More on I/O](#more-on-io)
    - [<&- and >&-](#--and--)
  - [In-line Input Redirection (here documents)](#in-line-input-redirection-here-documents)
    - [Shell Archives (!!!)](#shell-archives-)
- [Functions](#functions)
  - [Removing a Function Definition](#removing-a-function-definition)
  - [The return Command](#the-return-command)
  - [The type Command](#the-type-command)
- [Interactive and Nonstandard Shell Features](#interactive-and-nonstandard-shell-features)
  - [The ENV File](#the-env-file)
  - [Command-Line Editing](#command-line-editing)
  - [Command History](#command-history)
- [bash vs ksh functions](#bash-vs-ksh-functions)
  - [Integer Arithmetic](#integer-arithmetic)
  - [Integer Types](#integer-types)
  - [Numbers in Different Bases](#numbers-in-different-bases)
  - [Arrays](#arrays)
- [Job Control](#job-control)
  - [Stopped Jobs and the fg and bg Commands](#stopped-jobs-and-the-fg-and-bg-commands)
- [Order of Search](#order-of-search)

# Basics

## Filename Substitution
The Asterisk
$ echo *
chaptl chapt2 chapt3 chapt4
Any place that * appears on the command line, the shell performs its substitution: $ echo * : *
chaptl chapt2 chapt3 chapt4 : chaptl chapt2 chapt3 chapt4

## Standard Input/Output, and I/O Redirection
ctrl+d

Could be used in command `sort` and `wc` input from stdin instead of a file.

## Regular expression

The `ed` utility is a line-oriented text editor.  It is used to create, display, modify and otherwise manipulate text files.

```
/^the/  	Find the line that starts with the 
1,$s/^/>>/	Insert >> at the beginning of each line
1,$s/^/ / 	insert spaces at the start of each line 
\.$ 		matches any line that ends in a period 
^\. 		matches any line that starts with a period.^$ 		which matches any line that contains no characters at all. 
^$ 		which matches any line that consists of a single space character. 
/[tT]he/ 	Look for the or The 
1,$s/[aeiouAEIOU]//g 	Delete all vowels 
[0123456789] or [0-9]	match any digit character o through 9
[A-Z] 		To match an uppercase letter, use 
[A-Za-z] 	To match an upper- or lowercase letter, you write 
/[0-9]/ 		Find a line containing a digit 
/^[A-Z]/ 	Find a line that starts with an uppercase letter 
[^A-Z] 	matches any character except an uppercase letter. Similarly, 
[^A-Za-z] 	matches any non-alphabetic character. 

X* 		matches zero, one, two, three, ... capital X’s 
XX* 		matches one or more capital X’s 
XXX* 		means match at least two consecutive X’s.
because the expression specifies a single X followed by zero or more X’s. You can accomplish the same effect with a + instead: it matches one or more of the preceding expression, so XX* and X+ are identical in function. 
1,$s/ */ /g	Change multiple blanks to single blanks 
.* 		is often used to specify zero or more occurrences of any characters. 
e.*e 		matches all the characters from the first e on a line to the last one.
[A-Za-z][A-Za-z]* 	This matches any alphabetic character followed by zero or more alphabetic characters. 
1,$s/[A-Za-z0-9][A-Za-z0-9]*/X/g l,$p	substitute all alphabetic and numbers by “X”
[-0-9] [0-9-] 	matches a single dash or digit character.
[]a-z] 		matches a right bracket or a lowercase letter. 

X\{1,10\} 	matches from one to 10 consecutive X’s. 
[A-Za-z]\{4,7\} 	matches a sequence of alphabetic letters from four to seven characters long. 
If only one number is enclosed by braces, as in 
\{10\} 
that number specifies that the preceding regular expression must be matched exactly that many times. 
[a-zA-Z]\{7\} 		matches exactly seven alphabetic characters 
.\{10\} 			matches exactly 10 characters no matter what they are 
1,$s/^.\{10\}// 		Delete the first 10 chars from each line 
1,$s/.\{5\}$// 		Delete the last 5 chars from each line 
+\{5,\} 			matches at least five consecutive plus signs. 
Saving Matched Characters: \(...\) 
^\(.\) 	matches the first character on the line, whatever it is, and stores it into register 1. 
^\(.\)\1 
initially matches the first character on the line and stores it in register 1, then matches what- ever is stored in register 1, as specified by the \1. The net effect of this regular expression is to match the first two characters on a line if they are both the same character. 
^\(.\).*\1$ 
matches all lines in which the first character on the line (^.) is the same as the last character on the line (\1$). The .* matches all the characters in-between. 
^\(...\)\(...\) 
the first three characters on the line will be stored into register 1, and the next three characters into register 2. If you appended \2\1 to the pattern, you would match a 12-character stringin which characters 1–3 matched characters 10–12, and in which characters 4–6 matched characters 7–9. 

```

# Tools

## wc

Counting Words in a File: The `wc` Command 
With the wc command, you can get a count of the total number of lines, words, and characters contained in a file. Once again, the name of the file is expected to be specified as the argument to this command: 
```
$ wc names
5 7 27 names 
```

## cut

This command comes in handy when you need to extract (that is, “cut out”) various fields of data from a data file or the output of a command. The general format of the cut command is 
```
cut -cchars file 
```
where `chars` specifies which characters (by position) you want to extract from each line of file. 
```
cut -c5- data
```
extracts characters 5 through the end of the line from each line of data and writes the results to standard output. 
```
$ who | cut –c1-8 	Extract the first 8 characters 
$ who | cut –c1-8 | sort 
$ who | cut –c1-8,18- 
```
The `-d` and `-f` options are used with `cut` when you have data that is delimited by a particular character, with 
- `-d` specifying the field seperator delimiter and 
- `-f` the field or fields you want extracted. The invocation of the `cut` command becomes 
```
cut -ddchar –ffields file 
```
where `dchar` is the character that delimits each field of the data, and `fields` specifies the fields to be extracted from file. Field numbers start at 1, and the same type of formats can be used to specify field numbers as was used to specify character positions before (for example,` -fl,2,8,` `-fl-3`, `-f4-`). 
To extract the names of all users from `/etc/passwd`, you could type the following: 
```
$ cut -d: -f1 /etc/passwd 		Extract field 1 
```
In a situation where the fields are separated by tabs, you should use the -f option to cut instead: 
```
$ cut -f1 phonebook 
```
Recall that you don’t have to specify the delimiter character with the -d option because `cut` **defaults to a tab character delimiter**. 

How do you know in advance whether fields are delimited by blanks or tabs? 
```
sed -n l file
```
at your terminal. If a tab character separates the fields, `\t` will be displayed instead of the tab:

## paste

The `paste` command is the inverse of `cut`: Instead of breaking lines apart, it puts them together. The general format of the paste command is 
```
paste files 
```
where corresponding lines from each of the specified files are “pasted” or merged together to form single lines that are then written to standard output. The dash character - can also be used in the files sequence to specify that input is from standard input. 

**The -d Option** 
If you don’t want the output fields separated by tab characters, you can specify the -d option to specify the output delimiter: 
```
-dchars 
```
where `chars` is one or more characters that will be used to separate the lines pasted together. That is, the first character listed in chars will be used to separate lines from the first file that are pasted with lines from the second file; the second character listed in chars will be used to separate lines from the second file from lines from the third, and so on.

**The -s Option **
The `-s` option tells paste to paste together lines from the same file, not from alternate files. If just one file is specified, the effect is to merge all the lines from the file together, separated by tabs, or by the delimiter characters specified with the `-d` option. 
Paste all lines from names 
```
$ paste -s names
Tony Emanuel Lucy
```

```
ls | paste -d' ' -s -
```

## sed 

`sed` is a program used for editing data in a pipe or command sequence. It stands for stream editor. Unlike `ed`, `sed` cannot be used interactively, though its commands are similar. The general form of the sed command is 
```
sed command file 
```
where command is an ed-style command applied to each line of the specified file. If no file is specified, standard input is assumed. 
```
$ sed 's/Unix/UNIX/' intro 		# Substitute Unix with UNIX 
```

If your text included more than one occurrence of “Unix” on a line, the above `sed` would have changed just the **first occurrence** to “UNIX.” By appending the global option **g** to the end of the substitute command `s`, you can ensure that multiple occurrences on a line will be changed. 
```
$ sed 's/Unix/UNIX/g' intro > temp
```
Alternatively, you can use `sed` to delete all the characters from the first space (which marks the end of the username) through the end of the line by using a regular expression: 
```
$ who | sed 's/ .*$//' 
rootruthsteve 
pat 
$ 
```
The `sed` command substitutes a **blank space** followed by any characters up through the end of the line **( .*$)** with nothing **(//)**; that is, it deletes the characters from the first blank to the end of the line for each input line. 

**The -n Option** 
```
$ sed -n '1,2p' intro 		Just print the first 2 lines 
$ sed -n '/UNIX/p' intro 	Just print lines containing UNIX 
```
Deleting Lines 
```
$ sed '1,2d' intro 		Delete lines 1 and 2 
$ sed '/UNIX/d' intro 	Delete all lines containing UNIX 
```

## tr

The `tr` filter is used to translate characters from standard input. The general form of the command is 
```
tr from-chars to-chars 
```
The result of the translation is written to standard output. 

The following shows how `tr` can be used to translate all letter e’s to x’s: 
```
$ tr e x < intro
```

the following shows how to translate all lowercase letters in intro to their uppercase equivalents: 
```
$ tr '[a-z]' '[A-Z]' < intro
```

**The -s Option**

You can use `tr` to squeeze out the multiple spaces by using the `-s` option and by specifying a single space character as the first and second argument: 
```
$ tr –s ' ' ' ' < lotsaspaces 
```

**The –d Option** 

**tr** can also be used to delete individual characters from the input stream. The format of `tr` in this case is 
```
tr -d from-chars
```
where any character listed in from-chars will be deleted from standard input. In the following example, tr is used to delete all spaces from the file intro: 
```
$ tr -d ' ' < intro 
```
You probably realize that you could have also used sed to achieve the same results: 
```
$ sed 's/ //g' intro
```
```
tr '()' '{}'    # 
tr '[A-Z]' '[N-ZA-M]' # 
tr '    ' '' # traslate tabs to spaces
tr -s ' ' ' ' # traslate multiple spaces to single space
tr -d '\14' # delete all formfeed
tr -d '[0-9]' # delete all digits
```

## grep

You saw in the section on sed how you could print all lines containing the string UNIX from the file intro with the command 
```
sed -n '/UNIX/p' intro
```
But you could also use the following `grep` command to achieve the same result: 
```
grep UNIX intro
```

**Regular Expressions and grep**

```
$ grep '[tT]he' intro
```
A smarter alternative might be to utilize the -i option to grep which makes patterns case insensitive. That is, the command 
```
grep –i 'the' intro 
grep '\.pic$' filelist 	
```
Lines from filelist that end with .pic 

**The -v Option** 

```
$ grep -v 'UNIX' intro 	
```
Print all lines that don't contain UNIX 

**The -l Option** 

At times, you may not want to see the actual lines that match a pattern but just seek the names of the files that contain the pattern. 
```
$ grep -l 'Move_history' *.c 		# List the files that contain Move_history 
```

**The -n Option**

If the `-n` option is used with grep, each line from the file that matches the specified pattern is preceded by its corresponding line number. 
```
$ grep -n 'Move_history' testch.c 		Precede matches with line numbers 
```

## sort

At its most basic, the `sort` command is really easy to understand: give it lines of input and it’ll sort them **alphabetically**, with the result appearing as its output: 
```
$ sort names 
```

Special characters are sorted according to the internal encoding of the characters. For example, the space character is represented internally as the number `32`, and the double quote as the number `34`. This means that the former would be sorted before the latter.

**The `-u` Option**

The `-u` option tells sort to eliminate duplicate lines from the output. 
```
$ sort -u names 
```

**The -r Option**

Use the `-r` option to reverse the order of the sort: 

**The -o Option**

By default, sort writes the sorted data to standard output. To have it go into a file, you can use output redirection: 
```
$ sort names > sorted_names 
$ 
```
Alternatively, you can use the -o option to specify the output file. Simply list the name of the output file right after the -o: 
```
$ sort names -o sorted_names 
$ 
```

**The -n Option**

Suppose that you have a file containing pairs of (x, y) data points. And suppose that you want to feed this data into a plotting program called `plotdata`, but that the program requires that the incoming data pairs be sorted in increasing value of x (the first value on each line). 

The -n option to sort specifies that the first field on the line is to be considered a number, and the data is to be sorted arithmetically. 

**Skipping Fields**

If you had to sort your data file by the y value—that is, the second number in each line—you could tell sort to start with the second field by using the option 
-k2n 
```
$ sort -k2n data 		# Start with the second field in the sort 
```

**The -t Option**

As mentioned, if you skip over fields, sort assumes that the fields are delimited by space or tab characters. The -t option can indicate otherwise. In this case, the character that follows the -t is taken as the delimiter character. 

To sort the file instead by the third colon-delimited field (which contains what is known as your user ID), you would want an arithmetic sort, starting with the third field (-k3), and specifying the colon character as the field delimiter (-t:): 
```
$ sort -k3n -t: /etc/passwd 		# Sort by user id (the 3rd field delimited by ':')
```

## uniq

The uniq command is useful when you need to find or remove duplicate lines in a file. 
The basic format of the command is 

```
uniq in_file out_fileIf 
```
out_file is not specified, the results will be written to standard output. If in_file is also not specified, uniq acts as a filter and reads its input from standard input.

### The -d Option 

Frequently, you’ll be interested in finding just the duplicate entries in a file. The -d option to uniq can be used for such purposes: It tells uniq to write only the duplicated lines to out_file (or standard output). Such lines are written **just once**, no matter how many consecutive occurrences there are. 
```
$ sort names | uniq -d  # List duplicate lines Tony
$ sort /etc/passwd | cut -f1 -d: | uniq -d # Find duplicates 
cem
harry
```
It turns out that there are multiple entries in /etc/passwd for `cem` and `harry`. If you wanted more information on the particular entries, you could now grep them from /etc/passwd: 
```
$ grep -n 'cem' /etc/passwd 
```

**Other Options**

The -c option to uniq adds an **occurrence count**, which can be tremendously useful in scripts: 
```
$ sort names | uniq –c 	# Count line occurrences 
```

One common use of uniq -c is to figure out the most common words in a data file, easily done with a command like: 
```
tr '[A-Z]' '[a-z]' datafile | sort | uniq -c | head 
```
Should be 
'''
tr '[A-Z]' '[a-z]' datafile | sort | uniq -c | sort -r | head 

# Variables

## Built-in Integer Arithmetic 

The format for arithmetic expansion is 
```
$((expression)) 
```

### $(( )) Operators 

Valid operators are taken from the C programming language

There is a surprisingly extensive list of operators, including 
- the basic six: `+, -, *, /, % and **`, 
- along with more sophisticated notations including `+=, -=, *=, /=`, 
- easy incrementand decrement with `variable++` and `variable--`, 
- and more. 

Our favorite? You can work with different numerical bases and even convert from one number base to another. For example, here are the answers to what 100 octal (base 8) and 101010101010101010 binary (base 2) are in decimal: 
```
$ echo $(( 8#100 ))
64
$ echo $(( 2#101010101010101010 )) 
174762 
```
The result of computing expression is substituted on the command line. For example, 
```
echo $((i+1)) 
```
adds one to the value in the shell variable `i` and prints the result. 
Notice that the **variablei doesn’t have to be preceded by a dollar sign** because the shell knows that the only valid elements that can appear in arithmetic expansions are **operators, numbers, and variables**. If the variable is not defined or contains a NULL string, its value is assumed to be zero. 

**Parentheses** may be used freely inside expressions to force grouping, as in 
```
echo $((i = (i + 10) * j)) 
```
If you want to perform an assignment without echo or some other command, you can move the assignment before the arithmetic expansion. 
So to multiply the variable i by 5 and assign the result back to i you can write 
```
i=$(( i * 5 ))
```
Note that spaces are optional inside the double parentheses, but are not allowed when the assignment is outside them. 

A more succinct way to multiply $i by 5 is the following common notation, which would appear within another statement: 
```
$(( i *= 5 )) 
```
If you’re just adding 1 to the value, you can be even more succinct: 
```
$(( i++ ))
```
Finally, to test to see whether i is greater than or equal to 0 and less than or equal to 100, you can write 
```
result=$(( i >= 0 && i <= 100 ))
```
which assigns result the value of **1 (true) if the expression is true** or 0 (false) if it’s false: 
```
$ i=$(( 100 * 200 / 10 ))
$ j=$(( i < 1000 ))     # If i is < 1000, set j = 0; otherwise 1 
$ echo $i $j
2000 0  # i is 2000, so j was set to 0
$
```

## quote characters 

The shell recognizes four different types of quote characters: 
- The single quote character **'** 
- The double quote character **"** 
- The backslash character \ 
- The back quote character **`** 

### The Single Quote 

Worth emphasizing is that **all special characters** are ignored by the shell if they appear within single quotes. 

Even the Enter key will be retained as part of the command argument if it’s enclosed in single quotes.

···
$ text='* means all files in the directory' 
$ echo $text 
names nu numbers phonebook stat means all files in the directory 
···
The second sequence with the variable text highlights that the shell does filename substitution after variable name substitution, meaning that the *** is replaced by the names of all the files in the current directory** after the variable is expanded, but before the `echo` is executed. Annoying! 
How do you fix these sort of problems? Through the use of double quotes. 

### The Double Quote 

Double quotes work similarly to single quotes, except they’re less protective of their content: single quotes tell the shell to ignore all enclosed characters, double quotes say to ignore most. In particular, the following three characters are not ignored inside double quotes: 
- Dollar signs 	
- Back quotes 
- Backslashes 
    
The fact that dollar signs are not ignored means that variable name substitution is done by the shell inside double quotes. 

If you want to have the value of a variable substituted, but don’t want the shell to then parse the substituted characters specially, enclose the variable inside double quotes. 

The difference between double quotes and no quotes: 
```
$ address="39 East 12th Street
> New York, N. Y. 10003"
$ echo $address
39 East 12th Street New York, N. Y. 10003 
$ echo "$address" 
39 East 12th Street 
New York, N. Y. 10003 
$
```

### The Backslash 

Functionally, the backslash (used as a prefix) is equivalent to placing single quotes around a single character, though with a few minor exceptions. 
The backslash escapes the character that immediately follows it. The general format is 
```
\c
```
where c is the character you want to quote. 
Any special meaning normally attached to that character is removed. Here is an example: 
```
$ echo >
syntax error: 'newline or ;' unexpected 
$ echo \>
>
$ 
$ x=*
$ echo \$x 
$x
$ 
```

**Using the Backslash for Continuing Lines** 

As mentioned at the start of this section, \c is essentially equivalent to 'c'. The one exception to this rule is when the backslash is used as the very last character on the line: 

**When a backslash is the last character of a line of input, the shell treats it as a line continuation character.** 

It removes the newline character that follows and also does not treat the newline as an argument delimiter (it’s as if it wasn’t even typed). This construct is often used for entering long commands across multiple lines. 

**The Backslash Inside Double Quotes**

If the backslash precedes any other character inside double quotes, the backslash is ignored by the shell and passed on to the program: 
···
$ echo "\$x"
$x
$ echo "\ is the backslash character" 
\ is the backslash character
$ x=5
$ echo "The value of x is \"$x\""
The value of x is "5"
$ 
···

Here are two different ways to properly quote the string so that everything works as desired: 

···
$ echo "<<< echo \$x >>> displays the value of x, which is $x" 
<<< echo $x >>> displays the value of x, which is 1
$ echo '<<< echo $x >>> displays the value of x, which is' $x 
<<< echo $x >>> displays the value of x, which is 1 
$ 
···

There’s a slight danger to the latter solution, however: If the variable x contained filename substitution or whitespace characters, they would be interpreted. A safer way of writing the echo would have been 
···
echo '<<< echo $x >>> displays the value of x, which is' "$x" 
···

## Command Substitution 

### The Back Quote 
The back quote—often called “back tick”。 The general format for using back quotes is 

`command`

### The $(...) Construct

The general format is `$(command)`

This construct is better than back quotes for a couple of reasons. 
- First, complex commands that use combinations of forward and back quotes can be difficult to read, particularly if the typeface you’re using doesn’t visually differentiate between single and back quotes; 
- second, `$(...)` constructs can be easily nested, allowing command substitution within command substitution. Although nesting can also be performed with back quotes, it’s trickier. 

```
$ filelist=$(ls)
$ echo $filelist
addresses intro lotsaspaces names nu numbers phonebook stat 
$ 
```

What happened here? You end up with a horizontal listing of the files even though the newlines from `ls` were stored inside the filelist variable. 
The newlines got eaten up at display time when the value of filelist was substituted by the shell in processing the echo command line. 
Double quotes around the variable will preserve the newlines: 
```
$ echo "$filelist" 
```

If you want to mail the contents of the file `memo` to all the people listed in the `names` file, you can do the following: 
```
$ mail $(cat names) < memo 
$ name="Ralph Kramden"
$ name=$(echo $name | tr '[a-z]' '[A-Z]') 
$ echo $name
RALPH KRAMDEN
$ 
```

The technique of using echo in a pipeline to write data to the standard input of the subsequent command is simple but powerful, and is often used in shell programs.The next example shows how cut can be used to extract the first character from the values stored in a variable called filename: 
```
$  filename=/users/steve/memos 
$  firstchar=$(echo $filename | cut -c1) 
$  echo $firstchar 
/
$ 
```

`sed` is also often used to “edit” the value stored in a variable. Here it is used to extract the last character from each line of the file specified by the variable file: 
```
$  file=exec.o 
$  lastchar=$(echo $file | sed 's/.*\(.\)$/\1/') 
$  echo $lastchar 
o
$ 
```
The sed command replaces all the characters on the line with the last one (remember that surrounding a pattern in parentheses causes it to be saved in a register`[el]` in this case register 1, which is then referenced as `\1`). The result of the sed substitution is stored in the variable lastchar. The single quotes around the sed command are important because they prevent the shell from trying to interpret the backslashes. (Question: would double quotes also have worked?) 

Finally, command substitutions can be nested. Suppose that you want to change every occurrence of the first character in a variable to something else. In a previous example, `firstchar=$(echo $filename | cut -c1)` gets the first character from filename, but how would we use this character to change every occurrence of that character in filename? A two-step process is one way: 
```
$ filename=/users/steve/memos
$ firstchar=$(echo $filename | cut -c1)
$ filename=$(echo $filename | tr "$firstchar" "^") 	# translate / to ^
$ echo $filename
^users^steve^memos
$ 
```

But a single, nested command substitution can perform the same operation: 
```
$ filename=/users/steve/memos
$ filename=$(echo $filename | tr "$(echo $filename | cut -c1)" "^") 
$ echo $filename
^users^steve^memos
$ 
```

### The expr Command

Although the standard shell supports built-in integer arithmetic, older shells don’t have this capability. In that situation, the mathematical equation solver `expr` can be used instead: 
```
$ expr 1 + 2 
3
$ 
```
It’s easy to work with, but `expr` isn’t very good at parsing equations, so each operator and operand given to expr must be **separated by spaces** to be properly understood. That explains the following: 
```
$ expr 1+2 
1+2
$ 
$ expr 17 * 6 
expr: syntax error 
$ 
```

The shell saw the * and substituted the names of all the files in your directory, which expr had no idea how to interpret! 
This is a job for the backslash! 
```
$ expr 17 \* 6 
102
$ 
```

Also note that expr has other operators. One of the most frequently used is the `:` operator, which is used to match characters in the first operand against a regular expression given as the second operand. By default, it returns the number of characters matched. For example, the `expr` command 
```
expr "$file" : ".*" 
```
returns the number of characters stored in the variable file, because the regular expression `.*` matches all the characters in the string. 

# Passing Arguments

## ${n}

If you supply more than nine arguments to a program, you cannot access the tenth and greater arguments with $10, $11, and so on. If you try to access the tenth argument by writing $10 the shell actually substitutes the value of $1 followed by a 0. Instead, the format 
```
${n}
``` 
must be used. To directly access argument 10, you must write ${10} in your program, and so on for arguments 11, 12, and so on. 

## The shift Command 

The shift command allows you to effectively left-shift your positional parameters. If you execute the command `shift`, whatever was previously stored inside $2 will be assigned to $1, whatever was previously stored in $3 will be assigned to $2, and so on. The old value of $1 will be irretrievably lost.

When this command is executed, `$#` (the number of arguments variable) is also automatically decremented by one.

You can shift more than one “place” at once by writing a count immediately after shift, as in 
```
shift 3 
```

# Decisions, Decisions 

## The test Command 

```
test expression 
```
If the result is true, it returns an **exit status of zero**, otherwise the result is false, and it returns a nonzero exit status. 

## An Alternative Format for test 

This can also be expressed in the alternative format as `[ expression ]` Spaces must appear after the [ and before the ]. 

### The Logical Negation Operator !

The unary logical negation operator ! can be placed in front of any other test expression to negate the result of the evaluation of that expression. For example, 
```
[ ! -r /users/steve/phonebook ] 
```

### The Logical AND Operator –a 

The operator -a performs a logical AND of two expressions and returns TRUE only if the two joined expressions are both true. So 
```
[ -f "$mailfile" -a -r "$mailfile" ] 
```
The -a operator has lower precedence than the integer comparison operators (and the string and file operators, for that matter) 
In some cases, it’s important to know that **test immediately stops** evaluating an AND expression as soon as something is proven to be false, so a statement like 
```
[ ! -f "$file" -a $(who > $file) ] 
```

### Parentheses 
You can use parentheses in a test expression to alter the order of evaluation as needed; just make sure that the parentheses themselves are quoted because they have a special meaning to the shell. So to translate the earlier example into a test command, you would write 
```
[ \( "$count" -ge 0 \) -a \( "$count" -lt 10 \) ]
```
As is typical, spaces must surround the parentheses because test expects to see every element in the conditional statement as a separate argument. 

### The Logical OR Operator –o 

The -o operator is similar to the -a operator, only it forms a logical OR of two expressions. That is, evaluation of the expression will be true if either the first expression is true or the second expression is true or both expressions are true. 
```
[ -n "$mailopt" -o -r $HOME/mailfile ]
```

# The Null Command : 
Every matching case statement needs a resulting command, and every if-then conditional needs a resultant command too—but sometimes you don’t want to execute anything, just “eat” the result. How do you do that? With the shell’s built-in null command. The format of this command is simply 
```
: 
```
and the purpose of it is—you guessed it—to do nothing. 

# The && and || Constructs 

The shell has two special constructs that enable you to execute a command based on whether the preceding command succeeds or fails. In case you think this sounds similar to the if command, well it is. Sort of. It’s a shorthand form of the if. 
If you write 
```
command1 && command2 
```
anywhere that the shell expects to see a command, command1 will be executed, and if it returns an exit status of zero (success), command2 will be executed. If command1 returns a non-zero exit status (fail), command2 is not invoked but is ignored. 
```
if command1
then
	command2
fi
```

The `||` construct works similarly, except that the second command gets executed only if the exit status of the first is nonzero. So if you write 
```
grep "$name" phonebook || echo "Couldn't find $name" 
```
In this case, the equivalent if command would look like 
```
if grep "$name" phonebook 
then 
	:
else 
	echo "Couldn't find $name" 
fi 
```

**AND**
```
if validsys "$sys" && timeok 
then 
	sendmail "$user@$sys" < $message 
fi 
```
If `validsys` returns an exit status of zero, `timeok` is executed and its exit status is then tested for the if. If that status is zero, then sendmail is executed. If validsys returns a nonzero exit status, however, timeok is not executed, and the failed exit status is then tested by the if, and sendmail ends up not being executed. 

By comparison, when the || is used in an if, the effect is like a logical OR: 
```
if endofmonth || specialrequest 
then 
	sendreports 
fi 
```
If endofmonth returns a zero exit status, sendreports is executed; otherwise specialrequest is executed and if its exit status is zero, sendreports is executed. The net effect is that sendreports is executed if either endofmonth or specialrequest returns an exit status of zero. 

# Loops

## The for Command

The `for` command is used to execute one or more commands a specified number of times. Its basic format is as shown: 
```
for var in word1 word2 ... wordn 
do 	
    command 
	command 
	... 
done 
```

In short:
```
For var in word1 word2 word3 … wordn; do command command …; done;
```

### The $@ Variable 

While we’re utilizing `$*`, let’s have a closer look at how it and its cousin `$@` work. To do that, let’s write a program called args that displays all the arguments typed on the command line, one per line. 
```
$ cat argsecho Number of arguments passed is $# 
for arg in $* 
do 
	echo $arg 
done 
$ 
```

Now to try it: 
```
$ args a b c
Number of arguments passed is 3 
abc
$ args 'a b' c 
Number of arguments passed is 2 
abc 
$ 
```

Look closely at the second example: even though 'a b' was passed as a single argument to args, it was split into two values within the for loop. That’s because the `$*` in the `for` command was replaced by the shell with a b c and **the quotes were lost**. Thus the loop was executed three times. 

The shell replaces the value of `$*` with `$1, $2, ...` , but if you instead use the special shell variable `"$@"` the values will be passed with `"$1", "$2", ...` . The key difference is the double quotes around the `$@`: without them this variable behaves just like `$*`. 

Go back to the args program and replace the unquoted `$*` with `"$@"`: 
```
$ args ‘a b’ c
Number of arguments passed is 2 
a b
c
$ args 
Number 
$ 
```

Try it with no arguments of arguments passed is 0. In the last case, no arguments were passed to the program so the variable `"$@"` was replaced by nothing. The net result is that the body of the loop was not executed at all. 

### The for Without the List 

A special notation is recognized by the shell when writing for commands. If you omit the in element and its subsequent list 
```bash
for var 
do 
	command 
    command 
    ... 
done 
```
the shell automatically sequences through all the arguments typed on the command line, just as if you had written 
```bash
for var in "$@" 
do 
	command 
    command 
    ... 
done
```

## The while Command
The second type of looping command is the while statement. The format of this command is 
```bash
while commandt 
do 
	command 
	command 
	... 
done 
```
The `while` loop is often used in conjunction with the **shift** command to process an unknown number of arguments typed on the command line. 

## The until Command 

The `while` command continues execution as long as the test expression continues to return a TRUE (zero) exit status. 

The `until` command is the opposite: It continues executing the code block until the test expression returns a nonzero exit status and stops once a zero status is produced. 
Here is the general format of the until: 
```bash
until commandt
do 
	command 
	command 
	... 
done
```
Like the while, the commands between the do and done might never be executed if commandt  returns a zero exit status the first time it’s executed. 

While the two commands are quite similar, the until command is useful for writing programs that **wait for a particular event to occur**. For example, suppose that you want to see whether sandy is logged on because you have to give her something important. You could send her electronic mail, but you know that she usually doesn’t get around to reading her mail until late in the day. 

## More on Loops 

### Breaking Out of a Loop

If the break command is used in the form 
```bash
break n
``` 
the `n` innermost loops are immediately exited, 

### Skipping the Remaining Commands in a Loop

The `continue` command is similar to `break`, only it doesn’t cause the loop to be exited, just the remaining commands in the current iteration of the loop to be skipped. 

Like the break, an optional number can follow the continue, so 
```bash
continue n
```
causes the commands in the innermost n loops to be skipped, after which execution of the program continues as normal. 

### Executing a Loop in the Background

An entire loop can be sent to the background for execution simply by placing an ampersand after the done statement: 
```bash
$ for file in memo[1-4] 
>  do 
>  	run $file 
>  done & 		# Send it to the background 
[1] 9932
$
```

### I/O Redirection on a Loop 

You can also perform I/O redirection on a loop. Input redirected into the loop applies to all commands in the loop that read their data from standard input. Output redirected from the loop to a file applies to all commands in the loop that write to standard output. And it all happens at the loop closing statement done: 
```bash
$ for i in 1 2 3 4 
>  do 
>  	echo $i 
>  done > loopout 	# Redirect loop’s output to loopout 
```

You can also redirect the standard error output from a loop, simply by tacking on a `2>` file after the done:
```bash
while [ "$endofdata" -ne TRUE ] 
do
	…
done 2> errors 
```

Here output from all commands in the loop writing to standard error will be redirected to the file errors. 
A variation of the `2>` format is commonly used to ensure that error messages go to the terminal even when a script might have its output redirected into a file or pipe: 
```bash
echo "Error: no file" 1>&2 
```

By default, `echo` sends its output to standard output (file descriptor 1), while file descriptor 2 remains standard error and is not redirected on file redirection or pipes by default. So the notation above means that the error message from echo should have its “file #1” output redirected to “file #2”, that is, standard error. You can test this with code like this: 
```bash
for i in "once" 
do
  echo "Standard output message"
  echo "Error message" 1>&2 
done > /dev/null
```

only “Error message” is printed on the terminal.

### Piping Data into and out of a Loop 

A command’s output can be piped into a loop (by having the commands prior to the loop command end with a pipe symbol), and the output from a loop can be piped into another command too. Here’s an example of the output from a for command piped into `wc`: 
```bash
$ for i in 1 2 3 4 
> do 
> 	echo $i 
> done | wc –l 
	4 
$ 
```

# The getopts Command 

The general format of the command is 
```bash
getopts options variable 
```

letter-only options are specified as such and options that have a required argument have a trailing colon, so “ab:c” means that -a and -c are allowed, as is -b, but -b requires an additional parameter to be specified. 

`getopts` obtains options and their arguments from a list of parameters that follows the standard POSIX.2 option syntax (that is, single letters preceded by a `-` and possibly followed by an argument value; the single letters may be grouped). Typically, shell scripts use `getopts` to parse arguments passed to them. When you specify args on the getopts command line, getopts parses those arguments instead of the script command line.

our getopts call might look like this: 
```bash
getopts "air" option 
```

Here the first argument—air—specifies the three acceptable command flags (`-a, -i, and -r`) and option is the name of the variable that `getopts` will use to store each matching value encountered. 

The `getopts` command also allows options to be clustered or grouped together on the command line. This is done by following a single minus sign with more than one consecutive option. For example, our foo command can be executed like this: 
```bash
foo -a -r -i 
```
or like this: 
```bash
foo -ari 
```
using this simple grouping feature. 

To indicate to `getopts` that an option has a required argument, add a **colon character** after the option letter on the getopts command line. So the waitfor program, which allows both -m and -t options, the latter of which has a required additional argument, should call getopts like this: 
```bash
getopts mt: option 
```

If getopts doesn’t find an argument after an option that requires one, it stores a question mark inside the variable and outputs an error message to standard error. Otherwise, it stores the character in the variable and the user specified argument inside a special variable called OPTARG. 

One final note about getopts: Another special variable called OPTIND is initially set to 1 and is updated each time getopts returns to reflect the number of the next command line argument to be processed. 
```bash
# process command options while getopts mt:n: option 
do 	case "$option" 
	in 
		m) mailopt=TRUE;; 
		t) interval=$OPTARG;;
		n) num=$OPTARG;;		
        \?) echo "Usage: waitfor [-m] [-t n] user" 
			echo " -m means to be informed by mail" 
			echo " -t means check every n secs." 
			exit 1;; 
	esac 
done
# Make sure a user name was specified 
if [ "$OPTIND" -gt "$#" ] 
then 
	echo "Missing user name!" 
	exit 2 
fi 
shiftcount=$((OPTIND – 1)) 
shift $shiftcount
user=$1 
```
```
$ waitfor -m
Missing user name!
$ waitfor -x fred			
Illegal option waitfor: illegal option -- x 
Usage: waitfor [-m] [-t n] user 
	-m means to be informed by mail 
	-t means check every n secs. 
$ waitfor -m -t 600 ann &	
Check every 10 min. for ann 
[1] 5792
$ 
```

# Reading and Printing Data 

## The read Command

The general format of the read command is 
```bash
read variables
```

Special echo Escape Characters 

A slight annoyance with mycp is that after the `echo command` is run, the response typed by the user appears on the next line. This happens because the `echo command` automatically adds a terminating newline character after the last argument. 

Fortunately, this can be suppressed if the last two characters given to echo are the special escape characters `\c`. This tells echo to omit the newline after displaying the last argument. If you changed the echo command in mycp to read like this: 
```bash
echo "$to already exists; overwrite (yes/no)? \c" 
```

The user’s input would be typed right after the message on the same line. Bear in mind that the `\c` is interpreted by echo and not by the shell, meaning that it must be quoted so that the backslash makes it to echo. 

**Note** 
Some Linux and Mac OS X systems have shells that don’t interpret these echo escape characters, so the above would be shown asnewfile.txt 
```
already exists; overwrite (yes/no)? \c 
```
If testing reveals that your shell works like that, change those specific invocations of echo to the separate program `/bin/echo` and they’ll work fine. All your other echo statements can remain as just regular echo commands, of course. 

### The $$ Variable and Temporary Files 

For now, just keep in mind that when writing shell programs that can be run by more than one person, make sure that each user’s temporary files are unique. 
- One solution is to create temporary files in the user’s home directory instead of /tmp. 
Another way is to choose a temporary filename that will be unique and different for each invocation of the program. A neat way to do this is to embed the unique process ID (PID) of the specific invocation into the filename. This is easily accomplished by referring to the special `$$` shell variable: 
```
$ echo $$ 
4668
grep -v "$name" phonebook > /tmp/phonebook$$ 
mv /tmp/phonebook$$ phonebook 
```
to side-step any potential race conditions. 

### The Exit Status from read 

`read` returns an exit status of zero unless an end-of-file condition is encountered. 
- If the data is coming from the terminal, this means that the user has pressed Ctrl+d. 
- If the data is coming from a file, it means that there’s no more data to read from the file. 

## The printf Command 

The general format of the printf command is 
```bash
printf "format" arg1 arg2 ... 
```
The general format of a conversion specification is 
```bash
%[flags][width][.precision]type 
```


# Your Environment 

## Exported Variables 

There is a way to make the value of a variable known to a subshell, and that’s by exporting it with the export command. The format of this command is simply 
```bash
export variables 
```

That’s why this is true: There is no way to change the value of a variable in a parent shell from within a subshell. 

After a variable is exported, it remains exported to all subshells subsequently executed. 

To summarize the way local and exported variables work: 
1. Any variable that is not exported is a local variable whose existence will not be known to subshells. 
2. Exported variables and their values are copied into a subshell’s environment, where they may be accessed and changed. However, such changes have no effect on the variables in the parent shell. 
3. Exported variables retain this characteristic not only for directly spawned subshells, but also for subshells spawned by those subshells (and so on down the line). 
4. A variable can be exported any time before or after it is assigned a value but takes on its value at the moment of export; subsequent changes aren’t tracked. 

### export -p

If you type `export -p`, you’ll get a list of the variables and their values exported by your shell: 

**PS1 and PS2** 

The sequence of characters that the shell uses as your command prompt are stored in the environment variable PS1. It turns out that you can change this to be anything you want and as soon as you change it, the new value will be used by the shell from that point on. 
```
$ echo :$PS1:
:$ :
$ PS1="==> "
==> pwd
/users/steve
```
Your secondary command prompt, used when a command requires more than a single line of input, defaults to `>` and is kept in the variable PS2. This too you can change to your heart’s content: 
```
$ echo :$PS2:
:> :
$ PS2="=======> " 
```

### CDPATH 
The CDPATH variable works like the PATH variable: it specifies a list of directories to be searched by the shell whenever you execute a **cd** command. 

## More on Subshells 

You know that a subshell can’t change the value of a variable in a parent shell, nor can it change its current directory. Suppose that you want to write a program to set values for some variables that you like to use whenever you log on. 

### The . Command
To address this dilemma, there’s a built-in shell command called **.** (pronounced “dot”) whose general format is **. file** and whose purpose is to execute the contents of file in the current shell. That is, commands from file are executed by the current shell just as if they were typed, not within a subshell. 

### The exec Command 

Within the db program, once the shell process completed, you were done with everything, as demonstrated by the fact that no commands followed `/bin/sh` in the program. Instead of having db wait around for the subshell to finish, you can use the exec command to replace the current program (db) with the new one (/bin/sh). 

The general format of exec is 
```bash
exec program 
```
Because the exec’ed program replaces the current one, there’s one less process hanging around, which helps the system run quickly. The startup time of an exec’ed program is quicker too, due to how Unix systems execute processes. 

`exec` can also be used to close standard input and reopen it with any file that you want to read. To change standard input to `infile`, for example, use the exec command in the form 
```bash
exec < infile
```
Any commands that subsequently read data from standard input will read from infile. 

Redirection of standard output is done similarly. The command 
```bash
exec > report 
```
redirects all subsequent output written to standard output to the file report. 

Note in both of the previous examples that exec is not used to start up execution of a new program, just used to reassign standard input or standard output. 

If you use exec to reassign standard input and later want to reassign it someplace else, you can simply invoke exec again. To reassign standard input back to the terminal, you would write 
```bash
exec < /dev/tty 
```
The same concept also applies to reassignment of standard output. 

### The (...) and { ...; } Constructs 

Sometimes you want to group a set of commands together. For example, you may want to push a sort followed by your plotdata program into the background. Not connected with a pipe; just two commands one after the other. 
It turns out that you can group a set of commands together by enclosing them in parentheses or braces. 
- **The first form causes the commands to be executed by a subshell**, 
- **the latter form by the current shell.**

### Another Way to Pass Variables to a Subshell 

If you want to send the value of a variable to a subshell, there’s another way to do it besides exporting the variable. On the command line, precede the command with the assignment of one or more variables. For example, 
```bash
DBHOME=/uxn2/data DBID=452 dbrun 
```
places the variables DBHOME and DBID, and their indicated values, into the environment of dbrun, then dbrun gets executed. 

These variables will not be known to the current shell, however, because they’re only created for the execution of dbrun. 

In fact, the preceding command behaves identically to typing 
```bash
(DBHOME=/uxn2/data; DBID=452; export DBHOME DBID; dbrun) 
```

# More on Parameters 

## Parameter Substitution 

### ${parameter:-value} 

This construct says to use the value of parameter if it is not null, and to substitute value otherwise. 

### ${parameter:=value} 
 
This version is similar to the previous, but if parameter is null not only is value used, but it is also assigned to parameter as well (note the = in the construct).

### ${parameter:?value}

If parameter is not null, the shell substitutes its value; otherwise, the shell writes value to standard error and then exits (don’t worry—if it’s done from your login shell, you won’t be logged off). If value is omitted, the shell writes the default error message 

With this construct, you can easily check to see whether variables needed by a program are all set and not null: 
```bash
: ${TOOLS:?} ${EXPTOOLS:?} ${TOOLBIN:?} 
```

### ${parameter:+value} 

This one substitutes value if parameter is not null; otherwise, it substitutes nothing. It’s the opposite of `:-`, of course.

## Pattern Matching Constructs 

### ${variable%pattern} 

the shell looks inside variable to see whether it ends with the specified pattern. If it does, the contents of variable are used, with the shortest matching pattern removed from the right. 

### ${variable%%pattern} 
the shell once again looks inside variable to see whether it ends with pattern. This time, however, it removes the longest matching pattern from the right. This is relevant only if the `*` is used in pattern. Otherwise, the `%` and `%%` behave the same way. 
The `#` is used in a similar way to force the pattern matching to start from the left rather than the right. So, the construct. 

### ${variable#pattern}

tells the shell to use the value of variable on the command line, with pattern removed from the left.

### ${variable##pattern}

works like the `#` form, except that the longest occurrence of pattern is removed from the left. 

Remember that in all four cases, no changes are made to the variable itself.

Here are some simple examples to show how these constructs work: 
```bash
$ var=testcase 
$ echo $var 
testcase
$ echo ${var%e} 	# Remove e from right
testcas 
$ echo $var 		# Variable is unchanged
testcase 
$ echo ${var%s*e} 	# Remove smallest match from right 
testca 
$ echo ${var%%s*e} 	# Remove longest match
te 
$ echo ${var#?e} 	# Remove smallest match from left 
stcase 
$ echo ${var#*s} 	# Remove smallest match from left 
tcase 
$ echo ${var##*s} 	# Remove longest match from left 
e
$ echo ${var#test} 	# Remove test from left 
case
$ echo ${var#teas} 	# No match 
testcase$ 
```

# The set Command

## The -x Option 

Within a program, the statement 
```bash
set -x 
```
You can turn off trace mode at any time simply by executing set with the +x option 

## set with No Arguments 

If you don’t give any arguments to set, you’ll get an alphabetized list of all the variables that exist in the current environment, local or exported.

## Using set to Reassign Positional Parameters

You’ll recall that there’s no way to assign a new value to or reassign the value of a positional parameter. Attempts to reassign `$1` to be 100, for example, might be logically written like this: 
```bash
1=100 
```
But it won’t work. Positional parameters are set upon invocation of the shell program. However, there’s a sneaky trick: you can use `set` to change the value. 
```bash
set a b c 
```
will assign `a` to `$1`, `b` to `$2`, and `c` to `$3`. `$#` also gets set to 3 as appropriate for the new argument count.
```bash
$ set one two three four 
$ echo $1:$2:$3:$4 
one:two:three:four 
$ cat words
#
# Count words on a line # 
read line
set $line
echo $#
$ words		#Run it
# Here's a line for you to count. 
7 
$
```
The program reads the user input, storing the line read in the shell variable `line`, then executes the command 
```bash
set $line 
```

This causes each word stored in line to be assigned to the appropriate positional parameter. The variable `$#` is also set to the number of words assigned, which is also the number of words on the line. 

## The -- Option

This tells `set` not to interpret any subsequent dashes or argument-format words it encounters on the command line as options. It also prevents set from displaying all your variables if no other arguments follow, as was the case when you typed a null line. 


# The IFS Variable 

Succinctly, IFS contains a set of characters that are used as whitespace separators.

To determine the actual characters stored in there, pipe the output from echo into the `od` (octal dump) command with the -b (byte display) option: 
```bash
$ echo "$IFS" | od –b 
0000000 040 011 012 012 
0000004
$ 
```
The first column of numbers shown is the relative offset from the start of the input. The following numbers are the octal equivalents of the characters read by `od`. 
- The first such number is 040, which is the ASCII value of the space character. 
- It’s followed by 011, the tab character, 
- and then by 012, the newline character. 
- The next character is another newline which was added by echo. 

This set of characters for IFS should come as no surprise; they’re the whitespace characters we’ve talked about throughout the book. 

Now let’s change IFS to something more visible, the colon: 
```bash
$ IFS=:
$ read x y z
123:345:678
$ echo $x
123
$ echo $z
678
$ list="one:two:three"
$ for x in $list; do echo $x; done 
one
two
three
$ var=a:b:c
$ echo "$var"
a:b:c
$ 
```

Changing IFS is often done in conjunction with the **set** command: 
```bash
$  line="Micro Logic Corp.:Box 174:Hackensack, NJ 07602" 
$  IFS=: 
$  set $line 
$  echo $# 
3 
$  for field; do echo $field; done 
Micro Logic Corp.
Box 174
Hackensack, NJ 07602$
```

Because IFS has an influence on the way things are interpreted by the shell, if you’re going to change it in your program it’s usually wise to save the old value first in another variable (such as OIFS) and then restore it after you’ve finished the operations. 


## The readonly Command

The readonly command is used to specify variables whose values cannot be subsequently changed. For example, 
```bash
readonly PATH HOME
```
To get a list of your read-only variables, type readonly –p without any arguments: 
```bash
$ readonly -p
```

The read-only variable attribute is **not passed down to subshells**. Also, after a variable has been made read-only in a shell, there is no way to “undo” it. 

## The unset Command

Sometimes you may want to remove the definition of a variable from your environment. To do so, you type unset followed by the names of the variables: 
```bash
$ x=100
$ echo $x 
100 
$  unset x 		# Remove x from the environment 
$  echo $x 
$ You 
```
can’t unset a read-only variable. Furthermore, the variables IFS, MAILCHECK, PATH, PS1, and PS2 cannot be unset. 


# MISC Commands


## The eval Command

Its format is as follows: 
```bash
eval command-line 
```
The shell **scans the command line twice** before executing it, which can be very useful if the script is building a command that needs to be invoked, among other purposes. 

But consider the following example without the use of eval: 
```bash
$ pipe="|"
$ ls $pipe wc -l
|: No such file or directory 
wc: No such file or directory 
-1: No such file or directory $ 
$ eval ls $pipe wc –l 
16 
$ 
```

The eval command is frequently used in shell programs that build up command lines inside one or more variables. If the variables contain any characters that must be interpreted by the shell, eval is essential. Command terminator `(;, |, &)`, I/O redirection `(<, >)`, and quote characters are among the characters that must appear directly on the command line to have special meaning to the shell. 
```bash
$ cat last
eval echo \$$#
$ last one two three four 
four
$ last *
zoo_report
$ 
```
The first time the shell scans 
```bash
echo \$$# 
```
Get the `last` file.
The backslash tells it to ignore the `$` that immediately follows. After that, it encounters the special parameter `$#`, so it substitutes its value on the command line. The command now looks like this: 
```bash
echo $4
```
The backslash is removed by the shell after the first scan. When the shell rescans this line, it substitutes the value of $4 and then executes echo. 

**Display the positional parameter referenced by arg.**

```bash
eval echo \${$arg} 
```
The eval command can also be used to effectively create “pointers” to variables: 
```bash
$ x=100
$ ptrx=x
$ eval echo \$$ptrx 		# Dereference ptrx
100
$ eval $ptrx=50		# Store 50 in var that ptrx points to
$ echo $x			# See what happened
50
$ 
```

## The wait Command 

The wait command does the job. Its general format is 
```bash
wait process-id 
```

where process-id is the process ID of the process you want to complete. 
Execution of your current shell will be suspended until the process or processes finish execution. 

**The $! Variable** 

If you have only one process running in the background, then wait with no argument suffices. However, if you’re running more than one background command and you want to wait onthe most recently launched, you can access the process ID of the most recent background command as the special variable `$!`. So the command 
```bash
wait $! 
```

## The trap Command 

Signal handling in a shell program is done with the trap command, whose general format is 
```bash
trap commands signals 
```
where commands is one or more commands that will be executed whenever any of the signals specified by signals is received. 

As an example of the trap command, the following shows how you can remove some files and then exit if someone tries to interrupt the program from the terminal: 
```bash
trap "rm $WORKDIR/work1$$ $WORKDIR/dataout$$; exit" INT
```

Signal number 1—SIGHUP or just HUP—is generated for hangup: originally this related to dialup connections, but now more generally refers to an unexpected **disconnect like the Internet connection dropping**. 

The sequence specified to trap (also known as the trap handler) must be enclosed in quotes if it contains more than one command. 

Also note that the shell scans the command line at the time that the trap command gets executed and also again when one of the listed signals is received. (**TWICE!!!**)

In the preceding example, the value of WORKDIR and $$ will be substituted at the time that the trap command is executed. If you wanted this substitution to occur at the time that a signal was received, you can put the commands inside **single quotes**: (**ONCE!!!**)
```bash
trap 'rm $WORKDIR/work1$$ $WORKDIR/dataout$$; exit' INT HUP 
```

### trap with No Arguments

Executing trap with no arguments results in the display of any trap handlers that you have defined or modified.

### Ignoring Signals 

If the command listed for trap is null, the specified signal will be ignored when received. For example, the command 
```bash
trap "" SIGINT 
```
In the above example, the first argument must be specified as a null value for a signal to be ignored and is not equivalent to writing the following, which has a separate meaning of its own: 
```bash
trap 2 
```

- If you ignore a signal, all subshells also ignore that signal. 
- If you specify a signal handler action, however, all subshells will automatically take the default action on receipt of that signal, not the new code sequence. 

Suppose that you execute the command 
```bash
trap "" 2 
```

### Resetting Traps 

After you’ve changed the default action to be taken on receipt of a signal, you can change it back again with trap if you simply omit the first argument; so 
```bash
trap HUP INT
```

## More on I/O 
redirect standard error from any command simply by writing `2>` instead of just `>`: 
```bash
command 2> file
```
Sometimes you may want to explicitly write to standard error in your program. With a slight variation on the above, you can redirect standard output to standard error by writing 
```bash
command >&2 
```
The notation `>&` specifies output redirection to a file associated with the file descriptor that follows. It’s important to remember that no space is permitted between the `>` and the `&`. 

You may want to redirect both standard output (often abbreviated “stdout”) and standard error output (“stderr”) from a program into the same file. If you know the name of the file, this is straightforward: 
```bash
command > foo 2>> foo
```
Here both stdout and stderr will be written to foo. 
You can also write 
```bash
command > foo 2>&1 
```

You can also dynamically redirect standard input or output in a program using the **exec** command: 

```bash
exec < datafile
```
redirects standard input from the file datafile. Subsequent commands executed that read from standard input will read from datafile instead. 

The command 
```bash
exec > /tmp/output 
```
does the same thing with standard output: all commands that subsequently write to standard output will write to /tmp/output unless explicitly redirected elsewhere. 

Naturally, standard error can be reassigned as well: 
```
exec 2> /tmp/errors
```

All subsequent output to standard error will go to /tmp/errors. 

### <&- and >&-

The sequence `>&-` has the effect of closing standard output. If preceded by a file descriptor, the associated file is closed instead. So writing 
```bash
ls >&-
```
causes the output from `ls` to go nowhere because standard output is closed by the shell before ls is executed. Not hugely useful, we admit! 

## In-line Input Redirection (here documents)

If the `<<` characters follow a command in the format 
```bash
command <<word 
```
the shell uses the lines that follow as the input for command, until a line that contains just **word** is found. 

Here’s a common example of how this feature is used within a shell program: 
```bash
$ cat mailmsg
mail $* <<END-OF-DATA 
Attention: 
Our monthly computer users group meeting will take place on Friday, March 4, 2016 at 8pm in Room 1A-308. Please try to attend. 
END-OF-DATA 
$ 
```
To send this message to all members of the group as stored in the file users_list, you could invoke 
```bash
mailmsg $(cat users_list) 
```
To side-step all the issues with the shell interpreting the contents of the lines, use backslash on the end-of-document word instead: 
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

You now know about the `<<\` sequence, but there’s another one that most modern shells understand: If the first character that follows the `<<` is a **dash (-)**, any leading tab characters in the input will be removed by the shell. 

### Shell Archives (!!!)

One of the best uses of the in-line input redirection feature is for creating shell archive files. With this technique, one or more related shell programs can be put into a single file and then sent to someone else using the standard Unix mail commands. When the archive is received, it can be “unpacked” by invoking it as a shell program. 


# Functions 

To define a function, you use the general format: 
```bash
name () { command; ... command; } 
```

Note that **at least one whitespace character must separate the { from the first command**, and that a semicolon must separate the last command from the closing brace if they occur on the same line.

Functions exist only in the shell in which they’re defined so they can’t be passed to subshells. Because the function is executed in the current shell, changes made to the current directory or to variables remain after the function has completed execution, as if it had been invoked with the **.** command.

Functions execute faster than an equivalent shell program because the shell doesn’t have to search the disk for the program, open the file, and read its contents into memory; it can just jump right into executing the individual commands directly. 

## Removing a Function Definition 

To remove the definition of a function from the shell, use the unset command with the `–f` option. Look familiar? It is the same command you use to remove the definition of a variable from the shell. 
```bash
$ unset –f nu
```

## The return Command 

If you use exit from inside a function, its effect is not only to terminate execution of the function but also of the shell program that called the function. It exits all the way back to the command line. If you instead want to just exit the function, use the return command, whose format is 
```bash
return n
```

The value n is used as the return status of the function. If omitted, the status is that of the last command executed. This is also what gets returned if you don’t include a return statement in your function. The return status is in all other ways equivalent to the exit status: you can access its value through the shell variable `$?`, and you can test it in if, while, and until commands. 

## The type Command 

When you type in the name of a command to execute, it’s useful to know whether the command is a function, a shell built-in function, a standard Unix command or even a shell alias. This is where the type command comes in handy. The type command takes one or more command names as its argument and tells you what it knows about it. 


# Interactive and Nonstandard Shell Features 

## The ENV File 

When you start the shell, one of the first things it does is look in your environment for a variable called ENV. If it finds it and it’s non-null, the file specified by ENV will be executed, much like the .profile is executed when logging in.If you do decide to have an ENV file, you should set and export the ENV variable inside your .profile file: 
```bash
$ cat .profile
...
export ENV=$HOME/.alias 
...
$ 
```

## Command-Line Editing 

To turn on a line edit mode, use the set command with the -o mode option, where mode is either vi or emacs: 
```bash
$ set -o vi 		# Turn on vi mode 
```

Put this in your .profile or ENV file to automatically start up the shell with one of the edit modes turned on. 

## Command History 

You can change this filename to anything you want by setting the variable HISTFILE to the name of your history file. This variable can be set and exported in your .profile file. 

Other Ways to Access Your History 
The history Command
The fc Command 
The r Command 

# bash vs ksh functions

Bash and the Korn shell both have function features not available in the POSIX standard shell. Let’s have a look. 

##   Integer Arithmetic 

Both Bash and the Korn shell support evaluating arithmetic expressions without arithmetic expansion. The syntax is similar to `$((...))` but without the dollar sign. Because expansion is not performed, the construct can therefore be used by itself as a command: 
```bash
$ x=10
$ ((x = x * 12)) 
$ echo $x
120
$
``` 
So writing 
```bash
(( i == 100 ))
```
has the effect of testing i to see whether it is equal to 100 and setting the exit status appropriately. 

This makes integer arithmetic ideal for inclusion in if conditionals: 
```bash
if (( i == 100 )) 
then 
	... 
fi
```
The `(( i == 100 ))` returns an exit status of zero (true) if i equals 100 and one (false) 
otherwise, and has the same effect as writing 
```bash
if [ "$i" -eq 100 ] 
then 
	... 
fi
```
Another advantage of using `((...))` rather than `test` is the ability to perform arithmetic as part of the test: 
```bash
if (( i / 10 != 0 )) 
then 
	... 
fi
```

## Integer Types 

Both the Korn and Bash shells support an integer data type. You can declare variables to be integers by using the typeset command with the –i option 
```bash
typeset -i variables
```
where variables are any valid shell variable names. Initial values can also be assigned to the variables at the time they are declared: 
```bash
typeset -i signal=1 
```
The main benefit: arithmetic performed on integer variables with the `((...))` construct is faster than on non-integer values. 

However, an integer variable cannot be assigned anything but an integer value or integer expression. If you attempt to assign a non-integer to it, the message bad number is printed by the shell: 
```bash
$ typeset -i i
$ i=hello
ksh: i: bad number 
```

## Numbers in Different Bases 
To write a number in a different base with these shells, you use the notation base#numberYou can write constants in different bases anywhere an integer value is permitted. To assign octal 100 to the integer variable i, you can write 
```bash
typeset -i i=8#100
```
There’s a subtlety in the above example too: while the display value of i is set to octal, the default numeric base for values assigned to the variable remain decimal unless specified otherwise. In other words, `i=50` was not equivalent to `i=8#50` even though the shell knew i was to be referenced as base 8. 




## Arrays 

Both Korn and Bash provide a limited array capability. Bash arrays may contain an unlimited number of elements (subject to memory limitations); Korn shell arrays are limited to 4096 elements. Array indexing in both shells starts at zero. 
An array element is accessed with a subscript, which is an integer-valued expression enclosed within square brackets. 
```bash
$ arr[0]=hello
$ arr[1]="some text"
$ arr[2]=/users/steve/memos 
$ 
$ echo ${array[0]} 
hello
$ echo ${array[1]} 
some text 
$ echo ${array[2]} 
/users/steve/memos 
$ echo $array 
hello 
$ 
```
The construct `[*]` can be used as a subscript to produce all the elements of an array on the command line, with each element separated by a space. 
```bash
$ echo ${array[*]}
hello some text /users/steve/memos 
$ 
$ array[10]=foo
$ echo ${array[*]} 			#Display all elements 
hello some text /users/steve/memos foo
$ echo ${#array[*]} 			# Number of elements 
4
```
You can declare an array of integers by specifying the array name to `typeset -i`: 
```bash
typeset -i data 
```
```bash
$ typeset -i array
$ array[0]=100
$ array[1]=50
$ (( array[2] = array[0] + array[1] )) 
$ echo ${array[2]} 
150
$ i=1
$ echo ${array[i]}
50
$ array[3]=array[0]+array[2] 
$ echo ${array[3]}
250
$ 
```

# Job Control 

In its easiest usage, the jobs command is used to print the status of jobs that haven’t completed. 
```bash
$ jobs 
```
For example, the shell’s built-in kill command can be used to terminate a job running in the background. The argument to it can be a process ID or a percent sign (%) followed by a job number, a + (current job), a – (previous job), or another % (also current job). 

The preceding kill could have used `%+` or `%%` to refer to the same job. 

The first few characters of the command sequence can also be used to refer to a job; for example, `kill %pic` would have worked in the preceding example. 

## Stopped Jobs and the fg and bg Commands 

If you are running a job in the foreground (without an &) and you want to suspend it, you can press **Ctrl+z**. The job stops executing, and the shell prints the message 
```
[n] + Stopped (SIGTSTP) sequence 
```

The stopped job becomes the current job. To have it continue executing, use the fg or bg command: 
- The fg command causes the current job to resume execution in the foreground, 
- and bg causes the current job to resume execution in the background. 

You can also specify a job number, the first few characters of the pipeline, `a +, a -, or a %` preceded by `a %` to specify any job to the fg and bg commands. 

Output from a background job normally goes directly to the terminal, which can be confusing if you’re doing something else at the time. There’s a fix, though: The command 
```bash
stty tostop 
```
causes any background job that attempts to write to the terminal to be stopped and the message 
```
[n] - Stopped (SIGTTOU) sequenceto 
```
be printed.


# Order of Search 

It’s worthwhile understanding the search order that the shell uses when you type in a command name: 
1. The shell first checks to see whether the command is a reserved word (such as for or do). 
2. If it’s not a reserved word and is not quoted, the shell next checks its alias list, and if it finds a match, performs the substitution. If the alias definition ends in a space, it also attempts alias substitution on the next word. The final result is then checked against the reserved word list, and if it’s not a reserved word, the shell proceeds to step 3. 
3. The shell checks the command against its function list and executes the eponymous function if found. 
4. The shell checks to see whether the command is a built-in command (such as cd and pwd). 
5. Finally, the shell searches the PATH to locate the command. 
If the command still isn’t found, a “command not found” error message is issued. 


















































