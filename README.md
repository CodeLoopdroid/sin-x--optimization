# sin-x--optimization

This project demonstrates **gradient descent optimization** applied to the function \( f(x) = \sin(x) \).  
Gradient descent is an iterative optimization algorithm used to find the minimum of a function by moving in the direction opposite to the gradient (derivative).

### How the code works

- The target function is \( f(x) = \sin(x) \), which oscillates periodically.
- Its derivative \( f'(x) = \cos(x) \) is used to calculate the gradient at each point.
- The algorithm starts at \( x = \pi/4 \).
- In each iteration, it updates the current point \( x \) using the formula:
  
  \[
  x_{\text{new}} = x_{\text{old}} - \alpha \times f'(x_{\text{old}})
  \]
  
  where \( \alpha = 0.1 \) is the learning rate that controls the step size.
- The process is visualized with matplotlib, showing how the point moves towards a local minimum on the sine curve over 1000 iterations.

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/CodeLoopdroid/sin-x--optimization.git
cd sin-x--optimization
