# list datastructures
# list are mutable
# list are ordered
# list are indexed
from datatypes import students

fruits=['apple','banana','mango','orange','strawberry','peach','pineapple']
fruits[0]="Watermelon"
print(fruits)
numbers=[1,2,3,4,5,6,7,8,9]
numbers2=[67,5,2,8,89,90,78,65,64]
numbers2.sort(reverse=True)
print(numbers)
numbers.append(10)
print(f"i love eating {fruits[0]}")
print(numbers2)
# tuple datastructures
# tuple are immutable
# tuples are ordered
# tuples are indexed
cars=('audi','toyota','subaru','toyota')
numbers=(1,2,3,4,5,6,7,8,9)
print(cars)
nambari=(43,5,87,2,-3,-9,-100,-2345,9,1,0)
# nambari.sort(reverse=True)
print(sorted(nambari))
print(numbers)
# cars[2]="bmw"
print(cars)

# set datstructures
# set are unordered
# set are not indexed
computer={'hp','lenovo','apple','chromebook','hp AI','dell','ibm','toshiba'}
print(computer)
computer.add('google')
computer.remove('lenovo')
num1={1,2,3}
num2={4,5,6}
union_set = num1.union(num2)
print(union_set)
# dictionaries data structures
student=("Name':'John','age':5,'gender':'male','school':'University of Narobi")
print(student)
print(f"students name is {students['name']},age is {students['age']}, gender is{students['gender']}, school is {students['school']}")
