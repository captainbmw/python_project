# string
from importlib.metadata import unique_everseen

name="eMobilis"
# integer
num=86
# float
num2=86.9
# boolean
mybool=True
# list
fruits=["apple","banana","mangoes","orange"]
# tuple
coordinate=(23.67,456,789)
# dictionaries
students={"name":"Captain","age":18,"grade":"A"}
# set
unique_numbers=[1,2,3,4,5,6,7,8,9]

prev2=0
prev1=1
print(prev2)
print(prev1)
for fibo in range (18):
      newFibo=prev1+prev2
      print(newFibo)
      prev2=prev1
      prev1=newFibo