''' The following Python code is called an "arithmetic arranger". It accepts strings conatinng an arithmetic operation in a list
    within the 'problems' parameter.
    The 'solve' parameter is an optional parameter. Its only accepted value is teh boolean value 'True'. Its used if you want
    to solve the arithmetic operation. If not,, no value needed.'''
def arithmetic_arranger(problems, solve=None):
    global solution
    global index
    arranged_problems = '' # contain the adjusted string
    arrange_problems = [] # to contain all adjusted strings in a list

    '''I set a limit on the maximum number of problems involved. I set a maximum of 5 problems.'''
    # Test for maximum number of items in list
    if len(problems) > 5:
        return "Error: Too many problems."

    # list of operators the program will be indexing
    operators = ['+','-','*','/']
    for item in problems:
        # Index the addition or subtraction operator in each arithmetic operation
        for operation in operators:
            if operation in item:
                index = item.index(operation)

        # Code to extract the digits within the string.
        # The code is designed such that there has to be a space between the digits and the arithmetic operator
        int_1 = item[:index-1]
        int_2 = item[index+2:]

        # Ensure numbers entered consist of digits
        if not int_1.isdigit() or not int_2.isdigit():
            return "Error: Numbers must only contain digits."

        '''I am designing the code such that it doesn't take more than a 4 digit number'''
        # Ensure that numbers entered contain at most four(4) digits
        if len(int_1) > 4 or len(int_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            pass

        '''The 'solve' parameter in the function is an optional variable used to determine if the code should carry out the arithmetic operation
            arrange the arithmetic operation. If there is no value for the 'solve' parameter, the function simply just 
            arranges the arithmetic operation.'''
        # solve the arithmetic operation using the optional variable
        if solve == True:
            solution = str(eval(item))
        else:
            pass

        # Code to execute is the 'solve' parameter is True

        # variable to temporarily hold the modified string containing the arithmetic operation
        modified_i = ''

        # Arrange the arithmetic operation according to the maximum number of digits between the 2 digits
        if solve == True:
            max_digits = max(len(int_1), len(int_2))
            hyphen = '-'
            modified_i = f'{int_1.rjust(max_digits+2)}\n{item[index]} {int_2.rjust(max_digits)}\n{hyphen*(max_digits+2)}\n{solution.rjust(max_digits+2)}'

        else:
            max_digits = max(len(int_1), len(int_2))
            hyphen = '-'
            modified_i = f'{int_1.rjust(max_digits + 2)}\n{item[index]} {int_2.rjust(max_digits)}\n{hyphen * (max_digits + 2)}'

        arrange_problems.append(modified_i)

    # When the 'solve' variable is present
    if solve == True:
        # print the arithmetic in new lines
        # I will create a gap of 4 spaces between items
        for num in range(0,4):
            arranged_problems += '    '.join(string.split('\n')[num] for string in arrange_problems)
            arranged_problems += '\n'

    else:
        # print the arithmetic in new lines
        # I will create a gap of 4 spaces between items
        for num in range(0, 3):
            # range(0,3) used here because teh solution to the arithmetic operation is not involved
            arranged_problems += '    '.join(string.split('\n')[num] for string in arrange_problems)
            arranged_problems += '\n'

    return arranged_problems

# Test the function
print(arithmetic_arranger(["32 + 698", "3801 * 2", "45 + 43"], True))