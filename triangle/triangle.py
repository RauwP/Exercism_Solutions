def triangle(sides):
    a, b, c = sorted(sides)
    return a>0 and a+b>=c

def equilateral(sides):
    return len(set(sides))==1 and triangle(sides)

def isosceles(sides):
    return len(set(sides))<=2 and triangle(sides)

def scalene(sides):
    return len(set(sides)) ==3 and triangle(sides)
