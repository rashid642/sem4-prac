print("at start")
# print(3+2/3)
# name = "Rashid"
# message = "Good Morning"
# print(name+" "+message)
# print(type(name))
# ch = True
# print(type(ch))
# print(ch)
# ch2 = int(ch)
# ch3 = int(52.55)
# ch4 = float(52)
# print(ch2)
# print(ch3)
# print(ch4)
# print("Enter name: ");
# name = input();
# print("Enter two number: ");
# num1 = input();
# num2 = input();
# num3 = int(num1) + int(num2);
# print(name +" sum: ",num3, " after sum");
# print(len(name));

# name = "Rashid Aziz Aziz aziz"
# print(name[0:4]);
# # print(name[0:4:skipvalue]);
# print(name.endswith("id"));
# print(name.count("Aziz"));
# print(name.count("aziz"));
# print(name.upper());
# print(name.find("ziz"));

# l1 =["Rashid","Muskan","Yasin","Rehan"]
# print(l1);
# l1.sort();
# print(l1);
# l1.reverse();
# print(l1);
# print(l1[1: 2]);
# print(l1[2]);

# dic = {"name":"Rashid", "age":20, "colleges":{"A":"TSEC", "B":"RV"}};
# print(dic["age"], dic["name"]);
# print(dic["colleges"]["B"]);

# s = set();
# s.add("Rashid");
# s.add("Muskan");
# s.add("Rashid");
# s.add("Rehan");
# print(s);
# s2 = {"Rashid","Muskan"};
# print(s.isdisjoint(s2));
# print(s.union(s2));

# var1 = 5;
# var2 = 6;
# if var1 > var2:
#     print("greater");
# elif var1 == var2:
#     print("equal");
# else:
#     print("lesser")

# dic = {"name":"Rashid", "age":20, "colleges":{"A":"TSEC", "B":"RV"}};
# for x,y in dic.items():
#     print(x,y);

# items = {1, 2, 3, 4, 5};
# for item in items:
#     if item >= 4:
#         print(item)

# for x in range(2, 6):
#   print(x)

# def adding(a, b):
#     """add the two number"""
#     return a+b;

# print(adding(7,8));
# print(adding.__doc__);

# print("Enter the first number");
# num1 = input();
# print("Enter the second number");
# num2 = input();
# try:
#     print("the sum is ", int(num1)+int(num2));
# except Exception as e:
#     print(e);

# print("After try except")

print("Enter the number");
n = int(input());
for x in range (0, n+1):
    for y in range (0, x):
        print("*", end="");
    print();
# python atstart.py  --> to run