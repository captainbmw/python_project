from typing import List

name= "Captain BMW"
print("my name is "+name)
print(f"my name is {name}")
Age=18
# print("my age is"+str(Age))
# am learning python
num1=6
num2=47
print(f"The sum of {num1} and {num2} is {num1+num2}")
print(f"The difference of {num1} and {num2} is {num1-num2}")
print(f"The product of {num1} and {num2} is {num1*num2}")
print(f"The quotient of {num1} and {num2} is {num1/num2}")
print(f"The remainder of {num1} and {num2} is {num1%num2}")
print(f"The modulus of {num1} and {num2} is {num1%num2}")

def F (n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)
print(F(19))
my_array=[5,56,78,9,8,32,90,45]
minVal=my_array[0]

for i in my_array:
    if i<minVal:
        minVal=i

print('lowest value',minVal)

my_array=[5,59,78,9,8,32,90,45,3,4,6,13,10,67,56,7,2,17,21]
n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]<my_array[j+1]:
            my_array[j],my_array[j+1]=my_array [j+1],my_array[j]

print("sorted array:",my_array)

my_array=[5,56,78,9,8,32,90,45]
n = len(my_array)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_array[j]<my_array[min_index]:
            min_index=j
    min_value=my_array.pop(min_index)
    my_array.insert(i,min_value)

print("sorted array:",my_array)

def two_sum(nums, target):
    num_dict={}
    for

