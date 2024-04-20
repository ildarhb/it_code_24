list_1 = [0,1,3,4,2,3,0]
list_2 = [4,5,0,2,6,7,7]

merge = list_1 + list_2
merge.sort()

print(list(set(merge)))
