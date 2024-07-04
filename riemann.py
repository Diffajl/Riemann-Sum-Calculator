import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.set_page_config("Riemann Sum Calculator")
    st.markdown("<h1 style='text-align: center;'>Riemann Sum Calculator</h1>", unsafe_allow_html=True)
    
    # About Section
    st.markdown("""
    ## About
    This web application calculates the Riemann sum of a given function over a specified interval. 
    It allows users to input the function, the interval [a, b], and the number of rectangles (n) to approximate the integral.
    """)
    
    # How to Use Section
    st.markdown("""
    ## How to Use
    1. **Input the function**: Enter the mathematical function f(x) in the provided text box. For example, `np.exp(-x**2)` for \( e^{-x^2} \).
    2. **Enter the interval**: Specify the lower limit (a) and upper limit (b) of the interval.
    3. **Specify the number of rectangles**: Enter the number of rectangles (n) to use for the Riemann sum approximation.
    4. **Calculate**: Click the "Calculate" button to perform the calculation and display the results.
    """)
    
    st.latex(r'''
    \text{Riemann Sum: } \int_{a}^{b} f(x) \, dx \approx \sum_{i=1}^{n} f(x_i) \Delta x
    ''')

    with st.sidebar:
        func_input = st.text_input("Enter the function f(x): ", value="np.exp(-x**2)")
        a = st.number_input("Enter the lower limit: ", value=0.0)
        b = st.number_input("Enter the upper limit: ", value=1.0)
        n = st.number_input("Enter the number of rectangles: ", value=100, step=1, format="%i")

        if st.button("Calculate"):
            try:
                st.latex(rf'''
                \int_{{{int(a)}}}^{{{int(b)}}} {func_input}(x) \, dx \approx \sum_{{i=1}}^{{n}} {func_input}(x_i) \Delta x
                ''')
                func = eval(f"lambda x: {func_input}")
                
                if n > 1:
                    x = np.linspace(a, b, int(n))
                    dx = (b - a) / (n - 1)

                    result = 0

                    for i in range(int(n)):
                        result += func(x[i]) * dx

                    st.success(f"Integral result ≈ {result}")

                    fig, ax = plt.subplots()
                    xp = np.linspace(a, b, 1000)
                    ax.plot(xp, func(xp), label=f'f(x) = {func_input}', color='blue')

                    for i in range(int(n)):
                        ax.bar(x[i], func(x[i]), align='edge', width=dx, color='gray', edgecolor='red', alpha=0.5)

                    ax.set_xlabel('x')
                    ax.set_ylabel('f(x)')
                    ax.legend()

                    st.pyplot(fig)
                else:
                    st.write("The number of rectangles must be greater than 1.")
            except Exception as e:
                st.error(f"An error occurred while evaluating the function: {e}")

if __name__ == "__main__":
    main()
