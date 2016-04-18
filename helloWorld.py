import math
counter = 1
while counter <=5:
    print("hello world")
    counter = counter + 1

print("#####################")

for item in [1,3,6,2,5]:
    print(item)

print("#####################")

for item in range(5):
    print(item**2)

print("#####################")

wordlist = ['cat','dog','rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if not aletter in letterlist:
            letterlist.append(aletter)
print(letterlist)

print("#####################")

# n = int(input('give a number and I will sqrt it: '))
# if n<0:
#     print("sorry, value is negative")
# else:
#     print(math.sqrt(n))
#
# print("#####################")

# score = int(input('give me a score'))
# if score >= 90:
#     print('A')
# else:
#     if score >=80:
#         print('B')
#     else:
#         if score >=70:
#             print('C')
#         else:
#             if score >=60:
#                 print('D')
#             else:
#                 print('F')
#
# print("#####################")
#
# if score >= 90:
#     print('A')
# elif score >=80:
#     print('B')
# elif score >=70:
#     print('C')
# elif score >=60:
#     print('D')
# else:
#     print('F')

# print("#####################")
#
# if n<0:
#     n = abs(n)
# print(math.sqrt(n))

# print("#####################")

sqlist = []
for x in range(1,11):
    sqlist.append(x*x)
print(sqlist)

print("#####################")

sqlist1 = [x*x for x in range(1,11)]
print(sqlist1)

print("#####################")

sqlist1 = [x*x for x in range(1,11) if x%2 !=0]
print(sqlist1)

print("#####################")

noVocals = [ch.upper() for ch in 'comprehesion' if ch not in 'aeiou']
print(noVocals)

print("#####################")

letterlist1 = [aletter for aletter in "".join(wordlist)]
print(letterlist1)
print(list(set(letterlist1)))

print("#####################")

a = [1,2,3,4]
while a:
    print(a.pop(0))

print("#####################")

# anumber = int(input("Please enter an integer: "))
# try:
#     print(math.sqrt(anumber))
# except:
#     print("Bad Value for square root")
#     print("using absolute value instead")
#     print(math.sqrt(abs(anumber)))
#
# if anumber < 0:
#     raise RuntimeError('You can`t use a negative number')
# else:
#     print(math.sqrt(anumber))

print("#####################")


def squareroot(n):
    root = n/2 #initial gues will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n/root))

    return root

print(squareroot(9))
print(squareroot(1024))