import sympy as sp
import math
from bisection import Bisection
from newton import Newton

x = sp.symbols('x')
f_expr = x*x - 2
def f_func(x):
    return x*x - 2
x0 = 1 
a = 0
b = 2


print(f"Para f(x) = {f_expr}, con x∈[{a}, {b}] y x0 = {x0}, tenemos:")
print("\nMétodo bisección: ")
bisection_root = Bisection.bisection_method(f_func,a,b)
print("\nMétodo de Newton: ")
newton_root = Newton.newton_method(f_expr,x0)

print(f"\nRaíz del método de la bisección: {bisection_root}")
print(f"\nRaíz del método de Newton: {newton_root}")