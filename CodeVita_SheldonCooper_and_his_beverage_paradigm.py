from itertools import combinations

list1 = []
list2 = []

flag = 0

N = int(input("Enter the number of bottles:"))

for i in range(0, N):
    list1.append(int(input()))
    
X = int(input("Enter the quantity they intend to consume:"))

combi = list(combinations(list1, 3))

for j in range(0, len(combi)):
    list2.append(sum(combi[j]))
    
print(list1)
print(combi)
print(list2)

for i in range(0, len(list2)):
    if list2[i] == X:
        flag = 1
        
        
if flag == 1:
    print("True")
else:
    print("False")
