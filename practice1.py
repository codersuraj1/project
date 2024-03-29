digit=int(input("Enter the number which Multiplication Table you want : "))

print("Multiplication Table of:{} ".format(digit))

for i in range (1,11):
    print("{} x {} ===> {}".format(digit,i,(digit*i)))
