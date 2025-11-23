import sympy as sp
def z_transform_unit_step():
    n=sp.symbols('n')
    z=sp.symbols('z')
    u=sp.Heaviside(n)
    U=sp.summation(u*z**(-n),(n,0,sp.oo))
    return sp.simplify(U)
Uz=z_transform_unit_step()
print("Z-transform:",Uz)
pole=1
if abs(pole)<1:
    print("Stable")
else:
    print("Unstable")
