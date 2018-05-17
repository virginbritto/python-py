num = input("")
if num <= 1000:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"no")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"yes")
else:
   print(num,"no")
