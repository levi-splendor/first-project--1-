num=int(input("enter number"))
i=int(input("enter number"))
# # for i<=12 
# def multiplicationTimetable(num, i):
#      product = num*i  
#      while i<=12:
#          print(f"{ num}x{i}={product} ")
#          i=i+1
#          product=num*i
# multiplicationTimetable(num, i )

def multiplication_table(num):
    for i in range(1,11):
     product = num*i
     print(f"{num}x{i}={product}")
multiplication_table(num)

     
