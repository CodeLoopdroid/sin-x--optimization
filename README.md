# sin-x--optimization

This project visualizes gradient descent optimization applied to the function **sin(x)**.  
It demonstrates how gradient descent iteratively moves towards the minimum of the function using its derivative.

## How it works

- The function used is \( f(x) = \sin(x) \).
- The derivative used for gradient updates is \( f'(x) = \cos(x) \).
- The algorithm starts at \( x = \pi/4 \) and updates the point iteratively using the gradient descent formula:
  
  \[
  x_{\text{new}} = x_{\text{old}} - \alpha \times f'(x_{\text{old}})
  \]

- The process is visualized using matplotlib, showing the point moving towards a minimum on the curve.

## Usage

Run the script `gradient_descent.py` to see the visualization in action. Make sure you have `numpy` and `matplotlib` installed:

```bash
pip install numpy matplotlib
python gradient_descent.py