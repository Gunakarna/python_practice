list = [1, 2, 3, 4, 5, 6]
for i in range (1, 6):
 	 list[ i-1] = list[ i ]
print(list)
for j in range(0, 6):
 	 print(list[j], end=" ")
