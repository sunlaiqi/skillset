- [Dart Programming - Overview](#dart-programming---overview)
- [Dart Programming - Environment](#dart-programming---environment)
  - [Executing Script Online with DartPad](#executing-script-online-with-dartpad)
  - [Setting Up the Local Environment](#setting-up-the-local-environment)
  - [The dart2js Tool](#the-dart2js-tool)
- [Dart Programming - Syntax](#dart-programming---syntax)
  - [Execute a Dart Program](#execute-a-dart-program)
  - [Dart Command-Line Options](#dart-command-line-options)
  - [Enabling Checked Mode](#enabling-checked-mode)
  - [Identifiers in Dart](#identifiers-in-dart)
  - [Keywords in Dart](#keywords-in-dart)
  - [Whitespace and Line Breaks](#whitespace-and-line-breaks)
  - [Dart is Case-sensitive](#dart-is-case-sensitive)
  - [Statements end with a Semicolon](#statements-end-with-a-semicolon)
  - [Comments in Dart](#comments-in-dart)
  - [Object-Oriented Programming in Dart](#object-oriented-programming-in-dart)
- [Dart Programming - Data Types](#dart-programming---data-types)
  - [Numbers](#numbers)
  - [Strings](#strings)
  - [Boolean](#boolean)
  - [List and Map](#list-and-map)
  - [The Dynamic Type](#the-dynamic-type)
- [Dart Programming - Variables](#dart-programming---variables)
  - [Type Syntax](#type-syntax)
  - [The dynamic keyword](#the-dynamic-keyword)
  - [Final and Const](#final-and-const)
- [Dart Programming - Operators](#dart-programming---operators)
  - [Equality and Relational Operators](#equality-and-relational-operators)
  - [Bitwise Operators](#bitwise-operators)
  - [Assignment Operators](#assignment-operators)
  - [Logical Operators](#logical-operators)
  - [Conditional Expressions](#conditional-expressions)
- [Dart Programming - Loops](#dart-programming---loops)
  - [Classification Of Loops](#classification-of-loops)
  - [Using Labels to Control the Flow](#using-labels-to-control-the-flow)
- [Dart Programming - Decision Making](#dart-programming---decision-making)
- [Dart Programming - Numbers](#dart-programming---numbers)
  - [Parsing](#parsing)
  - [Number Properties](#number-properties)
  - [Number Methods](#number-methods)
- [Dart Programming - String](#dart-programming---string)
  - [String Interpolation](#string-interpolation)
  - [String Properties](#string-properties)
  - [Methods to Manipulate Strings](#methods-to-manipulate-strings)
- [Dart Programming - Boolean](#dart-programming---boolean)
- [Dart Programming - Lists](#dart-programming---lists)
  - [Fixed Length List](#fixed-length-list)
  - [Growable List](#growable-list)
  - [List Properties](#list-properties)
- [Dart Programming - Map](#dart-programming---map)
  - [Declaring a Map using Map Literals](#declaring-a-map-using-map-literals)
  - [Declaring a Map using a Map Constructor](#declaring-a-map-using-a-map-constructor)
  - [Map – Properties](#map--properties)
  - [Map - Functions](#map---functions)
- [Dart Programming - Symbol](#dart-programming---symbol)
  - [Convert Symbol to String](#convert-symbol-to-string)
- [Dart Programming - Runes](#dart-programming---runes)
  - [String.codeUnitAt() Function](#stringcodeunitat-function)
  - [String.codeUnits Property](#stringcodeunits-property)
  - [String.runes Property](#stringrunes-property)
- [Dart Programming - Enumeration](#dart-programming---enumeration)
- [Dart Programming - Functions](#dart-programming---functions)
  - [Optional Parameters](#optional-parameters)
  - [Recursive Dart Functions](#recursive-dart-functions)
  - [Lambda Functions](#lambda-functions)
- [Dart Programming - Interfaces](#dart-programming---interfaces)
  - [Implementing Multiple Interfaces](#implementing-multiple-interfaces)
- [Dart Programming - Classes](#dart-programming---classes)
  - [Declaring a Class](#declaring-a-class)
  - [Creating Instance of the class](#creating-instance-of-the-class)
  - [Accessing Attributes and Functions](#accessing-attributes-and-functions)
  - [Dart Constructors](#dart-constructors)
  - [Named Constructors](#named-constructors)
  - [The this Keyword](#the-this-keyword)
  - [Dart Class ─ Getters and Setters](#dart-class--getters-and-setters)
  - [Class Inheritance](#class-inheritance)
  - [Types of Inheritance](#types-of-inheritance)
  - [Dart – Class Inheritance and Method Overriding](#dart--class-inheritance-and-method-overriding)
  - [The static Keyword](#the-static-keyword)
  - [The super Keyword](#the-super-keyword)
- [Dart Programming - Object](#dart-programming---object)
  - [The Cascade operator (..)](#the-cascade-operator-)
  - [The toString() method](#the-tostring-method)
- [Dart Programming - Collection](#dart-programming---collection)
  - [Iterating Collections](#iterating-collections)
- [Dart Programming - Generics](#dart-programming---generics)
- [Dart Programming - Packages](#dart-programming---packages)
- [Dart Programming - Exceptions](#dart-programming---exceptions)
  - [The try / on / catch Blocks](#the-try--on--catch-blocks)
  - [Example: Using the ON Block](#example-using-the-on-block)
  - [Example: Using the catch Block](#example-using-the-catch-block)
  - [Example: on…catch](#example-oncatch)
  - [The Finally Block](#the-finally-block)
  - [Throwing an Exception](#throwing-an-exception)
  - [Custom Exceptions](#custom-exceptions)
- [Dart Programming - Typedef](#dart-programming---typedef)
- [Dart Programming - Libraries](#dart-programming---libraries)
  - [Importing a library](#importing-a-library)
  - [Encapsulation in Libraries](#encapsulation-in-libraries)
  - [Creating Custom Libraries](#creating-custom-libraries)
  - [Library Prefix](#library-prefix)
- [Dart Programming - Async](#dart-programming---async)
  - [Dart Future](#dart-future)
- [Dart Programming - Concurrency](#dart-programming---concurrency)
  - [Isolate v/s Future](#isolate-vs-future)
- [Dart Programming - Unit Testing](#dart-programming---unit-testing)
  - [Grouping Test Cases](#grouping-test-cases)
- [Dart Programming - HTML DOM](#dart-programming---html-dom)
  - [Example: Manipulating DOM](#example-manipulating-dom)


# Dart Programming - Overview

Dart is an object-oriented language with **C-style** syntax which can optionally trans compile into **JavaScript**. 
- It supports a varied range of programming aids like interfaces, classes, collections, generics, and optional typing.

- Dart can be extensively used to create single-page applications. 

- Google has released a special build of **Chromium – the Dart VM**. Using **Dartium** means you don’t have to compile your code to JavaScript until you’re ready to test on other browsers.
- You can compile Dart to native code, which makes it fast. 
- It also uses a virtual machine (VM) with a special feature: hot reload.

Excerpt From: By Michael Katz. “Flutter Apprentice.” Apple Books. 

The following table compares the features of Dart and JavaScript.

| Feature	| Dart	 | JavaScript |
|-----------|---------|------------|
Type system	| Optional, dynamic	|Weak, dynamic
Classes	| Yes, single inheritance	| Prototypical
Interfaces	| Yes, multiple interfaces	| No
Concurrency	| Yes, with isolates	| Yes, with HTML5 web workers


# Dart Programming - Environment

## Executing Script Online with DartPad
You may test your scripts online by using the online editor at https://dartpad.dartlang.org/. 
Strong mode helps with −

- Stronger static and dynamic checking
- Idiomatic JavaScript code generation for better interoperability.

## Setting Up the Local Environment



## The dart2js Tool
The dart2js tool compiles Dart code to JavaScript. Compiling Dart code to JS enables running the Dart script on browsers that do not support the Dart VM.

The dart2js tool is shipped as a part of the Dart SDK and can be found in the /dartsdk/bin folder.

To compile Dart to JavaScript, type the following command in the terminal
```
dart2js - - out = <output_file>.js  <dart_script>.dart
```


# Dart Programming - Syntax

```dart
main() { 
   print("Hello World!"); 
}
```

The `main()` function is a predefined method in Dart. This method acts as the entry point to the application. 

## Execute a Dart Program
You can execute a Dart program in two ways −

- Via the terminal
- Via the WebStorm IDE/vscode IDE

Via the Terminal
To execute a Dart program via the terminal −
```
dart file_name.dart
```

## Dart Command-Line Options
1	-c or --c
Enables both assertions and type checks (checked mode).

2	--version
Displays VM version information.

3	`--packages <path>`
Specifies the path to the package resolution configuration file.

4	`-p <path>`
Specifies where to find imported libraries. This option cannot be used with --packages.

5	-h or --help
Displays help.

## Enabling Checked Mode
Dart programs run in two modes namely −

- Checked Mode
- Production Mode (Default)

Consider the following Test.dart script file −
```dart
void main() { 
   int n = "hello"; 
   print(n); 
} 
```
Run the script by entering −
```
dart Test.dart
```

Though there is a type-mismatch the script executes successfully as the checked mode is turned off. The script will result in the following output −
```
hello
```
Now try executing the script with the "- - checked" or the "-c" option −
```
dart -c Test.dart 
```
Or,
```
dart - - checked Test.dart
```
The Dart VM will throw an error stating that there is a type mismatch.
```dart
Unhandled exception: 
type 'String' is not a subtype of type 'int' of 'n' where 
   String is from dart:core 
   int is from dart:core 
#0  main (file:///C:/Users/Administrator/Desktop/test.dart:3:9) 
#1  _startIsolate.<anonymous closure> (dart:isolate-patch/isolate_patch.dart :261) 
#2  _RawReceivePortImpl._handleMessage (dart:isolate-patch/isolate_patch.dart:148)
```
## Identifiers in Dart
Identifiers are names given to elements in a program like variables, functions etc. The rules for identifiers are −

- Identifiers can include both, characters and digits. However, the identifier cannot begin with a digit.

- Identifiers cannot include special symbols except for underscore (_) or a dollar sign ($).

- Identifiers cannot be keywords.

- They must be unique.

- Identifiers are case-sensitive.

- Identifiers cannot contain spaces.

The following tables lists a few examples of valid and invalid identifiers −

|Valid identifiers	| Invalid identifiers|
---------------------|---------------------
firstName	| Var
first_name	| first name
num1	| first-name
$result	| 1number

## Keywords in Dart
Keywords have a special meaning in the context of a language. The following table lists some keywords in Dart.
```dart
abstract 1	continue	false	new	this
as 1	default	final	null	throw
assert	deferred 1	finally	operator 1	true
async 2	do	for	part 1	try
async* 2	dynamic 1	get 1	rethrow	typedef 1
await 2	else	if	return	var
break	enum	implements 1	set 1	void
case	export 1	import 1	static 1	while
catch	external 1	in	super	with
class	extends	is	switch	yield 2
const	factory 1	library 1	sync* 2	yield* 2
```
## Whitespace and Line Breaks

Dart ignores spaces, tabs, and newlines that appear in programs. 
- You can use spaces, tabs, and newlines freely in your program and 
- you are free to format and indent your programs in a neat and consistent way that makes the code easy to read and understand.

## Dart is Case-sensitive
Dart is case-sensitive. This means that Dart differentiates between uppercase and lowercase characters.

## Statements end with a Semicolon

Each line of instruction is called a statement. Each dart statement must end with a semicolon (;). A single line can contain multiple statements. However, these statements must be separated by a semicolon.

## Comments in Dart

Dart supports the following types of comments −
```
Single-line comments ( // ) − Any text between a "//" and the end of a line is treated as a comment

Multi-line comments (/* */) − These comments may span multiple lines.
```

## Object-Oriented Programming in Dart

Dart is an Object-Oriented language. Object Orientation is a software development paradigm that follows real-world modelling. Object Orientation considers a program as a collection of objects that communicate with each other via mechanism called methods.

**Object** − An object is a real-time representation of any entity. As per Grady Brooch, every object must have three features −

- State − described by the attributes of an object.
- Behavior − describes how the object will act.
- Identity − a unique value that distinguishes an object from a set of similar such objects.

**Class** − A class in terms of OOP is a blueprint for creating objects. A class encapsulates data for the object.

**Method** − Methods facilitate communication between objects.

Example: Dart and Object Orientation
```dart
class TestClass {   
   void disp() {     
      print("Hello World"); 
   } 
}  
void main() {   
   TestClass c = new TestClass();   
   c.disp();  
}
```

The above example defines a class `TestClass`. The class has a method `disp()`. The method prints the string “Hello World” on the terminal. The `new` keyword creates an object of the class. The object invokes the method `disp()`.

# Dart Programming - Data Types

The Dart language supports the following types−

Numbers
Strings
Booleans
Lists
Maps

## Numbers

Numbers in Dart are used to represent numeric literals. The Number Dart come in two flavours −

Integer − Integer values represent non-fractional values, i.e., numeric values without a decimal point. For example, the value "10" is an integer. Integer literals are represented using the `int` keyword.

Double − Dart also supports fractional numeric values i.e. values with decimal points. The Double data type in Dart represents a 64-bit (double-precision) floating-point number. For example, the value "10.10". The keyword `double` is used to represent floating point literals.

## Strings

Strings represent a sequence of characters. A Dart string is a sequence of UTF-16 code units. Runes are used to represent a sequence of UTF-32 code units.

The keyword `String` is used to represent string literals. String values are embedded in either single or double quotes.

## Boolean

The Boolean data type represents Boolean values `true` and `false`. Dart uses the `bool` keyword to represent a Boolean value.

## List and Map

The data types list and map are used to represent a collection of objects. 
- A List is an ordered group of objects. The List data type in Dart is synonymous to the concept of an *array* in other programming languages. 
- The Map data type represents a set of values as key-value pairs. The `dart: core` library enables creation and manipulation of these collections through the predefined List and Map classes respectively.

## The Dynamic Type

Dart is an optionally typed language. If the type of a variable is not explicitly specified, the variable’s type is **dynamic**. The `dynamic` keyword can also be used as a type annotation explicitly.

# Dart Programming - Variables

A variable is “a named space in the memory” that stores values. In other words, it acts a container for values in a program. Variable names are called identifiers. 

A variable must be declared before it is used. Dart uses the `var` keyword to achieve the same. The syntax for declaring a variable is as given below −
```dart
var name = 'Smith';
```
All variables in dart store a **reference** to the value rather than containing the value. 

The variable called `name` contains a reference to a String object with a value of “Smith”.

## Type Syntax
Dart supports type-checking by prefixing the variable name with the data type. Type-checking ensures that a variable holds only data specific to a data type. The syntax for the same is given below −
```dart
String name = 'Smith'; 
int num = 10;
```
Consider the following example −
```dart
void main() { 
   String name = 1; 
}
```
The above snippet will result in a warning since the value assigned to the variable doesn’t match the variable’s data type.

All **uninitialized variables** have an initial value of `null`. This is because Dart considers all values as objects. The following example illustrates the same −

```dart
void main() { 
   int num; 
   print(num); 
}
```
Output
```
Null 
```

## The dynamic keyword
Variables declared without a static type are implicitly declared as dynamic. Variables can be also declared using the `dynamic` keyword in place of the var keyword.

The following example illustrates the same.
```dart
void main() { 
   dynamic x = "tom"; 
   print(x);  
}
```
Output
```
tom
```

## Final and Const

The `final` and `const` keyword are used to declare constants. Dart prevents modifying the values of a variable declared using the `final` or `const` keyword. These keywords can be used in conjunction with the variable’s data type or instead of the `var` keyword.

The `const` keyword is used to represent a **compile-time** constant. Variables declared using the `const` keyword are implicitly `final`.

Syntax: final Keyword
```dart
final variable_name
```
OR
```dart
final data_type  variable_name
```

Syntax: const Keyword
```dart
const variable_name
```
OR
```dart
const data_type variable_name
```

Note − Only const variables can be used to compute a **compile time constant**. Compile-time constants are constants whose values will be determined at compile time

# Dart Programming - Operators

- Operands − Represents the data
- Operator − Defines how the operands will be processed to produce a value.

## Equality and Relational Operators
Relational Operators tests or defines the kind of relationship between two entities. Relational operators return a Boolean value i.e. `true/ false`.

## Bitwise Operators

## Assignment Operators
The following table lists the assignment operators available in Dart.

```
1	=(Simple Assignment )

2	??=
Assign the value only if the variable is null

3	+=(Add and Assignment)
It adds the right operand to the left operand and assigns the result to the left operand.

4	─=(Subtract and Assignment)
It subtracts the right operand from the left operand and assigns the result to the left operand.

5	*=(Multiply and Assignment)
It multiplies the right operand with the left operand and assigns the result to the left operand.

6	/=(Divide and Assignment)
It divides the left operand with the right operand and assigns the result to the left operand.

Note − Same logic applies to Bitwise operators, so they will become ≪=, ≫=, ≫=, ≫=, |= and ^=.
```

## Logical Operators
Logical operators are used to combine two or more conditions. Logical operators return a Boolean value. 

## Conditional Expressions
Dart has two operators that let you evaluate expressions that might otherwise require ifelse statements −
```dart
condition ? expr1 : expr2
```

If condition is true, then the expression evaluates expr1 (and returns its value); otherwise, it evaluates and returns the value of expr2.
```dart
expr1 ?? expr2
```
If expr1 is non-null, returns its value; otherwise, evaluates and returns the value of expr2


# Dart Programming - Loops

## Classification Of Loops

1	for loop
The for loop is an implementation of a definite loop. The for loop executes the code block for a specified number of times. It can be used to iterate over a fixed set of values, such as an array

2	for…in Loop
The for...in loop is used to loop through an object's properties.

1	while Loop
The while loop executes the instructions each time the condition specified evaluates to true. In other words, the loop evaluates the condition before the block of code is executed.

2	do…while Loop
The do…while loop is similar to the while loop except that the do...while loop doesn’t evaluate the condition for the first time the loop executes.

1	break Statement
The break statement is used to take the control out of a construct. Using break in a loop causes the program to exit the loop. Following is an example of the break statement.

2	continue Statement
The continue statement skips the subsequent statements in the current iteration and takes the control back to the beginning of the loop.

## Using Labels to Control the Flow
A **label** is simply an identifier followed by a colon (:) that is applied to a statement or a block of code. A label can be used with `break` and `continue` to control the flow more precisely.

Line breaks are not allowed between the ‘continue’ or ‘break’ statement and its label name. Also, there should not be any other statement in between a label name and an associated loop.

Example: Label with Break
```dart
void main() { 
   outerloop: // This is the label name 
   
   for (var i = 0; i < 5; i++) { 
      print("Innerloop: ${i}"); 
      innerloop: 
      
      for (var j = 0; j < 5; j++) { 
         if (j > 3 ) break ; 
         
         // Quit the innermost loop 
         if (i == 2) break innerloop; 
         
         // Do the same thing 
         if (i == 4) break outerloop; 
         
         // Quit the outer loop 
         print("Innerloop: ${j}"); 
      } 
   } 
}
```

Example: Label with continue
```dart
void main() { 
   outerloop: // This is the label name 
   
   for (var i = 0; i < 3; i++) { 
      print("Outerloop:${i}"); 
      
      for (var j = 0; j < 5; j++) { 
         if (j == 3){ 
            continue outerloop; 
         } 
         print("Innerloop:${j}"); 
      } 
   } 
}
```

# Dart Programming - Decision Making

1	if statement
An if statement consists of a Boolean expression followed by one or more statements.

2	If...Else Statement
An if can be followed by an optional else block. The else block will execute if the Boolean expression tested by the if block evaluates to false.

3	else…if Ladder
The else…if ladder is useful to test multiple conditions. Following is the syntax of the same.

4	switch…case Statement
The switch statement evaluates an expression, matches the expression’s value to a case clause and executes the statements associated with that case.

# Dart Programming - Numbers

## Parsing
The `parse()` static function allows parsing a string containing numeric literal into a number. The following illustration demonstrates the same −


## Number Properties
The following table lists the properties supported by Dart numbers.
```
1	hashcode
Returns a hash code for a numerical value.

2	isFinite
True if the number is finite; otherwise, false.

3	isInfinite
True if the number is positive infinity or negative infinity; otherwise, false.

4	isNan
True if the number is the double Not-a-Number value; otherwise, false.

5	isNegative
True if the number is negative; otherwise, false.

6	sign
Returns minus one, zero or plus one depending on the sign and numerical value of the number.

7	isEven
Returns true if the number is an even number.

8	isOdd
Returns true if the number is an odd number.
```

## Number Methods
Given below are a list of commonly used methods supported by numbers −
```
1	abs
Returns the absolute value of the number.

2	ceil
Returns the least integer no smaller than the number.

3	compareTo
Compares this to other number.

4	Floor
Returns the greatest integer not greater than the current number.

5	remainder
Returns the truncated remainder after dividing the two numbers.

6	Round
Returns the integer closest to the current numbers.

7	toDouble
Returns the double equivalent of the number.

8	toInt
Returns the integer equivalent of the number.

9	toString
Returns the string equivalent representation of the number.

10	truncate
Returns an integer after discarding any fractional digits.
```

# Dart Programming - String

Triple quotes are used to represent multi-line strings.

The syntax of representing string values in Dart is as given below −

Strings are immutable. 


## String Interpolation

The process of creating a new string by appending a value to a static string is termed as *concatenation* or interpolation. In other words, it is the process of adding a string to another string.

The operator plus (+) is a commonly used mechanism to concatenate / interpolate strings.

You can use "${}" can be used to interpolate the value of a Dart expression within strings. The following example illustrates the same.
```dart
void main() { 
   int n=1+1; 
   
   String str1 = "The sum of 1 and 1 is ${n}"; 
   print(str1); 
   
   String str2 = "The sum of 2 and 2 is ${2+2}"; 
   print(str2); 
}
```

## String Properties

The properties listed in the following table are all read-only.
```
1	codeUnits
Returns an unmodifiable list of the UTF-16 code units of this string.

2	isEmpty
Returns true if this string is empty.

3	Length
Returns the length of the string including space, tab and newline characters.
```

## Methods to Manipulate Strings
The String class in the `dart: core` library also provides methods to manipulate strings. Some of these methods are given below −
```
1	toLowerCase()
Converts all characters in this string to lower case.

2	toUpperCase()
Converts all characters in this string to upper case.

3	trim()
Returns the string without any leading and trailing whitespace.

4	compareTo()
Compares this object to another.

5	replaceAll()
Replaces all substrings that match the specified pattern with a given value.

6	split()
Splits the string at matches of the specified delimiter and returns a list of substrings.

7	substring()
Returns the substring of this string that extends from startIndex, inclusive, to endIndex, exclusive.

8	toString()
Returns a string representation of this object.

9	codeUnitAt()
Returns the 16-bit UTF-16 code unit at the given index.
```

# Dart Programming - Boolean

Unlike JavaScript, the Boolean data type recognizes only the literal true as true. Any other value is considered as false. Consider the following example −
```dart
var str = 'abc'; 
if(str) { 
   print('String is not empty'); 
} else { 
   print('Empty String'); 
} 
```
The above snippet, if run in JavaScript, will print the message ‘String is not empty’ as the if construct will return true if the string is not empty.

However, in Dart, str is converted to false as str `!= true`. Hence the snippet will print the message ‘Empty String’ (when run in unchecked mode).

The above snippet if run in checked mode will throw an exception. The same is illustrated below −

```dart
void main() { 
   var str = 'abc'; 
   if(str) { 
      print('String is not empty'); 
   } else { 
      print('Empty String'); 
   } 
}
```
It will produce the following output, in Checked Mode −
```dart
Unhandled exception: 
type 'String' is not a subtype of type 'bool' of 'boolean expression' where 
   String is from dart:core 
   bool is from dart:core  
#0 main (file:///D:/Demos/Boolean.dart:5:6) 
#1 _startIsolate.<anonymous closure> (dart:isolate-patch/isolate_patch.dart:261) 
#2 _RawReceivePortImpl._handleMessage (dart:isolate-patch/isolate_patch.dart:148)
```

# Dart Programming - Lists

A List is simply an ordered group of objects. The `dart:core` library provides the List class that enables creation and manipulation of lists.

Lists can be classified as −

- Fixed Length List
- Growable List

## Fixed Length List
A fixed length list’s length cannot change at runtime. The syntax for creating a fixed length list is as given below −

Step 1 − Declaring a list

The syntax for declaring a fixed length list is given below −
```dart
var list_name = new List(initial_size)
```

Step 2 − Initializing a list

The syntax for initializing a list is as given below −
```dart
lst_name[index] = value;
```

## Growable List
A growable list’s length can change at run-time. The syntax for declaring and initializing a growable list is as given below −

Step 1 − Declaring a List
```dart
var list_name = [val1,val2,val3]   
```
--- creates a list containing the specified values  
OR  
```dart
var list_name = new List() 
```
--- creates a list of size zero 

Step 2 − Initializing a List

The index / subscript is used to reference the element that should be populated with a value. The syntax for initializing a list is as given below −
```dart
list_name[index] = value;
```
Example
The following example creates a zero-length list using the empty List() constructor. The add() function in the List class is used to dynamically add elements to the list.

```dart
void main() { 
   var lst = new List(); 
   lst.add(12); 
   lst.add(13); 
   print(lst); 
} 
```

## List Properties
The following table lists some commonly used properties of the List class in the `dart:core` library.
```
1	first
Returns the first element in the list.

2	isEmpty
Returns true if the collection has no elements.

3	isNotEmpty
Returns true if the collection has at least one element.

4	length
Returns the size of the list.

5	last
Returns the last element in the list.

6	reversed
Returns an iterable object containing the lists values in the reverse order.

7	Single
Checks if the list has only one element and returns it.
```

# Dart Programming - Map
The Map object is a simple key/value pair. Keys and values in a map may be of any type. A Map is a dynamic collection. In other words, Maps can grow and shrink at runtime.

Maps can be declared in two ways −

- Using Map Literals
- Using a Map constructor

## Declaring a Map using Map Literals
To declare a map using map literals, you need to enclose the key-value pairs within a pair of curly brackets "{ }".

Here is its syntax −
```dart
var identifier = { key1:value1, key2:value2 [,…..,key_n:value_n] }
```

## Declaring a Map using a Map Constructor
To declare a Map using a Map constructor, we have two steps. First, declare the map and second, initialize the map.

The syntax to declare a map is as follows −
```dart
var identifier = new Map()
```
Now, use the following syntax to initialize the map −
```dart
map_name[key] = value
```

Note − A map value can be any object including NULL.

## Map – Properties
The Map class in the `dart:core` package defines the following properties −

```
1	Keys
Returns an iterable object representing keys

2	Values
Returns an iterable object representing values

3	Length
Returns the size of the Map

4	isEmpty
Returns true if the Map is an empty Map

5	isNotEmpty
Returns true if the Map is an empty Map
```

## Map - Functions
Following are the commonly used functions for manipulating Maps in Dart.

```
1	addAll()
Adds all key-value pairs of other to this map.

2	clear()
Removes all pairs from the map.

3	remove()
Removes key and its associated value, if present, from the map.

4	forEach()
Applies f to each key-value pair of the map.
```

# Dart Programming - Symbol
Symbols in Dart are opaque, dynamic string name used in reflecting out metadata from a library. Simply put, symbols are a way to store the relationship between a human readable string and a string that is optimized to be used by computers.

Reflection is a mechanism to get metadata of a type at runtime like the number of methods in a class, the number of constructors it has or the number of parameters in a function. You can even invoke a method of the type which is loaded at runtime.

In Dart reflection specific classes are available in the `dart:mirrors` package. This library works in both web applications and command line applications.

Syntax
```dart
Symbol obj = new Symbol('name');  
// expects a name of class or function or library to reflect 
```
The name must be a valid public Dart member name, public constructor name, or library name.

Example
Consider the following example. The code declares a class `Foo` in a library `foo_lib`. The class defines the methods m1, m2, and m3.

Foo.dart

```dart
library foo_lib;   
// libarary name can be a symbol   

class Foo {         
   // class name can be a symbol  
   m1() {        
      // method name can be a symbol 
      print("Inside m1"); 
   } 
   m2() { 
      print("Inside m2"); 
   } 
   m3() { 
      print("Inside m3"); 
   } 
}
```
The following code loads `Foo.dart` library and searches for `Foo` class, with help of Symbol type. Since we are reflecting the metadata from the above library the code imports `dart:mirrors` library.

FooSymbol.dart
```dart
import 'dart:core'; 
import 'dart:mirrors'; 
import 'Foo.dart';  

main() { 
   Symbol lib = new Symbol("foo_lib");   
   //library name stored as Symbol 
   
   Symbol clsToSearch = new Symbol("Foo");  
   // class name stored as Symbol  
   
   if(checkIf_classAvailableInlibrary(lib, clsToSearch))  
   // searches Foo class in foo_lib library 
      print("class found.."); 
}  
   
bool checkIf_classAvailableInlibrary(Symbol libraryName, Symbol className) { 
   MirrorSystem mirrorSystem = currentMirrorSystem(); 
   LibraryMirror libMirror = mirrorSystem.findLibrary(libraryName); 
      
   if (libMirror != null) { 
      print("Found Library"); 
      print("checkng...class details.."); 
      print("No of classes found is : ${libMirror.declarations.length}"); 
      libMirror.declarations.forEach((s, d) => print(s));  
         
      if (libMirror.declarations.containsKey(className)) return true; 
      return false; 
   } 
}
```
Note that the line `libMirror.declarations.forEach((s, d) => print(s));` will iterate across every declaration in the library at runtime and prints the declarations as type of Symbol.

This code should produce the following output −
```
Found Library 
checkng...class details.. 
No of classes found is : 1 
Symbol("Foo") // class name displayed as symbol  
class found. 
```

Example: Display the number of instance methods of a class
Let us now consider displaying the number of instance methods in a class. The predefined class `ClassMirror` helps us to achieve the same.
```dart
import 'dart:core'; 
import 'dart:mirrors'; 
import 'Foo.dart';  

main() { 
   Symbol lib = new Symbol("foo_lib"); 
   Symbol clsToSearch = new Symbol("Foo");  
   reflect_InstanceMethods(lib, clsToSearch); 
}  
void reflect_InstanceMethods(Symbol libraryName, Symbol className) { 
   MirrorSystem mirrorSystem = currentMirrorSystem(); 
   LibraryMirror libMirror = mirrorSystem.findLibrary(libraryName); 
   
   if (libMirror != null) { 
      print("Found Library"); 
      print("checkng...class details.."); 
      print("No of classes found is : ${libMirror.declarations.length}"); 
      libMirror.declarations.forEach((s, d) => print(s));  
      
      if (libMirror.declarations.containsKey(className)) print("found class");
      ClassMirror classMirror = libMirror.declarations[className]; 
      
      print("No of instance methods found is ${classMirror.instanceMembers.length}");
      classMirror.instanceMembers.forEach((s, v) => print(s)); 
   } 
}    
```
This code should produce the following output −
```
Found Library 
checkng...class details.. 
No of classes found is : 1 
Symbol("Foo") 
found class 
No of instance methods found is 8 
Symbol("==") 
Symbol("hashCode") 
Symbol("toString") 
Symbol("noSuchMethod") 
Symbol("runtimeType") 
Symbol("m1") 
Symbol("m2") 
Symbol("m3")
```

## Convert Symbol to String
You can convert the name of a type like class or library stored in a symbol back to string using `MirrorSystem` class. The following code shows how you can convert a symbol to a string.

```dart
import 'dart:mirrors'; 
void main(){ 
   Symbol lib = new Symbol("foo_lib"); 
   String name_of_lib = MirrorSystem.getName(lib); 
   
   print(lib); 
   print(name_of_lib); 
}
```
It should produce the following output −
```
Symbol("foo_lib")   

foo_lib     
```

# Dart Programming - Runes
Strings are a sequence of characters. Dart represents strings as a sequence of Unicode UTF-16 code units. Unicode is a format that defines a unique numeric value for each letter, digit, and symbol.

Since a Dart string is a sequence of UTF-16 code units, 32-bit Unicode values within a string are represented using a special syntax. A `rune` is an integer representing a Unicode code point.

The String class in the `dart:core` library provides mechanisms to access runes. String code units / runes can be accessed in three ways −

- Using String.codeUnits property
- Using String.codeUnitAt() function
- Using String.runes property

## String.codeUnitAt() Function
Code units in a string can be accessed through their indexes. Returns the 16-bit UTF-16 code unit at the given index.

Syntax
```dart
String.codeUnitAt(int index);
```
Example
```dart
import 'dart:core'; 
void main(){ 
   f1(); 
} 
f1() { 
   String x = 'Runes'; 
   print(x.codeUnitAt(0)); 
}
```
It will produce the following output −
```
82
```

## String.codeUnits Property
This property returns an unmodifiable list of the UTF-16 code units of the specified string.

Syntax
```dart
String. codeUnits;
```

Example
```dart
import 'dart:core';  
void main(){ 
   f1(); 
}  
f1() { 
   String x = 'Runes'; 
   print(x.codeUnits); 
} 
```
It will produce the following output −
```
[82, 117, 110, 101, 115]
```

## String.runes Property
This property returns an iterable of Unicode code-points of this string.Runes extends iterable.

Syntax
```dart
String.runes
```

Example
```dart
void main(){ 
   "A string".runes.forEach((int rune) { 
      var character=new String.fromCharCode(rune); 
      print(character); 
   });  
} 
```
It will produce the following output −
```
A 
s 
t 
r 
i 
n 
g
```

Unicode code points are usually expressed as `\uXXXX`, where XXXX is a 4-digit hexadecimal value. To specify more or less than 4 hex digits, place the value in curly brackets. One can use the constructor of the Runes class in the `dart:core` library for the same.

Example
```dart
main() { 
   Runes input = new Runes(' \u{1f605} '); 
   print(new String.fromCharCodes(input)); 
}  
```
It will produce the following output −
```
Runes
```

# Dart Programming - Enumeration
An enumeration is used for defining named constant values. An enumerated type is declared using the `enum` keyword.

Syntax
```dart
enum enum_name {  
   enumeration list 
}
```

The `enumeration list` is a comma-separated list of identifiers

Each of the symbols in the enumeration list stands for an integer value, one greater than the symbol that precedes it. By default, the value of the first enumeration symbol is 0.

For example
```dart
enum Status { 
   none, 
   running, 
   stopped, 
   paused 
}

void main() { 
   print(Status.values); 
   Status.values.forEach((v) => print('value: $v, index: ${v.index}'));
   print('running: ${Status.running}, ${Status.running.index}'); 
   print('running index: ${Status.values[1]}'); 
}
```
It will produce the following output −
```
[Status.none, Status.running, Status.stopped, Status.paused] 
value: Status.none, index: 0 
value: Status.running, index: 1 
value: Status.stopped, index: 2 
value: Status.paused, index: 3 
running: Status.running, 1 
running index: Status.running 
```

# Dart Programming - Functions

## Optional Parameters
Optional parameters can be used when arguments need not be compulsorily passed for a function’s execution. A parameter can be marked optional by appending a question mark to its name. The optional parameter should be set as **the last argument** in a function.

We have three types of optional parameters in Dart −

```
1	Optional Positional Parameter
To specify optional positional parameters, use square [] brackets.

2	Optional named parameter
Unlike positional parameters, the parameter's name must be specified while the value is being passed. Curly brace {} can be used to specify optional named parameters.

3	Optional Parameters with Default Values
Function parameters can also be assigned values by default. However, such parameters can also be explicitly passed values.
```

## Recursive Dart Functions
Recursion is a technique for iterating over an operation by having a function call to itself repeatedly until it arrives at a result. Recursion is best applied when you need to call the same function repeatedly with different parameters from within a loop.

## Lambda Functions
Lambda functions are a concise mechanism to represent functions. These functions are also called as Arrow functions.

Syntax
```dart
[return_type]function_name(parameters)=>expression;
```
Example
```dart
void main() { 
   printMsg(); 
   print(test()); 
}  
printMsg()=>
print("hello"); 

int test()=>123;                       
// returning function
```
It should produce the following output −
```
hello 123 
```


# Dart Programming - Interfaces
An interface defines the syntax that any entity must adhere to. Interfaces define a set of methods available on an object. Dart does not have a syntax for declaring interfaces. Class declarations are themselves interfaces in Dart.

Classes should use the `implements` keyword to be able to use an interface. It is mandatory for the implementing class to provide a concrete implementation of all the functions of the implemented interface. In other words, a class must redefine every function in the interface it wishes to implement.

Syntax: Implementing an Interface
```dart
class identifier implements interface_name
```
Example
In the following program, we are declaring a class `Printer`. The `ConsolePrinter` class implements the implicit interface declaration for the `Printer` class. The main function creates an object of the `ConsolePrinter` class using the `new` keyword. This object is used to invoke the function `print_data` defined in the `ConsolePrinter` class.

```dart
void main() { 
   ConsolePrinter cp= new ConsolePrinter(); 
   cp.print_data(); 
}  
class Printer { 
   void print_data() { 
      print("__________Printing Data__________"); 
   } 
}  
class ConsolePrinter implements Printer { 
   void print_data() {  
      print("__________Printing to Console__________"); 
   } 
} 
```
It should produce the following output −
```
__________Printing to Console__________
```

## Implementing Multiple Interfaces
A class can implement multiple interfaces. The interfaces are separated by a comma. The syntax for the same is given below −
```dart
class identifier implements interface-1,interface_2,interface_4…….
```
The following example shows how you can implement multiple interfaces in Dart −

```dart
void main() { 
   Calculator c = new Calculator(); 
   print("The gross total : ${c.ret_tot()}"); 
   print("Discount :${c.ret_dis()}"); 
}  
class Calculate_Total { 
   int ret_tot() {} 
}  
class Calculate_Discount { 
   int ret_dis() {} 
}
class Calculator  implements Calculate_Total,Calculate_Discount { 
   int ret_tot() { 
      return 1000; 
   } 
   int ret_dis() { 
      return 50; 
   } 
}
```
It should produce the following output −
```
The gross total: 1000 
Discount:50 
```

# Dart Programming - Classes

## Declaring a Class

Syntax
```dart
class class_name {  
   <fields> 
   <getters/setters> 
   <constructors> 
   <functions> 
}
```
The `class` keyword is followed by the class name. The rules for identifiers must be considered while naming a class.

A class definition can include the following −
```
Fields − A field is any variable declared in a class. Fields represent data pertaining to objects.

Setters and Getters − Allows the program to initialize and retrieve the values of the fields of a class. A default getter/ setter is associated with every class. However, the default ones can be overridden by explicitly defining a setter/ getter.

Constructors − responsible for allocating memory for the objects of the class.

Functions − Functions represent actions an object can take. They are also at times referred to as methods.
```

These components put together are termed as the data members of the class.


## Creating Instance of the class

Syntax
```dart
var object_name = new class_name([ arguments ])
```

## Accessing Attributes and Functions

```dart
//accessing an attribute 
obj.field_name  

//accessing a function 
obj.function_name()
```

## Dart Constructors
Dart defines a constructor with **the same name** as that of the class. A constructor is a function and hence can be parameterized. However, unlike a function, constructors cannot have a return type. If you don’t declare a constructor, a default no-argument constructor is provided for you.

Syntax
```dart
Class_name(parameter_list) { 
   //constructor body 
}
```

## Named Constructors
Dart provides named constructors to enable a class define multiple constructors. The syntax of named constructors is as given below −

Syntax : Defining the constructor
```dart
Class_name.constructor_name(param_list)
```
Example
The following example shows how you can use named constructors in Dart −

```dart
void main() {           
   Car c1 = new Car.namedConst('E1001');                                       
   Car c2 = new Car(); 
}           
class Car {                   
   Car() {                           
      print("Non-parameterized constructor invoked");
   }                                   
   Car.namedConst(String engine) { 
      print("The engine is : ${engine}");    
   }                               
}
```
It should produce the following output −
```
The engine is : E1001 
Non-parameterized constructor invoked
```

## The this Keyword
The `this` keyword refers to the current instance of the class. Here, the parameter name and the name of the class’s field are the same. Hence to avoid ambiguity, the class’s field is prefixed with the `this` keyword. The following example explains the same −

Example
The following example explains how to use the `this` keyword in Dart −

```dart
void main() { 
   Car c1 = new Car('E1001'); 
}  
class Car { 
   String engine; 
   Car(String engine) { 
      this.engine = engine; 
      print("The engine is : ${engine}"); 
   } 
} 
```
It should produce the following output −
```
The engine is : E1001
```

## Dart Class ─ Getters and Setters

Getters and Setters, also called as accessors and mutators, allow the program to initialize and retrieve the values of class fields respectively. Getters or accessors are defined using the `get` keyword. Setters or mutators are defined using the `set` keyword.

A default getter/setter is associated with every class. However, the default ones can be overridden by explicitly defining a setter/ getter. A getter has no parameters and returns a value, and the setter has one parameter and does not return a value.

Syntax: Defining a getter
```dart
Return_type  get identifier 
{ 
} 
Syntax: Defining a setter
set identifier 
{ 
}
```
Example

The following example shows how you can use getters and setters in a Dart class −

```dart
class Student { 
   String name; 
   int age; 
    
   String get stud_name { 
      return name; 
   } 
    
   void set stud_name(String name) { 
      this.name = name; 
   } 
   
   void set stud_age(int age) { 
      if(age<= 0) { 
        print("Age should be greater than 5"); 
      }  else { 
         this.age = age; 
      } 
   } 
   
   int get stud_age { 
      return age;     
   } 
}  
void main() { 
   Student s1 = new Student(); 
   s1.stud_name = 'MARK'; 
   s1.stud_age = 0; 
   print(s1.stud_name); 
   print(s1.stud_age); 
} 
```
This program code should produce the following output −
```
Age should be greater than 5 
MARK 
Null 
```

## Class Inheritance

A class inherits from another class using the ‘extends’ keyword. Child classes inherit all properties and methods except constructors from the parent class.

Syntax
```dart
class child_class_name extends parent_class_name 
```
Note − Dart doesn’t support multiple inheritance.

## Types of Inheritance
Inheritance can be of the following three types −
```
Single − Every class can at the most extend from one parent class.

Multiple − A class can inherit from multiple classes. Dart doesn’t support multiple inheritance.

Multi-level − A class can inherit from another child class.
```

## Dart – Class Inheritance and Method Overriding
Method Overriding is a mechanism by which the child class redefines a method in its parent class.

The number and type of the function parameters must match while overriding the method. In case of a mismatch in the number of parameters or their data type, the Dart compiler throws an error. The following illustration explains the same −

```dart
import 'dart:io'; 
void main() { 
   Child c = new Child(); 
   c.m1(12); 
} 
class Parent { 
   void m1(int a){ print("value of a ${a}");} 
} 
class Child extends Parent { 
   @override 
   void m1(String b) { 
      print("value of b ${b}");
   } 
}
```
It should produce the following output −
```
value of b 12
```

## The static Keyword

The `static` keyword can be applied to the data members of a class, i.e., fields and methods. A static variable retains its values till the program finishes execution. Static members are referenced by the class name.

Example
```dart
class StaticMem { 
   static int num;  
   static disp() { 
      print("The value of num is ${StaticMem.num}")  ; 
   } 
}  
void main() { 
   StaticMem.num = 12;  
   // initialize the static variable } 
   StaticMem.disp();   
   // invoke the static method 
}
```
It should produce the following output −
```
The value of num is 12
```

## The super Keyword
The `super` keyword is used to refer to the immediate parent of a class. 

Example
```dart
void main() { 
   Child c = new Child(); 
   c.m1(12); 
} 
class Parent { 
   String msg = "message variable from the parent class"; 
   void m1(int a){ print("value of a ${a}");} 
} 
class Child extends Parent { 
   @override 
   void m1(int b) { 
      print("value of b ${b}"); 
      super.m1(13); 
      print("${super.msg}")   ; 
   } 
}
```
It should produce the following output −
```
value of b 12 
value of a 13 
message variable from the parent class
```

# Dart Programming - Object

Object-Oriented Programming defines an object as “any entity that has a defined boundary.” An object has the following −
```
State − Describes the object. The fields of a class represent the object’s state.

Behavior − Describes what an object can do.

Identity − A unique value that distinguishes an object from a set of similar other objects. Two or more objects can share the state and behavior but not the identity.
```

The period operator (.) is used in conjunction with the object to access a class’ data members.

## The Cascade operator (..)

The cascade ( .. ) operator can be used to issue a sequence of calls via an object. The above example can be rewritten in the following manner.

```dart
class Student { 
   void test_method() { 
      print("This is a  test method"); 
   } 
   
   void test_method1() { 
      print("This is a  test method1"); 
   } 
}  
void main() { 
   new Student() 
   ..test_method() 
   ..test_method1(); 
}
```
It should produce the following output −
```
This is a test method 
This is a test method1
```

## The toString() method
This function returns a string representation of an object. 

```dart
void main() { 
   int n = 12; 
   print(n.toString()); 
} 
```
It should produce the following output −
```
12
```

# Dart Programming - Collection


1	List
A List is simply an ordered group of objects. The `dart:core` library provides the `List` class that enables creation and manipulation of lists.

2	Set
Set represents a collection of objects in which each object can occur only once. The `dart:core` library provides the `Set` class to implement the same.

3	Maps
The Map object is a simple key/value pair. Keys and values in a map may be of any type. A Map is a dynamic collection. In other words, Maps can grow and shrink at runtime. The `Map` class in the `dart:core` library provides support for the same.

4	Queue
A Queue is a collection that can be manipulated at both ends. Queues are useful when you want to build a first-in, first-out collection. Simply put, a queue inserts data from one end and deletes from another end. The values are removed / read in the order of their insertion.


## Iterating Collections
The `Iterator` class from the `dart:core` library enables easy collection traversal. Every collection has an iterator property. This property returns an iterator that points to the objects in the collection.

Example
The following example illustrates traversing a collection using an iterator object.

```dart
import 'dart:collection'; 
void main() { 
   Queue numQ = new Queue(); 
   numQ.addAll([100,200,300]);  
   Iterator i= numQ.iterator; 
   
   while(i.moveNext()) { 
      print(i.current); 
   } 
}
```
The `moveNext()` function returns a Boolean value indicating whether there is a subsequent entry. The `current` property of the iterator object returns the value of the object that the iterator currently points to.

This program should produce the following output −
```
100 
200 
300
```

# Dart Programming - Generics

Dart is an optionally typed language. Collections in Dart are **heterogeneous** by default. In other words, a single Dart collection can host values of various types. However, a Dart collection can be made to hold homogenous values. The concept of Generics can be used to achieve the same.

The use of Generics enforces a restriction on the data type of the values that can be contained by the collection. Such collections are termed as **type-safe** collections. Type safety is a programming feature which ensures that a memory block can only contain data of a specific data type.

All Dart collections support type-safety implementation via generics. A pair of angular brackets containing the data type is used to declare a type-safe collection. The syntax for declaring a type-safe collection is as given below.

Syntax

```dart
Collection_name <data_type> identifier= new Collection_name<data_type> 
// Generic List
List <String> logTypes = new List <String>(); 
// Generic Set
Set <int> numberSet = new  Set<int>(); 
// Generic Queue
Queue<int> queue = new Queue<int>(); 
// Generic Map
// Map <Key_type, value_type>
Map <String,String> m = {'name':'Tom','Id':'E1001'}; 
```

# Dart Programming - Packages

Every language has a mechanism for managing external packages like Maven or Gradle for Java, Nuget for .NET, npm for Node.js, etc. The package manager for Dart is `pub`.

Pub helps to install packages in the repository. The repository of packages hosted can be found at https://pub.dartlang.org/.

The package **metadata** is defined in a file, `pubsec.yaml`. 

Every Dart application has a `pubspec.yaml` file which contains the application dependencies to other libraries and metadata of applications like application name, author, version, and description.

The contents of a `pubspec.yaml` file should look something like this −
```yaml
name: 'vector_victor' 
version: 0.0.1 
description: An absolute bare-bones web app. 
... 
dependencies: browser: '>=0.10.0 <0.11.0' 
```

The important pub commands are as follows −

1	‘pub get’

Helps to get all packages your application is depending on.

2	‘pub upgrade’

Upgrades all your dependencies to a newer version.

3	‘pub build’

This is used for building your web application and it will create a build folder , with all related scripts in it.

4	‘pub help’

This will give you help for all different pub commands.


# Dart Programming - Exceptions

Built-in Dart exceptions include −

1	DeferredLoadException
Thrown when a deferred library fails to load.

2	FormatException
Exception thrown when a string or some other data does not have an expected format and cannot be parsed or processed.

3	IntegerDivisionByZeroException
Thrown when a number is divided by zero.

4	IOException
Base class for all Inupt-Output related exceptions.

5	IsolateSpawnException
Thrown when an isolate cannot be created.

6	Timeout
Thrown when a scheduled timeout happens while waiting for an async result.

Every exception in Dart is a subtype of the pre-defined class `Exception`. Exceptions must be handled to prevent the application from terminating abruptly.

## The try / on / catch Blocks

- The try block embeds code that might possibly result in an exception. 
- The on block is used when the exception type needs to be specified. 
- The catch block is used when the handler needs the exception object.

The `try` block must be followed by either exactly one `on` / `catch` block or one `finally` block (or one of both). When an exception occurs in the `try` block, the control is transferred to the `catch`.

The syntax for handling an exception is as given below −
```dart
try { 
   // code that might throw an exception 
}  
on Exception1 { 
   // code for handling exception 
}  
catch Exception2 { 
   // code for handling exception 
} 
```

Following are some points to remember −

- A code snippet can have more than one on / catch blocks to handle multiple exceptions.

The on block and the catch block are mutually inclusive, i.e. a try block can be associated with both- the on block and the catch block.

The following code illustrates exception handling in Dart −

## Example: Using the ON Block

The following program divides two numbers represented by the variables x and y respectively. The code throws an exception since it attempts division by zero. The on block contains the code to handle this exception.

```dart
main() { 
   int x = 12; 
   int y = 0; 
   int res;  
   
   try {
      res = x ~/ y; 
   } 
   on IntegerDivisionByZeroException { 
      print('Cannot divide by zero'); 
   } 
} 
```

It should produce the following output −
```
Cannot divide by zero
```

## Example: Using the catch Block

In the following example, we have used the same code as above. The only difference is that the catch block (instead of the ON block) here contains the code to handle the exception. The parameter of catch contains the exception object thrown at runtime.

```dart
main() { 
   int x = 12; 
   int y = 0; 
   int res;  
   
   try {  
      res = x ~/ y; 
   }  
   catch(e) { 
      print(e); 
   } 
} 
```
It should produce the following output −
```
IntegerDivisionByZeroException
```

## Example: on…catch

The following example shows how to use the on...catch block.

```dart
main() { 
   int x = 12; 
   int y = 0; 
   int res;  
   
   try { 
      res = x ~/ y; 
   }  
   on IntegerDivisionByZeroException catch(e) { 
      print(e); 
   } 
} 
```

It should produce the following output −
```
IntegerDivisionByZeroException
```

## The Finally Block
The finally block includes code that should be executed irrespective of an exception’s occurrence. The optional finally block executes unconditionally after try/on/catch.

The syntax for using the finally block is as follows −
```dart
try { 
   // code that might throw an exception 
}  
on Exception1 { 
   // exception handling code 
}  
catch Exception2 { 
   //  exception handling 
}  
finally { 
   // code that should always execute; irrespective of the exception 
}
```

The following example illustrates the use of finally block.

```dart
main() { 
   int x = 12; 
   int y = 0; 
   int res;  
   
   try { 
      res = x ~/ y; 
   } 
   on IntegerDivisionByZeroException { 
      print('Cannot divide by zero'); 
   } 
   finally { 
      print('Finally block executed'); 
   } 
}
```
It should produce the following output −
```
Cannot divide by zero 
Finally block executed
```

## Throwing an Exception

The `throw` keyword is used to explicitly raise an exception. A raised exception should be handled to prevent the program from exiting abruptly.

The syntax for raising an exception explicitly is −
```dart
throw new Exception_name()
```

Example

The following example shows how to use the throw keyword to throw an exception −

```dart
main() { 
   try { 
      test_age(-2); 
   } 
   catch(e) { 
      print('Age cannot be negative'); 
   } 
}  
void test_age(int age) { 
   if(age<0) { 
      throw new FormatException(); 
   } 
}
```
It should produce the following output −
```
Age cannot be negative
```

## Custom Exceptions
As specified above, every exception type in Dart is a subtype of the built-in class Exception. Dart enables creating custom exceptions by extending the existing ones. The syntax for defining a custom exception is as given below −

Syntax: Defining the Exception
```dart
class Custom_exception_Name implements Exception { 
   // can contain constructors, variables and methods 
} 
```
Custom Exceptions should be raised explicitly and the same should be handled in the code.

Example

The following example shows how to define and handle a custom exception.
```dart
class AmtException implements Exception { 
   String errMsg() => 'Amount should be greater than zero'; 
}  
void main() { 
   try { 
      withdraw_amt(-1); 
   } 
   catch(e) { 
      print(e.errMsg()); 
   }  
   finally { 
      print('Ending requested operation.....'); 
   } 
}  
void withdraw_amt(int amt) { 
   if (amt <= 0) { 
      throw new AmtException(); 
   } 
}  
```

The code should produce the following output −
```
Amount should be greater than zero 
Ending requested operation.... 
```

# Dart Programming - Typedef

A typedef, or a function-type alias, helps to define pointers to executable code within memory. Simply put, a typedef can be used as a pointer that references a function.

Given below are the steps to implement typedefs in a Dart program.

**Step 1: Defining a typedef**

A typedef can be used to specify a function signature that we want specific functions to match. A function signature is defined by a function’s parameters (including their types). The return type is not a part of the function signature. Its syntax is as follows.
```dart
typedef function_name(parameters)
```

**Step 2: Assigning a Function to a typedef Variable**

A variable of typedef can point to any function having the same signature as typedef. You can use the following signature to assign a function to a typedef variable.
```dart
type_def  var_name = function_name
```

**Step 3: Invoking a Function**

The typedef variable can be used to invoke functions. Here is how you can invoke a function −
```dart
var_name(parameters) 
```
Example:

```dart
typedef ManyOperation(int firstNo , int secondNo); 
//function signature  

Add(int firstNo,int second){ 
   print("Add result is ${firstNo+second}"); 
} 
Subtract(int firstNo,int second){ 
   print("Subtract result is ${firstNo-second}"); 
}
Divide(int firstNo,int second){ 
   print("Divide result is ${firstNo/second}"); 
}  
Calculator(int a, int b, ManyOperation oper){ 
   print("Inside calculator"); 
   oper(a,b); 
}  
void main(){ 
   // Declare a variable of the ManyOperations type.
   ManyOperation oper = Add; 
   // can point to any method of same signature 
   oper(10,20); 
   oper = Subtract; 
   oper(30,20); 
   oper = Divide; 
   oper(50,5); 
} 
```

Note − The above code will result in an error if the typedef variable tries to point to a function with a different function signature.

Example

Typedefs can also be passed as a parameter to a function. Consider the following example −

```dart
typedef ManyOperation(int firstNo , int secondNo);   //function signature 
Add(int firstNo,int second){ 
   print("Add result is ${firstNo+second}"); 
}  
Subtract(int firstNo,int second){
   print("Subtract result is ${firstNo-second}"); 
}  
Divide(int firstNo,int second){ 
   print("Divide result is ${firstNo/second}"); 
}  
Calculator(int a,int b ,ManyOperation oper){ 
   print("Inside calculator"); 
   oper(a,b); 
}  
main(){ 
   Calculator(5,5,Add); 
   Calculator(5,5,Subtract); 
   Calculator(5,5,Divide); 
} 
```

# Dart Programming - Libraries

A library in a programming language represents a collection of routines (set of programming instructions). 

## Importing a library
Importing makes the components in a library available to the caller code. The `import` keyword is used to achieve the same. A dart file can have multiple import statements.

Built in Dart library URIs use the `dart: scheme` to refer to a library. Other libraries can use a file system path or the `package: scheme` to specify its URI. Libraries provided by a package manager such as the `pub` tool uses the `package: scheme`.

The syntax for importing a library in Dart is given below −
```dart
import 'URI'
```
Consider the following code snippet −
```dart
import 'dart:io' 
import 'package:lib1/libfile.dart' 
```
If you want to use only part of a library, you can selectively import the library. The syntax for the same is given below −
```dart
import 'package: lib1/lib1.dart' show foo, bar;  
// Import only foo and bar. 

import 'package: mylib/mylib.dart' hide foo;  
// Import all names except foo
```

Some commonly used libraries are given below −

1	dart:io
File, socket, HTTP, and other I/O support for server applications. This library does not work in browser-based applications. This library is imported by default.

2	dart:core
Built-in types, collections, and other core functionality for every Dart program. This library is automatically imported.

3	dart: math
Mathematical constants and functions, plus a random number generator.

4	dart: convert
Encoders and decoders for converting between different data representations, including JSON and UTF-8.

5	dart: typed_data
Lists that efficiently handle fixed sized data (for example, unsigned 8 byte integers).

## Encapsulation in Libraries

Dart scripts can prefix identifiers with an underscore ( _ ) to mark its components private. Simply put, Dart libraries can restrict access to its content by external scripts. This is termed as encapsulation. The syntax for the same is given below −

Syntax
```dart
_identifier
```

Example

At first, define a library with a private function.

```dart
library loggerlib;                            
void _log(msg) {
   print("Log method called in loggerlib msg:$msg");      
} 
```
Next, import the library
```
import 'test.dart' as web; 
void main() { 
   web._log("hello from webloggerlib"); 
} 
```
The above code will result in an error.
```dart
Unhandled exception: 
No top-level method 'web._log' declared.  
NoSuchMethodError: method not found: 'web._log' 
Receiver: top-level 
Arguments: [...] 
#0 NoSuchMethodError._throwNew (dart:core-patch/errors_patch.dart:184) 
#1 main (file:///C:/Users/Administrator/WebstormProjects/untitled/Assertion.dart:6:3) 
#2 _startIsolate.<anonymous closure> (dart:isolate-patch/isolate_patch.dart:261) 
#3 _RawReceivePortImpl._handleMessage (dart:isolate-patch/isolate_patch.dart:148)
```

## Creating Custom Libraries

Dart also allows you to use your own code as a library. Creating a custom library involves the following steps −

Step 1: Declaring a Library

To explicitly declare a library, use the `library` statement. The syntax for declaring a library is as given below −
```dart
library library_name  
// library contents go here 
```
Step 2: Associating a Library

You can associate a library in two ways −

Within the same directory
```dart
import 'library_name'
```
From a different directory
```dart
import 'dir/library_name'
```

Example: Custom Library

First, let us define a custom library, `calculator.dart`.

```dart
library calculator_lib;  
import 'dart:math'; 

//import statement after the libaray statement  
int add(int firstNumber,int secondNumber){ 
   print("inside add method of Calculator Library ") ; 
   return firstNumber+secondNumber; 
}  
int modulus(int firstNumber,int secondNumber){ 
   print("inside modulus method of Calculator Library ") ; 
   return firstNumber%secondNumber; 
}  
int random(int no){ 
   return new Random().nextInt(no); 
}
```

Next, we will import the library −

```dart
import 'calculator.dart';  
void main() {
   var num1 = 10; 
   var num2 = 20; 
   var sum = add(num1,num2); 
   var mod = modulus(num1,num2); 
   var r = random(10);  
   
   print("$num1 + $num2 = $sum"); 
   print("$num1 % $num2= $mod"); 
   print("random no $r"); 
} 
```

## Library Prefix

If you import two libraries with conflicting identifiers, then you can specify a prefix for one or both libraries. Use the 'as' keyword for specifying the prefix. The syntax for the same is given below −

Syntax
```dart
import 'library_uri' as prefix
```
Example

First, let us define a library: `loggerlib.dart`.
```dart
library loggerlib;  
void log(msg){ 
   print("Log method called in loggerlib msg:$msg");
}   
```

Next, we will define another library: `webloggerlib.dart`.
```dart
library webloggerlib; 
void log(msg){ 
   print("Log method called in webloggerlib msg:$msg"); 
} 
```
Finally, we will import the library with a prefix.
```dart
import 'loggerlib.dart'; 
import 'webloggerlib.dart' as web;  

// prefix avoids function name clashes 
void main(){ 
   log("hello from loggerlib"); 
   web.log("hello from webloggerlib"); 
} 
```

# Dart Programming - Async

An asynchronous operation executes in a thread, separate from the main application thread. When an application calls a method to perform an operation asynchronously, the application can continue executing while the asynchronous method performs its task.

In computing, we say something is synchronous when it waits for an event to happen before continuing. 

A synchronous execution model will block every other user’s request till it finishes processing the current request. 

Asynchronous programming basically means no waiting or non-blocking programming model. The `dart:async` package facilitates implementing asynchronous programming blocks in a Dart script.

Example
The following example better illustrates the functioning of an asynchronous block.

Step 1 − Create a contact.txt file as given below and save it in the data folder in the current project.

```
1, Tom 
2, John 
3, Tim 
4, Jane
```

Step 2 − Write a program which will read the file without blocking other parts of the application.

```dart
import "dart:async"; 
import "dart:io";  

void main(){ 
   File file = new File( Directory.current.path+"\\data\\contact.txt"); 
   Future<String> f = file.readAsString();  
  
   // returns a futrue, this is Async method 
   f.then((data)=>print(data));  
   
   // once file is read , call back method is invoked  
   print("End of main");  
   // this get printed first, showing fileReading is non blocking or async 
}
```
The output of this program will be as follows −
```
End of main 
1, Tom 
2, John 
3, Tim 
4, Jan
```

The "end of main" executes first while the script continues reading the file. The `Future` class, part of `dart:async`, is used for getting the result of a computation after an asynchronous task has completed. This Future value is then used to do something after the computation finishes.

Once the read operation is completed, the execution control is transferred within "then()". This is because the reading operation can take more time and so it doesn’t want to block other part of program.

## Dart Future

The Dart community defines a Future as "a means for getting a value sometime in the future." Simply put, Future objects are a mechanism to represent values returned by an expression whose execution will complete at a later point in time. Several of Dart’s built-in classes return a `Future` when an asynchronous method is called.

Dart is a **single-threaded** programming language. If any code blocks the thread of execution (for example, by waiting for a time-consuming operation or blocking on I/O), the program effectively freezes.

Asynchronous operations let your program run without getting blocked. Dart uses Future objects to represent asynchronous operations.

# Dart Programming - Concurrency

Concurrency is the execution of several instruction sequences at the same time. It involves performing more than one task simultaneously.

Dart uses `Isolates` as a tool for doing works in parallel. The `dart:isolate` package is Dart’s solution to taking single-threaded Dart code and allowing the application to make greater use of the hard-ware available.

`Isolates`, as the name suggests, are isolated units of running code. The only way to send data between them is by **passing messages**, like the way you pass messages between the client and the server. An isolate helps the program to take advantage of multicore microprocessors out of the box.

Example
Let’s take an example to understand this concept better.

```dart
import 'dart:isolate';  
void foo(var message){ 
   print('execution from foo ... the message is :${message}'); 
}  
void main(){ 
   Isolate.spawn(foo,'Hello!!'); 
   Isolate.spawn(foo,'Greetings!!'); 
   Isolate.spawn(foo,'Welcome!!'); 
   
   print('execution from main1'); 
   print('execution from main2'); 
   print('execution from main3'); 
}
```

Here, the `spawn` method of the Isolate class facilitates running a function, foo, in parallel with the rest of our code. The spawn function takes two parameters −

- the function to be spawned, and
- an object that will be passed to the spawned function.

In case there is no object to pass to the spawned function, it can be passed a NULL value.

The two functions (foo and main) might not necessarily run in the same order each time. There is no guarantee as to when foo will be executing and when main() will be executing. The output will be different each time you run.
```
Output 1
execution from main1 
execution from main2 
execution from main3 
execution from foo ... the message is :Hello!! 
Output 2
execution from main1 
execution from main2 
execution from main3 
execution from foo ... the message is :Welcome!! 
execution from foo ... the message is :Hello!! 
execution from foo ... the message is :Greetings!! 
```
From the outputs, we can conclude that the Dart code can spawn a new isolate from running code like the way Java or C# code can start a new thread.

Isolates differ from threads in that an isolate has its own memory. There’s no way to share a variable between isolates—the only way to communicate between isolates is via message passing.

Note − The above output will be different for different hardware and operating system configurations.

## Isolate v/s Future

Doing complex computational work asynchronously is important to ensure responsiveness of applications. Dart Future is a mechanism for retrieving the value of an asynchronous task after it has completed, while Dart Isolates are a tool for abstracting parallelism and implementing it on a practical high-level basis.

# Dart Programming - Unit Testing

Unit Testing involves testing every individual unit of an application. It helps the developer to test small functionalities without running the entire complex application.

The Dart external library named "test" provides a standard way of writing and running unit tests.

Dart unit testing involves the following steps −

Step 1: Installing the "test" package

To installing third-party packages in the current project, you will require the `pubspec.yaml` file. To install test packages, first make the following entry in the `pubspec.yaml` file −
```
dependencies: 
test:
```

Packages can be installed from the command line too. Type the following in the terminal −
```
pub get
```

Step 2: Importing the "test" package
```dart
import "package:test/test.dart";
```

Step 3 Writing Tests

Tests are specified using the top-level function `test()`, while test assertions are made using the `expect()` function. For using these methods, they should be installed as a pub dependency.

Syntax
```dart
test("Description of the test ", () {  
   expect(actualValue , matchingValue) 
});
```
The `group()` function can be used to group tests. Each group's description is added to the beginning of its test's descriptions.

Syntax
```dart
group("some_Group_Name", () { 
   test("test_name_1", () { 
      expect(actual, equals(exptected)); 
   });  
   test("test_name_2", () { 
      expect(actual, equals(expected)); 
   }); 
}) 
```

Example 1: A Passing Test

The following example defines a method `Add()`. This method takes two integer values and returns an integer representing the sum. To test this `add()` method −

Step 1 − Import the test package as given below.

Step 2 − Define the test using the test() function. Here, the test() function uses the expect() function to enforce an assertion.
```dart
import 'package:test/test.dart';      
// Import the test package 

int Add(int x,int y)                  
// Function to be tested { 
   return x+y; 
}  
void main() { 
   // Define the test 
   test("test to check add method",(){  
      // Arrange 
      var expected = 30; 
      
      // Act 
      var actual = Add(10,20); 
      
      // Asset 
      expect(actual,expected); 
   }); 
}
```
It should produce the following output −
```
00:00 +0: test to check add method 
00:00 +1: All tests passed! 
```

Example 2: A Failing Test

The `subtract()` method defined below has a logical mistake. The following test verifies the same.
```dart
import 'package:test/test.dart'; 
int Add(int x,int y){ 
   return x+y; 
}
int Sub(int x,int y){ 
   return x-y-1; 
}  
void main(){ 
   test('test to check sub',(){ 
      var expected = 10;   
      // Arrange 
      
      var actual = Sub(30,20);  
      // Act 
      
      expect(actual,expected);  
      // Assert 
   }); 
   test("test to check add method",(){ 
      var expected = 30;   
      // Arrange 
      
      var actual = Add(10,20);  
      // Act 
      
      expect(actual,expected);  
      // Asset 
   }); 
}
```
Output − The test case for the function add() passes but the test for subtract() fails as shown below.
```
00:00 +0: test to check sub 
00:00 +0 -1: test to check sub 
Expected: <10> 
Actual: <9> 
package:test  expect 
bin\Test123.dart 18:5  main.<fn> 
   
00:00 +0 -1: test to check add method 
00:00 +1 -1: Some tests failed.  
Unhandled exception: 
Dummy exception to set exit code. 
#0  _rootHandleUncaughtError.<anonymous closure> (dart:async/zone.dart:938) 
#1  _microtaskLoop (dart:async/schedule_microtask.dart:41)
#2  _startMicrotaskLoop (dart:async/schedule_microtask.dart:50) 
#3  _Timer._runTimers (dart:isolate-patch/timer_impl.dart:394) 
#4  _Timer._handleMessage (dart:isolate-patch/timer_impl.dart:414) 
#5  _RawReceivePortImpl._handleMessage (dart:isolate-patch/isolate_patch.dart:148) 
```

## Grouping Test Cases
You can group the test cases so that it adds more meaning to you test code. If you have many test cases this helps to write much cleaner code.

In the given code, we are writing a test case for the `split()` function and the trim function. Hence, we logically group these test cases and call it String.

Example
```dart
import "package:test/test.dart"; 
void main() { 
   group("String", () { 
      test("test on split() method of string class", () { 
         var string = "foo,bar,baz"; 
         expect(string.split(","), equals(["foo", "bar", "baz"])); 
      }); 
      test("test on trim() method of string class", () { 
         var string = "  foo "; 
         expect(string.trim(), equals("foo")); 
      }); 
   }); 
} 
```
Output − The output will append the group name for each test case as given below −
```
00:00 +0: String test on split() method of string class 
00:00 +1: String test on trim() method of string class 
00:00 +2: All tests passed
```

# Dart Programming - HTML DOM

Every webpage resides inside a browser window which can be considered as an object.

A Document object represents the HTML document that is displayed in that window. The Document object has various properties that refer to other objects which allow access to and modification of document content.

The way a document content is accessed and modified is called the **Document Object Model**, or DOM. The Objects are organized in a hierarchy. This hierarchical structure applies to the organization of objects in a Web document.

**Window** − Top of the hierarchy. It is the outmost element of the object hierarchy.

**Document** − Each HTML document that gets loaded into a window becomes a document object. The document contains the contents of the page.

**Elements** − represent the content on a web page. Examples include the text boxes, page title etc.

**Nodes** − are often elements, but they can also be attributes, text, comments, and other DOM types.

Dart provides the `dart:html` library to manipulate objects and elements in the DOM. 
- Console-based applications cannot use the `dart:html` library. 

To use the HTML library in the web applications, import `dart:html` −
```dart
import 'dart:html';
```

Finding DOM Elements
The `dart:html` library provides the `querySelector` function to search for elements in the DOM.
```dart
Element querySelector(String selectors);
```
The `querySelector()` function returns the **first element** that matches the specified group of selectors. "selectors should be string using CSS selector syntax as given below
```dart
var element1 = document.querySelector('.className'); 
var element2 = document.querySelector('#id'); 
```

## Example: Manipulating DOM


Index.html
```html
<!DOCTYPE html>   
<html> 
   <head>     
      <meta charset = "utf-8">     
      <meta http-equiv = "X-UA-Compatible" content = "IE = edge">     
      <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
      <meta name = "scaffolded-by" content = "https://github.com/google/stagehand">
      <title>DemoWebApp</title>     
      <link rel = "stylesheet" href = "styles.css">     
      <script defer src = "main.dart" type = "application/dart"></script>
      <script defer src = "packages/browser/dart.js"></script> 
   </head>
   
   <body>   
      <h1>
         <div id = "output"></div> 
      </h1>  
   </body> 
</html> 
```

Main.dart

```dart
import 'dart:html';  
void main() {   
   querySelector('#output').text = 'Your Dart web dom app is running!!!.'; 
} 
```

Run the `index.html` file; you will see the following output on your screen.
```
Demo Web App
Event Handling
```

The `dart:html` library provides the `onClick` event for DOM Elements. The syntax shows how an element could handle a stream of click events.
```dart
querySelector('#Id').onClick.listen(eventHanlderFunction); 
```

The `querySelector()` function returns the element from the given DOM and `onClick.listen()` will take an eventHandler method which will be invoked when a click event is raised. The syntax of eventHandler is given below −
```dart
void eventHanlderFunction (MouseEvent event){ } 
```

Let us now take an example to understand the concept of Event Handling in Dart.

TestEvent.html
```html
<!DOCTYPE html> 
<html> 
   <head> 
      <meta charset = "utf-8"> 
      <meta http-equiv = "X-UA-Compatible" content = "IE = edge"> 
      <meta name = "viewport" content = "width = device-width, initial-scale = 1.0"> 
      <meta name = "scaffolded-by" content ="https://github.com/google/stagehand"> 
      <title>DemoWebApp</title> 
      <link rel = "stylesheet" href = "styles.css"> 
      <script defer src = "TestEvent.dart" type="application/dart"></script> 
      <script defer src = "packages/browser/dart.js"></script> 
   </head> 
   
   <body> 
      <div id = "output"></div> 
      <h1> 
         <div> 
            Enter you name : <input type = "text" id = "txtName"> 
            <input type = "button" id = "btnWish" value="Wish"> 
         </div> 
      </h1> 
      <h2 id = "display"></h2> 
   </body>
   
</html>
```

TestEvent.dart

```dart
import 'dart:html'; 
void main() { 
   querySelector('#btnWish').onClick.listen(wishHandler); 
}  
void wishHandler(MouseEvent event){ 
   String name = (querySelector('#txtName')  as InputElement).value; 
   querySelector('#display').text = 'Hello Mr.'+ name; 
}
```
