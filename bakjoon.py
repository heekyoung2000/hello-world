n,k=map(int, input().split())
coin=[]
for i in range(n):
    coin.append(int(input()))
coin.sort()
count=0

for i in coin:
    count=k//i+count
    k=k%i
print(count)