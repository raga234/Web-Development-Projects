rows = int(input("Enter the number of rows: "))  

#Outer for loop to handle number of rows  
for i in range(1, rows+1):  
        for j in range(1, i-1):  
            print(j, end=" ")     
            rows += 1  
        for j in range(i-1,0,-1):  
            print(j, end=" ")     
             
        print()


rows = int(input("Enter the number of rows: "))  
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print((i * 2-1), end=" ")
        j += 1
    i +=  1

    print()

rows = int(input("Enter the number of rows: "))  
lastnum = 2 * rows
even = lastnum

#Outer for loop to handle number of rows  
for i in range(1, rows+1):  
  even = lastnum
  for j in range(i): 
    print(even, end=" ")     
    even -= 2  
  print()


rows = int(input("Enter the number of rows: "))  
#Outer for loop to handle number of rows  
for i in range(0, rows):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop 
    for j in range(0, i+1):  
      print(i*j, end=" ")     

    #End line after each row        
    print()


rows = int(input("Enter the number of rows: "))  
m = (2*rows)-2

#Outer for loop to handle number of rows  
for i in range(0, rows):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(0, m):  
            print(end=" ")
        #decrementing m after each loop
        m -= 1 
        for j in range(0, i+1):  
            #printing triangle pyramid using asterik
            print("*",end=" ")              
  
        #End line after each row  
        print()


rows = int(input("Enter the number of rows: "))  
m = (2*rows)-2

#Outer for loop to handle number of rows  
for i in range(rows-1,-1,-1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(m,0,-1):  
            print(end=" ")
        #incrementing m after each loop
        m += 1 
        for j in range(0, i+1):  
            #printing triangle pyramid using asterik
            print("*",end=" ")              
  
        #End line after each row  
        print()


rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()



rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()