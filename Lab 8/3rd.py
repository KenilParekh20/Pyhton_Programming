import math
def evaluate_funciton(x):
    f=math.cos(2*x)
    f_derivative=-2*math.sin(2*x)
    f_double_derivative=-4*math.cos(2*x)
    return f,f_derivative,f_double_derivative
x= math.pi
results=evaluate_funciton(x)
print("f = ",results[0])
print("f_derivative = ",results[1])
print("f_double_derivative = ",results[2])
