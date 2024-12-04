import re

def partOne(mul_list):
    output = []
    for mul in mul_list :
        number_one = mul[4:-1].split(",")[0]
        number_two = mul[4:-1].split(",")[1]
        number_one = int(number_one)
        number_two = int(number_two)
        multiplication = number_one * number_two
        output.append(multiplication)

    output = sum(output)
    return output

def partTwo(mul_list):
    splitted_list = []
    split_value = ['do()',"don't()"]
    do_it = True

    for mul in mul_list:
        if mul == split_value[0] : 
            do_it = True
            continue
        elif mul == split_value[1] or not do_it :
            do_it = False
            continue
        elif do_it :
            splitted_list.append(mul)

    output = partOne(splitted_list)
    return output

def main() :
    file = open("input.txt","r")
    input = file.read()
    mul_list = re.findall("mul[(][0-9]*,[0-9]*[)]|do[(][)]|don't[(][)]", input)
    print(mul_list)
    sum = partOne(mul_list)
    sum = partTwo(mul_list)


    print(f'Part 1: {sum}')
    print(f'Part 2: {sum}')

if __name__ == "__main__" :
    main()