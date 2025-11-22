# CLI Expense-Tracker
VITyarthi CSE Flipped course project , Python

# Introduction
To design a simple console based python program that help end user to track his budget and expenses in monthly basis or earlier if the user wants to exit <br>
**name:** Uday Pratap Singh <br>
**reg no.:** 25BAI11360

# Overview of the project
This is a command-line interface (CLI) application designed for personal monthly expense and budget tracking. The program is implemented in Python and utilizes an in-memory data structure (a list of dictionaries) to store daily and cumulative financial data for a maximum of 30 days. The primary goal of the system is to help a user monitor their spending across several predefined categories, manage a monthly budget, and track cumulative expenses. The following sections detail the system's design, functional components, architecture, and potential future enhancements.

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
* **Add expenses:** You can add expenses by choosing option 1 from the menu, later choose the sub category for adding expenses in to particular section where you money was spent.It also calculates the total expenses on that day additionally it tracks the cumulative expense in category wise and total expense in a month.at last it prints the budget left  after the amount you spent at the instance.
