import streamlit as st
from math_operations import (
    basic_operations,
    trigonometry,
    logarithmic,
    complex_operations,
    solve_equation
)
from utils import parse_complex_input

st.set_page_config(page_title="Advanced Calculator")
st.title("Advanced Scientific Calculator")

menu = st.sidebar.selectbox("Select Operation", [
    "Basic Arithmetic", "Trigonometry", "Log/Exp", "Complex Numbers", "Solve Equation"
])

if menu == "Basic Arithmetic":
    st.header("Basic Arithmetic")
    a = st.number_input("Enter first number", key="ba1")
    b = st.number_input("Enter second number", key="ba2")
    op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])
    result = basic_operations(a, b, op)
    st.write("Result:", result)

elif menu == "Trigonometry":
    st.header("Trigonometric Functions")
    angle = st.number_input("Enter angle in degrees", key="trig")
    func = st.selectbox("Function", ["sin", "cos", "tan"])
    result = trigonometry(angle, func)
    st.write(f"{func}({angle}°) = {result}")

elif menu == "Log/Exp":
    st.header("Logarithmic and Exponential Functions")
    num = st.number_input("Enter number", min_value=0.0)
    func = st.selectbox("Function", ["log", "ln", "exp"])
    result = logarithmic(num, func)
    st.write(f"{func}({num}) = {result}")

elif menu == "Complex Numbers":
    st.header("Complex Number Operations")
    z1_str = st.text_input("Enter first complex number (e.g., 3+4j)", "3+4j")
    z2_str = st.text_input("Enter second complex number (e.g., 1-2j)", "1-2j")
    op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])
    z1, z2 = parse_complex_input(z1_str), parse_complex_input(z2_str)
    result = complex_operations(z1, z2, op)
    st.write("Result:", result)

elif menu == "Solve Equation":
    st.header("Solve Equation")
    eq = st.text_input("Enter equation (e.g., x**2 - 4 = 0)")
    if st.button("Solve"):
        solution = solve_equation(eq)
        st.write("Solution:", solution)
