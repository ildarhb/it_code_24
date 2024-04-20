n = input()

sum_1 = 0
for i in range(n):
    sum_1 += i+1

sum_2 = 0
j = 1
while j <= n:
    sum_2 += j
    j += 1

print(sum_1)
print(sum_2)