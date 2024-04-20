date_dict = {'year': 2024, 'month': 4, 'day': 14}
values = list(date_dict.values())
values = list(map(str, values))
print(values[0] + '-' + values[1] + '-' + values[2])