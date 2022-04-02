def arithmetic_arranger(problems: list, solve=False) -> list:
    arranged_problems = []
    if len(problems) > 5:
        return "Error: Too many problems."
    number1s = ''
    number2s = ''
    equals = ''
    solutions = ''
    problemsDone = 0
  
    for problem in problems:
        components = problem.split()
        number1 = components[0]
        operator = components[1]
        number2 = components[2]
        solution = 0

        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if ((number1.isnumeric()) == False) or (number2.isnumeric() == False):
            return "Error: Numbers must only contain digits."

        if (operator == '+'):
            solution = int(number1) + int(number2)
        elif (operator == '-'):
            solution = int(number1) - int(number2)
        else:
            return "Error: Operator must be '+' or '-'."
          
        if problemsDone < (len(problems) - 1):
            if (len(str(solution)) > len(str(number1))) and (len(str(solution)) > len(str(number2))):
                number1s = number1s + '  ' + ' ' * ((len(str(solution)) - 1) - len(str(number1))) + number1 + '    '
                number2s = number2s + operator + ' ' + ' ' * ((len(str(solution)) - 1) - len(str(number2))) + number2 + '    '
                solutions = solutions + ' ' + str(solution) + '    '
                equals = equals + '-' * (len(str(solution)) + 1) + '    '
            else:
                number1s = number1s + '  ' + ' ' * (len(str(solution)) - len(str(number1))) + number1 + '    '
                number2s = number2s + operator + ' ' + ' ' * (len(str(solution)) - len(str(number2))) + number2 + '    '
                solutions = solutions + '  ' + str(solution) + '    '
                equals = equals + '-' * (max(len(str(number1)), len(str(number2)),len(str(solution))) + 2) + '    '
        else:
            if (len(str(solution)) > len(str(number1))) and (len(str(solution)) > len(str(number2))):
                number1s = number1s + '  ' + ' ' * ((len(str(solution)) - 1) - len(str(number1))) + number1
                number2s = number2s + operator + ' ' + ' ' * ((len(str(solution)) - 1) - len(str(number2))) + number2
                solutions = solutions + ' ' + str(solution)
                equals = equals + '-' * (len(str(solution)) + 1)
            else:
                number1s = number1s + '  ' + ' ' * (len(str(solution)) - len(str(number1))) + number1
                number2s = number2s + operator + ' ' + ' ' * (len(str(solution)) - len(str(number2))) + number2
                solutions = solutions + '  ' + str(solution)
                equals = equals + '-' * (max(len(str(number1)), len(str(number2)),len(str(solution))) + 2)

        problemsDone += 1

    if solve == True:
        arranged_problems = number1s + '\n' + number2s + '\n' + equals + '\n' + solutions
    else:
        arranged_problems = number1s + '\n' + number2s + '\n' + equals
    return arranged_problems
