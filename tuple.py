mytuple = ()
print(mytuple)

mytuple = (1,2,3)
print(mytuple)

mytuple = ("a","b","c","d","e","f")
print(mytuple)

ntuple = ("codingal",[1,2,3],(4,5,6))
print(ntuple[0][3])
print(ntuple[2][1])

print("slicing",mytuple)

for i in mytuple :
    print("Hi",i)

myset = {1,1,2,2,3,3,4,4,5,6}
print(myset)

myset.add(2)
print(myset)

set1 = myset
set2 = {2,2,4,4,5,5}

print("Set1",set1)
print("Set2",set2)

print("Difference",set1.difference(set2))
print("Symmetric Difference",set1.symmetric_difference(set2))


setx = {"yellow","Green"}
sety = {"Blue","Green"}

seta = setx.intersection(sety)
print("Intersection",seta)

setb = setx.union(sety)
print("Union",setb)