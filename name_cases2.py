profit = [
    [1000.00,2000.00,3000.00,1000.00],
    [2000.00,3000.00,2500.00,4000.00],
    [3000.00,4500.00,5000.00,6000.00],
]
year= [ "year 1","year 2","year 3"]
  

for yi in range(len(profit)):
  s =sum(profit[yi])
  avg=s/4
  profit[yi].append(avg)
  m=max(profit[yi])
  profit[yi].append(m)

 
for yi in range(len(profit)):  
  print(f"year{yi+1:3}",end="")
  for ci in range (len(profit[2])):
      
    print (f'{profit[yi][ci]:16.2f}',end="")
  print()    
   
 