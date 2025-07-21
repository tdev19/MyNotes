
1) Difference between DELETE and Truncate Command
--> Delete command is used to delete a row in a table
     It is a DML command (Data Modification)
     you can roll back data after using the delete statement
     It is slower than truncate statement.
Truncate command is used to  delete all the rows in the table
data cant be rolled back
It is faster.
It is DDL command.

2) Different subsets of SQL
--> DDL - Data definition Language -- commands which can be used to define the database schema
    DML - Data modification Language -- commands which manipulate the data
	DCL - Data control Language -- >commands which deal with rights and permissions
	TCL - Includes commands which deals with transactions of database

3) What is a primary Key?
--> A set of attributes that can be used to uniquely identify every table is  a primary key. So there are 3-4 candidate keys present in a relationship then out of those one can be chosen as a primary key.

4) What are constraints?
--> Constraints are used to specify the limit on the data type of the table. It can be specified while creating or altering the table statements.

NOT NULL - 
UNIQUE  - ensures all values entered in a column are unique
CHECK -  ensures that all values in the column satisfy a specific condition
DEFAULT - consists of set of default values for a column when no values is specified.
INDEX - used to create and retrieve data from  the database very quickly.

5) What is a foreign key?
--> Foreign key maintains referential integrity by enforcing link between the data in two tables.
Foreign key in child table references primary key in parent table
The foreign key prevents actions that would destroy links between the child and parent tables.


Get 2nd highest salary from the table

```sql
select max(sal) from emp  where sal not in (select max(sal) from emp)
```



What is a left join ?

All matching values from left side table are shown
and matching rows from right side table are shown
while null values are shown in place where there was no match between the tables.
