list1=[1, 2, 3] 
list2=[11, 22, 33]
list3 =[]
min_len = min(len(list1),len(list2))
for i in range(min_len):
    list3.append(list1[i])
    list3.append(list2[i])
list3.extend(list1[min_len:])
list3.extend(list1[min_len:])
print(list3)

