# Using print
print("Twinkle, twinkle, little star,\n\t\"How I wonder what you are!\"\n\t\tUp above the world so high, \n\t\tLike a diamond in the sky, \nTwinkle, ' twinkle ', little star, \n\tHow I wonder what you are");

print("\n")

name = "Rashid";
print(f"My name is {name}");
print("Let's learn {} and cuurently i am a {}".format("python","beginner"));
print("trying to {str1} {str2}".format(str1="string", str2="format"));
print("Year = {0}".format(2021));
print("Current Temp = {0: .2f}".format(29.25678));
# yr = 2021;
# print("hey, %s, it's %d"{%name,%yr})
print("\n")

print("Enter the year: ")
year = int(input());
if year % 4 == 0:
    print("It's a leap year");
else:
    print("It's not a leap year");

print("\n");

for i in range(0, 9):
    for j in range(0, 9):
        for k in range(0, 9):
            temp = pow(i, 3) + pow(j, 3) + pow(k, 3);
            if temp == (i*100 + j*10 + k) :
                print(temp);

print("\nEnter n");
n = int(input());
prev2 = 0;
prev1 = 1;
print(prev2);
print(prev1);
for i in range(0, n+1):
    print(prev1+prev2);
    temp = prev1;
    prev1 = prev1 + prev2;
    prev2 = temp;

print("\n")
count = 0
for i in 'ABCDEF':
    for j in range(0, count+1):
        print (i, end='');
    print ("\n"); 
    count = count + 1;

print("\nEnter n");
n = int(input());
for i in range(0,n):
    for j in range(0,i):
        print(" ",end='');
    for j in range(i, n):
        print("*", end='');
    print("\n");

print("\nEnter n");
n = int(input());
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='');
    temp = 1;
    for j in range(0, i+1):
        print(temp, end='');
        temp = temp + 1;
    temp = temp - 1;
    for j in range(0, i):
        temp = temp - 1;
        print(temp, end='');
    print("\n");

print("\nEnter n");
n = int(input());
for i in range(0, n):
    for j in range(0,n-i):
        print(" ",end='');
    for j in range(0, i+1):
        print("* ",end='');
    print("\n");