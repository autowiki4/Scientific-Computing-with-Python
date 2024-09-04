'''The code below is for a budget app. Budgets are stored in classes where each class represents a certain type of budget. For
    example, the budget used for food would be stored initiated with the class as a new object, distinct from budget spent for clothing.
    '''
import decimal, math

# FUnction to print the title of the budget above the items in the budget
def print_title(title):
            length = len(title)
            space = 30 - length
            no_space = space/2

            if space % 2 == 0:
                no_space = int(no_space)
                return f"{('*' * no_space)}{title}{('*' * no_space)}"
            elif space % 2 != 0:
                no_space = int(no_space-0.5)
                return f"{('*' * (no_space+1))}{title}{('*' * no_space)}"

# convert numbers entered into the ledger to float
def float_amount(money):
            # Converting the total balance number to decimal
            deciValue = decimal.Decimal(money)
            # rounding the number up to 2 digits after the decimal point
            float_balance = str(deciValue.quantize(decimal.Decimal('0.00')))
            return float_balance

# creation of budget category
class Category:
    def __init__(self,name):
        self.name = name  # name of budget category
        self.ledger = []
        self.withdraw_list = []

    # get_balance method
    def get_balance(self):
        return sum(map(lambda expense: expense['amount'], self.ledger))

    def print_ledger(self):
         return self.ledger

    # check funds method
    def check_funds(self, sample_amount):
        self.sample_amount = sample_amount

        # ensure that the amount being withdrawn is not more than the amount in the ledger
        if self.sample_amount > self.get_balance():
            return False
        else:
            return True

        # deposit method - deposit an amount of money in the budget category
    def deposit(self,amount,description=None):
        self.amount = amount
        self.description = description
        (self.ledger).append({"amount": amount, "description": description})


    # withdraw method
    def withdraw(self,w_amount,w_description=None):
        self.w_amount = w_amount
        self.w_description = w_description

        (self.withdraw_list).append(w_amount)

        if  not self.check_funds(self.w_amount):
            return False
        elif self.check_funds(self.w_amount):
            (self.ledger).append({"amount": -w_amount, "description": w_description})
            return True

    def withdraw_sum(self):
        return sum(self.withdraw_list)

    def transfer(self,t_amount,other_budget):
        self.t_amount = t_amount
        self.other_budget = other_budget

        if not self.check_funds(self.t_amount):
            return False
        elif self.check_funds(self.t_amount):
            (self.ledger).append({"amount": -t_amount, "description": f'Transfer to {other_budget.name}'})
            (other_budget.ledger).append({"amount": t_amount, "description": f'Transfer from {self.name}'})
            return True


    def __str__(self):
        result = ""
        for x in self.print_ledger():
            # to extract the amount and desciption for each item in the list
            float_money = float_amount(x["amount"])
            try:
                remove = 30 - len(x["description"])
                result += (f'{x["description"][:24]}{float_money.rjust(remove)}\n')
            except:
                remove = 30 - len(str(x["amount"]))
                result += (f'{float_money.rjust(30)}\n')
        return f'{print_title(self.name)}\n{result}Total:{str(float_amount(self.get_balance())).rjust(24)}'

def create_spend_chart(categories):
    total_list = []
    for i in categories:
        total_list.append(i.withdraw_sum())
    total = int(sum(total_list))

    # Delineate the lines for the vertical axis showing the percentage
    first_line = ['100|']
    second_line = [' 90|']
    third_line = [' 80|']
    fourth_line = [' 70|']
    fifth_line = [' 60|']
    sixth_line = [' 50|']
    seventh_line = [' 40|']
    eighth_line = [' 30|']
    ninth_line = [' 20|']
    tenth_line = [' 10|']
    eleventh_line = ['  0|']
    lines = [eleventh_line,tenth_line,ninth_line,eighth_line,seventh_line,sixth_line,fifth_line,fourth_line,third_line,
             second_line,first_line]
    real_lines = [first_line, second_line,third_line,fourth_line,fifth_line,sixth_line,seventh_line,eighth_line,
                  ninth_line,tenth_line,eleventh_line]

    global max_name,print_list
    name_list = []
    # list containing print out for budget names
    print_list = []

    # operation for each item in the budget list
    for budget in categories:
        # collect the names of all the budgets
        name_list.append(budget.name)

        # number of items on teh withdraw list
        list_total = int(sum(budget.withdraw_list))
        # list to contain the representative circles that shows the proportion of budget
        circle_list = []
        # calculate the proportion and round to nearest 10
        percent = int(math.floor((list_total / total) * 100)) // 10

        # append the corresponding number of circles
        for _ in range(percent + 1):
            circle_list.append('o')

        no_lines = 0
        circle_index = 0
        while no_lines < 11:
            try:
                (lines[no_lines]).append(circle_list[circle_index])
            except:
                pass
            no_lines += 1
            circle_index += 1

    # determine the length of the longest budget name
    max_length = max(len(name) for name in name_list)
    for budg in name_list:
        name_char = []
        for char in budg:
            # add each letter from the budget name
            name_char.append(char)
        for _ in range((max_length-len(budg))):
            # add extra spaces for the budget names with the least number of letters
            name_char.append(' ')
        print_list.append(name_char)

    # the - character will occupy the horizontal axis
    printed_lines = '-' * (1 + len(categories)*3)

    def print_lines(samp_lines):
        print_result = ''
        for line in samp_lines:
            # join each line by 2 spaces
            result = '  '.join(line)
            line_delineator = result.index('|')
            result = result[:line_delineator+1]+result[line_delineator+2:]
            print_result += f'{result}\n'
        return print_result

    resu = f'Percentage spent by category\n{print_lines(real_lines)}    {printed_lines}\n'

    max_name = max(len(obje) for obje in print_list)
    columns = '     '
    index = 0
    while index <= (max_name-1):
        columns += '  '.join(string[index] for string in print_list)
        columns += '\n     '
        index += 1
    modi_columns = columns.rstrip('\n     ')
    resu += modi_columns
    return resu


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
