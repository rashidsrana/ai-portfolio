
# # Getting started with sympy


# - Sympy (sybmolic pyhton) is python library used for symbolic maths in the field of physics, engineering and maths. It is used in:
# - Symbolic computations
# - Equations
# - Calculas
# - Linear algebra
# - Discrete math
# - Code generation 


import sympy as sp


sp.pi


sp.gcd(12,18)


sp.lcm(12,18)


sp.sqrt(9)


sp.sqrt(2)


sp.N(sp.sqrt(2))


sp.N(sp.sqrt(2))


sp.Rational(5,6)


sp.N(sp.Rational(5,6))


sp.__version__


sp.oo


sp.pi


print(sp.pi)


#from pprint import pprint
sp.pprint(sp.pi)


sp.pprint(sp.oo)


a,b=sp.symbols('a b')


sp.And(a,b)


sp.Or(a,b)


sp.pprint(sp.And(a,b))


sp.Not(a)


sp.Nand(a,b)


sp.Nor(a,b)


sp.Xor(a,b)


sp.Not(a)


sp.Not(sp.Xor(a,b))


sp.prime(40)


sp.factorial(7)


from sympy.utilities.iterables import permutations
list(permutations([1,2,3]))


# # Simplification


from sympy import simplify,symbols



x,y=symbols('x y')


ex1=(x**2-1)/(x-1)
sm1=simplify(ex1)
sm1


exp2 = x**2 + 2*x + x**2 - x
sm2=simplify(exp2)
sm2


exp2=(x+y)**2-(x**2 + 2*x*y + y**2)
sm2 = simplify(exp2)
sm2



exp3=(x**3-3*x**2+3*x-1)/(x-1)
sm3=simplify(exp3)
sm3


# # Solving Equations


from sympy import Eq, solve


#  x,y,z=symbols('x y z')


# x2-5x+6=0
eq1=Eq(x**2-5*x,-6)
so1=solve(eq1)
so1


# x2-5x+20=0
eq2=Eq(x**2-9*x+20,0)
sol2=solve(eq2)
sol2


exp3=Eq(3*x**2+4*x-6,0)
sol3=solve(exp3)
print(sol3)
print(sp.N(sol3[0]))
print(sp.N(sol3[1]))


exp4=Eq(x**3-3*x**2+4*x-2,0)
sol4=solve(exp4)
print(sol4)
print(sp.N(sol4[0]))
print(sp.N(sol4[1]))



from sympy import sin, cos,log, exp


exp5=Eq(log(x),2)
sol5=solve(exp5)
print(sol5)
#print(sp.N(sol5[0]))
#print(sp.N(sol5[1]))


exp5=Eq(sin(x),0)
sol5=solve(exp5)
print(sol5)


x,y,z = sp.symbols('x y z')


e1=sp.Eq(3*x+2*y,12)
e2=sp.Eq(x-y,1)
s1=solve((e1,e2))
s1


e1=sp.Eq(4*x-y,5)
e2=sp.Eq(2*x+3*y,7)
s1=solve((e1,e2))
s1


d1=x**4
dr1=sp.diff(d1)
dr1


from sympy import diff,integrate


d1=x**3+2*x**2+4*x+8
dr1=sp.diff(d1)
dr1


i1=x**4
int1=integrate(i1)
int1


i1=x**3+2*x**2+4*x+8
int1=sp.integrate(i1)
int1


l2=log(x)
print(integrate(l2))


# # Matrices in Sympy


from sympy import Matrix


A=Matrix([[1,2],[3,4]])
B=Matrix([[11,22],[33,44]])
A



B


A+B


B-A


A*10


A.T


A.det()


A.inv()


# # solving equations using Matrices


A=Matrix([[2,1],[1,-1]])
B=Matrix([5,1])
x=A.solve(B)
x


A=Matrix([[2,1],[1,-1]])
B=Matrix([5,1])
x=A.solve(B)
x





