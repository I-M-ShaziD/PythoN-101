"""
Python list is a  list of mixed data whatever that can be intiger float string or any sort of the data. From where we can retrive the data by the index and all.

    * List contains multiple values which is various kind of data.
    * Each of the item is separeted by comma.
    * The list is created by the square brackets.
    * Index start with the 0
    * Negative indexing starts from the end of the items of the list.
    * We can add or replace any item of the list.
    * We can use for loop in list that will provide us the values separately and serially through the index.
    * We can also delete item from the list for deleting any items from the list we have two method which are:

            - Delete item by Index: For doing this sort of delete we need to use the method pop(index number). Such as fruits.pop(3)

            - Delete Item by Value: For doing this sort of deletion we need to provide the value as well as we need to use the method called remove. Such as fruits.remove("anarosh")

    * We can find out the length of any particuller list by using the "len" method on any list. Such as len(fruits)
    * We can clear any list by using the function called "clear". Such as fruits.clear()

"""


fruits = ["Amm" , "Jamm" , "Kathal", "lichu", "kola"]

#List
print(fruits)

#List Indexing
print(fruits[2])


#Negative Indexing
print(fruits[-2])

#List replacing
fruits[0] = "begun"
print(fruits)

#List Addition
fruits.append("anarosh")
print(fruits)

#List Deletion By Value:
fruits.remove("anarosh")


#List Deletion By Index:
fruits.pop(2)
print(fruits)


#Mixed List:
mixed_list = [ "amm" , "jaam" , 3 , True , 8.9 ]
print(mixed_list)

#For in List:
for x in mixed_list:
    print(x)

#List length
a = len(fruits)
print(a)

#List Clear
mixed_list.clear()
print(mixed_list)






 