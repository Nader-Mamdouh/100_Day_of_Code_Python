Password Manager

Project Overview:
This Python-based password manager utilizes the Tkinter library to provide a user-friendly graphical interface. It enables users to securely store website names, email addresses, and passwords in a JSON file.

Features:
1. Generate Strong Password:
Click the "Generate" button to create a robust and secure password using the built-in password generation function.
2. Add to File:
Input website names, email addresses, and passwords, then save the data to a JSON file by clicking the "Add to File" button.
3. Search Functionality:
Retrieve email and password associated with a specific website by clicking the "Search" button.
4. GUI Elements:
Three labels are provided for clear information display.
A visually appealing photo enhances the overall user interface.
Files:
password_manager.py:

Main code for the password manager application.
password_data.json:

JSON file to securely store website, email, and password data.
Dependencies:
Python 3.x
Tkinter (standard GUI toolkit for Python)

How to Run:

Ensure Python is installed on your machine.
Run the password_manager.py script.
Instructions:
Click "Generate" to create a strong password.
Enter the website name, email, and password.
Click "Add to File" to save the data to the JSON file.
Use "Search" to retrieve email and password by entering the website name.
Important Notes:
Keep the password_data.json file secure, as it contains sensitive information.
Do not share your master password or any generated passwords with others.
Improvements and Future Work:
Implement encryption for enhanced security.
Allow users to update or delete saved entries.
Add the ability to copy passwords to the clipboard for easy use.
