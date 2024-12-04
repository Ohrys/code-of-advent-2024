def get_data() : 
    file = open("input.txt", "r")
    output = []
    for line in file :
        line = line.strip().split(" ")
        to_int(line)
        output.append(line)
    return output

def to_int(values):
    for i in range(len(values)) :
        values[i] = int(values[i])


def check_increase(levelLeft, levelRight) -> bool :
    return levelRight > levelLeft and (levelRight - levelLeft in range(1,4))

def check_decrease(levelLeft, levelRight) -> bool :
    return levelRight < levelLeft and (levelLeft - levelRight in range(1,4))

def skip_it(skip_index, list_to_iterate) :
    for index, item in enumerate(list_to_iterate):
        if index != skip_index:
            yield item


def part_one(data) : 
    safe_count = 0
    for report in data :
        check = check_increase if report[0] < report[-1] else check_decrease
        if all(check(level1,level2) for level1,level2 in zip(report,report[1:])):
            safe_count +=1

    return safe_count

def part_two(data):
    safe_count = 0
    for report in data :
        check = check_increase if report[0] < report[-1] else check_decrease
        if (all(check(level1, level2) for level1, level2 in zip(report,report[1:]))):
            safe_count +=1
            continue
        for skip_index in range(len(report)):
            skip_list = list(skip_it(skip_index, report))
            check = check_increase if skip_list[0] < skip_list[-1] else check_decrease
            if all(check(level1,level2) for level1, level2 in zip(skip_list,skip_list[1:])):
                safe_count +=1
                break
    
    return safe_count


def main() : 
    data = get_data()
    safePart1 = part_one(data)
    safePart2 = part_two(data)

    print(f'Part 1 : {safePart1}')
    print(f'Part 2 : {safePart2}')


if __name__ == "__main__" :
    main()