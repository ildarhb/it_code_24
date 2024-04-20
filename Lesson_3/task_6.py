number = 123.46
string = str(number)

count = 0
for i in range(len(string)):
    if string[i].isdigit():
        count += 1
print(count)

count = 0
for item in string:
    if item.isdigit():
        count += 1
print(count)