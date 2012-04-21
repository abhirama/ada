fh = open('HashInt.txt')

nos = {}
for line in fh.readlines():
    no = int(line.strip())
    if no in nos:
        nos[no] = nos[no] + 1
    else:
        nos[no] = 1

targetSums = [231552, 234756, 596873, 648219, 726312, 981237, 988331, 1277361, 1283379]

result = []

for index, targetSum in enumerate(targetSums):
    for no in nos:
        if no >= targetSum:
            continue
        else:
            dif = targetSum - no

            if dif == no:
                if nos[dif] > 1:
                    result.append(1)
                    break
            else:   
               if dif in nos:
                   result.append(1)
                   break


    if len(result) - 1 == index:
        pass
    else:
        result.append(0)
        

import pprint
pprint.pprint(result)
