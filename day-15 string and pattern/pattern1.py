# for i in range(3):
#     print("*")

# for i in range((3)):
#     print("*",end="  ")    

# for i in range(3):
#     for a in range(3):
#         print("*",end=" ")
#     print()    
 

 # left-incremental triangle
count=int(input("enter row count="))
for i in range(count):
    for j in range(i+1):
        print("*",end="")
    print()

count=int(input("enter row count="))
for i in range(count):
    for j in range(i+1):
        print(1,end="")
    print()    


count=int(input("enter row count="))
for i in range(count):
    for j in range(i+1):
        print(j,end="")
    print()


count=int(input("enter row count="))
n=1
for i in range(count):
    for j in range(i+1):
        print(n,end="")
    print()