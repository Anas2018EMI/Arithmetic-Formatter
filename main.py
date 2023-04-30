def arithmetic_arranger(arith_prob: list, calculate=False):
    if len(arith_prob) > 5:
        return print("Error: Too many problems.")

    operands1_list = ""
    operands2_list = ""
    operations_lines = ""
    results = ""
    for prob in arith_prob:
        elements = prob.split()

        if len(elements[0]) > 4 or len(elements[2]) > 4:
            return print("Error: Numbers cannot be more than four digits.")

        if '+' in elements or '-' in elements:
            try:
                operand1 = int(elements[0])
                operand2 = int(elements[2])
            except:
                return print('Error: Numbers must only contain digits.')
            length_diff = abs(len(elements[0]) - len(elements[2]))
            if len(elements[0]) >= len(elements[2]):
                elements[2] = ' '*length_diff + elements[2]
                # print(f"elements[2] = '{elements[2] }'")
            else:
                elements[0] = ' '*length_diff + elements[0]
                # print(f"elements[0] = '{elements[0] }' ")

            elements[0] = '  ' + elements[0]
            elements[2] = elements[1] + ' ' + elements[2]
            operands1_list += elements[0]+' '*4
            operands2_list += elements[2]+' '*4
            operations_lines += '-'*len(elements[2])+' '*4

            # operation = elements[0]+'\n'+elements[2]+'\n'+'-'*len(elements[2])

            if calculate:
                if elements[1] == '+':
                    result = operand1+operand2
                elif elements[1] == '-':
                    result = operand1-operand2
                # print(f"result={result}")
                # operation += '\n' + ' ' * \
                # abs(len(elements[2])-len(f"{result}")) + f"{result}"
                results += ' ' * \
                    abs(len(elements[2])-len(f"{result}")) + f"{result}"+' '*4
            # print(operation)

        else:
            return print("Error: Operator must be '+' or '-'.")
    operands1_list = operands1_list[0:len(operands1_list)-4]
    operands2_list = operands2_list[0:len(operands2_list)-4]
    operations_lines = operations_lines[0:len(operations_lines)-4]
    arranged_problems = operands1_list+'\n' + \
        operands2_list+'\n' + operations_lines
    if calculate:
        results = results[0:len(results)-4]
        arranged_problems += '\n' + results
    print(operands1_list)
    print(operands2_list)
    print(operations_lines)
    print("//////////////////////////////")
    print(arranged_problems)


# , '575555 + 25'
list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
l1 = ['3801 - 2', '123 + 49']
arithmetic_arranger(l1, True)
