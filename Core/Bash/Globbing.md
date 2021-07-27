- [Usage Scenaria](#usage-scenaria)
  - [Case Statement](#case-statement)
  - [Comparison](#comparison)
  - [Parameter Expansion](#parameter-expansion)
- [Wildcard matching](#wildcard-matching)
  - [Character classes](#character-classes)
  - [Ranges](#ranges)
  - [Complementation](#complementation)
- [Pathnames](#pathnames)
- [Empty lists](#empty-lists)
- [Regular expressions](#regular-expressions)
- [Character classes and internationalization](#character-classes-and-internationalization)
- [Compared to regular expressions](#compared-to-regular-expressions)
- [Options which change globbing behavior](#options-which-change-globbing-behavior)
  - [extglob](#extglob)
  - [nullglob](#nullglob)
  - [dotglob](#dotglob)
  - [globstar (since bash 4.0-alpha)](#globstar-since-bash-40-alpha)
  - [failglob](#failglob)
- [GLOBIGNORE](#globignore)
- [nocasematch](#nocasematch)
- [Tips](#tips)
  - [Match all hidden files](#match-all-hidden-files)

"Glob" is the common name for a set of Bash features that match or expand specific types of patterns. Some synonyms for globbing (depending on the context in which it appears) are pattern matching, pattern expansion, filename expansion, and so on.

glob is a shell built-in to expand wildcard patterns.

The rules are as follows (POSIX.2, 3.13).

Unix globbing is handled by the shell per POSIX tradition. Globbing is provided on filenames at the command line and in shell scripts.

# Usage Scenaria

## Case Statement

The POSIX-mandated **case** statement in shells provides pattern-matching using glob patterns.
```bash
   case "$input" in
       [Yy]|'') confirm=1;;
       [Nn]*) confirm=0;;
       *) echo "I don't understand.  Please try again.";;
   esac
```

## Comparison

Bash also allows globs to appear on the **right-hand side** of a comparison inside a `[[` command:
```bash
if [[ $output = *[Ee]rror* ]]; then ...
```

## Parameter Expansion

Finally, globs are used during parameter expansion to indicate patterns which may be stripped out, or replaced, during a substitution. 
```bash
   filename=${path##*/}    # strip leading pattern that matches */ (be greedy)
   dirname=${path%/*}      # strip trailing pattern matching /* (non-greedy)
 
   printf '%s\n' "${arr[@]}"          # dump an array, one element per line
   printf '%s\n' "${arr[@]/error*/}"  # dump array, removing error* if matched
```

The Bash shell also supports the following extensions

- Extended globbing (extglob): allows other pattern matching operators to be used to match multiple occurrences of a pattern enclosed in parentheses, essentially providing the missing kleene star and alternation for describing regular languages. It can be enabled by setting the extglob shell option. This option came from ksh93. The GNU fnmatch and glob has an identical extension.
- globstar: allows ** on its own as a name component to recursively match any number of layers of non-hidden directories. Also supported by the JS libraries and Python's glob.

# Wildcard matching

A string is a wildcard pattern if it contains one of the characters '?', '*', or '['.  

    Tip: If you have a file with wildcard expressions in it then you can use 
    single quotes to stop bash expanding them or use backslashes (escape characters), or both.

**Globbing** is the operation that expands a wildcard pattern into the list of pathnames matching the pattern.  Matching is defined by:

    A '?' (not between brackets) matches any single character.

    A '*' (not between brackets) matches any string, including the
    empty string.

    [ ] (square brackets)
    specifies a range. If you did m[a,o,u]m it can become: mam, mum, mom if you did: 
    m[a-d]m it can become anything that starts and ends with m and has any character a to d inbetween. 
    For example, these would work: mam, mbm, mcm, mdm. 
    This kind of wildcard specifies an “or” relationship (you only need one to match).

    To match a literal -, include it as first or last character.

    { } (curly brackets)
    terms are separated by commas and each term must be the name of something or a wildcard. 
    This wildcard will copy anything that matches either wildcard(s), or exact name(s) (an “or” relationship, one or the other).

    For example, this would be valid:

    cp {*.doc,*.pdf} ~
    This will copy anything ending with .doc or .pdf to the users home directory. 
    Note that spaces are not allowed after the commas (or anywhere else).

    [!]
    This construct is similar to the [ ] construct, except rather than 
    matching any characters inside the brackets, it'll match any character, 
    as long as it is not listed between the [ and ]. 
    This is a logical NOT. For example rm myfile[!9] will remove all 
    myfiles* (ie. myfiles1, myfiles2 etc) but won't remove a file with the 
    number 9 anywhere within it's name.

    In most shell implementations, one may also use ^ as the range negation
    character, e.g. [^[:space:]]. However, POSIX specifies ! for this role, 
    and therefore ! is the standard choice.

    \ (backslash)
    is used as an "escape" character, i.e. to protect a subsequent special 
    character. Thus, "\\” searches for a backslash. Note you may need to use 
    quotation marks and backslash(es).



## Character classes

    An expression "[...]" where the first character after the leading '[' is not an '!' matches a single character, namely any of the characters enclosed by the brackets. 
    
    The string enclosed by the brackets cannot be empty; therefore ']' can be allowed between the brackets, provided that it is the first character.  
    
    (Thus, "[][!]" matches the three characters '[', ']', and '!'.)

## Ranges

    There is one special convention: two characters separated by '-' denote a range.  
    (Thus, "[A-Fa-f0-9]" is equivalent to "[ABCDEFabcdef0123456789]".)  
    One may include '-' in its literal meaning by making it the first or last character between the brackets.  
    (Thus, "[]-]" matches just the two characters ']' and '-', and "[--0]" matches the three characters '-', '.', '0',
    since '/' cannot be matched.)

## Complementation

    An expression "[!...]" matches a single character, namely any
    character that is not matched by the expression obtained by
    removing the first '!' from it.  (Thus, "[!]a-]" matches any
    single character except ']', 'a', and '-'.)

    One can remove the special meaning of '?', '*', and '[' by
    preceding them by a backslash, or, in case this is part of a
    shell command line, enclosing them in quotes.  Between brackets
    these characters stand for themselves.  Thus, "[[?*\]" matches
    the four characters '[', '?', '*', and '\'.

# Pathnames

    Globbing is applied on each of the components of a pathname
    separately.  A '/' in a pathname cannot be matched by a '?' or
    '*' wildcard, or by a range like "[.-0]".  A range containing an
    explicit '/' character is syntactically incorrect.  (POSIX
    requires that syntactically incorrect patterns are left
    unchanged.)

    If a filename starts with a '.', this character must be matched
    explicitly.  (Thus, rm * will not remove .profile, and tar c *
    will not archive all your files; tar c . is better.)

# Empty lists

    The nice and simple rule given above: "expand a wildcard pattern
    into the list of matching pathnames" was the original UNIX
    definition.  It allowed one to have patterns that expand into an
    empty list, as in

        xv -wait 0 *.gif *.jpg

    where perhaps no *.gif files are present (and this is not an error).  
    However, POSIX requires that a wildcard pattern is left
    unchanged when it is syntactically incorrect, or the list of
    matching pathnames is empty.  With bash one can force the
    classical behavior using this command:

        shopt -s nullglob

    (Similar problems occur elsewhere.  For example, where old scripts have

        rm `find . -name "*~"`

    new scripts require

        rm -f nosuchfile `find . -name "*~"`

    to avoid error messages from rm called with an empty argument list.)

# Regular expressions

Note that wildcard patterns are not regular expressions, although they are a bit similar.  

- First of all, they match filenames, rather than text, and 
- Secondly, the conventions are not the same:
    
    for example, in a regular expression '*' means zero or more copies of the preceding thing.

    Now that regular expressions have bracket expressions where the
    negation is indicated by a '^', POSIX has declared the effect of
    a wildcard pattern "[^...]" to be undefined.


Regular expressions are a type of globbing pattern used when working with text. They are used for any form of manipulation of multiple parts of text and by various programming languages that work with text. 

man 7 regex
Regular expressions can be used by: Regular Expressions are used by **grep** (and can be used) by **find** and many other programs.

**Tip**: If your regular expressions don't seem to be working then you probably need to use single quotation marks over the sentence and then use backslashes on every single special character.

    . (dot)
    will match any single character, equivalent to ? (question mark) in standard wildcard expressions. 
    Thus, "m.a" matches "mpa" and "mea" but not "ma" or "mppa".

    \ (backslash)
    is used as an "escape" character, i.e. to protect a subsequent special character. 
    Thus, "\\" searches for a backslash. Note you may need to use quotation marks and backslash(es).

    .* (dot and asterisk)
    is used to match any string, equivalent to * in standard wildcards.

    * (asterisk)
    the proceeding item is to be matched zero or more times. ie. n* will match n, nn, nnnn, nnnnnnn but not na or any other character.

    ^ (caret)
    means "the beginning of the line". So "^a" means find a line starting with an "a".

    $ (dollar sign)
    means "the end of the line". So "a$" means find a line ending with an "a".

    For example, this command searches the file myfile for lines starting with an "s" and ending with an "n", and prints them to the standard output (screen):
    
    cat myfile | grep '^s.*n$'
    
    [ ] (square brackets)
    specifies a range. If you did m[a,o,u]m it can become: mam, mum, mom 
    if you did: m[a-d]m it can become anything that starts and ends with m and has any character a to d inbetween. 
    For example, these would work: mam, mbm, mcm, mdm. 
    This kind of wildcard specifies an “or” relationship (you only need one to match).

    |
    This wildcard makes a logical OR relationship between wildcards. 
    This way you can search for something or something else (possibly using two different regular expressions). 
    You may need to add a '\' (backslash) before this command to work, because the shell may attempt to interpret this as a pipe.

    [^]
    This is the equivalent of [!] in standard wildcards. 
    This performs a logical “not”. 
    This will match anything that is not listed within those square brackets. 
    For example, rm myfile[^9] will remove all myfiles* (ie. myfiles1, myfiles2 etc) but won't remove a file with the number 9 anywhere within it's name.


# Character classes and internationalization

    Of course ranges were originally meant to be ASCII ranges, so
    that "[ -%]" stands for "[ !"#$%]" and "[a-z]" stands for "any
    lowercase letter".  Some UNIX implementations generalized this so
    that a range X-Y stands for the set of characters with code
    between the codes for X and for Y.  
    
    However, this requires the user to know the character coding in 
    use on the local system, and
    moreover, is not convenient if the collating sequence for the
    local alphabet differs from the ordering of the character codes.
    
    Therefore, POSIX extended the bracket notation greatly, both for
    wildcard patterns and for regular expressions.  In the above we
    saw three types of items that can occur in a bracket expression:
    namely 
    (i) the negation, 
    
    (ii) explicit single characters, and

    (iii) ranges.  POSIX specifies ranges in an internationally more
    useful way and adds three more types:

    (iii) Ranges X-Y comprise all characters that fall between X and
    Y (inclusive) in the current collating sequence as defined by the
    LC_COLLATE category in the current locale.

    (iv) Named character classes, like

    [:alnum:]  [:alpha:]  [:blank:]  [:cntrl:]
    [:digit:]  [:graph:]  [:lower:]  [:print:]
    [:punct:]  [:space:]  [:upper:]  [:xdigit:]

    so that one can say "[[:lower:]]" instead of "[a-z]", and have
    things work in Denmark, too, where there are three letters past
    'z' in the alphabet.  These character classes are defined by the
    LC_CTYPE category in the current locale.

    (v) Collating symbols, like "[.ch.]" or "[.a-acute.]", where the
    string between "[." and ".]" is a collating element defined for
    the current locale.  Note that this may be a multicharacter
    element.

    (vi) Equivalence class expressions, like "[=a=]", where the
    string between "[=" and "=]" is any collating element from its
    equivalence class, as defined for the current locale.  For
    example, "[[=a=]]" might be equivalent to "[aáaäâ]", that is, to
    "[a[.a-acute.][.a-grave.][.a-umlaut.][.a-circumflex.]]".

# Compared to regular expressions

Globs do not include syntax for the Kleene star which allows multiple repetitions of the preceding part of the expression; thus they are not considered regular expressions, which can describe the full set of regular languages over any given finite alphabet.

    Common wildcard	Equivalent  regular expression
    ?	                        .
    *	                        .*

Globs attempt to match the entire string (for example, S*.DOC matches S.DOC and SA.DOC, but not POST.DOC or SURREY.DOCKS), whereas, depending on implementation details, regular expressions may match a substring.

# Options which change globbing behavior

## extglob

In addition to the traditional globs (supported by all Bourne-family shells) that we've seen so far, Bash (and Korn Shell) offers extended globs, which have the expressive power of regular expressions. Korn shell enables these by default; in Bash, you must run the command
```bash
   shopt -s extglob
```

in your shell (or at the start of your script -- see note on parsing below) to use them.

```
?(pattern-list)
    Matches zero or one occurrence of the given patterns.
*(pattern-list)
    Matches zero or more occurrences of the given patterns.
+(pattern-list)
    Matches one or more occurrences of the given patterns.
@(pattern-list)
    Matches one of the given patterns.
!(pattern-list)
    Matches anything except one of the given patterns.
```
Patterns in a list are separated by | characters.

```bash
# To remove all the files except ones matching *.jpg:
rm !(*.jpg)
# All except *.jpg and *.gif and *.png:
rm !(*.jpg|*.gif|*.png)

# To copy all the MP3 songs except one to your device
cp !(04*).mp3 /mnt
```

To use an extglob in a parameter expansion (this can also be done in one BASH statement with read):
```bash
# To trim leading and trailing whitespace from a variable
x=${x##+([[:space:]])}; x=${x%%+([[:space:]])}
```

Extended glob patterns can be nested, too.
```bash
[[ $fruit = @(ba*(na)|a+(p)le) ]] && echo "Nice fruit"
```

extglob changes the way certain characters are parsed. It is necessary to have a newline (not just a semicolon) between `shopt -s extglob` and any subsequent commands to use it. You cannot enable extended globs inside a **group command** that uses them, because the entire block is parsed before the shopt is evaluated. Note that the typical **function** body is a group command. An unpleasant workaround could be to use a **subshell** command list as the function body.

Therefore, if you use this option in a script, it is best put right under the shebang line.
```bash
#!/usr/bin/env bash
shopt -s extglob   # and others, such as nullglob dotglob
```

If your code must be sourced and needs extglob, ensure it preserves the original setting from your shell:
```bash
# remember whether extglob was originally set, so we know whether to unset it
shopt -q extglob; extglob_set=$?
# set extglob if it wasn't originally set.
((extglob_set)) && shopt -s extglob
# Note, 0 (true) from shopt -q is "false" in a math context.

# The basic concept behind the following is to delay parsing of the globs until evaluation.
# This matters at group commands, such as functions in { } blocks

declare -a s='( !(x) )'
echo "${s[@]}"

echo "${InvalidVar:-!(x)}"

eval 'echo !(x)'  # using eval if no other option.

# unset extglob if it wasn't originally set
((extglob_set)) && shopt -u extglob
```

**This should also apply for other shell options.**

## nullglob

nullglob expands non-matching globs to zero arguments, rather than to themselves.
```bash
$ ls *.c
ls: cannot access *.c: No such file or directory

# with nullglob set
shopt -s nullglob
ls *.c
# Runs "ls" with no arguments, and lists EVERYTHING
```

Typically, nullglob is used to count the number of files matching a pattern:
```bash
shopt -s nullglob
files=(*) # Here (*) is an array. You can files=(*.c) to include all files *.c
echo "There are ${#files[@]} files in this directory."
# To list all files in a loop
for f in "${files[@]}"; do cmd "$f"; done
# Or you use * directly
for f in *.c; do cmd "$f"; done
```
Without nullglob, the glob would expand to a literal * in **an empty directory**, resulting in an erroneous count of 1.

Remember: sh-compliant shells don’t expand globs during **variable assignment**.

## dotglob
By convention, a filename beginning with a dot is "hidden", and not shown by ls. Globbing uses the same convention -- filenames beginning with a dot are not matched by a glob, unless the glob also begins with a dot. Bash has a dotglob option that lets globs match "dot files":
```bash
shopt -s dotglob nullglob
files=(*)
echo "There are ${#files[@]} files here, including dot files and subdirs"
```
    It should be noted that when dotglob is enabled, * will match files like 
    .bashrc but not the . or .. directories. This is orthogonal to the 
    problem of matching "just the dot files" -- a glob of .* will match . 
    and .., typically causing problems.

## globstar (since bash 4.0-alpha)
globstar recursively repeats a pattern containing '**'.

```bash
$ shopt -s globstar
$ files=(**)
# equivalent to: files=(* */* */*/*)
# finds all files recursively

$ files=(**/*.c)
# equivalent to: files=(*.c */*.c */*/*.c)
# finds all *.c files recursively
# corresponds to: find -name "*.c"
# Caveat: **.c will not work, as it expands to *.c/*.c/…

$ files=(**/)
# finds all subdirectories

$ files=(. **/)
# finds all subdirectories, including the current directory
# corresponds to: find -type d
```

## failglob
If a pattern fails to match, bash reports an expansion error. This can be useful at the commandline:
```bash
# Good at the command line!
$ > *.foo # creates file '*.foo' if glob fails to match
$ shopt -s failglob
$ > *.foo # doesn't get executed
-bash: no match: *.foo
```

# GLOBIGNORE
The Bash variable (not shopt) GLOBIGNORE allows you to specify patterns a glob should not match. This lets you work around the infamous "I want to match all of my dot files, but not . or .." problem:

```bash
$ echo .*
. .. .bash_history .bash_logout .bashrc .inputrc .vimrc
$ GLOBIGNORE=.:..
$ echo .*
.bash_history .bash_logout .bashrc .inputrc .vimrc
# Unset GLOBIGNORE
$ GLOBIGNORE=
$ echo .*
. .. .bash_history .bash_logout .bashrc .inputrc .vimrc

```

# nocasematch
Globs inside [[ and case commands are matched case-insensitive:
```bash
foo() {
   local f r=0 nc=0
   shopt -q nocasematch && nc=1 || shopt -s nocasematch
   for f; do
      [[ $f = *.@(txt|jpg) ]] || continue
      cmd -on "$f" || r=1
   done
   ((nc)) || shopt -u nocasematch
   return $r
}
# This is conventionally done this way:
case $f in
    *.[Tt][Xx][Tt]|*.[Jj][Pp][Gg]) : ;;
    *) continue
esac
```




# Tips

## Match all hidden files

    Traditionally, globs do not match hidden files in the form of Unix 
    dotfiles; to match them the pattern must explicitly start with .. For 
    example, * matches all visible files while .* matches all hidden files.




