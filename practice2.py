# Using While Loop For Multiplication Table
number = int(input ("Enter the number of which you want multiplication table: "))
count = 1

print ("The Multiplication Table of: ", number)
while count <= 10:
    number = number * 1
    print ("{} x {} ====> {}".format(number,count,number*count))
    count += 1