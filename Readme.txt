Project Overview:
I created a database for "Las Palmas Medical Center", as part of a project aimed at implementing a database system to support the hospital's operations. The project involved designing a relational database schema, writing SQL scripts to create and populate the database, and developing a Python program to interact with the database for various queries and data management tasks.

Database Design and Implementation:

  Designed a relational schema consisting of 13 tables, including Physician, Department, Patient, Nurse, Medication, Room, and Appointment.
  Implemented the schema in MySQL using create_db.sql to define tables, primary keys, foreign keys, and value constraints.
  Populated the tables with sample data using insert_db.sql.


Python Program for Database Interaction:

  Developed a Python program to perform various database operations such as retrieving data, calculating averages, inserting new records, and    deleting existing records.
  The program connects to the MySQL database using the mysql.connector library.

  Implemented functions to handle specific tasks:

    Retrieve: Fetches all records from a specified table.
    Average: Calculates the average value of a specified column in a specified table.
    Insert: Adds new records to specified tables based on user input.
    Delete: Removes records from specified tables based on user input.


*** Please read all the instructions then run the .py file ***

*** Please follow the instructions below to run p3_Ahmed.py file ***



Step-1: Creating the database



2) Open the create_db.sql file in MYSQL Workbench.

3) Run all the queries in create_db.sql file.

4) Open the insert_db.sql file in MYSQL Workbench.

5)Run all the queries in insert_db.sql file.


Step-2: Creating the database connection

1. Please install mysql-connector-python package using the command in terminal: "pip3 install mysql-connector-python"

2. Create a MYSQL Connection in Mysql Workbench.

3. Open the p3_Ahmed.py file in a python IDE

4. Enter your User AND Password for database connection inside the p3_Ahmed.py file and save.


Step-3 Run the p3_Ahmed.py in terminal

1) Please store the p3_Ahmed.py file in home directory of your computer so that it can be run from terminal.

2) To run the p3_Ahmed.py file in terminal enter the following command in terminal: "python p3_Ahmed.py".

3) Then follow instructions shown in terminal to use project functionalities.


IMPORTANT Notes:

- While entering user input use ` ` for mysql reserved words. 

-Data of every tables can be found in the Data.pdf file.







