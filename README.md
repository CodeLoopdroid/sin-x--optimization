# sin-x--optimization

This project visualizes **gradient descent** optimization applied to the function $f(x) = \sin(x)$.
It demonstrates how the gradient descent algorithm iteratively updates the input to approach a local minimum of the sine function by using its derivative.

## How it works

- The function used is $f(x) = \sin(x)$.
- The derivative used for gradient updates is $f'(x) = \cos(x)$.
- The input domain spans from $-8\pi$ to $8\pi$ with small steps.
- The algorithm starts at $x = \frac{\pi}{4}$.
- In each iteration, the input value is updated by moving opposite to the gradient direction scaled by a learning rate $\alpha = 0.1$:

$$
x_{\text{new}} = x_{\text{old}} - \alpha \times f'(x_{\text{old}})
$$

- The process is animated with matplotlib to show the current point moving along the sine curve toward a minimum.

## Usage

Run the script `gradient_descent.py` to watch the gradient descent visualization in action.  
Make sure you have the required dependencies installed:

```bash
pip install numpy matplotlib
python gradient_descent.py
