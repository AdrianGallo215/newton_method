class Bisection():
    
    def __init__(self):
        pass

    def bisection_method(f, a, b, tol=1e-6, max_iter=100):

        if f(a) * f(b) > 0:
            print("La función debe tener signos opuestos en los extremos del intervalo.")
            return None

        for i in range(max_iter):
            c = (a + b) / 2 
            print(f"Iteración {i+1}: c = {c:.6f}, f(c) = {f(c):.6f}")
            
            if abs(f(c)) < tol :
                print(f"Se necesitaron {i+1} iteraciones para aproximar la raíz con el método de la bisección.")
                return c
            
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
                
        print("No se encontró la raíz después del número máximo de iteraciones.")
        return (a + b) / 2

