numbers = [1,4,3,7,6,5,9,80,54,76]
for a in numbers:
    b=2
    k=0
    while b<a:
     if a%b==0:
      b=b+1
      k=k+1
     else: 
       b=b+1
    if k==0:
     print(a)
    