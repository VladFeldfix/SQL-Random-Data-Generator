<h1>DB-RANDOM-DATA-GENERATOR</h1>
<h2>Introduction:</h2>
<p>
This simple script generates random entries to fill your database<br>
The generated file is in mySQL languege in a form of INSERT VALUES query
</p>
<h2>Instructions:</h2>
<ol>
<li>Download file DBRANDATAGEN.exe to your device</li>
<li>Create a new file named: script.txt in the same folder</li>
<li>Insert parameters into script.txt according to the syntax (see below)</li>
<li>Save changes, exit the file and run DBRANDATAGEN.exe</li>
<li>After the code says DONE! press Enter to close the program and see the created .sql file</li>
</ol>
<h2>Syntax:</h2>
<p>
Write every command in a separate line.<br>
Make sure to separate words by exactly one Space</p>
<p>
TABLE_NAME [The name of your table]<br>
ENTRIES [The number of random entries you want to make]<br>
# [Field name] [Parameters]<br>
GENERATE_FULL [Filename you want to transfer from .lst to .sql]<br>
</p>
<p><b>Parameters types:</b></p>
<p>
STR - random assmbly of letters:              MIN_LENGTH, MAX_LENGTH, *UNIQUE, *UPPERCASE, *LOWERCASE, *NUMBERS<br>
INT - random INT from min to max:             MIN, MAX<br>
FLOAT - random FLOAT:                         MIN, MAX<br>
CHAR - random single character:               FIRST_OPTION, SECOND_OPTION ... <br>
BOOL - randomly assign true or false:         CHANCE_OF_TRUE, CHANCE_OF_FALSE<br>
LST - choose random value from an .lst file:  FILE_NAME<br>
</p>
<p><b>Example 1:</b></p>
<p>
TABLE_NAME customers<br>
ENTRIES 10000<br>
# id_number INT 100000000 999999999 UNIQUE<br>
# username STR 5 10 LOWERCASE UPPERCASE NUMBERS UNIQUE<br> 
# password STR 6 12 LOWERCASE UPPERCASE NUMBERS<br>
# first_name LST first_names.lst<br>
# last_name LST last_names.lst<br>
# sex CHAR M F<br>
# phone_number LST phones.lst<br>
# city INT 1 100000<br>
</p>
<p><b>Example 2:</b></p>
<p>
TABLE_NAME cities<br>
GENERATE_FULL cities.lst<br>
</p>
<P><b>For more information:</b></P>
<p>
To see the examples in progress download the following files:<br>
DBRANDATAGEN.exe<br>
cities.sql<br>
first_names.lst<br>
last_names.lst<br>
cities.lst<br>
phones.lst<br>
example1.txt (To activate rename it to script.txt)<br>
example2.txt (To Activate rename it to script.txt)<br>
</p>
