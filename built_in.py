#LISTS
list = [1,2,3,4]
list.append(5)
list.remove(2)
for i in range(0,len(list)):
    print(list[i])

#TUPLES
tuple = (6) #not tuple >>>> integer
tuple1 = (6,) #>>>>>> tuple
print(type(tuple))
print(type(tuple1))

#DICTIONARYS
dictionary_classroom = {"Ahmet" : 229 , "Ayse" : 730 ,"Mehmet" : 742}
for key in dictionary_classroom:
    print(dictionary_classroom[key])

del dictionary_classroom["Mehmet"] ## silme
print(dictionary_classroom)

dictionary_classroom["Kemal"] = 245 ## ekleme
print(dictionary_classroom)

dictionary_teachers = {"Ali" : "Math" , "Kerem" : "Music"}
dictionary_members = {"Students": dictionary_classroom,"Teachers" : dictionary_teachers}
print(dictionary_members)

#SETS
s = set("hello")
print(s)

s1 = set([1,2,3,4,2])
print(s1)

s2 = {5,6,7,8}
print(type(s2))

s2.add(9) ##ekleme
print(s2)
s2.remove(5) ##silme
print (s2)

for i in s1:
    print(i)