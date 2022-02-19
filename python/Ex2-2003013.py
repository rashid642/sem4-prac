# from array import *
# arr = array('i',[]);
# print("enter the size of array");
# n = int(input());
# for i in range(n):
#     a = int(input());
#     arr.append(a);
# print(arr);
# arr.append(7);

# print(arr[::-1]);

# print(arr[0])
# x = len(arr)
# print("size of one element of array=",arr.itemsize);

# arr1 = [100, 200];
# arr2 = [101, 20];
# # arr1.append(arr2) # Output: [1, 2, 3, [10, 20]]
# arr1.extend(arr2) #Output[100, 200, 101, 20]
# print(arr1);
# a = int(input("Enter the element you want to delete:"));

# try:
#     ind = arr1.index(a);
#     arr1.remove(a);
#     print("Removed!!");
# except:
#     print("element not found")
# print(arr1);

# a = int(input("Enter the element you want to Insert:"));
# b = int(input("Enter the index you want to Insert:"));
# try:
#     arr1.insert(b, a);
#     print("inserted");
# except:
#     print("invalid index");

# print(arr1);




# lst = [None] * 1000
# for i in range(2,100):
#     temp=i
#     j = 2*i;
#     if lst[i] == None:
#         while j<1000:
#             lst[j] = 1;
#             j = j + temp
# for i in range(1000):
#     if lst[i] == None:
#         print(f"{i} ",end='')
# lst[2] = 1;
# arr = [1, 2, 3 ,4, 5, 9,12 ,10,16,17,20];
# for i in arr:
#     if lst[i] == None:
#         arr.remove(i);

# print(arr);


# s = "apple a day";
# flag = False;
# ans = "";
# for ch in range(0, len(s)):
#     if ((s[ch] == "a") and (flag == True)):
#         ans = ans + "@"
#     elif ((s[ch] == "a") and (flag == False)):
#         ans = ans + s[ch];
#         flag = True;
#     else:
#         ans = ans + s[ch];

# print(ans);


s = input("Enter a string:");
print(sorted(s))

rev = s[::-1];
if s == rev:
    print("yes it is palindrome");
else:
    print("its not a palindrome")

