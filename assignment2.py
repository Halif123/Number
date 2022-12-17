

x = int(input("enter a value:"))   # python program to check positive or a negative value


if x >= 0:

    print("positive number")
elif x < 0:
    print("negative number")

# python program to check the highest value
t = int(input("enter a value:"))
y = int(input("enter a value:"))
z = int(input("enter a value:"))

if t > y:
    if t > z:
        print("highest number", t)
    else:
        print("highest number is", z)
else:
    if y > z:
        print("highest number", y)
    else:
        print("highest number is ", z)







