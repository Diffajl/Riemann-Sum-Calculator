# Riemann Sum Calculator

## Overview

The **Riemann Sum Calculator** is a web application that approximates the integral of a given function over a specified interval using the Riemann sum method. This tool allows users to input a mathematical function, define the interval, and specify the number of rectangles to use for the approximation.

## Features

- Input mathematical functions using standard Python syntax.
- Define the lower and upper limits of the interval.
- Specify the number of rectangles for the Riemann sum approximation.
- Visualize the function and the Riemann sum approximation graphically.

## How to Use

1. **Input the Function**: Enter the mathematical function \( f(x) \) in the provided text box. For example, `np.exp(-x**2)` for \( e^{-x^2} \).
2. **Enter the Interval**: Specify the lower limit (a) and upper limit (b) of the interval.
3. **Specify the Number of Rectangles**: Enter the number of rectangles (n) to use for the Riemann sum approximation.
4. **Calculate**: Click the "Calculate" button to perform the calculation and display the results.

## Riemann Sum Formula

\[ \text{Riemann Sum: } \int_{a}^{b} f(x) \, dx \approx \sum_{i=1}^{n} f(x_i) \Delta x \]

## Installation

To run this application locally, you'll need Python installed. Follow these steps to get started:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/riemann-sum-calculator.git
    cd riemann-sum-calculator
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:

    ```bash
    streamlit run riemann.py
    ```

## Requirements

- `streamlit`
- `numpy`
- `matplotlib`

These dependencies are listed in the `requirements.txt` file and can be installed using the command `pip install -r requirements.txt`.

## Example

Here's a quick example of how to use the Riemann Sum Calculator:

1. **Function**: `np.exp(-x**2)`
2. **Interval**: [0, 1]
3. **Number of Rectangles**: 100

After clicking the "Calculate" button, the application will display the approximate integral value and a plot of the function with the Riemann sum rectangles.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any features, enhancements, or bug fixes.
