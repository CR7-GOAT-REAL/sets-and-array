#set operations
my_set = {1, 2, 3}
print(my_set)

my_set2 = {1.0,"Hello",(1,2,3)} 
print(my_set2)
 
my_set3 = {1,2,3,4,3,2}
print(my_set3)

my_set4 = set([11, 12, 13])
print(my_set4)

my_set4.pop()
print("The set after pop is :",my_set4)



#set intersection
setx = {"blue","yellow"}
sety = {"green","blue"}
print("The original sets are:",setx,sety)
setz = setx.intersection(sety)
print("The intersection of", setx, "and", sety, "is", setz)


#array operations
import array as arr

array_num = arr.array('i', [1, 3, 5, 7, 9, 3, 5, 3, 5])
print("Original array: ", str(array_num))
#count number of ocurrences of an element in an array
print("Occurrences of 3 in the said array: ", array_num.count(3))

#reverse the array
array_num.reverse()
print("The reversed array: ", str(array_num))