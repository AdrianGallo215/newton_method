In this repository, I make a simulation of the Newton Method for non-linear ecuations. Also, I compare it to the Bisection Method.

To use it, just run the main.py file.

Also, if anyone seeing this wants to try it with a different function, just declare that function in the main.py file like this:

f_expr = {The correspondence rule of the function}
def f_func(x):
  return {The correspondence rule of the function on the variable x}

Please make sure to use the variable declared with x = sp.symbols('x') (In this case, 'x') on f_expr.

Adrian Gallo.
