"""This program is made to track expenses and also the budget of a person on monthly basis,
next day can be additionally shown in the option,
otherwise the expense will be updated in the same day with starting day as 1st day of a month,
for expenses on food and daily care item the expense tracker will subject that to "grocery",
additionally expenses on car and other related to transportation would be subjected to  "car expenses",
clothes expenses would be subjected under the "clothes" ,monthly bills as "bills"
And lastly expenses on subsriptions would be subjected to "subsrciption" and would be asked in the first day of the month """

# variable intitialisation
l = []
c = ["total", "biils", "food", "cars", "clothes", "other"]
for i in range(0, 31):
    l.append({})
    for j in range(0, 6):
        l[i][c[j]] = 0
l[0]["budget"] = 0
l[0]["subscription"] = 0
i = 1
budget = 0


def add_expense():
    """function add expense"""
    print("""choose where to add your expenses
          1. bills
          2. food and daily things
          3. cars and transport
          4. clothes
          5. other expenses""")
    o = int(input("enter option no. : "))
    if o > 0 and o < 6:
        v = int(input("enter amount of money you spent "))
        l[i][c[o]] += v
        l[i][c[0]] += v
        l[0][c[o]] += v
        l[0][c[0]] += v
        l[0]["budget"] -= v
        print(f"total budget left = {l[0]["budget"]}")
    else:
        print("enter a valid option")


def add_budget():
    """function to add more to budget"""
    v = int(input("input money you want to add in your budget "))
    l[0]["budget"] += v
    budget += v


def next_day():
    """function to jump to next day"""
    print(
        f"total money spent today - {l[i][c[0]]} \nTotal budget left - {l[0]["budget"]}")


def exits():
    """function to exit from program at any point"""
    print("expense tracker uptill now \n")
    show()
    print("Total expenses till now is ", l[0][c[0]])
    print("total budget left is", l[0]["budget"])
    print("Thankyou for using expense tracker")
    exit()


def show():
    """"to print the expence tracker table till ther given date"""
    print("day \tbills \tfood \tcars \tclothes other \tTotal")
    for k in range(1, i+1):
        print(i, end="\t")
        for j in range(1, 6):
            print(l[k][c[j]], end="\t")
        print(l[i][c[0]])
    print("subscription on day 1 costed", l[0]["subscription"])


# main working
budget = int(input("enter the budget for this month : "))
l[0]["budget"] = budget
l[0]["subscription"] = int(
    input("enter the amount you spend monthly on subscription : "))
while i < 31:
    print("""Menu:
         1. to add expense on the current day
         2. to add more money to your budget
         3. to start next day
         4. to show the expense chart till now
         5. to exit from the program""")
    p = int(input("enter the choice"))
    if p == 1:
        add_expense()
    elif p == 2:
        add_budget()
    elif p == 3:
        next_day()
        i = i+1
    elif p == 4:
        show()
    elif p == 5:
        exits()
    else:
        print("enter a valid choice")
print("Thankyou for choosing expense tracker")
exits()
