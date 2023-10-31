# ehealth
ehalth assignment v1.0

Read Me: eHealth Job Application Assignment
=======================================									October 31st, 2023

System Requirement
=======================
In order to be able to run the assignment python (Django) App, you must have the following, running on your system:
-Python 3.11.3 or above
-pip 23.1.2 or above
-Apache, MySql, Perl Server 3.3.0 or above
-Windows 10 or Linux (Ubuntu) 20.0 and above

Installation
========================
You may install the python (Django) App by following the steps below:
- Download all the code into a folder named 'ehealth'
- Open the command prompt(window), shell(linux), and navigate to the folder ehealth, located in the root ehealth folder
- Create an empty database named 'ehealth_db' on your Apache, MySql, Perl Server once you have started it and it is running.
- Type 'python manage.py migrate' at the command prompt to run the migration files.
- Also run the sql script located in the deploy folder against the database to install records for states and ailment tables.
- Navigate to the Scripts folder and type 'activate' at the command/shell to activate the virtual environment.
- Once the virtual environment is running, navigate into the 'ehealth' folder and type 'python manage.py runserver' to run the app
- You would see information such as: 
	System check identified no issues (0 silenced).
	October 31, 2023 - 16:36:28
	Django version 4.2.6, using settings 'ehealth.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.
- then type http://127.0.0.1:8000/ into any web browser and start, Voila!

I have also included 10 screen shots of the running app to help you quickly familiarize with the environment.

Hope this help!

Abdulrahman Obaje

