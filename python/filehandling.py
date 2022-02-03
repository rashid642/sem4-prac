print("at start")
f = open("testing1.txt","r");
# print(f.read())
print(f.readline())
print(f.readline())

f.close();

# f = open("testing2.txt","w");
# f.write("inside testing 2.txt")
# f.close();
f = open("testing2.txt","a");
a=f.write("inside testing 2.txt appending\n")
print(a);
f.close();
