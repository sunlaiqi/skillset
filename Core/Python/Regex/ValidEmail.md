


# Validate Email Addresses

Problem
You have a form on your website or a dialog box in your application that asks the user for an email address. You want to use a regular expression to validate this email address before trying to send email to it. This reduces the number of emails returned to you as undeliverable.

Solution
Simple
This first solution does a very simple check. It only validates that the string contains an at sign (@) that is preceded and followed by one or more nonwhitespace characters.

`^\S+@\S+$`
Regex options: None
Regex flavors: .NET, Java, JavaScript, PCRE, Perl, Python
\A\S+@\S+\Z
Regex options: None
Regex flavors: .NET, Java, PCRE, Perl, Python, Ruby
Simple, with restrictions on characters
The domain name, the part after the @ sign, is restricted to characters allowed in domain names. Internationalized domain names are not allowed. The local part, the part before the @ sign, is restricted to characters commonly used in email local parts, which is more restrictive than what most email clients and servers will accept:

^[A-Z0-9+_.-]+@[A-Z0-9.-]+$
Regex options: Case insensitive
Regex flavors: .NET, Java, JavaScript, PCRE, Perl, Python
\A[A-Z0-9+_.-]+@[A-Z0-9.-]+\Z
Regex options: Case insensitive
Regex flavors: .NET, Java, PCRE, Perl, Python, Ruby
Simple, with all valid local part characters
This regular expression expands the previous one by allowing a larger set of rarely used characters in the local part. Not all email software can handle all these characters, but we’ve included all the characters permitted by RFC 5322, which governs the email message format. Among the permitted characters are some that present a security risk if passed directly from user input to an SQL statement, such as the single quote (') and the pipe character (|). Be sure to escape sensitive characters when inserting the email address into a string passed to another program, in order to prevent security holes such as SQL injection attacks:

^[A-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Z0-9.-]+$
Regex options: Case insensitive
Regex flavors: .NET, Java, JavaScript, PCRE, Perl, Python
\A[A-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Z0-9.-]+\Z
Regex options: Case insensitive
Regex flavors: .NET, Java, PCRE, Perl, Python, Ruby
No leading, trailing, or consecutive dots
Both the local part and the domain name can contain one or more dots, but no two dots can appear right next to each other. Furthermore, the first and last characters in the local part and in the domain name must not be dots:

^[A-Z0-9_!#$%&'*+/=?`{|}~^-]+(?:\.[A-Z0-9_!#$%&'*+/=?`{|}~^-]+↵
)*@[A-Z0-9-]+(?:\.[A-Z0-9-]+)*$
Regex options: Case insensitive
Regex flavors: .NET, Java, JavaScript, PCRE, Perl, Python
\A[A-Z0-9_!#$%&'*+/=?`{|}~^-]+(?:\.[A-Z0-9_!#$%&'*+/=?`{|}~^-]+↵
)*@[A-Z0-9-]+(?:\.[A-Z0-9-]+)*\Z
Regex options: Case insensitive
Regex flavors: .NET, Java, PCRE, Perl, Python, Ruby
Top-level domain has two to six letters
This regular expression adds to the previous versions by specifying that the domain name must include at least one dot, and that the part of the domain name after the last dot can only consist of letters. That is, the domain must contain at least two levels, such as secondlevel.com or thirdlevel.secondlevel.com. The top-level domain (.com in these examples) must consist of two to six letters. All country-code top-level domains (.us, .uk, etc.) have two letters. The generic top-level domains have between three (.com) and six letters (.museum):

^[\w!#$%&'*+/=?`{|}~^-]+(?:\.[\w!#$%&'*+/=?`{|}~^-]+)*@↵
(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$
Regex options: Case insensitive
Regex flavors: .NET, Java, JavaScript, PCRE, Perl, Python
\A[\w!#$%&'*+/=?`{|}~^-]+(?:\.[\w!#$%&'*+/=?`{|}~^-]+)*@↵
(?:[A-Z0-9-]+\.)+[A-Z]{2,6}\Z
Regex options: Case insensitive
Regex flavors: .NET, Java, PCRE, Perl, Python, Ruby
Discussion
About email addresses
If you thought something as conceptually simple as validating an email address would have a simple one-size-fits-all regex solution, you’re quite wrong. This recipe is a prime example that before you can start writing a regular expression, you have to decide exactly what you want to match. There is no universally agreed-upon rule as to which email addresses are valid and which not. It depends on your definition of valid.

asdf@asdf.asdf is valid according to RFC 5322, which defines the syntax for email addresses. But it is not valid if your definition specifies that a valid email address is one that accepts mail. There is no top-level asdf domain.

The short answer to the validity problem is that you can’t know whether john.doe@somewhere.com is an email address that can actually receive email until you try to send email to it. And even then, you can’t be sure if the lack of response signals that the somewhere.com domain is silently discarding mail sent to nonexistent mailboxes, or if John Doe hit the Delete button on his keyboard, or if his spam filter beat him to it.

Because you ultimately have to check whether the address exists by actually sending email to it, you can decide to use a simpler or more relaxed regular expression. Allowing invalid addresses to slip through may be preferable to annoying people by blocking valid addresses. For this reason, you may want to select the “simple” regular expression. Though it obviously allows many things that aren’t email addresses, such as #$%@.-, the regex is quick and simple, and will never block a valid email address.

If you want to avoid sending too many undeliverable emails, while still not blocking any real email addresses, the regex in Top-level domain has two to six letters is a good choice.

You have to consider how complex you want your regular expression to be. If you’re validating user input, you’ll likely want a more complex regex, because the user could type in anything. But if you’re scanning database files that you know contain only valid email addresses, you can use a very simple regex that merely separates the email addresses from the other data. Even the solution in the earlier subsection may be enough in this case.

Finally, you have to consider how future-proof you want your regular expression to be. In the past, it made sense to restrict the top-level domain to only two-letter combinations for the country codes, and exhaustively list the generic top-level domains—that is, ‹com|net|org|mil|edu›. With new top-level domains being added all the time, such regular expressions now quickly go out of date.

Regular expression syntax
The regular expressions presented in this recipe show all the basic parts of the regular expression syntax in action. If you read up on these parts in Chapter 2, you can already do 90% of the jobs that are best solved with regular expressions.

All the regular expressions, except the “simple” one, require the case-insensitive matching option to be turned on. Otherwise, only uppercase characters will be allowed. Turning on this option allows you to type ‹[A-Z]› instead of ‹[A-Za-z]›, saving a few keystrokes.

‹\S› is a shorthand character class, as Recipe 2.3 explains. ‹\S› matches any character that is not a whitespace character.

‹@› and ‹\.› match a literal @ sign and a dot, respectively. Since the dot is a metacharacter when used outside character classes, it needs to be escaped with a backslash. The @ sign never has a special meaning with any of the regular expression flavors in this book. Recipe 2.1 gives you a list of all the metacharacters that need to be escaped.

‹[A-Z0-9.-]› and the other sequences between square brackets are character classes. This one allows all letters between A and Z, all digits between 0 and 9, as well as a literal dot and hyphen. Though the hyphen normally creates a range in a character class, the hyphen is treated as a literal when it occurs as the first or last character in a character class. Recipe 2.3 tells you all about character classes, including combining them with shorthands, as in ‹[A-Z0-9_!#$%&'*+/=?`{|}~^.-]›. This class matches a word character, as well as any of the 19 listed punctuation characters.

‹+› and ‹*›, when used outside character classes, are quantifiers. The plus sign repeats the preceding regex token one or more times, whereas the asterisk repeats it zero or more times. In these regular expressions, the quantified token is usually a character class, and sometimes a group. Therefore, ‹[A-Z0-9.-]+› matches one or more letters, digits, dots, and/or hyphens.

As an example of the use of a group, ‹(?:[A-Z0-9-]+\.)+› matches one or more letters, digits, and/or hyphens, followed by one literal dot. The plus sign repeats this group one or more times. The group must match at least once, but can match as many times as possible. Recipe 2.12 explains the mechanics of the plus sign and other quantifiers in detail.

‹(?:⋯)› is a noncapturing group. The capturing group ‹(⋯)› does the same thing with a cleaner syntax, so you could replace ‹(?:› with ‹(› in all of the regular expressions we’ve used so far without changing the overall match results. But since we’re not interested in separately capturing parts of the email address, the noncapturing group is somewhat more efficient, although it makes the regular expression somewhat harder to read. Recipe 2.9 tells you all about capturing and noncapturing groups.

In most regex flavors, the anchors ‹^› and ‹$› force the regular expression to find its match at the start and end of the subject text, respectively. Placing the whole regular expression between these characters effectively requires the regular expression to match the entire subject.

This is important when validating user input. You do not want to accept drop database; -- joe@server.com haha! as a valid email address. Without the anchors, all the previous regular expressions will match because they find joe@server.com in the middle of the given text. See Recipe 2.5 for details about anchors. That recipe also explains why the “^ and $ match at line breaks” matching option must be off for these regular expressions.

In Ruby, the caret and dollar always match at line breaks. The regular expressions using the caret and dollar work correctly in Ruby, but only if the string you’re trying to validate contains no line breaks. If the string may contain line breaks, all the regexes using ‹^› and ‹$› will match the email address in drop database; -- LFjoe@server.comLF haha!, where LF represents a line break.

To avoid this, use the anchors ‹\A› and ‹\Z› instead. These match at the start and end of the string only, regardless of any options, in all flavors discussed in this book, except JavaScript. JavaScript does not support ‹\A› and ‹\Z› at all. Recipe 2.5 explains these anchors.

CAUTION
The issue with ‹^› and ‹$› versus ‹\A› and ‹\Z› applies to all regular expressions that validate input. There are a lot of these in this book. Although we will offer the occasional reminder, we will not constantly repeat this advice or show separate solutions for JavaScript and Ruby for each and every recipe. In many cases, we’ll show only one solution using the caret and dollar, and list Ruby as a compatible flavor. If you’re using Ruby, remember to use ‹\A› and ‹\Z› if you want to avoid matching one line in a multiline string.

Building a regex step-by-step
This recipe illustrates how you can build a regular expression step-by-step. This technique is particularly handy with an interactive regular expression tester, such as RegexBuddy.

First, load a bunch of valid and invalid sample data into the tool. In this case, that would be a list of valid email addresses and a list of invalid email addresses.

Then, write a simple regular expression that matches all the valid email addresses. Ignore the invalid addresses for now. ‹^\S+@\S+$› already defines the basic structure of an email address: a local part, an at sign, and a domain name.

With the basic structure of your text pattern defined, you can refine each part until your regular expression no longer matches any of the invalid data. If your regular expression only has to work with previously existing data, that can be a quick job. If your regex has to work with any user input, editing the regular expression until it is restrictive enough will be a much harder job than just getting it to match the valid data.

Variations
If you want to search for email addresses in larger bodies of text instead of checking whether the input as a whole is an email address, you cannot use the anchors ‹^› and ‹$›. Merely removing the anchors from the regular expression is not the right solution. If you do that with the final regex, which restricts the top-level domain to letters, it will match john@doe.com in john@doe.com77, for example. Instead of anchoring the regex match to the start and end of the subject, you have to specify that the start of the local part and the top-level domain cannot be part of longer words.

This is easily done with a pair of word boundaries. Replace both ‹^› and ‹$› with ‹\b›. For instance, ‹^[A-Z0-9+_.-]+@[A-Z0-9.-]+$› becomes ‹\b[A-Z0-9+_.-]+@[A-Z0-9.-]+\b›.

