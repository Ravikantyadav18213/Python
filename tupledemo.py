# tuple:collection different data element cnclosed into () parenthesies
#it is sequare,index follows,orderd but it is imutable means cant do crud operation


# create tuple
tup=()
print(tup,type(tup))
t1=tuple()
print(t1,type(t1))


t2=(500)
print(t2,type(t2))


t3=(500,100,"hello",True,5j,45.8448)
print(t3,type(t3))

t4=tuple(45,45,67)
t4=tuple((45,67,54))
print(t4,type(t4))