import sympy as sp

class Newton():
    
    def __init__(self):
        pass

    def newton_method(f_expr, x0, max_iter=10):
        x = sp.symbols('x')

        df_expr = sp.diff(f_expr, x)
        f = sp.lambdify(x, f_expr)
        df = sp.lambdify(x, df_expr)
        x = x0

        for i in range(max_iter):
            print(f"Iteracion {i+1}: x = {x}, f(x) = {f(x)}")

            if(f(x) == 0):
                print(f"Se necesitaron {i+1} iteraciones para aproximar la raíz con el método de Newton.")
                break
            else:
                x = x - f(x) / df(x)
            
        return x



