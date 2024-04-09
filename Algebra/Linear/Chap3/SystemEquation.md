# Systems of Equations

## Definitions

A system of equations is like a matrix, it has 2 dimensions $m$ and $n$.

When we are saying it's a $m*n$ equation system it says that there is $m$ equations of $n$ variables.

## Example

A system of $3*4$ equations looks like this:

$
\begin{cases}
a_1x + b_1y + c_1z + d_1t &= k_1 \\
a_2x + b_2y + c_2z + d_2t &= k_2 \\
a_3x + b_3y + c_3z + d_3t &= k_3 \\
a_4x + b_4y + c_4z + d_4t &= k_4 \\
\end{cases}
$

## Exercices

$$
\begin{cases}
x_1 + x_2 + 4x_3 + 3x_4 &= 5 \\
2x_1 + 3x_2 + x_3 - 2x_4 &= 1 \\
x_1 + 2x_2 - 5x_3 + 4x_4 &= 3
\end{cases} \newline
u=\begin{pmatrix}-8 & 6 & 1 & 1\end{pmatrix} \Longrightarrow \begin{cases}
-8 + 6 + 4 + 3 &= 5 \\
-16 + 18 + 1 - 2 &= 1 \\
-8 + 12 - 5 + 4 &= 3
\end{cases} \newline
v=\begin{pmatrix}-10 & 5 & 1 & 2\end{pmatrix} \Longrightarrow \begin{cases}
-10 + 5 + 4 + 6 &= 5 \\
-20 + 15 + 1 - 4 &\ne 1 \\
-10 + 10 - 5 + 8 &= 3
\end{cases}
$$


## Linear Combinatinos, Homogeneous Systems

### 3.34

Write $v$ as a linear combinations of $u_1$, $u_2$, and $u_3$. where

---
$
v = \begin{pmatrix}3 & 10 & 7\end{pmatrix}, u_1 = \begin{pmatrix}1 & 3 & -2\end{pmatrix},u_2 = \begin{pmatrix}1 & 4 & 2\end{pmatrix}, u_3 = \begin{pmatrix}2 & 8 & 1\end{pmatrix}\newline v = au_1 + bu_2 + cu_3 \newline \Longrightarrow \begin{cases}
    3 &= a + b + 2c \\
    10 &= 3a + 4b + 8c \\
    7 &= -2a + 2b + c
\end{cases} \newline
\begin{align}
L2 - 3L1 \rightarrow L2 & \Longrightarrow \begin{cases}
    3 &= a + b + 2c \\
    10 - 3*3 &= 3a + 4b + 8c - 3(a + b + 2c) = b + 2c \\
    7 &= -2a + 2b + c
\end{cases} \newline L3 + 2L1 \rightarrow L3 & \Longrightarrow \begin{cases}
    3 &= a + b + 2c \\
    1 &= b + 2c \\
    7 + 2 * 3 &= -2a + 2b + c + 2(a + b + 2c) = 4b + 5c
\end{cases} \newline L3 - 4L2 \rightarrow L3 & \Longrightarrow \begin{cases}
    3 &= a + b + 2c \\
    1 &= b + 2c \\
    13 - 4 * 1 &= 4b + 5c - 4(b + 2c) = -3c
\end{cases} \newline & \Longrightarrow \begin{cases}
    3 &= a + b + 2c \\
    1 &= b + 2c \\
    c &= -3
\end{cases} \newline & \Longrightarrow \begin{cases}
    a &= 3 - 7 - 2 * -3 = 2 \\
    b &= 1 - 2 * -3 = 7 \\
    c &= -3
\end{cases} \end{align} \newline
\Longrightarrow v = 2u_1 + 7u_2 - 3u_3
$

---

$
v=(2, 7, 10), u_1 = (1, 2, 3), u_2 = (1, 3, 5), u_3 = (1, 5, 9) \newline
v = au_1 + bu_2 + cu_3 \newline
\Longrightarrow \begin{cases}
    2 &= a + b + c \\
    7 &= 2a + 3b + 5c \\
    10 &= 3a + 5b + 9c
\end{cases} \newline
\begin{align}
L2 - 2L1 \rightarrow L2 & \Longrightarrow \begin{cases}
    2 &= a + b + c \\
    7 - 2*2 &= 2a + 3b + 5c - 2(a + b + c) = b + 3c \\
    10 &= 3a + 5b + 9c
\end{cases} \newline
L3 - 3L1 \rightarrow L3 & \Longrightarrow \begin{cases}
    2 &= a + b + c \\
    3 &= b + 3c \\
    10 - 3*2 &= 3a + 5b + 9c - 3(a + b + c) = 2b + 6c
\end{cases} \newline
L3 - 2L2 \rightarrow L3 & \Longrightarrow \begin{cases}
    2 &= a + b + c \\
    3 &= b + 3c \\
    4 - 2*3 &= 2b + 6c - 2(b + 3c) = 0
\end{cases}
\end{align} \newline
-2 = 0 \Rightarrow \text{No solution}
$

---

$
v=(1, 5, 4), u_1=(1, 3, -2), u_2=(2, 7, -1), u_3=(1, 6, 7) \newline
v = au_1 + bu_2 + cu_3 \newline \Longrightarrow
\begin{cases}
    1 = a + 2b + c \\
    5 = 3a + 7b + 6c \\
    4 = -2a - b + 7c
\end{cases} \newline
M = \begin{bmatrix}
    1 & 2 & 1 & 1 \\
    3 & 7 & 6 & 5 \\
    -2 & -1 & 7 & 4
\end{bmatrix} \sim \begin{bmatrix}
    1 & 2 & 1 & 1 \\
    0 & 1 & 3 & 2 \\
    0 & 3 & 9 & 6
\end{bmatrix} \sim \begin{bmatrix}
    1 & 2 & 1 & 1 \\
    0 & 1 & 3 & 2 \\
    0 & 0 & 0 & 0
\end{bmatrix} \sim \begin{bmatrix}
    1 & 0 & -5 & -3 \\
    0 & 1 & 3 & 2 \\
    0 & 0 & 0 & 0
\end{bmatrix} \newline
\Longrightarrow \begin{cases}
    a = 5c - 3 \\
    b = -3c + 2 \\
    c = c
\end{cases} \newline
v = (5c - 3)u_1 + (-3c + 2)u_2 + cu_3
$
