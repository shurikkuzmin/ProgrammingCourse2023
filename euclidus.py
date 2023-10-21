
# for x in range(1,11):
#     print(x*x*x*x)

# for x in ["apple","pear","orange","bimbimbambam"]:
#     print(x)

# for x in range(1000,2001):
#     if x%37 == 0:
#         print("The first number between 1000 and 2000 that can be divided by 37 is",x)
#         break

# x=1000
# while x<=2000:
#     if x%37 == 0 and x%3 == 0:
#         print("The first number between 1000 and 2000 that can be divided by 37 is",x)
#         break
#     x = x+1

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
k = max(m, n)
l = min(m, n)
while k%l != 0:
    k = l
    l = k%l


