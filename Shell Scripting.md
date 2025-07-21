
#!/bin/bash
Get a particular column from output of ps

```shell
 ps -ef | awk -F" " '{print $3}'
```

```shell
if [ condition ]; then
    # commands to execute if condition is true
elif [ another_condition ]; then
    # commands to execute if another condition is true
else
    # commands to execute if none of the above conditions are true
fi
```
- IF else


Do while 

```shell
do 
    # commands to execute at least once
done while [ condition ]
```


Count number of occurences of a letter in a word

x="mississipi"
grep -o "s" <<< "$x" | wc -l

```shell
x="mississipi"
grep -o "s" <<< "$x" | wc -l

```

Run a shell script in debug mode:

add below command at the start of the script

```shell
set -x
```

What is the difference between soft link and hard link in shell scripting?

![[Pasted image 20240717005544.png]]

Bash is Dynamically typed or statically typed?

Bash is dyanmically typed -- meaning we don't need to specify data types while defining variables
Python is also dynamically Typed.

Different types of loop in shell scripting and their use cases?


How will you manage logs in a system that generates alot of logs everyday?


using logrotate command we can specify how long do we want to keep the logs
after a certain interval the logs will be zipped.

logrotate()

Loops syntax shell scripting


**Loops**

For Loop syntax
```shell
#!/bin/bash

# set counter 'c' to 1 and condition

# c is less than or equal to 5

for (( c=1; c<=5; c++ ))

do 

   echo "Welcome $c times"

done

```


|                                                |     |
| ---------------------------------------------- | --- |
| 2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7 |     |

==I have directory which have multiple sub directories and I want to replace some content in a specific file in each directory



```shell

#!/bin/bash

# Root directory (adjust this as needed)
ROOT_DIR="/path/to/root"

# File name to search for in each subdirectory
TARGET_FILE="config.txt"

# What to replace (from -> to)
FROM="foo"
TO="bar"

# Find and replace
find "$ROOT_DIR" -type f -name "$TARGET_FILE" | while read -r file; do
  echo "Updating $file"
  sed -i "s/$FROM/$TO/g" "$file"
done

```

==AWK

```shell
awk options 'selection _criteria {action }' input-file > output-file
```

for example.
https://www.geeksforgeeks.org/awk-command-unixlinux-examples/