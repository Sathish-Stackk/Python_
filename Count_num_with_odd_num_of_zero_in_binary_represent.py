n = int(input())
count = 0
for i in range(1,n+1):
  b = bin(i)[2:]
  if zeros % 2==1:
     count +=1
print(count)
