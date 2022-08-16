'''

a = [4, 3, 7, -5, 8]  # The input list
print("Input list", a)
n = len(a)  # Get length of list
for i in range(n - 1):  # Loop through the array one time less than the length of the list
    if a[i] <= a[i + 1]:  # Compare neighboring elements and continue till they are in order
        continue
    j = i + 1
    t = a[j]
    while j >= 1 and a[j - 1] > t:  # Loop through the array till elements are greater than t
        a[j] = a[j - 1]
        j -= 1
    a[j] = t
    print("Array after ", i + 1, " iterations ", a)
print("Sorted Array ", a)
'''

from turtle import *
speed(0)
bgcolor('red')
color('white')
hideturtle()

n = 1
p = True

while True:
    circle(n)
    if p:
        n = n - 1
    else:
        n = n + 1
        if n == 0 or n ==60:
            p = not p
        left(1)


done()
