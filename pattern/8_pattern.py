rows = int(input("Enter the number of rows: "))  

#Outer for loop to handle number of rows  
for i in range(1, rows+1):  
    num = 1
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
    for j in range(rows,0,-1):  
      if j > i:
        print(" ", end=" ") 
      else:
        print(num, end=" ")
        num += 1
  
    #End line after each row  
    print()