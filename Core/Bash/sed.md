- [GNU sed](#gnu-sed)
  - [Command](#command)
  - [Address ranges](#address-ranges)
    - [Addresses with lines](#addresses-with-lines)
    - [Addresses with regular expressions](#addresses-with-regular-expressions)
  - [Regular expression refresher](#regular-expression-refresher)
  - [More on addresses](#more-on-addresses)
  - [Substitution!](#substitution)
  - [Regexp snafus](#regexp-snafus)
  - [More character matching](#more-character-matching)
  - [Advanced substitution stuff](#advanced-substitution-stuff)
    - [& insert the entire matched regex](#-insert-the-entire-matched-regex)
    - [Those wonderful backslashed parentheses](#those-wonderful-backslashed-parentheses)
  - [Mixing things up](#mixing-things-up)
  - [Multiple commands for one address](#multiple-commands-for-one-address)
  - [Append, insert, and change line](#append-insert-and-change-line)
- [Muscular sed](#muscular-sed)
  - [Text translation](#text-translation)
  - [Reversing lines](#reversing-lines)
    - [Reversal explained](#reversal-explained)
  - [sed QIF magic](#sed-qif-magic)
    - [A tale of two formats](#a-tale-of-two-formats)
    - [Starting the process](#starting-the-process)
    - [Refinement](#refinement)
    - [Finishing touches](#finishing-touches)
- [Don't get confused](#dont-get-confused)


# GNU sed

## Command 

Sed works by performing any number of user-specified editing operations ("commands") on the input data. Sed is line-based, so the commands are performed on each line in order. And, sed writes its results to standard output (stdout); it doesn't modify any input files.

Let's look at some examples. The first several are going to be a bit weird because I'm using them to illustrate how sed works rather than to perform any useful task. However, if you're new to sed, it's very important that you understand them. Here's our first example:
```
user $ sed -e 'd' /etc/services
```

If you type this command, you'll get absolutely no output. Now, what happened? In this example, we called sed with one editing command, `d`. 
1. Sed opened the /etc/services file, 
2. read a line into its pattern buffer, 
3. performed our editing command ("delete line"), and 
4. then printed the pattern buffer (which was empty). 
5. It then repeated these steps for each successive line. 
6. This produced no output, because the `d` command zapped every single line in the pattern buffer!

There are a couple of things to notice in this example. 
- First, /etc/services was not modified at all. 
- The second thing to notice is that sed is line-oriented. 
  - The d command didn't simply tell sed to delete all incoming data in one fell swoop. 
  - Instead, sed read each line of /etc/services one by one into its internal buffer, called the pattern buffer. 
  - Once a line was read into the pattern buffer, it performed the d command and printed the contents of the pattern buffer (nothing in this example). 
  - Later, I'll show you how to use address ranges to control which lines a command is applied to -- but in the absence of addresses, a command is applied to all lines.
- The third thing to notice is the use of **single quotes** to surround the `d` command. 
  - It's a good idea to get into the habit of using single quotes to surround your sed commands, so that shell expansion is disabled.

## Address ranges

### Addresses with lines

Now, let's look at how to specify an address range. In this example, sed will delete lines 1-10 of the output:
```
user $ sed -e '1,10d' /etc/services | more
```
When we separate two addresses by a comma, sed will apply the following command to the range that starts with the first address, and ends with the second address. In this example, the `d` command was applied to lines 1-10, inclusive. All other lines were ignored.

### Addresses with regular expressions

Now, it's time for a more useful example. Let's say you wanted to view the contents of your /etc/services file, but you aren't interested in viewing any of the included comments. As you know, you can place comments in your /etc/services file by starting the line with the '#' character. To avoid comments, we'd like sed to delete lines that start with a '#'. Here's how to do it:
```
user $ sed -e '/^#/d' /etc/services | more
```

To understand the '/^#/d' command, we first need to dissect it. First, let's remove the 'd' -- we're using the same delete line command that we've used previously. The new addition is the '/^#/' part, which is a new kind of regular expression address. Regular expression addresses are always surrounded by slashes. They specify a **pattern**, and the command that immediately follows a regular expression address will only be applied to a line if it happens to match this particular pattern.

So, '/^#/' is a regular expression. But what does it do? Obviously, this would be a good time for a regular expression refresher.

## Regular expression refresher

Here are the special characters that you can use in regular expressions:
```
Character	Description
^	        Matches the beginning of the line
$	        Matches the end of the line
.	        Matches any single character
*	        Will match zero or more occurrences of the previous character
[ ]	        Matches all the characters inside the [ ]
```

Probably the best way to get your feet wet with regular expressions is to see a few examples. All of these examples will be accepted by `sed` as valid addresses to appear on the left side of a command. Here are a few:
```
Regular expression	Description
/./	                Will match any line that contains at least one character
/../	            Will match any line that contains at least two characters
/^#/	            Will match any line that begins with a '#'
/^$/	            Will match all blank lines
/}$/	            Will match any lines that ends with '}' (no spaces)
/} *$/	            Will match any line ending with '}' followed by zero or more spaces         
/[abc]/	            Will match any line that contains a lowercase 'a', 'b', or 'c'
/^[abc]/	        Will match any line that begins with an 'a', 'b', or 'c'
```

user $ sed -n -e '/regexp/p' /path/to/my/test/file | more
Note the new '-n' option, which tells sed to not print the pattern space unless explicitly commanded to do so. You'll also notice that we've replaced the `d` command with the `p` command, which as you might guess, explicitly commands sed to print the pattern space. Voila, now only matches will be printed.

## More on addresses

Up till now, we've taken a look at **line addresses**, **line range addresses**, and **regexp addresses**. But there are even more possibilities. We can specify two **regular expressions separated by a comma**, and s`ed` will match all lines starting from the first line that matches the first regular expression, up to and including the line that matches the second regular expression. For example, the following command will print out a block of text that begins with a line containing "BEGIN", and ending with a line that contains "END":
```
user $ sed -n -e '/BEGIN/,/END/p' /my/test/file | more
```
If "BEGIN" isn't found, no data will be printed. And, if "BEGIN" is found, but no "END" is found on any line below it, all subsequent lines will be printed. This happens because of sed's stream-oriented nature -- it doesn't know whether or not an "END" will appear.

**C source example**

If you want to print out only the main() function in a C source file, you could type:
```
user $ sed -n -e '/main[[:space:]]*(/,/^}/p' sourcefile.c | more
```
The first regular expression will match the string "main" followed by any number of spaces or tabs, followed by an open parenthesis. This should match the start of your average ANSI C main() declaration.

In this particular regular expression, we encounter the '`[[:space:]]`' character class. This is simply a special keyword that tells sed to match either a TAB or a space. If you wanted, instead of typing '`[[:space:]]`', you could have typed '[', then a literal space, then Control-V, then a literal tab and a ']' -- The Control-V tells bash that you want to insert a "real" tab rather than perform command expansion. It's clearer, especially in scripts, to use the '`[[:space:]]`' command class.

 '/^}/' will match a '}' character that appears at the beginning of a new line. If your code is formatted nicely, this will match the closing brace of your main() function. If it's not, it won't -- one of the tricky things about performing pattern matching.

 ## Substitution!

Let's look at one of sed's most useful commands, the substitution command. Using it, we can replace a particular string or matched regular expression with another string. Here's an example of the most basic use of this command:
```
user $ sed -e 's/foo/bar/' myfile.txt
```
The above command will output the contents of myfile.txt to stdout, with the first occurrence of 'foo' (if any) on each line replaced with the string 'bar'. Please note that I said first occurrence on each line, though this is normally not what you want. Normally, when I do a string replacement, I want to perform it globally. That is, I want to replace all occurrences on every line, as follows:
```
user $ sed -e 's/foo/bar/g' myfile.txt
```

The additional 'g' option after the last slash tells sed to perform a global replace.

Here are a few other things you should know about the `s///` substitution command. First, it is a command, and a command only; there are no addresses specified in any of the above examples. This means that the `s///` command can also be used with addresses to control what lines it will be applied to, as follows:
```
$ sed -e '1,10s/enchantment/entrapment/g' myfile2.txt
```

The above example will cause all occurrences of the phrase 'enchantment' to be replaced with the phrase 'entrapment', but only on lines one through ten, inclusive.
```
$ sed -e '/^$/,/^END/s/hills/mountains/g' myfile3.txt
```
This example will swap 'hills' for 'mountains', but only on blocks of text beginning with a blank line, and ending with a line beginning with the three characters 'END', inclusive.

Another nice thing about the `s///` command is that we have a lot of options when it comes to those `/` separators. If we're performing string substitution and the regular expression or replacement string has a lot of slashes in it, we can change the separator by specifying a different character after the 's'. For example, this will replace all occurrences of /usr/local with /usr:
```
user $ sed -e 's:/usr/local:/usr:g' mylist.txt
```

In this example, we're using the colon as a separator. If you ever need to specify the separator character in the regular expression, put a backslash before it.

## Regexp snafus

Up until now, we've only performed simple string substitution. While this is handy, we can also match a regular expression. For example, the following sed command will match a phrase beginning with '<' and ending with '>', and containing any number of characters inbetween. This phrase will be deleted (replaced with an empty string):
```
user $ sed -e 's/<.*>//g' myfile.html
```
This is a good first attempt at a sed script that will remove HTML tags from a file, but it won't work well, due to a regular expression quirk. The reason? When sed tries to match the regular expression on a line, it finds the longest match on the line. This wasn't an issue in my previous sed article, because we were using the `d` and `p` commands, which would delete or print the entire line anyway. But when we use the `s///` command, it definitely makes a big difference, because the entire portion that the regular expression matches will be replaced with the target string, or in this case, deleted. This means that the above example will turn the following line:
```
<b>This</b> is what <b>I</b> meant.
```
Into this:
```
meant.
```
Rather than this, which is what we wanted to do:
```
This is what I meant.
```

Fortunately, there is an easy way to fix this. Instead of typing in a regular expression that says "a '<' character followed by any number of characters, and ending with a '>' character", we just need to type in a regexp that says "a '<' character followed by any number of non-'>' characters, and ending with a '>' character". This will have the effect of matching the shortest possible match, rather than the longest possible one. The new command looks like this:
```
user $ sed -e 's/<[^>]*>//g' myfile.html
```

## More character matching
The '[ ]' regular expression syntax has some more additional options. To specify a range of characters, you can use a '-' as long as it isn't in the first or last position, as follows:

'[a-x]*'
This will match zero or more characters, as long as all of them are 'a','b','c'...'v','w','x'. In addition, the '`[:space:]`' character class is available for matching whitespace. Here's a fairly complete list of available character classes:
```
Character class	Description
[:alnum:]	Alphanumeric [a-z A-Z 0-9]
[:alpha:]	Alphabetic [a-z A-Z]
[:blank:]	Spaces or tabs
[:cntrl:]	Any control characters
[:digit:]	Numeric digits [0-9]
[:graph:]	Any visible characters (no whitespace)
[:lower:]	Lower-case [a-z]
[:print:]	Non-control characters
[:punct:]	Punctuation characters
[:space:]	Whitespace
[:upper:]	Upper-case [A-Z]
[:xdigit:]	hex digits [0-9 a-f A-F]
```
It's advantageous to use character classes whenever possible, because they adapt better to nonEnglish speaking locales (including accented characters when necessary, etc.).

## Advanced substitution stuff

### & insert the entire matched regex

We've looked at how to perform simple and even reasonably complex straight substitutions, but sed can do even more. We can actually refer to either parts of or the entire matched regular expression, and use these parts to construct the replacement string. As an example, let's say you were replying to a message. The following example would prefix each line with the phrase "ralph said: ":
```
user $ sed -e 's/.*/ralph said: &/' origmsg.txt
```
The output will look like this:
```
ralph said: Hiya Jim,
ralph said:
ralph said: I sure like this sed stuff!
ralph said:
```
In this example, we use the '&' character in the replacement string, which tells sed to insert the entire matched regular expression. So, whatever was matched by '.*' (the largest group of zero or more characters on the line, or the entire line) can be inserted anywhere in the replacement string, even multiple times. This is great, but sed is even more powerful.

### Those wonderful backslashed parentheses

Even better than '&', the `s///` command allows us to define **regions** in our regular expression, and we can refer to these specific regions in our replacement string. As an example, let's say we have a file that contains the following text:
```
foo bar oni
eeny meeny miny
larry curly moe
jimmy the weasel
```

Now, let's say we wanted to write a sed script that would replace "eeny meeny miny" with "Victor eeny-meeny Von miny", etc. To do this, first we would write a regular expression that would match the three strings, separated by spaces:
```
'.* .* .*'
```

There. Now, we will define regions by inserting backslashed parentheses around each region of interest:
```
'\(.*\) \(.*\) \(.*\)'
```

This regular expression will work the same as our first one, except that it will define three logical regions that we can refer to in our replacement string. Here's the final script:
```
user $ sed -e 's/\(.*\) \(.*\) \(.*\)/Victor \1-\2 Von \3/' myfile.txt
```
As you can see, we refer to each parentheses-delimited region by typing '\x', where x is the number of the region, starting at one. Output is as follows:
```
Victor foo-bar Von oni
Victor eeny-meeny Von miny
Victor larry-curly Von moe
Victor jimmy-the Von weasel
```
As you become more familiar with sed, you will be able to perform fairly powerful text processing with a minimum of effort. You may want to think about how you'd have approached this problem using your favorite scripting language -- could you have easily fit the solution in one line?

## Mixing things up

As we begin creating more complex sed scripts, we need the ability to enter more than one command. There are several ways to do this. First, we can use semicolons between the commands. For example, this series of commands uses the '=' command, which tells sed to print the line number, as well as the `p` command, which explicitly tells sed to print the line (since we're in '-n' mode):
```
user $ sed -n -e '=;p' myfile.txt
```
Whenever two or more commands are specified, each command is applied (in order) to every line in the file. In the above example, first the '=' command is applied to line 1, and then the `p` command is applied. Then, sed proceeds to line 2, and repeats the process. While the semicolon is handy, there are instances where it won't work. Another alternative is to use two -e options to specify two separate commands:
```
user $ sed -n -e '=' -e 'p' myfile.txt
```

However, when we get to the more complex append and insert commands, even multiple '-e' options won't help us. For complex multiline scripts, the best way is to put your commands in a separate file. Then, reference this script file with the -f options:
```
user $ sed -n -f mycommands.sed myfile.txt
```
This method, although arguably less convenient, will always work.

## Multiple commands for one address
Sometimes, you may want to specify multiple commands that will apply to a single address. This comes in especially handy when you are performing lots of `s///` to transform words or syntax in the source file. To perform multiple commands per address, enter your `sed` commands in a file, and use the '{ }' characters to group commands, as follows:
```
1,20{
        s/[Ll]inux/GNU\/Linux/g
        s/samba/Samba/g
        s/posix/POSIX/g
}
```
The above example will apply three substitution commands to lines 1 through 20, inclusive. You can also use regular expression addresses, or a combination of the two:
```
1,/^END/{
        s/[Ll]inux/GNU\/Linux/g 
        s/samba/Samba/g 
        s/posix/POSIX/g 
       p
}
```
This example will apply all the commands between '{ }' to the lines starting at 1 and up to a line beginning with the letters "END", or the end of file if "END" is not found in the source file.

## Append, insert, and change line

Now that we're writing sed scripts in separate files, we can take advantage of the append, insert, and change line commands. These commands will insert a line after the current line, insert a line before the current line, or replace the current line in the pattern space. They can also be used to insert multiple lines into the output. 

The `insert` line command is used as follows:

```
i\
This line will be inserted before each line
```

If you don't specify an address for this command, it will be applied to each line and produce output that looks like this:
```
This line will be inserted before each line
line 1 here
This line will be inserted before each line
line 2 here
This line will be inserted before each line
line 3 here
This line will be inserted before each line
line 4 here
```

If you'd like to insert multiple lines before the current line, you can add additional lines by appending a backslash to the previous line, like so:
```
i\
insert this line\
and this one\
and this one\
and, uh, this one too.
```
The `append` command works similarly, but will insert a line or lines after the current line in the pattern space. It's used as follows:
```
a\
insert this line after each line.  Thanks! :)
```

On the other hand, the "change line" command will actually replace the current line in the pattern space, and is used as follows:
```
c\
You're history, original line! Muhahaha!
```

Because the append, insert, and change line commands need to be entered on multiple lines, you'll want to type them in to text sed scripts and tell sed to source them by using the '-f' option. Using the other methods to pass commands to sed will result in problems.


https://www.funtoo.org/Sed_by_Example,_Part_3

# Muscular sed

## Text translation

Our first practical script converts UNIX-style text to DOS/Windows format. As you probably know, DOS/Windows-based text files have a CR (carriage return) and LF (line feed) at the end of each line, while UNIX text has only a line feed. There may be times when you need to move some UNIX text to a Windows system, and this script will perform the necessary format conversion for you.
```
user $ sed -e 's/$/\r/' myunix.txt > mydos.txt
```
In this script, the '$' regular expression will match the end of the line, and the '\r' tells sed to insert a carriage return right before it. Insert a carriage return before a line feed, and presto, a CR/LF ends each line. Please note that the '\r' will be replaced with a CR only when using GNU sed 3.02.80 or later. 

The following sed invocation will convert DOS/Windows format text to trusty UNIX format:
```
user $ sed -e 's/.$//' mydos.txt > myunix.txt
```
The way this script works is simple: our substitution regular expression matches the last character on the line, which happens to be a carriage return. We replace it with nothing, causing it to be deleted from the output entirely. 

## Reversing lines

Here's another handy little script. This one will reverse lines in a file, similar to the "tac" command that's included with most Linux distributions. The name "tac" may be a bit misleading, because "tac" doesn't reverse the position of characters on the line (left and right), but rather the position of lines in the file (up and down). Tacing the following file:
```
foo
bar
oni
```
....produces the following output:
```
oni
bar
foo
```
We can do the same thing with the following sed script:
```
user $ sed -e '1!G;h;$!d' forward.txt > backward.txt
```
### Reversal explained

First, this script contains three separate sed commands, separated by semicolons: '1!G', 'h' and '$!d'. Now, it's time to get a good understanding of the addresses used for the first and third commands. If the first command were '1G', the 'G' command would be applied only to the first line. However, there is an additional '!' character -- this '!' character negates the address, meaning that the 'G' command will apply to all but the first line. For the '$!d' command, we have a similar situation. If the command were '$d', it would apply the 'd' command to only the last line in the file (the '$' address is a simple way of specifying the last line). However, with the '!', '$!d' will apply the 'd' command to all but the last line. Now, all we need to to is understand what the commands themselves do.

When we execute our line reversal script on the text file above, the first command that gets executed is 'h'. This command tells sed to copy the contents of the pattern space (the buffer that holds the current line being worked on) to the hold space (a temporary buffer). Then, the 'd' command is executed, which deletes "foo" from the pattern space, so it doesn't get printed after all the commands are executed for this line.

Now, line two. After "bar" is read into the pattern space, the 'G' command is executed, which appends the contents of the hold space ("foo\n") to the pattern space ("bar\n"), resulting in "bar\n\foo\n" in our pattern space. The 'h' command puts this back in the hold space for safekeeping, and 'd' deletes the line from the pattern space so that it isn't printed.

For the last "oni" line, the same steps are repeated, except that the contents of the pattern space aren't deleted (due to the '$!' before the 'd'), and the contents of the pattern space (three lines) are printed to stdout.

Now, it's time to do some powerful data conversion with sed.

## sed QIF magic

For the last few weeks, I've been thinking about purchasing a copy of Quicken to balance my bank accounts. Quicken is a very nice financial program, and would certainly perform the job with flying colors. But, after thinking about it, I decided that I could easily write some software that would balance my checkbook. After all, I reasoned, I'm a software developer!

I developed a nice little checkbook balancing program (using awk) that calculates by balance by parsing a text file containing all my transactions. After a bit of tweaking, I improved it so that I could keep track of different credit and debit categories, just like Quicken can. But, there was one more feature I wanted to add. I recently switched my accounts to a bank that has an online Web account interface. One day, I noticed that my bank's Web site allowed me to to download my account information in Quicken's .QIF format. In very little time, I decided that it would be really neat if I could convert this information into text format.

### A tale of two formats

Before we look at the QIF format, here's what my checkbook.txt format looks like:
```
28 Aug 2000     food    -       -       Y     Supermarket             30.94
25 Aug 2000     watr    -       103     Y     Check 103               52.86
```

In my file, all fields are separated by one or more tabs, with one transaction per line. After the date, the next field lists the type of expense (or "-" if this is an income item). The third field lists the type of income (or "-" if this is an expense item). Then, there's a check number field (again, "-" if empty), a transaction cleared field ("Y" or "N"), a comment and a dollar amount. Now, we're ready to take a look at the QIF format. When I viewed my downloaded QIF file in a text viewer, this is what I saw:
```
!Type:Bank
D08/28/2000
T-8.15
N
PCHECKCARD SUPERMARKET
^
D08/28/2000
T-8.25
N
PCHECKCARD PUNJAB RESTAURANT
^
D08/28/2000
T-17.17
N
PCHECKCARD SUPERMARKET
```
After scanning the file, wasn't very hard to figure out the format -- ignoring the first line, the format is as follows:
```
D<date>
T<transaction amount>
N<check number>
P<description>
^ (this is the field separator)
```

### Starting the process

When you're tackling a significant sed project like this, don't get discouraged -- sed allows you to gradually massage the data into its final form. As you progress, you can continue to refine your sed script until your output appears exactly as intended. You don't need to get it exactly right on the first try.

To start off, I created a file called qiftrans.sed, and started massaging the data:
```
1d
/^^/d
s/[[:cntrl:]]//g
```

The first '1d' command deletes the first line, and the second command removes those pesky '^' characters from the output. The last line removes any control characters that may exist in the file. Since I'm dealing with a foreign file format, I want to eliminate the risk of encountering any control characters along the way. So far, so good. Now, it's time to add some processing punch to this basic script:
```
1d
/^^/d
s/[[:cntrl:]]//g
/^D/ {
  s/^D\(.*\)/\1\tOUTY\tINNY\t/
        s/^01/Jan/
        s/^02/Feb/
        s/^03/Mar/
        s/^04/Apr/
        s/^05/May/
        s/^06/Jun/
        s/^07/Jul/
        s/^08/Aug/
        s/^09/Sep/
        s/^10/Oct/
        s/^11/Nov/
        s/^12/Dec/
        s:^\(.*\)/\(.*\)/\(.*\):\2 \1 \3: 
}
```

First, I add a '/^D/' address so that sed will only begin processing when it encounters the first character of the QIF date field, 'D'. All of the commands in the curly braces will execute in order as soon as sed reads such a line into its pattern space.

The first line in the curly braces will transform a line that looks like:
```
D08/28/2000
```
into one that looks like this:
```
08/28/2000  OUTY  INNY
```
Of course, this format isn't perfect right now, but that's OK. We'll gradually refine the contents of the pattern space as we go. The next 12 lines have the net effect of transforming the date to a three-letter format, with the last line removing the three slashes from the date. We end up with this line:
```
28 Aug 2000  OUTY  INNY
```
The OUTY and INNY fields are serving as placeholders and will get replaced later. I can't specify them just yet, because if the dollar amount is negative, I'll want to set OUTY and INNY to "misc" and "-", but if the dollar amount is positive, I'll want to change them to "-" and "inco" respectively. Since the dollar amount hasn't been read yet, I need to use placeholders for the time being.

### Refinement

Now, it's time for some further refinement:
```
1d 
/^^/d
s/[[:cntrl:]]//g 
/^D/ { 
        s/^D\(.*\)/\1\tOUTY\tINNY\t/ 
        s/^01/Jan/ 
        s/^02/Feb/ 
        s/^03/Mar/ 
        s/^04/Apr/ 
        s/^05/May/ 
        s/^06/Jun/ 
        s/^07/Jul/ 
        s/^08/Aug/ 
        s/^09/Sep/ 
        s/^10/Oct/ 
        s/^11/Nov/ 
        s/^12/Dec/ 
        s:^\(.*\)/\(.*\)/\(.*\):\2 \1 \3: 
        N 
        N 
        N 
        s/\nT\(.*\)\nN\(.*\)\nP\(.*\)/NUM\2NUM\t\tY\t\t\3\tAMT\1AMT/ 
        s/NUMNUM/-/ 
        s/NUM\([0-9]*\)NUM/\1/ 
        s/\([0-9]\),/\1/ 
}
```
The next seven lines are a bit complicated, so we'll cover them in detail. First, we have three 'N' commands in a row. The 'N' command tells sed to read in the next line in the input and append it to our current pattern space. The three 'N' commands cause the next three lines to be appended to our current pattern space buffer, and now our line looks like this:
```
28 Aug 2000  OUTY  INNY  \nT-8.15\nN\nPCHECKCARD SUPERMARKET
```
Sed's pattern space got ugly -- we need to remove the extra newlines and perform some additional formatting. To do this, we'll use the substitution command. The pattern we want to match is:
```
'\nT.*\nN.*\nP.*'
```

This will match a newline, followed by a 'T', followed by zero or more characters, followed by a newline, followed by an 'N', followed by any number of characters and a newline, followed by a 'P', followed by any number of characters. Phew! This regexp will match the entire contents of the three lines we just appended to the pattern space. But we want to reformat this region, not replace it entirely. The dollar amount, check number (if any) and description need to reappear in our replacement string. To do this, we surround those "interesting parts" with backslashed parentheses, so that we can refer to them in our replacement string (using '\1', '\2\, and '\3' to tell sed where to insert them). Here is the final command:
```
s/\nT\(.*\)\nN\(.*\)\nP\(.*\)/NUM\2NUM\t\tY\t\t\3\tAMT\1AMT/
```
This command transforms our line into:
```
28 Aug 2000  OUTY  INNY  NUMNUM    Y     CHECKCARD SUPERMARKET AMT-8.15AMT
```
While this line is getting better, there are a few things that at first glance appear a bit...er...interesting. The first is that silly "NUMNUM" string -- what purpose does that serve? You'll find out as you inspect the next two lines of the sed script, which will replace "NUMNUM" with a "-", while "NUM"<number>"NUM" will be replaced with `<number>`. As you can see, surrounding the check number with a silly tag allows us to conveniently insert a "-" if the field is empty.

### Finishing touches

The last line removes a comma following a number. This converts dollar amounts like "3,231.00" to "3231.00", which is the format I use. Now, it's time to take a look at the final, production script:
```
1d
/^^/d
s/[[:cntrl:]]//g
/^D/ {
  s/^D\(.*\)/\1\tOUTY\tINNY\t/
  s/^01/Jan/
  s/^02/Feb/
  s/^03/Mar/
  s/^04/Apr/
  s/^05/May/
  s/^06/Jun/
  s/^07/Jul/
  s/^08/Aug/
  s/^09/Sep/
  s/^10/Oct/
  s/^11/Nov/
  s/^12/Dec/
  s:^\(.*\)/\(.*\)/\(.*\):\2 \1 \3:
  N
  N
  N
  s/\nT\(.*\)\nN\(.*\)\nP\(.*\)/NUM\2NUM\t\tY\t\t\3\tAMT\1AMT/
  s/NUMNUM/-/
  s/NUM\([0-9]*\)NUM/\1/
  s/\([0-9]\),/\1/
  /AMT-[0-9]*.[0-9]*AMT/b fixnegs
  s/AMT\(.*\)AMT/\1/
  s/OUTY/-/
  s/INNY/inco/
  b done
:fixnegs
  s/AMT-\(.*\)AMT/\1/
  s/OUTY/misc/
  s/INNY/-/
:done
}
```

The additional eleven lines use substitution and some branching functionality to perfect the output. We'll want to take a look at this line first:
```
        /AMT-[0-9]*.[0-9]*AMT/b fixnegs
```
This line contains a branch command, which is of the format "/regexp/b label". If the pattern space matches the regexp, sed will branch to the fixnegs label. You should be able to easily spot this label, which appears as ":fixnegs" in the code. If the regexp doesn't match, processing continues as normal with the next command.

Now that you understand the workings of the command itself, let's take a look at the branches. If you look at the branch regular expression, you'll see that it will match the string 'AMT', followed by a '-', followed by any number of digits, a '.', any number of digits and 'AMT'. As I'm sure you've figured out, this regexp deals specifically with a negative dollar amount. Earlier, we surrounded our dollar amount with 'AMT' strings so we could easily find it later. Because the regexp only matches dollar amounts that begin with a '-', our branch will only happen if we happen to be dealing with a debit. If we are dealing with a debit, OUTY should be set to 'misc', INNY should be set to '-', and the negative sign in front of the debit amount should be removed. If you follow the code, you'll see that this is exactly what happens. If the branch isn't executed, OUTY gets replaced with '-', and INNY gets replaced with 'inco'. We're finished! Our output line is now perfect:
```
28 Aug 2000  misc  -  -       Y     CHECKCARD SUPERMARKET  8.15
```

# Don't get confused

As you can see, converting data using sed isn't all that hard, as long as you approach the problem incrementally. Don't try to do everything with a single sed command, or all at once. Instead, gradually work your way toward the goal, and continue to enhance your sed script until your output looks just the way you want it to. 


































