import random
a = random.randint(1,10)
b=int(input("Отгадайте число:"))
if b==a:
  print("Молодец!")
else:
  b=int(input("Попробуй ещё раз)"))
  if b==a:
    print("Молодец!")
  else:
     b=int(input("Попробуй ещё раз)"))
     if b==a:
      print("Молодец!")
     else:
      print("Ты не угадал, число было такое:",a)


  