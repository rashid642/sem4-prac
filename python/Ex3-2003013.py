# 1
# def isPerfect(n):
#     sum1 = 0
#     for i in range(1, n):
#         if(n % i == 0):
#             sum1 = sum1 + i
#     if (sum1 == n):
#         print("The number is a Perfect number!")
#     else:
#         print("The number is not a Perfect number!")
# n = int(input("enter the number"))
# isPerfect(n);

# # 2

# def ispangram(str):
# 	alphabet = "abcdefghijklmnopqrstuvwxyz"
# 	for char in alphabet:
# 		if char not in str.lower():
# 			return False

# 	return True
	

# string = 'th quick brown fox jumps over the lazy dog'
# if(ispangram(string) == True):
# 	print("Yes")
# else:
# 	print("No")
	
	
# 4

# def factorial(n):
#     if n<=1:
#         return n;
#     return n*factorial(n-1);
    
# n = int(input("enter the number "));
# print(factorial(n));

# # 5
# def square(n):
#     def increaseBy4(a):
#         return a+4;
#     return increaseBy4(n*n);
# def cube(n):
#     def mulBy2(a):
#         return a*2;
#     return mulBy2(n*n*n);
        
# a = int(input("enter the number"));
# b = int(input("enter the 2nd number"));
# print(square(a));
# print(cube(b));

# def add(*argv):
#     print(argv)
#     sum = 0;
#     for i in argv:
#         sum += i;
#     return sum;
    
# def mul(*argv):
#     mul = 1;
#     for i in argv:
#         mul *= i;
#     return mul;
        

def add(*argv):
    print(argv)
    sum = 0;
    for i in argv:
        sum += i;
    return sum;
    
def mul(*argv):
    mul = 1;
    for i in argv:
        mul *= i;
    return mul;
ch = 'y';
while ch == 'y':
    n = int(input("enter the number of element:"));
    arr = [];
    for i in range(0, n):
        a = int(input("enter ele "));
        arr.append(a);
    print(arr);
    print("enter 1 for Addition\nenter 2 for multiplication");
    b = int(input());
    if b == 1:
        print("addition of numer is", add(*arr));
    else:
        print("multiplication of numbers is", mul(*arr));
    ch = input("do u want to continue: ")