#Arithmetic Operators
a = 3
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b) #ans should be in float form
print(a % b) #Remainder
print(a ** b) #3^2 = 9

#Relational Operators
print(a == b) #False
print(a != b) #True
print(a > b) #True
print(a >= b) #True
print(a < b) #False
print(a <= b) #False

#Assignment Operators
c = 5
d = 10
e = 2
f = 12
g = 12
h = 2
c += 10 #c = c + 10 => 15
d -= 10 #d = d - 10 => 0
e *= 2 #e = e * 2 => 4
f /= 2 #f = f / 2 => 6 #ans should be float form
g %= 2 #g = g % 2 => 0
h **= 4 #h = h ** 4 => 16
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

#Logical Operators
x = 2
y = 3
print(not False) #True
print(not True) #False
print(not (x > y)) #True
val1 = True
val2 = False
print(val1 and val2) #False
print(val1 or val2) #True
print((x == y) or (x > y)) #False