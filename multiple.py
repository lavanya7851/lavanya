def multiple(x, y): 
  
    # inserts all elements from y to  
    # (x * y)+1 incremented by y. 
    a = range(y, (x * y)+1, y) 
      
    print(*a) 
  
# driver code  
x = 5
y = 7
multiple(x, y) 
