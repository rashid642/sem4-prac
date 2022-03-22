# ch = 'y'
# item = []
# while ch == 'y':
#     print("enter number of elements :");
#     n = int(input());
#     size = n
#     while n > 0:
#         a = int(input());
#         item.append(a);
#         n = n -1
    # print(item);
    # itemOdd = []
    # itemEven = []
    # for i in range(0, size):
    #     if item[i] % 2 == 0:
    #         itemEven.append(item[i])
    #     else:
    #         itemOdd.append(item[i])
    # print(itemEven)
    # print(itemOdd)
    # item2 = [];
    # print("enter number of elements for list 2 :");
    # n = int(input());
    # size2 = n
    # while n > 0:
    #     a = int(input());
    #     item2.append(a);
    #     n = n -1
    # print(item2)
    # item.extend(item2)
    # print(item)
    # item.sort()
    # print(item)
    # a = int(input("enter the elemt you want to update: "))
    # item[0] = a;
    # print(item)
    # ch = input("do you want to continue: ");

# ch = 'y'
# student = []
# while ch == 'y':
#     n = int(input("enter the number of students :"))
#     for i in range(0, n):
#         name = input("enter name of student: ");
#         rn = int(input("enter roll number of student: "));
#         marks = int(input("enter marks of student: "));
#         tup = (name, rn, marks)
#         student.append(tup)

#     print(student)
#     name = input("enter the name of student you want to search :");
#     for i in range(0, n):
#         if student[i][0] == name:
#             print(student[i]);
#     ch = input("do you want to continue: ");

# n1 = int(input("enter the size of set1: "))
# set1 = set()
# print(type(set1))
# for i in range(0, n1):
#     a = int(input())
#     set1.add(a);
# n2 = int(input("enter the size of set2: "))
# set2 = set()
# for i in range(0, n2):
#     a = int(input())
#     set2.add(a);

# print(set1, set2)
# print("union of two set", set1.union(set2));
# print("intersection of two set", set1.intersection(set2));
# print("diffrence of two set", set1.difference(set2))
# print("set symmetric diffrence of two set", set1.symmetric_difference(set2))

n = int(input("enter the number of element in dict : "))
dic = {}
for i in range(0, n):
    a = int(input("enter key :"))
    b = input("enter value :")
    dic[a] = b

print(dic)
# dict1 = OrderedDict(sorted(dic.items()))
# print(dict1)


n = int(input("enter the number of element in dict2 : "))
dic2 = {}
for i in range(0, n):
    a = int(input("enter key :"))
    b = input("enter value :")
    dic2[a] = b

dic.update(dic2)
print(dic)

