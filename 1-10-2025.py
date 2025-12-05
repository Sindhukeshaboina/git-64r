# def addition(num1=0,num2=0,num3=0):
#     c = num1+num2+num3
#     if c==0:
#         return "no values passed"
#     else:
#         return c
    
# print(addition(10,20))
# print(addition(20))
# print(addition(1,2,3))
# print(addition())




# def details(name,age,salary):
#     text = f"Name: {name}, Age:{age}, Salary:{salary}"
#     return text
    
# print(details(12,2500,"Arun"))


# def addition(*args):
#     arguments = len(args)
#     if arguments == 0:
#         return "No values passed"
    
#     return f"sum of {arguments} values is {sum(args)}"

# print(addition(1,10,3,5,6))
# print(addition(1,10))
# print(addition())




# def fibonacci(num):
#     a,b=0,1
#     i=1
#     while i<=num:
#         print(a,end=" ")
#         # c=a+b
#         # a=b
#         # b=c
#         a,b=b,a+b
#         i+=1
# n = int(input("Enter series: "))
# fibonacci(n)





# def fibonacci(num):
#     res=""
#     a,b=0,1
#     while a<=num:
#         res=res+str(a)+" "
#         # c=a+b
#         # a=b
#         # b=c
#         a,b=b,a+b
#     return res
# n = int(input("Enter series: "))
# print(fibonacci(n))

#swapping of 2 nos
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# print (f"num1: {num1} and num2:{num2}")
# # c = num1
# # num1 = num2
# # num2 = c
# num1,num2 =num2,num1 # another logic 
# print (f"num1: {num1} and num2: {num2}")


# letter = input ("enter a letter :")
# print ((letter >= 'A'and letter <='Z') or (letter >= 'a' and letter <='z'))


# num1 = int (input ("enter a number : "))
# if num1 | 1==0:
#     print(f"{num1}is an odd")
# else:
#     print(f"{num1}is even")

# num = int (input ("enter a number :"))
# if num%2:
#     print("odd number")
#     print(f"{num}'s last digit is: {num%10}")
#     if num>=1000:
#         print ("is more than 3 digits number")
#     elif num>=100:
#         print("is 3 digit number")
#     elif num>=10:
#         print("is 2 digit number")
#     else:
#         print("is a 1 digit number")
# else:
#     print("even number")
#     print(f"{num}'s last digit is:{num%10}")


# num =[2,4,5,6,2,7,1,-9]
# i=0
# while (i<len(num)):
#     print(num[i])
#     i=i+1

# num = [2,3,44,13,7,3,3,8]
# for i in range (0, len(num)):
#     print(num[i])


#while loop example: 
# num=int(input("enter a number: "))
# i=1
# while i<=num:
#     print(i,end=" ")
#     i=i+1
# print()

# j=num
# while j>=1:
#     print(j,end=" ")
#     j-=1
# print()

# k=-1
# while k>=-(num):
#     print(k,end=" ")
#     k-=1
# print()

# m=-(num)
# while m<=-1:
#     print(m,end=" ")
#     m+=1
# print()