string = 'egbt wrg wrgehy'
list = string.split(' ')

max_len = 0
max_item = 0
for item in list:
    if len(item) > max_len:
        max_len = len(item)
        max_item = item
print(max_item)


max_len = 0
max_item = 0
for i in range(len(list)):
    if len(list[i]) > max_len:
        max_len = len(list[i])
        max_item = list[i]
print(max_item)


