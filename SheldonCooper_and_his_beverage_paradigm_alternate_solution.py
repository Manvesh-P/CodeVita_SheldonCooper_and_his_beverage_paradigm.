
list1 = []
list2 = []
list3 = []
list4 = []

flag = 0

N = int(input("Enter the number of bottles: "))

for i in range(0, N):
    list1.append(int(input()))
    
X = int(input("Enter the intended quantity:"))

for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        for k in range(j+1, len(list1)):
            
            list2.append(list1[i])
            list2.append(list1[j])
            list2.append(list1[k])
            list3.append(list2)
            list2 = []
            
            
for i in range(0, len(list3)):
    list4.append(sum(list3[i]))
    
for i in range(0, len(list4)):
    if list4[i] == X:
        flag = 1
        
        

if flag == 1:
    print("True")
else:
    print("False")
    
    
