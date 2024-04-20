string = 'asdsa'

for i in range(int(len(string) / 2)):
    if string[i] != string[-i-1]:
        print(False)
        break
else:
    print(True)