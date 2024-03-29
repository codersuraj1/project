# Using While Loop For Multiplication Table
number = int(input ("Enter the number which Multiplication Table you want : "))
count = 1

print ("Multiplication Table of:{} ".format(number))
while count <= 10:
    number = number * 1
    print ("{} x {} ====> {}".format(number,count,number*count))
    count += 1