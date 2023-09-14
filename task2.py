a = int(input("Введите число:"))
b=2
k=0
while b<a:
    if a%b==0:
     b=b+1
     k=k+1
    else: 
       b=b+1
if k==0:
   print("Число простое")
elif k>0:
   print("Число не простое")