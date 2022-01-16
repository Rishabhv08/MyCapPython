lists=[]
n=int(input("Enter Number of Elements : "))
for i in range(0,n) :
    ele=int(input())
    lists.append(ele)

for i in range(0,n):
    if lists[i]>0:
        print(lists[i])
