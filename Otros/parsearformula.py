import parser
formula = "x*2"
#a + bM + cR + dS
code = parser.expr(formula).compile()

from math import sin
x = 10
print eval(code)