# Testing my knowledge of loops, including a little while-loop revision

# used a while loop to countdown from 20 - 0
print ( "step 1" )
count_down = 20
while count_down >= 0 :
    print(count_down)
    count_down -= 1

# used a for loop to and if statement
print("step 2")
even_numbers = 1 - 20
for even_numbers in range (1,20):
    if even_numbers % 2 == 0 :
     print(even_numbers)

# used a for loop to display the star signs 
print("step3")
star_signs = " "
for i in range (0,5):
    star_signs = star_signs + "*"
    print(star_signs )

# created two variables to store numbers 
print("step4")
num1 = 10
num2 = 55

# used if, else statements 
if num1 < num2 :
    lesser_num = num1
else:
    lesser_num = num2 

# used a for loop to calculate the greatest common divisor 
for G_C_D in range (1,(lesser_num + 1)):
    if num1 % G_C_D == 0 and num2 % G_C_D == 0:
        i= G_C_D 
    print(i)
print(f"The highest G_C_D is {i}")
