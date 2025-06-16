import math
import cmath
from sympy import symbols, Eq, solve, sympify

def basic_operations(a, b, operation):
    if operation == "Add":
        return a + b
    elif operation == "Subtract":
        return a - b
    elif operation == "Multiply":
        return a * b
    elif operation == "Divide":
        return a / b if b != 0 else "Error: Division by zero"

def trigonometry(angle_deg, function):
    angle_rad = math.radians(angle_deg)
    if function == "sin":
        return math.sin(angle_rad)
    elif function == "cos":
        return math.cos(angle_rad)
    elif function == "tan":
        try:
            return math.tan(angle_rad)
        except:
            return "Error"

def logarithmic(x, func):
    try:
        if func == "log":
            return math.log10(x)
        elif func == "ln":
            return math.log(x)
        elif func == "exp":
            return math.exp(x)
    except Exception as e:
        return f"Error: {e}"

def complex_operations(z1, z2, operation):
    try:
        if operation == "Add":
            return z1 + z2
        elif operation == "Subtract":
            return z1 - z2
        elif operation == "Multiply":
            return z1 * z2
        elif operation == "Divide":
            return z1 / z2
    except ZeroDivisionError:
        return "Error: Division by zero"

def solve_equation(equation_str):
    try:
        x = symbols('x')
        equation = Eq(*sympify(equation_str).as_two_terms())
        solution = solve(equation, x)
        return solution
    except Exception as e:
        return f"Error: {e}"
