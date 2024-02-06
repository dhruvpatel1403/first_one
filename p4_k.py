# x=input("Enter string : ")
# n=int(input("Enter value : "))
# y=x.split()
# z=[]
# for i in y:
#     if i.__len__() > n:
#         z.append(i)
# print(z)
# l = [1, [2, [3, 4]], 5]
# l[1].append(8)
# print(l)
# l.extend(["a", "v", "a"])
# print(l)

# Ask user to enter the marks for each student, store them in a list and print the second lowest mark.
# x = int(input("How many marks do you wont to enter  : "))
# list = []
# for i in range(0, x):
#     val = int(input("Enter the value  : "))
#     list.append(val)
# list.sort()
# list2 = []
# for i in list:
#     if i in list2:
#         pass
#     else:
#         list2.append(i)
# try:
#     print(list2[1])
# except:
#     print(0)

# Write a program that accepts a sentence and calculate the number of letters and digits.
# x = input("Enter the string : ")
# l = 0
# j = 0
# for i in x:
#     if i.isalpha():
#         l = l + 1
#     elif i.isdigit():
#         j = j + 1
#     else:
#         pass
# print(f"letter : {l}\ndigit : {j}")

# Flatten list
# l = [1, [2, 3], [4, 5, 6]]
# f = []
# for i in l:
#     if type(i) is list:
#         for j in i:
#             f.append(j)
#     else:
#         f.append(i)
# print(f)

# left shift in list
# l = [1, 2, 3]
# y = l.pop(0)
# l.append(y)
# print(l)

# goodbad string
# x = input("Enter the string : ")
# cnot = x.find("not")
# cbad = x.find("bad")
# if cnot < cbad and cnot >= 0 and cbad >= 0:
#     x = x.replace(x[cnot:cbad+3], "good")
# else:
#     pass
# print(x)

# sum but not 13
# x = [13, 2, 3, 4, 13]
# sum = 0
# i = 0
# while i <= len(x):
#     if x[i] == 13:
#         i = i+1
#     else:
#         sum = sum+x[i]
#     i = i+1
# print(sum)

# sum of missing number
# l = [11, 12, 15, 16]
# sum = 0
# max = max(l)
# min = min(l)
# l.sort()
# i = min
# for i in range(min, max+1):
#     if i in l:
#         pass
#     else:
#         sum = sum+i
# print(sum)

# valid pin or not
# x = input("Enter the pin : ")
# def valid(p):
#     if len(p) == 4 or len(p) == 6:
#         if p.isdigit():
#             return True
#         else:
#             return False
#     else:
#         return False
# print(valid(x))

# smilly string :):(
# def num(s):
#     a = s.count(":)")
#     b = s.count("(:")
#     c = s.count(":(")
#     d = s.count("):")
#     sum = a+b-c-d
#     return(sum)
# x = input("Enter the string : ")
# print(num(x))

# return repeated word
# def first(s):
#     l = ""
#     for i in s:
#         if i in l:
#             return(i)
#         else:
#             l = l+i
#     else:
#         return(-1)
# print(first("Gandlf"))
# count = 0
# f = open("C:\\Users\\DELL\\Desktop\\ans.txt", "r")
# x = []
# for line in f:
#     y = line.split(" ")
#     for i in y:
#         if i not in x:
#             x.append(i)
# print(len(x))
# dict = {}
# for line in f:
#     y = line.split(" ")
#     for i in y:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] = dict[i]+1
# for key in dict.keys():
#     print(key, " : ", dict[key])

# s = "efgh"
# # t = "efg"
# def find(s, t):
#     for i in t:
#         if i not in s:
#             return i
#     else:
#         for i in s:
#             if i not in t:
#                 return i
# print(find(s, t))

# j = "p.one.two"
# def st(s):
#     if "#" in s:
#         x = s.split("#")
#         s1 = str(x[0])
#         y = s1.split(".")
#         print("<p class : ", y[1], " ", y[2], " id : ", x[1], "><\p>")
#     else:
#         y = s.split(".")
#         print("<p class : ", y[1], " ", y[2], "><\p>")
# st(j)

# x = int(input("Enter the number : "))
# def a(n):
#     sn = str(n)
#     c = 1
#     sum = 0
#     for i in sn:
#         sum = sum+int(i)**c
#         c = c+1
#     if sum == n:
#         return True
#     else:
#         return False
# print(a(x))

# l = ["a", "c", "d", "e"]
# s = "abc"
# def remove(a, b):
#     for i in a:
#         if i in b:
#             a.remove(i)
#     return(a)
# print(remove(l, s))
# print([(a, b) for a in range(3) for b in range(a)])
# a = [1, "e", []]
# b = a[:]
# a.append("v")
# b.append("a")
# print(a)
# print(b)
# print("abbzxyzxzxabb".count("abb", -10, -1))
# d = {"g": 1, "m": 2}
# d2 = {"m": 3, "y": 3}
# d.update(d2)
# for key, values in d.items():
#     print(key, values)
# def inc(l, i):
#     j = 0
#     while j < len(l):
#         l[j] = l[j]+i
#         j = j+1
# v = [1, 2, 3]
# print(inc(v, 2))
# print(v)
# val = [[3, 4, 5, 1], [33, 6, 1, 2]]
# v = val[0][0]
# for row in range(0, len(val)):
#     for col in range(0, len(val[row])):
#         if v < val[row][col]:
#             v = val[row][col]
# print(v)

# def per(n):
#     l = []
#     for i in range(1, n):
#         if n % i == 0:
#             l.append(i)
#     if sum(l) == n:
#         print("perfect", l)
# per(6)
# l1 = [1, 2, 3, 4]
# l2 = l1
# l2.append(5)
# print(l1, l2)
# l = [[0]*4 for i in range(2)]
# print(l)
# a = [1, 2, 3, 4, 5]
# for a[-1] in a:
#     print(a[-1])
# l = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# print(l[-1][0][0])
# from collections import deque
# queue = deque([1, 2, 3, 4, 5])
# val = queue.popleft()
# print(val) 1
# val = queue.pop()
# print(val) 5
# l = [1, 2, 3]
# l.append(4, 5)
# print(l)error
# f = [lambda x:x=10]
# print(f[10])error
# def prime(n):
#     flag = False
#     for i in range(2, n):
#         if n % i == 0:
#             flag = True
#     if flag == False:
#         return(True)
#     else:
#         return(False)
# x = int(input("Enter the range value"))
# li = [i for i in range(2, x+1)]
# plist = list(filter(prime, li))
# print(plist)
# st = "abcasAB1234"
# d = 0
# s = 0
# c = 0
# for i in st:
#     if i.isdigit() == True:
#         d = d+1
#     if i.islower() == True:
#         s = s+1
#     if i.isupper() == True:
#         c = c+1
# print(f"digit is : {d}\nsmall latters : {s}\ncapital latters : {c}")

# l = [1, 2, 3, 0, -1, -2, -3, 4, 2]
# n = []
# for i in l:
#     for j in l:
#         for k in l:
#             if (i+j+k) == 0:
#                 n.append([i, j, k])
# for m in n:
#     print(m)
# def per(n):
#     s = 0
#     for i in range(1, n):
#         if n % i == 0:
#             s = s+i
#     if s == n:
#         print("perfect")


# per(6)
class st:
    s = ""

    def getstring(self, s):
        self.s = s

    def validate(self, s):
        if len(self.s) >= 6 and len(self.s) <= 12:
            if self.s[::-1] == self.s:
                print("valid")


o = st()
# o.getstring("abcba")
o.validate("abcdcba")
