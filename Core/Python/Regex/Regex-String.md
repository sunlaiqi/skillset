- [shlex](#shlex)
  - [An example](#an-example)
  - [Definitions](#definitions)
  - [shlex Class](#shlex-class)
  - [shlex Objects](#shlex-objects)
  - [Module Functions](#module-functions)
- [csv — CSV File Reading and Writing](#csv--csv-file-reading-and-writing)
  - [Introduction](#introduction)
  - [The example](#the-example)
  - [Module Contents](#module-contents)
- [regex](#regex)
  - [An example](#an-example-1)


# shlex

The shlex class makes it easy to write lexical analyzers for simple syntaxes resembling that of the Unix shell. 

## An example

To split a string by comma ',' but preserving quotes '"', like this:
```python
import shlex

s = '044,Octoplat,"Grass,Poison","Fire,Flying,Ice,Psychic","045,182"'

def convert_list(s):
    # First, create a instance of shlex class
    parser = shlex.shlex(s)
    # Then add comma ',' as delimiter
    parser.whitespace += ','
    # Convert shlex instance into a list
    lst = list(parser)
    # since shlex preserves quote, we need to strip it
    for i in range(len(lst)):
        lst[i] = lst[i].strip('"')
    return lst
print(convert_list(s))

```
The result will be:
```
['044', 'Octoplat', 'Grass,Poison', 'Fire,Flying,Ice,Psychic', '045,182']
```
## Definitions

**token**
A sequence of characters considered a single unit by the shell. It is either a word or an operator.


## shlex Class

The shlex module defines the following class:
```python
class shlex.shlex(instream=None, infile=None, posix=False, punctuation_chars=False)
```
A shlex instance or subclass instance is a lexical analyzer object. 
- The initialization argument, if present, specifies where to read characters from. It must be a file-/stream-like object with read() and readline() methods, or a string. If no argument is given, input will be taken from sys.stdin. 
- The second optional argument is a filename string, which sets the initial value of the infile attribute. If the instream argument is omitted or equal to sys.stdin, this second argument defaults to “stdin”. 
- The posix argument defines the operational mode: when posix is not true (default), the shlex instance will operate in compatibility mode. When operating in POSIX mode, shlex will try to be as close as possible to the POSIX shell parsing rules.
- The punctuation_chars argument provides a way to make the behaviour even closer to how real shells parse. This can take a number of values: the default value, False, preserves the behaviour seen under Python 3.5 and earlier. If set to True, then parsing of the characters ();<>|& is changed: any run of these characters (considered punctuation characters) is returned as a single token. If set to a non-empty string of characters, those characters will be used as the punctuation characters. Any characters in the wordchars attribute that appear in punctuation_chars will be removed from wordchars.

## shlex Objects

A shlex instance has the following methods:

shlex.get_token()
Return a token. If tokens have been stacked using push_token(), pop a token off the stack. Otherwise, read one from the input stream. If reading encounters an immediate end-of-file, eof is returned (the empty string ('') in non-POSIX mode, and None in POSIX mode).

shlex.whitespace
Characters that will be considered whitespace and skipped. Whitespace bounds tokens. By default, includes space, tab, linefeed and carriage-return.
```python
shlex.whitespace += ','
```

shlex.escape
Characters that will be considered as escape. This will be only used in POSIX mode, and includes just '\' by default.


shlex.quotes
Characters that will be considered string quotes. The token accumulates until the same quote is encountered again (thus, different quote types protect each other as in the shell.) By default, includes ASCII single and double quotes.

shlex.token
The token buffer. It may be useful to examine this when catching exceptions.

## Module Functions

The shlex module defines the following functions:

shlex.split(s, comments=False, posix=True)
Split the string s using shell-like syntax. If comments is False (the default), the parsing of comments in the given string will be disabled (setting the commenters attribute of the shlex instance to the empty string). This function operates in POSIX mode by default, but uses non-POSIX mode if the posix argument is false.

shlex.join(split_command)
Concatenate the tokens of the list split_command and return a string. This function is the inverse of split().


# csv — CSV File Reading and Writing

## Introduction

The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.

The lack of a well-defined standard means that subtle differences often exist in the data produced and consumed by different applications. These differences can make it annoying to process CSV files from multiple sources. 
Still, while **the delimiters and quoting characters vary**, the overall format is similar enough that it is possible to write a single module which can efficiently manipulate such data, hiding the details of reading and writing the data from the programmer.

The csv module implements classes to read and write tabular data in CSV format. It allows programmers to say, “write this data in the format preferred by Excel,” or “read data from this file which was generated by Excel,” without knowing the precise details of the CSV format used by Excel. Programmers can also describe the CSV formats understood by other applications or define their own special-purpose CSV formats.

The csv module’s reader and writer objects read and write sequences. Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.

## The example


```python
import csv

with open('database.csv', newline='') as f:
    f.readline()
    reader = csv.reader(f, delimiter=',')
    # print(list(reader))
    for line in reader:
        print(line)
```
result:
```
['004', 'Banub', 'Fire', 'Ground,Rock,Water', '005']
['005', 'Banubeleon', 'Fire', 'Ground,Rock,Water', '006']
['006', 'Banubizard', 'Fire,Flying', 'Rock,Electric,Water', '']
['043', 'Octopeat', 'Grass,Poison', 'Fire,Flying,Ice,Psychic', '044']
['044', 'Octoplat', 'Grass,Poison', 'Fire,Flying,Ice,Psychic', '045,182']
['045', 'Octonyte', 'Grass,Poison', 'Fire,Flying,Ice,Psychic', '']
['182', 'Bibyss', 'Grass', 'Bug,Fire,Flying,Ice,Poison', '']
```

The best solution for csv file operation!!!
1. It automatically append the missing fields with `''`.
2. It is lazy, like a generator (may be a generator). Kind of like a wrapper around file object but with additional functions.
3. It automatically take care of `\n` for each line.
4. You can convert it into a list by `list(reader)`
5. You can use `quotechar` parameter to change the demiliter. The default is `"`.
   ```python
    reader = csv.reader(f, delimiter=',', quotechar='|')
   ```
## Module Contents

The csv module defines the following functions:

csv.reader(csvfile, dialect='excel', **fmtparams)
- Return a reader object which will iterate over lines in the given csvfile. csvfile can be any object which supports the iterator protocol and returns a string each time its `__next__()` method is called — file objects and list objects are both suitable. 
  - If csvfile is a file object, it should be opened with `newline=''`. 
  - An optional dialect parameter can be given which is used to define a set of parameters specific to a particular CSV dialect. It may be an instance of a subclass of the Dialect class or one of the strings returned by the `list_dialects()` function. 
  - The other optional `fmtparams` keyword arguments can be given to override individual formatting parameters in the current dialect. 

- Each row read from the csv file is returned as a list of strings. No automatic data type conversion is performed unless the `QUOTE_NONNUMERIC` format option is specified (in which case unquoted fields are transformed into floats).

**Note:** 
If **newline=''** is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use \r\n linendings on write an extra \r will be added. It should always be safe to specify `newline=''`, since the csv module does its own (universal) newline handling.

csv.writer(csvfile, dialect='excel', **fmtparams)
Return a writer object responsible for converting the user’s data into delimited strings on the given file-like object. 
- csvfile can be any object with a `write()` method. If csvfile is a file object, it should be opened with `newline=''`. 
- An optional dialect parameter can be given which is used to define a set of parameters specific to a particular CSV dialect. It may be an instance of a subclass of the Dialect class or one of the strings returned by the list_dialects() function. 
- The other optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect. For full details about the dialect and formatting parameters, see section Dialects and Formatting Parameters. To make it as easy as possible to interface with modules which implement the DB API, the value None is written as the empty string. While this isn’t a reversible transformation, it makes it easier to dump SQL NULL data values to CSV files without preprocessing the data returned from a cursor.fetch* call. All other non-string data are stringified with str() before being written.

A short usage example:
```python
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
```
```
Spam Spam Spam Spam Spam |Baked Beans|
Spam |Lovely Spam| |Wonderful Spam|
```

# regex

## An example

Same exaple as above, we can use `re` module to implement the same function.

```python

import re
line = '044,Octoplat,"Grass,Poison","Fire,Flying,Ice,Psychic","045,182"'

def line_split(line):
    return re.findall(r'(?:".*?"|[^,])+', line)

print(line_split(line))

```
Result
```
['044', 'Octoplat', '"Grass,Poison"', '"Fire,Flying,Ice,Psychic"', '"045,182"']
```

Explain:

Non-capturing Group `(?:".*?"|[^,])+`
- `+` Quantifier — Matches between one and unlimited times, **as many times as possible**, giving back as needed (greedy)
- 1st Alternative `".*?"`
  - `"` matches the character " literally (case sensitive)
  - `.*?` matches any character (except for line terminators)
  - `*?` Quantifier — Matches between zero and unlimited times, **as few times as possible**, expanding as needed (lazy)
- `"` matches the character " literally (case sensitive)
- 2nd Alternative `[^,]`
  - Match a single character not present in the list below `[^,]`
  - `,` matches the character , literally (case sensitive)
- `(?:)` Non-capturing group

Simplied version by Michael:
```python
lst = re.findall(r'".*?"|[^,]+', line)
```
```
['044', 'Octoplat', '"Grass,Poison"', '"Fire,Flying,Ice,Psychic"', '"045,182"']
```
If I added `?`, like this
```python
lst = re.findall(r'".*?"|[^,]+?', line)
```
```
['0', '4', '4', 'O', 'c', 't', 'o', 'p', 'l', 'a', 't', '"Grass,Poison"', '"Fire,Flying,Ice,Psychic"', '"045,182"']
```

So, we found the BIG difference when using **+** and **?**:
- When use **+**, the token (matching result) will return **as many as possible**, meaning it will try hard to expand its matching token. So it returns '044' instead of '0', '4', '4'. Thus called **greedy**.
- For **?**, the content in the token will be **as few as possible**. That's why it returns '0', '4', '4' instead of '044'. Thus called **lazy**.

Make it simpler: (It does't work sometime.)
```
lst = re.findall(r'".*"|[^,]+', line)
```

Thus, `str.split(',')` equels to `re.find(r'[^,]+', str)`
