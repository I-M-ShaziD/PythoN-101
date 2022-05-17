"""
In this part we are going to discuss about the Data Types of the Python where we can see how Python reacts on various kind and parts of the data. In Python we are specificly using:-

    Most Using Python Data type is:
        - Premtive Data Type
        - Non Primtive Data Tyoe
    
    Premtive Data Type:
        * Numerical Data Type : Such as Integer , Float as well as we can store Complex Number as well.
        * Sting Data Type: Here all the data are stored as the string.
        * Boolean Data Type: Here all the has only two outputs such as Yes/No or boolean value (0/1).

    Non Premtive Data Type:
        * List
        * Set
        * Tuple
        * Dictionary

       - List: List a kind to data type that contains varius elements separated by comma (,) where each of the elements are indexed from the zero. Such as on other Programming languages like C or Javascript we can calles is as array. It is started with the square[] braces. The elements of the List can be duplicate. It can also be empty.

            a = [1,1 ,2,3]

       - Set: Set is also kind of data type where we have multiple elements which is also separated by comma.But duplicate value of key is not allowed in the set. It is started with the curly{} braces. It can also be empty.

            a = {1 , 2 , 3}

       - Tuple: Tuple is also a data type similar to list and set but started with nornal() as well as it cant be empty. It must have multiple values.

            a = (1, 2 , 3)
    
       - Dictionary: Dictionary is also kind of data type where we have multiple elements which is also separated by comma but it is represented " key : value " format where we can set the value  for any particuller key. But duplicate value of key is not allowed in the Dictionary. It is started with the curly{} braces. It can also be empty.

            a = {
                "name" : "Shazid,
                "age" : 27,
                "married" : True
            }

"""

# Some Non Premtive Data Type

a = 1
b = 2.0
name = "Shazid"
c = True
d = 1+5j


# Some Primtive Data Types are


# li
e = [1, 1, 2, 3]

# Set
f = {1, 2, 3}

# Tuple
g = (1, 2, 3)

# Dictionary

h = {
    "name": "Shazid",
    "age": 27,
    "married": True
}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(name))

# Python is Strongly Typed Language
# Python is Stricktly Typed Language
