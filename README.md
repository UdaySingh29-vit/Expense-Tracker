# CLI Expense-Tracker
VITyarthi CSE Flipped course project , Python

# Introduction
To design a simple console based python program that help end user to track his budget and expenses in monthly basis or earlier if the user wants to exit <br>
**name:** Uday Pratap Singh <br>
**reg no.:** 25BAI11360

# Overview of the project
This is a command-line interface (CLI) application designed for personal monthly expense and budget tracking. The program is implemented in Python and utilizes an in-memory data structure (a list of dictionaries) to store daily and cumulative financial data for a maximum of 30 days. The primary goal of the system is to help a user monitor their spending across several predefined categories, manage a monthly budget, and track cumulative expenses. 

# Features
* **Monthly Budget Management:** Allows the user to set an initial total budget for the month upon startup.

* **Real-Time Budget Tracking:** Automatically calculates and displays the remaining budget after every single transaction.

* **Fixed Expense Handling (Subscription):** Asks for and deducts a fixed monthly subscription cost on the first day of the month.

* **Expense Categorization (Predefined):** Supports logging expenses into five specific, hardcoded categories:<br>
           - Bills: For monthly bills.<br>
           - Food: For groceries and daily care items.<br>
           - Cars: For car and transportation-related costs.<br>
           - Clothes: For clothing expenses.<br>
           - Other: For miscellaneous expenditures.<br>

* **Daily and Cumulative Totals:** Automatically tracks and accumulates the total money spent both for the current day and for the entire month.

* **Day Advancement:** Provides an explicit option to manually move the tracking to the next day.

* **Historical Reporting:** Generates and displays a detailed, tabular chart showing the expense breakdown for every tracked day up to the current date.

* **Exit Summary:** When the program is terminated, it prints a final summary including total expenses and the final remaining budget.

# Technologies/Tools Used
* **Language:** Python 3.x
* **Code Editor:** VS Code

# Steps to Install & Run
1.  **Prerequisites:** Ensure you have Python installed on your system. You can check by running `python --version` in your terminal.<br>
2.  **Download:** Download the `main.py` file to a local directory.<br>
3.  **Run:** Open your terminal or command prompt, navigate to the directory, and run:
    ```bash
    python main.py
    ```
# Instructions For Testing 
1. Start the VS Code
2. Copy the code in the new file created in VS Code.
3. Run the Program and in the terminal use test case given below to get the results
* **For intial budget setup:** input monthly budget you want to use
* **subscription amount:** input amount you pay on subsciption
* **Add expenses and budget update:** You can add expenses by choosing **option 1** from the menu, later choose the sub category for adding expenses in to particular section where you money was spent.It also calculates the total expenses on that day additionally it tracks the cumulative expense in category wise and total expense in a month.at last it prints the budget left  after the amount you spent at the instance.
* **Budget update:** by choosing **option 2** from the menu you can add more value to budget.
* **Day advancement:** By choosinng **option 3** from the menu you can jump to next day and add more expenses on the next day.
* **to print expense chart till date:** by choosing **option 4** from the menu you can print the expense chart till the moment.
* **to exit the program:** by choosing **option 5** from the menu you can exit the expense tracker and it print the final expense chart at the end and budget left.

# Screenshots
**Initial Run**<br>
<img width="930" height="369" alt="image" src="https://github.com/user-attachments/assets/1cb95be2-3e5a-4965-8bbe-867169124484" />
<br>
**menu option 1**<br>
<img width="940" height="503" alt="image" src="https://github.com/user-attachments/assets/33f964a7-dca4-4386-82e5-314fa67cee8a" />
<br>
**invalid choice display**<br>
<img width="911" height="522" alt="image" src="https://github.com/user-attachments/assets/de9ba6bc-263d-4cc1-8d29-69dd7f563fd3" />
<br>
**Menu option 2**<br>
<img width="863" height="281" alt="image" src="https://github.com/user-attachments/assets/e3a14d29-a90d-41f2-bbac-8441e387aa15" />
<br>
**Menu option 3**<br>
<img width="931" height="313" alt="image" src="https://github.com/user-attachments/assets/386fcf93-4b8a-4f36-8396-a8a1c9422ef5" />
<br>
**Menu option 4**<br>
<img width="940" height="324" alt="image" src="https://github.com/user-attachments/assets/1b0fbb1e-3f28-4e37-8aa5-5c06ee66e47e" />
<br>
**Menu option 5**<br>
<img width="940" height="829" alt="image" src="https://github.com/user-attachments/assets/abf07395-d2f4-4f34-a9cb-e328b98ea09c" />

