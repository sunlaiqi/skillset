


# Literals

Literals are the simplest form of pattern matching in regular expressions. They will simply succeed whenever that literal is found.

# Boundary Matchers

Matcher Description
```
^       Matches at the beginning of a line
$       Matches at the end of a line
\b      Matches a word boundary
\B      Matches the opposite of \b. Anything that is not a word boundary 
\A      Matches the beginning of the input
\Z      Matches the end of the input
```

# Predefined Character Classes (a.k.a. Special Sequences)

A character class (or character set) is a set of characters enclosed within square brackets. It specifies the characters that will successfully match a single character from a given input string.

```
Element     Description (for regex with default flags)

.           any character except newline \n
\d          any decimal digit; this is equivalent to the class [0-9]
\D          any non-digit character; this is equivalent to the class [^0-9]
\s          any whitespace character; this is equivalent to the class [⇢\t\n\r\f\v]
\S          any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v]
\w          any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]
\W          any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]
\b          the boundary (or empty string) at the start and end of a word, that is, between \w and \W.
\B          Matches where \b does not, that is, the boundary of \w characters.
\A          its right at the absolute start of a string whether in single or multi-line mode. ignores m flag
\Z          its left at the absolute end of a string whether in single or multi-line mode. ignores m flag
\g<id>      matches a previously defined group
[\b]        Backspace character
\YYY	    Octal character YYY
\xYY	    Hexadecimal character YY
```

# Sets

```
[ ]         Contains a set of characters to match.
[amk]       Matches either a, m, or k. It does not match amk.
[a-z]       Matches any alphabet from a to z.
[a\-z]      Matches a, -, or z. It matches - because \ escapes it.
[a-]        Matches a or -, because - is not being used to indicate a series of characters.
[-a]        As above, matches a or -.
[a-z0-9]    Matches characters from a to z and also from 0 to 9.
[(+*)]      Special characters become literal inside a set, so this matches (, +, *, and ).
[^ab5]      Adding ^ excludes any character in the set. Here, it matches characters that are not a, b, or 5.
```

# Groups

```
( )             Matches the expression inside the parentheses and groups it.
(? )            ? acts as an extension notation. Its meaning depends on the character immediately to its right.
(?P<name>AB)    Creates a named capturing group. Matches the expression AB, and it can be accessed with the group name.
(?aiLmsux)      Here, a, i, L, m, s, u, and x are flags: Set flags within regex
                a — Matches ASCII only
                i — Ignore case
                L — Locale dependent
                m — Multi-line, ^ and $ match start and end of line
                s — Matches all, . matches newline as well
                u — Matches unicode
                x — Verbose, Allow spaces and comments
(?:A)           Matches the expression as represented by A, but unlike (?PAB), Non-capturing group.
(?#...)         A comment. Contents are for us to read, not for matching.
A(?=B)          Lookahead assertion. This matches the expression A only if it is followed by B.
A(?!B)          Negative lookahead assertion. This matches the expression A only if it is not followed by B.
(?<=B)A         Positive lookbehind assertion. This matches the expression A only if B is immediately to its left. 
                This can only matched fixed length expressions.
(?<!B)A         Negative lookbehind assertion. This matches the expression A only if B is not immediately to its left. 
                This can only matched fixed length expressions.
(?P=name)       Matches the expression matched by an earlier group named “name”.
(...)\1         The number 1 corresponds to the first group to be matched. 
                If we want to match more instances of the same expresion, simply use its number instead of writing out 
                the whole expression again. We can use from 1 up to 99 such groups and their corresponding numbers.
\N	            backreference, gives matched portion of Nth capture group, applies to both search and replacement sections
\0 and \100     onwards are considered as octal values, hence cannot be used as backreferences.
(?(id)yes|no)   Match 'yes' if group 'id' matched, else 'no'
```

# Popular Python re Module Functions

```
re.findall(A, B)        Matches all instances of an expression A in a string B and returns them in a list.
re.finditer(A, B)       Iterator with re.Match object for each match
re.search(A, B)         Matches the first instance of an expression A in a string B, and returns it as a re match object.
re.split(A, B)          Split a string B into a list using the delimiter A.
re.sub(A, B, C)         Replace A with B in the string C.
re.compile(A)	        Compile a pattern A for reuse, outputs re.Pattern object
re.subn(A, B, C)	    Gives tuple of modified string and number of substitutions
```

The function definitions are given below:

```
re.search(pattern, string, flags=0)
re.fullmatch(pattern, string, flags=0)
re.compile(pattern, flags=0)
re.sub(pattern, repl, string, count=0, flags=0)
re.escape(pattern)
re.split(pattern, string, maxsplit=0, flags=0)
re.findall(pattern, string, flags=0)
re.finditer(pattern, string, flags=0)
re.subn(pattern, repl, string, count=0, flags=0)
```

# Metacharacters

A metacharacter is a character that has a special meaning during pattern processing.
The metacharacters should be escaped if they are to be used with their literal meaning:
```
Backslash               \   Escapes special characters or denotes character classes.
Caret                   ^   Matches the expression to its right at the start of every string before \n.
Dollar sign             $   Matches the expression to its left at the start of every string before \n.
Dot                     .   Matches any character except line terminators like \n.
Pipe symbol             |   A|B - Matches expression A or B. If A is matched first, B is left untried.
Question mark           ?   Greedily matches the expression to its left 0 or 1 times. 
                            But if ? is added to qualifiers (+, *, and ? itself) it matches in a non-greedy manner.
Asterisk                *   Greedily matches the expression to its left 0 or more times.
Plus sign               +   Greedily matches the expression to its left 1 or more times.
Opening parenthesis     (
Closing parenthesis     )
Opening square bracket  [
Closing square bracket  ]
Opening curly brace     {   {m} - Matches the expression to its left m times, and not less.
Closing curly brace     }   {m,n} - Matches the expression to its left m to n times, and not less.
                            {m,n}? - Matches the expression to its left m to n times, as few as possible.
```

Metacharacters are not active inside classes. For example, `[akm$]` will match any of the characters `'a', 'k', 'm', or '$'`.


# The Backslash Plague

In short, to match a literal backslash, one has to write '`\\\\`' as the RE string, because the regular expression must be `\\`, and each backslash must be expressed as `\\` inside a regular Python string literal.

The solution is to use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with 'r', so `r"\n"` is a two-character string containing '`\`' and 'n', while `"\n"` is a one-character string containing a newline. 

```
Regular String      Raw string
"ab*"               r"ab*"
"\\\\section"       r"\\section"
"\\w+\\s+\\1"       r"\w+\s+\1"
```

# Greedy and reluctant quantifiers

- The greedy behavior of the quantifiers is applied by default in the quantifiers. A greedy quantifier will try to match as much as possible to have the biggest match result possible.
- The non-greedy behavior can be requested by adding an extra question mark to the quantifier; for example, `??, *? or +?`. A quantifier marked as reluctant will behave like the exact opposite of the greedy ones. They will try to have the smallest match possible.


#  Regular Expressions with Python

## RegexObject

It is also known as Pattern Object. It represents a compiled regular expression

**MatchObject**: It represents the matched pattern

If we want to re-use the regular expression, we can use the following code:
```
   >>> pattern = re.compile(r'<HTML>')
   >>> pattern.match("<HTML>")
```
On the other hand, we can directly perform the operation on the module using the following line of code:
```
>>> re.match(r'<HTML>', "<HTML>")
```

**match(string[, pos[, endpos]])**

This method tries to match the compiled pattern only **at the beginning of the string**. If there is a match, then it returns a `MatchObject`.

**search(string[, pos[, endpos]])**

It tries to match the pattern at any location of the string and not just at the beginning. If there is a match, it returns a `MatchObject`.

**findall(string[, pos[, endpos]])**

The previous operations worked with one match at a time. On the contrary, in this case it returns a list with all the non-overlapping occurrences of a pattern and not the `MatchObject` like `search` and `match` do.

Keep in mind that empty matches are a part of the result:
```python
   >>> pattern = re.compile(r'a*')
   >>> pattern.findall("aba")
       ['a', '', 'a', '']
```

In case there are groups in the pattern, they are returned as tuples.

```python
>>> pattern = re.compile(r"(\w+) (\w+)")
>>> pattern.findall("Hello world hola mundo")
    [('Hello', 'world'), ('hola', 'mundo')]
```

**finditer(string[, pos[, endpos]])**

Its working is essentially the same as `findall`, but it returns an iterator in which each element is a `MatchObject`, so we can use the operations provided by this object.

## Compilation flags
```
re.I        The pattern will match lower case and upper case.
re.M        Match multiple lines
re.S        The metacharacter "." will match any character even the newline.
```

## Grouping 

**group([group1, ...])**

The `group` operation gives you the subgroups of the match. If it's invoked with no arguments or zero, it will return the entire match; while if one or more group identifiers are passed, the corresponding groups' matches will be returned.

```python
>>> pattern = re.compile(r"(\w+) (\w+)") 
>>> match = pattern.search("Hello world")
>>> match.group() 
'Hello world'
>>> match.group(0) 
'Hello world'
>>> match.group(1)
'Hello'
>>> match.group(2)
'world'
>>> match.group(3)
   ...
   IndexError: no such group
>>> match.group(0, 2) 
('Hello world', 'world')
```
Groups can be named,

```python
>>> pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")
>>> match = pattern.search("Hello world") 
>>> match.group('first')
'Hello'
>>> match.group(1)
'Hello'
>>> match.group(0, 'first', 2) 
('Hello world', 'Hello', 'world')
```

**groups([default])**

It returns a tuple with all the subgroups in the match instead of giving you one or some of the groups.
```python
>>> match.groups()
      ('Hello', 'World')
```

In case there are groups that don't match, the default argument is returned. If the default argument is not specified then `None` is used, for example:
```python
>>> pattern = re.compile("(\w+) (\w+)?") 
>>> match = pattern.search("Hello ")
>>> match.groups("mundo")
('Hello', 'mundo') 
>>> match.groups() 
('Hello', None)
```

**groupdict([default])**

The `groupdict` method is used in the cases where named groups have been used. It will return a dictionary with all the groups that were found:
```python
>>> pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)") 
>>> pattern.search("Hello world").groupdict()
{'first': 'Hello', 'second': 'world'}
```

### Backreferences

using the captured group inside the regex or other operations.
```python
>>>pattern = re.compile(r"(\d+)-(\w+)") 
>>>pattern.sub(r"\2-\1", "1-a\n20-baer\n34-afcr") 
'a-1\nbaer-20\nafcr-34'
```

### Named groups

```
Use                                             Syntax
Inside a pattern                                (?P=name)
In the repl string of the sub operation         \g<name>
In any of the operations of the MatchObject     match.group('name')
```

### Flags per group

`(?iLmsux)`

```
Letter  Flag
i       re.IGNORECASE 
L       re.LOCALE
m       re.MULTILINE
s       re.DOTALL
u       re.UNICODE 
x       re.VERBOSE
```

### Capturing and Non-capturing groups

The only difference between capture groups and non-capture groups is that the former captures the matched character sequences for possible later re-use with a numbered back reference while a non-capture group does not.   Both are used to group subexpressions, which is the main reason most people will utilize parentheses `( )` within regular expressions.

For example, if we want to match a repeating sequence such as `Urgent` we could use either `(Urgent)+` or `(?:Urgent)+`.  Both will match sequences such as `UrgentUrgent` and `UrgentUrgentUrgent`.   The only difference is that the capture group consisting just of parentheses `( )` stores the matched pattern internally in a results array from which we can summon it later in that same regular expression using the back reference `\1` while the non-capture group consisting of an opening sequence of `(?: with a closing sequence of )` does not store the matched pattern internally.

**Capturing groups**:

```py
str1 = "Jane Isabelll Smith John"
print(re.findall(r'(Jane|John|Alison)\s(.*?)\s(Smith|Smuth)', str1))

match = re.search(r'(Jane|John|Alison)\s(.*?)\s(Smith|Smuth)', str1)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
```
Result:
```
[('Jane', 'Isabelll', 'Smith')]
Jane Isabelll Smith
Jane
Isabelll
Smith
```

**Non-capturing groups**:

```py
str1 = "Jane Isabelll Smith John"
print(re.findall(r'(?:Jane|John|Alison)\s(.*?)\s(?:Smith|Smuth)', str1))

match = re.search(r'(?:Jane|John|Alison)\s(.*?)\s(?:Smith|Smuth)', str1)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
```
Result:
```
['Isabelll']
Jane Isabelll Smith
Isabelll
Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print(match.group(2))
IndexError: no such group
```


# Validate Email Addresses

Simple

This first solution does a very simple check. It only validates that the string contains an at sign (@) that is preceded and followed by one or more non-whitespace characters.

`^\S+@\S+$`


Simple, with restrictions on characters
The domain name, the part after the @ sign, is restricted to characters allowed in domain names. Internationalized domain names are not allowed. The local part, the part before the @ sign, is restricted to characters commonly used in email local parts, which is more restrictive than what most email clients and servers will accept:
```
^[A-Z0-9+_.-]+@[A-Z0-9.-]+$
```

Simple, with all valid local part characters
This regular expression expands the previous one by allowing a larger set of rarely used characters in the local part. Not all email software can handle all these characters, but we’ve included all the characters permitted by RFC 5322, which governs the email message format. Among the permitted characters are some that present a security risk if passed directly from user input to an SQL statement, such as the single quote `(')` and the pipe character `(|)`. Be sure to escape sensitive characters when inserting the email address into a string passed to another program, in order to prevent security holes such as SQL injection attacks:
```
^[A-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Z0-9.-]+$
```

No leading, trailing, or consecutive dots
Both the local part and the domain name can contain one or more dots, but no two dots can appear right next to each other. Furthermore, the first and last characters in the local part and in the domain name must not be dots:
```
^[A-Z0-9_!#$%&'*+/=?`{|}~^-]+(?:\.[A-Z0-9_!#$%&'*+/=?`{|}~^-]+↵)*@[A-Z0-9-]+(?:\.[A-Z0-9-]+)*$
```

Top-level domain has two to six letters
This regular expression adds to the previous versions by specifying that the domain name must include at least one dot, and that the part of the domain name after the last dot can only consist of letters. That is, the domain must contain at least two levels, such as `secondlevel.com` or `thirdlevel.secondlevel.com`. The top-level domain (`.com` in these examples) must consist of two to six letters. All country-code top-level domains (`.us`, `.uk`, etc.) have two letters. The generic top-level domains have between three (`.com`) and six letters (`.museum`):
```
^[\w!#$%&'*+/=?`{|}~^-]+(?:\.[\w!#$%&'*+/=?`{|}~^-]+)*@↵(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$
```

Discussion
About email addresses
If you thought something as conceptually simple as validating an email address would have a simple one-size-fits-all regex solution, you’re quite wrong. This recipe is a prime example that before you can start writing a regular expression, you have to decide exactly what you want to match. There is no universally agreed-upon rule as to which email addresses are valid and which not. It depends on your definition of valid.

