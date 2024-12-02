def part1(listA, listB):
    diff = 0
    while len(listA) > 0 : 
        valueA = listA.pop(0)
        valueB = listB.pop(0)
        
        if valueB < valueA :
            valueA, valueB = valueB, valueA
        
        diff += valueB - valueA

    print(diff)

def part2(listA, listB):
    similarity = 0
    for valueA in listA : 
        for valueB in listB :
            if valueA == valueB :
                # we need to multiply, so it's valueA time each encounters (so a sum of valueA for this iteration of loop)
                similarity += valueA

    print(similarity)

def main() :
    listA = []
    listB = []
    file = open("input.txt","r")

    for line in file :
        values = line.strip().split("   ")
        values[0] = int(values[0])
        values[1] = int(values[1])

        listA.append(values[0])
        listB.append(values[1])

    # We sort to have the lowest numbers first.
    listA.sort()
    listB.sort()


    #part1(listA, listB)
    #part2(listA, listB)
             



if __name__ == "__main__" :
    main()