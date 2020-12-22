


Here’s a complete list of the metacharacters
```
. ^ $ * + ? { } [ ] \ | ( )
```

- Metacharacters are not active inside classes. For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$'; '$' is usually a metacharacter, but inside a character class it’s stripped of its special nature.


# The Backslash Plague

In short, to match a literal backslash, one has to write '`\\\\`' as the RE string, because the regular expression must be `\\`, and each backslash must be expressed as `\\` inside a regular Python string literal.

The solution is to use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with 'r', so `r"\n"` is a two-character string containing '`\`' and 'n', while `"\n"` is a one-character string containing a newline. R

```
Regular String      Raw string
"ab*"               r"ab*"
"\\\\section"       r"\\section"
"\\w+\\s+\\1"       r"\w+\s+\1"
```










