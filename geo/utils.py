import math

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    # PDF의 오류(r*2)를 r**2 (제곱)으로 수정
    area = math.pi * r**2 
    return area