list = [0,1,2,3,4,5,6,6]

def first(list):
    for x in list: 
        if list.count(x) > 1:
            list.remove(x)
    return list

def second(list):
    for i in range(len(list)): 
        if list.count(list[i]) > 1:
            list.remove(list[i])
    return list
    
print(first(list))
print(second(list))