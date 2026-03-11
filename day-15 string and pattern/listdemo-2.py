# list1=[11,23,43,45]
# print(list1)


# operation
# x=[1,2,3]
# y=[4,5,4]
# print(x+y)

# x.append(100)
# print(x)

# x[2]=222
# print(x)


#method
colors=[]
print(colors)
colors.append("red")
print(colors)
colors.append("green")

colors.append(["bule","white"])
print(colors)
print(colors[-1])
print(colors[2])
colors.append(("cycle","whhhhh"))
print(colors)
colors.append({"black","yello"})
print(colors)


# update last element
colors[-1]="mitesh"
print(colors)

#addd element by usin insert
colors.insert(0,"ravi")
print(colors)

colors.insert(11,"crem")
print(colors)
print(len(colors))
print(colors.index("crem"))

#delete element
colors.pop()
print(colors)
colors.pop(2)
print(colors)
colors.remove('red')
print(colors)
del colors[0]
print(colors)


# traversing list
for i in colors:
    print(i)