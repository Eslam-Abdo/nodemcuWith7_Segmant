i = 5
flag = 0
for y in range (10):
    if (i==4) and (flag != 1):
      flag = 1
      print(flag)
    elif (i == 0 )and (flag != 2):
      flag = 2
      print(flag)
      
    elif (i==5) and (flag != 3):
      flag = 3
      i -=1
      print(flag)
    elif (flag != 4) : 
      flag = 4
