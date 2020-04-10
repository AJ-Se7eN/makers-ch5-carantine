# Hackerrank
"""https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?h_r=internal-search"""

parts = list(map(float, input().split()))
a = complex(parts[0], parts[1])
parts = list(map(float, input().split()))
b = complex(parts[0], parts[1])
def p(comp):
    if comp.real != 0 and comp.imag != 0:
        print('%.2f %s %.2fi' % (comp.real, '+' if comp.imag >= 0 else '-', abs(comp.imag)))  
    elif comp.imag == 0:
        print("%.2f" % comp.real)
    elif comp.real == 0:
        print("%.2fi" % comp.imag)
    
p(a+b)
p(a-b)
p(a*b)
p(a/b)
print("%.2f" % abs(a))
print("%.2f" % abs(b))