# part (i)
def circle_area(radius):
    pie = 3.14
    area = pie * (radius ** 2)
    return area
radius = 4
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}.")

# part(ii)
numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for number in numbers:
    if number %2!= 0: 
        print(number)
        odd_sum += number
print("Sum of all odd numbers:", odd_sum)

# part (iii)
def numbers(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "Undefined (division by zero)"
    
    return sum_result, difference_result, product_result, quotient_result
num1 = 10
num2 = 5
sum_result, difference_result, product_result, quotient_result = numbers (num1, num2)
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")

# part (iv)
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 26
student_info['city'] = 'Kampala'
print(student_info)

 