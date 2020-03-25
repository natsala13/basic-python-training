# Page 116

def input_path():
    """Gets Path input from user, Checks its validity"""
    import os
    path_input = input("Please enter folder path of files:")
    if os.path.isdir(path_input):
        return path_input
    else:
        print("Directory not found.")
        return -1


def input_file_names(path):
    """Takes file name as input from user , Checks if files exist , returns list with path to files"""
    import os
    input_file_name1 = input("Please enter exercise file name:")
    input_file_path1 = path + "\\" + input_file_name1
    if not os.path.exists(input_file_path1):
        print("File not found.")
        return -1
    input_file_name2 = input("Please enter solution file name:")
    input_file_path2 = path + "\\" + input_file_name2
    if not os.path.exists(input_file_path2):
        print("File not found.")
        return -1
    if input_file_name1 == input_file_name2:
        print("File name are identical. Please try again")
        return -1
    return [input_file_path1, input_file_path2]


def solve_excersice(exr):
    """Checks That excercise is in the right format, if so , solves it"""
    """Correct format is 'a + b' whole numbers only """
    num1_str = ''
    num2_str = ''
    # Checks first number and stores it in num2_str, stops storing for space
    k = 0
    for k, i in enumerate(exr):
        if i.isdigit():
            num1_str = num1_str + i
        elif i == ' ':
            k += 1
            break
        else:
            return 'err'
    # Checks action and stores it
    action = exr[k]
    k += 2
    if action not in '+-*/':
        return 'err'
    # Checks second number and stores it in num2_str
    for i in exr[k:]:
        if i.isdigit():
            num2_str = num2_str + i
        elif i == '' or i == '\n':
            break
        else:
            return 'err'
    # Calculates result and returns
    if action == '+':
        return int(int(num1_str) + int(num2_str))
    if action == '-':
        return int(int(num1_str) - int(num2_str))
    if action == '*':
        return int(int(num1_str) * int(num2_str))
    if action == '/':
        if int(num2_str) == 0:
            return 'err'
        return float(int(num1_str) / int(num2_str))


def string_to_write(exr):
    """Solves exercise and returns string exr = result """
    result = solve_excersice(exr)
    if result == 'err':
        return 'There has been an error \n'
    # If exr has a new line at the end , remove it
    elif exr[-1] == '\n':
        return exr[:-1] + ' = ' + str(result) + '\n'
    else:
        return exr + ' = ' + str(result) + '\n'


def solution_file_write(file_exr_path, file_sol_path):
    """reads from exercise file and writes to solution file """
    exr_file = open(file_exr_path, 'r')
    sol_file = open(file_sol_path, 'w')
    for exr_line in exr_file:
        sol_output = string_to_write(exr_line)
        sol_file.write(sol_output)
    exr_file.close()
    sol_file.close()
    return 0

def main():
    path_folder = input_path()
    if path_folder == -1:
        return -1
    files_path = input_file_names(path_folder)
    if files_path == -1:
        return -1
    file_exr_path = files_path[0]
    file_sol_path = files_path[1]
    solution_file_write(file_exr_path, file_sol_path)
    return 0

if __name__ == '__main__':
    main()