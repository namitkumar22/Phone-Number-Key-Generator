import time
import csv


phone_number = []
name = input("Enter name :")
number = int(input("Enter phone number :"))

while number > 0:
    phone_number.append(number%10)
    number = (number - number%10) // 10

first_digit = str(phone_number[-1])
second_digit = str(phone_number[-2])
third_digit = str(phone_number[-3])
fourth_digit = str(phone_number[-4])
fifth_digit = str(phone_number[-5])
sixth_digit = str(phone_number[-6])
seventh_digit = str(phone_number[-7])
eighth_digit = str(phone_number[-8])
nineth_digit = str(phone_number[-9])
tenth_digit = str(phone_number[-10])

first_three_digit = first_digit+second_digit+third_digit
first_step = int(first_three_digit)*40*25

next_three_digit = fourth_digit+fifth_digit+sixth_digit
second_step = ((((first_step + int(next_three_digit))*50)+1)*400)

last_four_digit = seventh_digit+eighth_digit+nineth_digit+tenth_digit
securityKey = second_step + int(last_four_digit) + int(last_four_digit)

print("Generating Security.....")
time.sleep(2)
print("Making a Record.....")
time.sleep(2)
print("Security Key Generated :", securityKey)

field = [name, str(securityKey)]

f = open("keys.csv", 'w')
f.write(str(field))
f.close()