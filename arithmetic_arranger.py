def arithmetic_solver(first_operand, second_operand, operation):
  first_operand = int(first_operand)
  second_operand = int(second_operand)
  if operation == '+':
    return first_operand + second_operand
  elif operation == '-':
    return first_operand - second_operand
  else:
    return print('Arithmetic Solver Error')

def arithmetic_arranger(problems, solved = False):
  parser = []
  problem_count = 0
  for problem in problems:
    splitted = problem.split()
    if problem_count > 4:
     return "Error: Too many problems."
    elif splitted[1] != "+" and splitted[1] != "-":
      return "Error: Operator must be '+' or '-'."
    elif splitted[0].isdigit() == False or splitted[2].isdigit() == False:
      return "Error: Numbers must only contain digits."
    elif len(splitted[0]) > 4 or len(splitted[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    else:
      parser.append(splitted)
      problem_count += 1

  first_line = ""
  second_line = ""
  third_line = ""
  space_diff = 0

  for items in parser:
    space_diff = len(items[0]) - len(items[2])
    if space_diff <= 0:
     first_line += (abs(space_diff)+2)*" " + items[0] + 4*" "
     second_line += items[1] + " " + items[2] + 4*" "
    else:
     first_line += 2*" " + items[0] + 4*" "
     second_line += items[1] + " " + abs(space_diff)*" " + items[2] + 4*" "
    third_line += (max(len(items[0]), len(items[2])) + 2)*"-" + 4*" "

  arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()
  if solved == True:
    arranged_problems += "\n"
    for problems in parser:
      solution = str(arithmetic_solver(problems[0], problems[2], problems[1]))
      if len(solution) >= 4:
        arranged_problems += " " + solution + 4*" "
      else:
        arranged_problems += 2*" " + solution + 4*" "
        
  

  return arranged_problems.rstrip()