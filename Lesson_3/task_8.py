list = [0,1,2,3,4,5,6,6]
dict = {}
for item in list:
    if item in dict:
        print(True)
        break
    dict[item] = 1
else:
    print(False)