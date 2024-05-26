import time

name = input("Enter name :")

f = open("keys.csv", 'r')
securityKey = f.read()

length = len(name)+2
length_for_key = len(name) + 6

print("Checking Name.....")
time.sleep(2)

if (securityKey[2:length] == name):
    print("Record Found!")
    print("Getting security key.....")
    time.sleep(2)
    print("Key found :", securityKey[length_for_key:-3])
    print("Getting phone number.....")
    time.sleep(2)
    print("Phone number found !")
    phone_number = ((int(securityKey[length_for_key: -2])/2)-200)
    print("Phone number : ", int(phone_number))

else:
    print("Record Not Found")

f.close()