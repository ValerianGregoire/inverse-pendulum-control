"""*****************************************************************************
This script computes the decoupled equations of motion of the pendulum and the 
cart, then compares the results with results found using MATLAB. This code 
provides redudancy in the found result, to guarantee the viability of the 
controller.

Valerian Gregoire--Begranger
*****************************************************************************"""

import sympy as sp

# Declaration of the symbols
x, dx, ddx, th, dth, ddth = sp.symbols(
    'x, dx, ddx, th, dth, ddth')  # Variables
F, m, M, l, g = sp.symbols('F, m, M, l, g')  # Parameters

# Homogeneous equations of motion
eq1 = (F - m*l*dth**2*sp.sin(th) + m*l*ddth*sp.cos(th))/(M + m) - ddx
eq2 = (ddx*sp.cos(th) + g*sp.sin(th))/(l) - ddth
system = (eq1, eq2)

# Solving of the system
print(f"\n{'-'*30}\nComputing the solution...")
sol = sp.solve(system, (ddx, ddth), dict=True)[0]

for key in sol:
    print(f"{'-'*15}\n{key}: {sp.simplify(sol[key])}\n")

# Verification of the correctness of the solution
print(f"\n{'-'*30}\nNow comparing MATLAB\'s solution with sympy\'s:")
matlab_ddth_sol = (- l*m*sp.cos(th)*sp.sin(th)*dth ** 2 + F*sp.cos(th) +
                   g*m*sp.sin(th) + M*g*sp.sin(th))/(l*(- m*sp.cos(th) ** 2 + M + m))
matlab_ddx_sol = (- l*m*sp.sin(th)*dth ** 2 + F + g*m*sp.cos(th)
                  * sp.sin(th))/(- m*sp.cos(th) ** 2 + M + m)
comparisons = {ddth: sp.simplify(sol[ddth] - matlab_ddth_sol),
               ddx: sp.simplify(sol[ddx] - matlab_ddx_sol)
               }

for key in comparisons:
    print(f"{'-'*15}\nSympy_{key} - Matlab_{key} = {comparisons[key]}\n")
