5**What is a shell?**

--> Shell is a command line interpreter. which converts the commands entered by the user into
a language that is understood by kernel.

**Variables are of two types in shell scripting**

1) System Defined Variables 
2) User Defined Variables

An expression can be: String comparison, Numeric comparison, File operators and Logical operators and it is represented by [expression]:
String Comparisons:  
---------------------------------
=  compare if two strings are equal
!=  compare if two strings are not equal
-n  evaluate if string length is greater than zero
-z  evaluate if string length is equal to zero 

Examples: 
[ s1 = s2 ]  (true if s1 same as s2, else false)
[ s1 != s2 ]  (true if s1 not same as s2, else false)
[ s1 ]   (true if s1 is not empty, else false)
[ -n s1 ]   (true if s1 has a length greater then 0, else false)
[ -z s2 ]   (true if s2 has a length of 0, otherwise false)

Number Comparisons: 
------------------------------------
-eq compare if two numbers are equal
-ge compare if one number is greater than or equal to a number
-le  compare if one number is less than or equal to a number
-ne  compare if two numbers are not equal
-gt  compare if one number is greater than another number
-lt  compare if one number is less than another number 

Examples: 
[ n1 -eq n2 ]  (true if n1 same as n2, else false)
[ n1 -ge n2 ]  (true if n1greater then or equal to n2, else false)
[ n1 -le n2 ]  (true if n1 less then or equal to n2, else false)
[ n1 -ne n2 ]  (true if n1 is not same as n2, else false)
[ n1 -gt n2 ]  (true if n1 greater then n2, else false)
[ n1 -lt n2 ]  (true if n1 less then n2, else false)

---> A program which contains information about a specific filesystem.

**What are different stages that a linux process passes through?**
-->
	Waiting
	Running
	Stopped
	Zombie -- Process is stopped but still active in process table.


What is the Significance of the shebang line in shell scripts?

--> It simply provides information regarding the location where the engine is placed. The engine is the one which executes the script. It can be ignored if we want to use the default engine.

**Get the number of parameters passed to a script?**
 --> $# is used to get the number of parameters.

**Get script name inside the script?**

--> $0 is used to get the name of the script.

**check status of previous command?**

--> $?

**Get last line from a file?**

--> tail -1 <filename>

**Get first line from a file?**

--> head -1 <filename>


****Read input from user on the same line****
--->
read -p 'Enter username: '  $username
echo $username
#input from user will be store in $username variable.

**Read input securely from the user on the same line**
-->
read -sp 'Enter password:' $pass
#password will be stored in $pass variable.



# **If-else statements in shell scripting**

if [ condition ]
then
	statement
fi

can use below operators for integer comparison
-eq, -ne, -gt, -lt, 

whenever we use angle brackets for comparison use 
[[ a > b]] or ((a > b))

An expression can be: String comparison, Numeric comparison, File operators and Logical operators and it is represented by [expression]:
String Comparisons:  
---------------------------------
=  compare if two strings are equal
!=  compare if two strings are not equal
-n  evaluate if string length is greater than zero
-z  evaluate if string length is equal to zero 

Examples: 
[ s1 = s2 ]  (true if s1 same as s2, else false)
[ s1 != s2 ]  (true if s1 not same as s2, else false)
[ s1 ]   (true if s1 is not empty, else false)
[ -n s1 ]   (true if s1 has a length greater then 0, else false)
[ -z s2 ]   (true if s2 has a length of 0, otherwise false)

Number Comparisons: 
------------------------------------
-eq compare if two numbers are equal
-ge compare if one number is greater than or equal to a number
-le  compare if one number is less than or equal to a number
-ne  compare if two numbers are not equal
-gt  compare if one number is greater than another number
-lt  compare if one number is less than another number 

Examples: 
[ n1 -eq n2 ]  (true if n1 same as n2, else false)
[ n1 -ge n2 ]  (true if n1greater then or equal to n2, else false)
[ n1 -le n2 ]  (true if n1 less then or equal to n2, else false)
[ n1 -ne n2 ]  (true if n1 is not same as n2, else false)
[ n1 -gt n2 ]  (true if n1 greater then n2, else false)
[ n1 -lt n2 ]  (true if n1 less then n2, else false)

# File name testing options

if [ -e $filename ]  --> returns true if file exists
if [ -d $dir_name ] --> returns true if directory exists
if [ -s $filename ] --> returns true if file is not empty