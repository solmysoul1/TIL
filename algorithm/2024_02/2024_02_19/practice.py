import math

start = (1,1)
end = (4,4)

a = (4-1)
b = (4-1)
c = math.sqrt((a**2)+(b**2))

tan1 = math.atan(b/a)
degree = math.degrees(tan1)

print(c, degree)
