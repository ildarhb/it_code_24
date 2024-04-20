list_1 = [0,1,2,3,4,5,6]
list_2 = [0,1,1,2,3,4,5,6]

print(len(list_1) == len(list(set(list_1))))
print(len(list_2) == len(list(set(list_2))))