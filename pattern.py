print('1\n'"1 2\n""1 2 3\n""1 2 3 4\n""1 2 3\n""1 2\n""1\n")

  
for i in range(1,5):
    for j in range(0,i):
        print(i)
        
        
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
    
    
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")  
    print(" ")    
