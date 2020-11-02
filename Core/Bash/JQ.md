
## How to read /etc/fstab Line by line:
```bash
egrep -v '^#' /etc/fstab | while read dev dir type opts dump pass ; do
    echo "mount -o remount,${opts} ${dir}";
done
```
Remember the variables in while loop will be lost since while is a subprocess.

This produces output like this:
```
mount -o remount,nodev,noexec,nosuid /proc
mount -o remount,relatime,errors=remount-ro /
mount -o remount,defaults /misc
```

## Delete paths:
```bash
jq 'delpaths([["results"],["timestamp"]])'

{
    "timestamp": 1234567890,
    "report": "Age Report",
    "results": [
        { "name": "John", "age": 43, "city": "TownA" },
        { "name": "Joe",  "age": 10, "city": "TownB" }
    ]
}

{
  "report": "Age Report"
}

```

## Compose an array with string entries:
```bash
ENTRY="A string ..."
$ echo '[]' | jq --arg entry "${ENTRY}" '. + [ $entry ]'

```

## Read string entries with spaces in between from array:
```bash
sample='[{"name":"foo"},{"name":"bar"}]'
for row in $(echo "${sample}" | jq -r '.[] | @base64'); do
    _jq() {
     echo ${row} | base64 --decode | jq -r ${1}
    }

   echo $(_jq '.name')
done

foo
bar
```

Jq -r : to get rid of the extra quotes.
Jq -c: (--compact-output) get each object one a newline

We could start iterating of the above with a Bash for loop if our data does not contain spaces or newlines. But since certificates contain newlines we better base64 encode each line. Also, instead of -c, we now use -r to get rid of the extra quotes.
```bash
sample='[{"name":"foo"},{"name":"bar"}]'
echo "${sample}" | jq -r '.[] | @base64'

eyJuYW1lIjoiZm9vIn0=
eyJuYW1lIjoiYmFyIn0=
```

- To extract keys from arrays and remove []
```bash
jq 'keys | .[]'

"report"
"results"
"timestamp"
```

```
{
    "timestamp": 1234567890,
    "report": "Age Report",
    "results": [
        { "name": "John", "age": 43, "city": "TownA" },
        { "name": "Joe",  "age": 10, "city": "TownB" }
    ]
}
```
- To delete keys "timestamp" and "report"
```bash
$jq 'if has("timestamp") then del(.timestamp) else . end | if has("report") then del(.report) else . end'

# Or

$jq 'if .timestamp then del(.timestamp) else . end | if .report then del(.report) else . end'
```
```
{
  "results": [
    {
      "name": "John",
      "age": 43,
      "city": "TownA"
    },
    {
      "name": "Joe",
      "age": 10,
      "city": "TownB"
    }
  ]
}
```

- To get values of the json:
```bash
$jq '.[]'
```
```
1234567890
"Age Report"
[
  {
    "name": "John",
    "age": 43,
    "city": "TownA"
  },
  {
    "name": "Joe",
    "age": 10,
    "city": "TownB"
  }
]
```


- To extract top level attributes "timestamp" and "report"
```bash
$jq '{timestamp,report} |.[]'
```
```
1234567890
"Age Report"

{"xml": 1, "yaml": 2, "json": 3}

$ echo '["xml", "yaml", "json"]' | jq '. - ["a", "b", "xml", "yaml"]'
[
  "json"
]
```

- To obtain the specified keys from json

```bash
$ echo '{"xml": 1, "yaml": 2, "json": 3}' | jq 'keys | . - ["a", "b", "xml", "yaml"]'
```
```
[
  "json"
]
```


## To process each key:value of each object: use |=
This will modify the value of the json locally

```bash
$ jq '.[].age |= ((. - .%8)|tostring + "+")'
```

Input:
```
{
  "aaa": {
    "name": "John",
    "age": 46,
    "city": "TownA"
  },
  "bbb": {
    "name": "Joe",
    "age": 13,
    "city": "TownB"
  }
}
```
Output:
```
{
  "aaa": {
    "name": "John",
    "age": "40+",
    "city": "TownA"
  },
  "bbb": {
    "name": "Joe",
    "age": "8+",
    "city": "TownB"
  }
}
```

Plus if then else end:
```bash
$ jq '.[].age |= if (. > 8) then ((. - .%8)|tostring + "+") else . end'
```
Input
``` 
{
  "aaa": {
    "name": "John",
    "age": 46,
    "city": "TownA"
  },
  "bbb": {
    "name": "Joe",
    "age": 13,
    "city": "TownB"
  },
  "ccc": {
    "name": "Joe",
    "age": 7,
    "city": "TownB"
  }
}
```

Output:
```
{
  "aaa": {
    "name": "John",
    "age": "40+",
    "city": "TownA"
  },
  "bbb": {
    "name": "Joe",
    "age": "8+",
    "city": "TownB"
  },
  "ccc": {
    "name": "Joe",
    "age": 7,
    "city": "TownB"
  }
}
```

## Filter JSON by child object's key value:
```bash
$ jq '.[] |= select( .name == "Joe" )'
```
Input:
```
{
  "aaa": {
    "name": "John",
    "age": 46,
    "city": "TownA"
  },
  "bbb": {
    "name": "Joe",
    "age": 13,
    "city": "TownB"
  },
  "ccc": {
    "name": "Joe",
    "age": 7,
    "city": "TownB"
  }
}
```
Output:
```
{
  "bbb": {
    "name": "Joe",
    "age": 13,
    "city": "TownB"
  },
  "ccc": {
    "name": "Joe",
    "age": 7,
    "city": "TownB"
  }
}
```

The same result using:
```bash
$ jq 'with_entries ( select ( .value.testA.testB == "123" ))'
```
input:
```
{
  "aaa": {
    "name": "John",
    "age": 46,
    "city": "TownA",
    "testA": {
        "testB": "123"
    }
  },
  "bbb": {
    "name": "Joe",
    "age": 13,
    "city": "TownB",
        "testA": {
        "testB": "124"
    }
  },
  "ccc": {
    "name": "Joe",
    "age": 7,
    "city": "TownB",
        "testA": {
        "testB": "125"
    }
  }
}
```

Output:
```
{
  "aaa": {
    "name": "John",
    "age": 46,
    "city": "TownA",
    "testA": {
      "testB": "123"
    }
  }
}
```

## Iteration
Now let’s see how iteration works. The array or object value iterator operator, .[] , is what makes it possible.

Here’s a really basic example:
```bash
echo '[1,2,3]' | jq '.[]'
```
That will output 1, 2, 3 on separate lines.

In an array of objects, you can access a property on each item in the array like so:
```bash
echo '[ {"id": 1}, {"id": 2} ]' | jq '.[].id'
```
Or on an object, .[] will output the value of each key/value pair:
```bash
echo '{ "a": 1, "b": 2 }' | jq '.[]'
```
So that will return 1 2.
```bash
echo '{ "a": 1, "b": 2 }' | jq 'keys'
```
So that will return ["a","b"]

Note that you can also pass an index to .[], so
```bash
echo '["foo", "bar"]' | jq '.[1]'
```
will return just bar.

Now how do we do something for each line? In the same way you’d handle anything that outputs multiple lines of information in bash: xargs , for loops, or some commands just handle multiple input items, etc. For example:
```bash
echo '["foo", "bar"]' | jq '.[]' | touch
```
## jq Functions
- keys
jq also has built-in “functions”. Returning to the previous object iteration example — let’s say we wanted get the keys of the object (not the values) as an array:
```bash
echo '{ "a": 1, "b": 2 }' | jq 'keys | .[]'
```
which will return a b . Note that we’re also using the pipe | operator, which works the same in jq as it does in bash — it takes the output from the left and passes it as input to the right.
- length
Another handy function for arrays and objects is the `length` function, which returns the array’s length property or the number of properties on an object.
```bash
echo '[1,2,3]' | jq 'length'
```
You can get even fancier and create intermediary arrays and objects on the fly. Here, combining the keys of the dependencies and devDependencies objects (from a package.json file) into an array, flattening it, and then getting the length.
```bash
jq -r '[(.dependencies, .devDependencies) | keys] | flatten | length' package.json
```
That returns the number of dependencies and devDependencies a package.json contains.

## Creating objects
You can also create objects on the fly. This can be useful for re-shaping some JSON. For example:
```bash
echo '{"user": {"id": 1, "name": "Cameron"}}' | jq '{ name: .user.name }'
# { "name": "Cameron" }
```

## From a JSON file
Just pass the file path after the jq script.
```bash
jq '.name' package.json
```

## In a chain of pipes
You’ll probably want to use the -r (raw) command if you’re using it in a pipeline or saving the output to a variable. -r gets rid of formatting like quotes and spaces for single values. For objects, it outputs valid JSON so it will have quotes.
```bash
# this downloads the latest APOD and saves to a file
url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
curl -o apod.png "$(curl -s $url | jq -r '.hdurl')"
```
## Array


- The array operator: []

.artObjects returned one big array of JSON objects. Before we can access the values inside those objects, we need to break them out of the array that they’re in. By adding [] onto the end of our filter, jq will break up this one array into 10 separate objects:

Try it:

.artObjects[]
Notice that the [] wrapping our results are now gone. To make clear what has happened, check the “Compact Output” checkbox in the upper right. This removes the cosmetic line breaks in the results, returning one JSON object per line. You should have a 10-line output now.


- Get an array element by index

```bash
echo '[0, 1, 1, 2, 3, 5, 8]' | jq '.[3]'
# 3
```


- Slice an array

Slices an array on by index.
```bash
echo '["a", "b", "c", "d"]' | jq '.[1:3]'
# ["b", "c"]
```
Either the first or last index can be omitted to go from the begining or end.
```bash
echo '["a", "b", "c", "d"]' | jq '.[1:]'
# ["b", "c", "d"]
```

- Creating a new object

The syntax looks like this: `{ myPropertyName: .propertyFromJSON }`.
```bash
echo '{ "a": 1, "b": 2 }' | jq '{ a: .b, b: .a }'
# { "a": 2, "b": 1 }
```

## Useful functions

- keys

Gets an object’s keys as an array.
```bash
echo '{ "a": 1, "b": 2 }' | jq 'keys'
# [a, b]
```

- length

Gets the length of the array/
```bash
echo '[0, 1, 1, 2, 3, 5, 8]' | jq 'length'
# 7
```
Or the number of top level keys.

```bash
echo '{"a": 1, "b": 2}' | jq 'length'
# 2
```

- flatten

Condense a nested array into one.

```bash
echo '[1, 2, [3, 4]]' | jq 'flatten'
# [1, 2, 3, 4]
```
- All together

All the above functions used together, just for fun
This gets the total number of dependencies in a package.json file.
```bash
jq -r '[(.dependencies, .devDependencies) | keys] | flatten | length' package.json
```
- unique

Gets an array of unique values.
```bash
echo '[1, 2, 2, 3]' | jq 'unique'
# [1, 2, 3]
```
- join

Joins the elements of an array using a separator.
```bash
echo '{ "firstName": "Cameron", "lastName": "Nokes" }' | jq '[.firstName, .lastName] | join(" ")'
# Cameron Nokes
```

We create an array of the properties we want joined, pipe to join which is passed a space as the separator.




