def fibo(n):
     if n<=1:
          return n
     else:
          fibo(n-1)+fibo(n-2)
num=int(input("enter the number"))
if num<0:
     print("factorial of negative number is ")
if num==0:
     print("1")
if num>0:
     print(fibo(num))
     
