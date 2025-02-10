weight=float(input("Enter the weight of a person: "))
height=float(input("Enter the height of a person: "))
# body mass  index formula
bmi=weight/(height**2)
# calculator of bmi
if bmi <18.5:
        classification="You are Underweight"
elif 18.5>bmi<= 24.9:
        classification="You are  Normal weight"
elif 24.9> bmi <=29.9:
        classification="You are Overweight"

else:
        classification="Obesity"


print(f"Your weight is {bmi*2},which is {classification}")
# end of bmi