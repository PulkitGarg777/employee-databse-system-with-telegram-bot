# employee-databse-system-with-telegram-bot

A BRIEF OVERVIEW  
1.	Firstly, the code asks the user to enter the password so that they can enter new data and/or modify existing data.
2.	After entering the correct password, the user is given a menu from which they can select various functions. These functions are:
3.	The user can accordingly enter the menu number in the prompt provided:
 
WORKING OF FUNCTIONS

1.	The first option enables the user to add a new employee. The code checks if the ID entered is already present. If not, it continues, else gives a prompt.
2.	The second option enables the user to clear (delete) an employee data. As employee ID is the primary key, deleting the record of an employee is easy and can be done without any error. If the ID is not present the code prompts the user to enter an already present ID.
3.	The third option enables the users to promote or demote a certain employee.
4.	The forth option is a searching function. In this the employee is provided with a menu from which he/she can search an employee on the basis of their ID, NAME, DOB etc. 
Also, in an employee record management system, the user may want to obtain the record of the employees’ earning a certain amount or which are earning less than/greater than a certain sum. 
Hence if the user chooses to search via salary, he/she is again given a menu to choose from.
5.	The fifth option allows the user to view all the records present in the table.
6.	The sixth option allows the user to exit/stop modifying the table content.

INTEGRATION OF TG BOT
In this code, we’ve also managed to link a telegram bot that pings us every time there has been an activity with the code.  
The API of the bot


 









 
