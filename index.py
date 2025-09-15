for i in range(10): 
    if i % 3 == 0: 
        print(i, end=" ")


x = 0 
y = 10 
if x != 0 or y / x > 1: 
    print("Pass") 
else: 
    print("Fail")

n = 5 
sum = 0 
while n > 0: 
    if n % 2 == 0: 
        sum += n 
    n -= 1 
print(sum)

 
x = 12 
if x % 3 == 0 and x % 4 == 0: 
    print("Divisible by 3 and 4") 
elif x % 3 == 0: 
    print("Only by 3") 
else: 
    print("Not divisible")

 
x = 4 
y = 7 
 
if x < y: 
    if x + y > 10: 
        print("A") 
    else: 
        print("B") 
else: 
    print("C")

a = 7 
b = 3 
if a % b == 1: 
    if a > b * 2: 
        print("X") 
    else: 
        print("Y") 
else: 
    print("Z") 

 
x = 10 
if x < 5: 
    print("Low") 
elif x < 15 and x % 2 == 0: 
    print("Medium") 
else: 
    print("High")

 
for i in range(10, 2, -3): 
    print(i, end=" ") 

a = True 
b = False 
if a and not b: 
    print("1") 
elif not a and b: 
    print("2") 
else: 
    print("3") 

x = 10 
while x > 5: 
    x -= 2 
print(x) 

n = int(input("Enter a number: "))
if n <= 1:
    print(False)
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(False)
            break
    else:
        print(True)


n = int(input("Enter a number: "))
even = []
odd = []
for i in range(1, n + 1):
    if i % 2 == 0:
        even.append(str(i))
    else:
        odd.append(str(i))
print("Even numbers:", " ".join(even))
print("Odd numbers:", " ".join(odd))
