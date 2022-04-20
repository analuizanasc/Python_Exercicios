num = 16
i = 1
res = 0

while i <= num:
   if (num % i == 0):
        res = res + 1
   break
   i = i + 1
print(res)