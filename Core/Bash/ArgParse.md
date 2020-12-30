- [parsing command line arguments in Bash](#parsing-command-line-arguments-in-bash)
  - [The usual way](#the-usual-way)
    - [1 - usage function](#1---usage-function)
    - [2 - Declaring Variables](#2---declaring-variables)
    - [3 - Arguments to Variables](#3---arguments-to-variables)
    - [4 - Verifying required arguments](#4---verifying-required-arguments)
- [getopt(s)](#getopts)
  - [A Better Way](#a-better-way)
- [Example 1](#example-1)

# parsing command line arguments in Bash

## The usual way
So here I am, maintaining the command line arguments, which in turn, will be variables, in four different places. Why four? Here we go!

### 1 - usage function
The usage function should pop up whenever the user attempts to provide wrong or missing arguments
```bash
usage()
{
cat << EOF
usage: bash ./scripts/packndeploy -n service_name
-n    | --service_name      (Required)            Service to deploy
-b    | --branch            (master)              Source branch
-h    | --help                                    Brings up this menu
EOF
}
```
### 2 - Declaring Variables

To get the command line arguments, we need to declare variables that can store them, and also set the default values for these variables/arguments.
```bash
service_name=
branch=master # default value
```
### 3 - Arguments to Variables

Mapping arguments to variables with while case shift is a great trick to fetch variables! 
```bash
while [ "$1" != "" ]; do
    case $1 in
        -n | --service_name )
            shift
            service_name=$1
        ;;
        -b | --branch )
            shift
            branch=$1              
        -h | --help )    usage
            exit
        ;;
        * )              usage
            exit 1
    esac
    shift
done
```
### 4 - Verifying required arguments

After the while loop above ☝️ we need to make sure that the required variables were provided. So here's a quick and dirty way to do it
```bash
if [ -z $service_name ]; then
    echo "Service name is required, provide it with the flag: -n service_name"
    exit
fi
```
NOTE: I'm sure that it's better to write a function that performs some of the tasks above dynamically, but it still means we need to write it or copy-paste it to our Bash script.

# getopt(s)

Goals

The ideal argument parser will recognize both short and long option flags, preserve the order of positional arguments, and allow both options and arguments to be specified in any order relative to each other. In other words both of these commands should result in the same parsed arguments:
```
$ ./foo bar -a baz --long thing
$ ./foo -a baz bar --long thing
```
The most widely recognized tools for parsing arguments in bash are getopt and getopts. Though both tools are similar in name, they’re very different. getopt is a GNU library that parses argument strings and supports both short and long form flags. getopts is a bash builtin that also parses argument strings but only supports short form flags. Typically, if you need to write a simple script that only accepts one or two flag options you can do something like:
```bash
while getopts “:a:bc” opt; do
  case $opt in
    a) AOPT=$OPTARG ;;
  esac
done
```
This works great for simple option parsing, but things start to fall apart if you want to support long options or mixing options and positional arguments together.

## A Better Way

As it turns out, it’s pretty easy to write your own arg parser once you understand the mechanics of the language. Doing so affords you the ability to cast all manner of spells to bend arguments to your will. Here’s a basic example:
```bash
#!/bin/bash
PARAMS=""
while (( "$#" )); do
  case "$1" in
    -a|--my-boolean-flag)
      MY_FLAG=0
      shift
      ;;
    -b|--my-flag-with-argument)
      if [ -n "$2" ] && [ ${2:0:1} != "-" ]; then
        MY_FLAG_ARG=$2
        shift 2
      else
        echo "Error: Argument for $1 is missing" >&2
        exit 1
      fi
      ;;
    -*|--*=) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      exit 1
      ;;
    *) # preserve positional arguments
      PARAMS="$PARAMS $1"
      shift
      ;;
  esac
done
# set positional arguments in their proper place
eval set -- "$PARAMS"
```

There’s a lot going on here so let’s break it down. First we set a variable `PARAMS` to save any positional arguments into for later. Next, we create a while loop that evaluates the length of the arguments array and exits when it reaches zero. Inside of the while loop, pass the first element in the arguments array through a case statement looking for either a custom flag or some default flag patterns. If the statement matches a flag, we do something (like the save the value to a variable) and we use the `shift` statement to pop elements off the front of the arguments array before the next iteration of the loop. If the statement matches a regular argument, we save it into a string to be evaluated later. Finally, after all the arguments have been processed, we set the arguments array to the list of positional arguments we saved using the `set` command.


# Example 1

```python
# arguments.sh

# Default values of arguments
SHOULD_INITIALIZE=0
CACHE_DIRECTORY="/etc/cache"
ROOT_DIRECTORY="/etc/projects"
OTHER_ARGUMENTS=()

# Loop through arguments and process them
for arg in "$@"
do
    case $arg in
        -i|--initialize)
        SHOULD_INITIALIZE=1
        shift # Remove --initialize from processing
        ;;
        -c=*|--cache=*)
        CACHE_DIRECTORY="${arg#*=}"
        shift # Remove --cache= from processing
        ;;
        -r|--root)
        ROOT_DIRECTORY="$2"
        shift # Remove argument name from processing
        shift # Remove argument value from processing
        ;;
        *)
        OTHER_ARGUMENTS+=("$1")
        shift # Remove generic argument from processing
        ;;
    esac
done

echo "# Should initialize: $SHOULD_INITIALIZE"
echo "# Cache directory: $CACHE_DIRECTORY"
echo "# Root directory: $ROOT_DIRECTORY"
echo "# Other arguments: ${OTHER_ARGUMENTS[*]}"
```

Defining default values
```bash
# Default values of arguments
SHOULD_INITIALIZE=0
CACHE_DIRECTORY="/etc/cache"
ROOT_DIRECTORY="/etc/projects"
OTHER_ARGUMENTS=()
```

This is simple enough. If the user doesn't pass in a certain argument, we fill it with some default value we're happy with. Alternatively you can make the strings empty and check if these empty values are still there. In this way you can easily verify that you have all necessary arguments passed in.

Looping through arguments
```bash
for arg in "$@"
do
  .. SNIP ..
done
```
Looping through the arguments is equally simple. You simply loop over the magic $@ variable your shell provides to you. It contains an array of the exact command as it was called, starting after the file name.

So if you call your script using `./arguments.sh -i --cache=/var/cache --root /var/www/html/public my-project`, then the array will look a bit like so
```bash
(
   $0 = ./arguments.sh
   $1 = -i
   $2 = --cache=/var/cache
   $3 = --root
   $4 = /var/www/html/public
   $5 = my-project
)
```
Note that the `$@`variable does not contain the value of `$0`. If you however access `$0` normally, it will return the file name you used to call the script.

For our purposes we loop over each entry in the array and put it in a temporary `$arg` variable. Now we can process the arguments.

Processing all arguments
The arguments will be processed in a switch-case statement. As you may have noticed in the full code sample above, those come with their own delightful idiosyncrasies in syntax. Like a lot of other things in shell scripting, really. A case statement looks like this:
```bash
    case $arg in
        .. SNIP ..
    esac
```
The `$arg` variable in this case is the one we declared in the for-loop above

Now let's look at the various ways to process arguments and how to write switch cases.

**Boolean flags**

Boolean flags are those which may be there or not. A good example might be a --help flag. Parsing those looks like so
```bash
-i|--initialize)
SHOULD_INITIALIZE=1
shift # Remove --initialize from processing
;;
```
Note the two semicolons. Yes, you need those. Both of those.

This case statement checks whether the current value of `$arg` is either `-i` or `--initialize`. In our case this is true and thus we set the `SHOULD_INITIALIZE` variable to 1 to indicate that the flag is present. Afterwards we pop the value `$arg` off of our `$@` array using **shift**. It now looks like the following:
```bash
(
   $0 = ./arguments.sh
   $1 = --cache=/var/cache
   $2 = --root
   $3 = /var/www/html/public
   $4 = my-project
)
```
Note that the value of $0 stayed the same while everything else shifted up by one.

**Equals-separated flags**

Our next case statement parses command-line flag of the form `--arg=value`, which is the traditional style of passing arguments. You can often see this when using Unix tools such as ls `--color=auto`.
```bash
-c=*|--cache=*)
CACHE_DIRECTORY="${arg#*=}"
shift # Remove --cache= from processing
;;
```
This is where you realize that shell scripting has magical features

In this case we check if the current `$arg` matches the either `-c=` or `--cache=` followed by any number of characters. If it does we take that arg variable into our string and remove the parts of it we don't need. The `#*=` part looks super confusing at first. What it does is remove everything character from the beginning of `$arg` until it finds an equals sign.

This means that `--cache=/var/cache` becomes `/var/cache`. 

After this our `$@` array of arguments now looks as follows:
```bash
(
   $0 = ./arguments.sh
   $1 = --root
   $2 = /var/www/html/public
   $3 = my-project
)
```

**Space-separated flags**

Our third case statement handles command-line flags of the form `--arg` value, which is a more modern approach. You can usually see it with command-line tools written with Node.js or Python.
```bash
-r|--root)
ROOT_DIRECTORY="$2"
shift # Remove argument name from processing
shift # Remove argument value from processing
;;
```
At this point these are probably a breeze to go through

Compared to the previous handler, this one is again rather easy to understand. We check whether $arg is equal to `-r` or `root` then we take the value of `$2` into our `ROOT_DIRECTORY` variable and **shift** twice.

Why do we take `$2`? Remember: We have shifted away all previous arguments passed to the script so that now `$1` is equal to the value of `$arg` and thus `$2` now contains the arguments value.

After we shift the next two values off, we remain with this arguments array
```bash
(
   $0 = ./arguments.sh
   $1 = my-project
)
```
Just one more step to go and we're done

As the last step we will handle all the other arguments passed in without a flag. Let's go!

**Matching other arguments**

Our final case matches any value that wasn't matched by our previous handlers. These can be arguments passed without any flag, like a project name, or something else entirely.
```bash
*)
OTHER_ARGUMENTS+=("$1")
shift # Remove generic argument from processing
;;
```
"Pop!" goes the weasel and adds the value to an array

For this handler we simply take the value of `$1` and add it to a miscellaneous array. After all the additional arguments have been added to the array, you can decide to do whatever you like. For example the first entry in the array could be a project name. Who knows!

**Trying it all out**

Now if you add some echo statements and try to run your script as stated above with `./arguments.sh -i --cache=/var/cache --root /var/www/html/public my-project` you could see output like the following
```
$ ./arguments.sh -i --cache=/var/cache --root /var/www/html/public my-project

# Should initialize: 1
# Cache directory: /var/cache
# Root directory: /var/www/html/public
# Other arguments: my-project
```


















