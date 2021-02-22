


# Redirecting man page output to file results in double letters in words

man djpeg | col -b > textfile.txt

Output to be formatted as pdf file.
man -t jq | pstopdf -i -o jq.pdf



# `$(...), (...), $((...)), ((...)), ${...}, {...}`


`$(...)` means execute the command in the parens in a subshell and return its stdout. Example:
```
$ echo "The current date is $(date)"
The current date is Mon Jul  6 14:27:59 PDT 2015
```

`(...)` means run the commands listed in the parens in a subshell. Example:
```
$ a=1; (a=2; echo "inside: a=$a"); echo "outside: a=$a"
inside: a=2
outside: a=1
```

`$((...))` means perform arithmetic and return the result of the calculation. Example:
```
$ a=$((2+3)); echo "a=$a"
a=5
```

`((...))` means perform arithmetic, possibly changing the values of shell variables, but don't return its result. Example:
```
$ ((a=2+3)); echo "a=$a"
a=5
```

`${...}` means return the value of the shell variable named in the braces. Example:
```
$ echo ${SHELL}
/bin/bash
```

`{...}` means execute the commands in the braces as a group, not in subshell. Example:
```
$ false || { echo "We failed"; exit 1; }
We failed
```


`[..]` is used in conditions or logical expressions. Example:
```
$ VAR=2
$ if [ $VAR -eq 2 ]

> then
> echo 'yes'
> fi
yes
```

`[[...]]` offers extended functionality to single square brackets. Particularly, it is useful for `=~` operator (used in regular expressions). Example:
```
$ VAR='some string'
$ if [[ $VAR =~ [a-z] ]]; then
> echo 'is alphabetic'
> fi
is alphabetic
```

The `$` sign invariably signifies an expansion. i.e., based on what comes after the `$` (like `((, (, {`, etc.) some string value is computed and the `$...` expression is replaced with the computed string. 