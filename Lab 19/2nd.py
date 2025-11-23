import sympy as sp
z=sp.symbols('z')
Hz=0.5*(z-0.7)*(z-0.9)/((z-0.6)*(z-0.4))
print("H(z) =",Hz)
zeros=sp.solve(0.5*(z-0.7)*(z-0.9),z)
poles=sp.solve((z-0.6)*(z-0.4),z)
print("Zeros:",zeros)
print("Poles:",poles)
stable=all(abs(p)<1 for p in poles)
if stable:
    print("System is Stable")
else:
    print("System is Unstable")
