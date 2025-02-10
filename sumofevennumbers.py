numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum_of_even_numbers=0
for number in numbers:
    if number % 2 == 0:
        sum_of_even_numbers += number
print(f"The sum of even numbers is {sum_of_even_numbers}")

sum_of_odd_numbers=0
for i in numbers:
    if i % 2 == 1:
        sum_of_odd_numbers += i

print(f"The sum of odd numbers is {sum_of_odd_numbers}")