## 2.1
$$
A = \begin{bmatrix} 1 & -2 & 3 \\ 4 & 5 & -6 \\ \end{bmatrix}, \quad
B = \begin{bmatrix} 3 & 0 & 2 \\ -7 & 1 & 8 \\ \end{bmatrix}
$$
---
$$
A + B = \begin{bmatrix} 1 & -2 & 3 \\ 4 & 5 & -6 \\ \end{bmatrix} + \begin{bmatrix} 3 & 0 & 2 \\ -7 & 1 & 8 \\ \end{bmatrix} \newline
= \begin{bmatrix} 1 + 3 & -2 + 0 & 3 + 2 \\ 4 - 7 & 5 + 1 & -6 + 8 \\ \end{bmatrix} \newline
= \begin{bmatrix} 4 & -2 & 5 \\ -3 & 6 & 2 \\ \end{bmatrix}
$$
---
$$
2A - 3B = 2\begin{bmatrix} 1 & -2 & 3 \\ 4 & 5 & -6 \\ \end{bmatrix} -3\begin{bmatrix} 3 & 0 & 2 \\ -7 & 1 & 8 \\ \end{bmatrix} \newline
= \begin{bmatrix} 2 & -4 & 6 \\ 8 & 10 & -12 \\ \end{bmatrix} -\begin{bmatrix} 9 & 0 & 6 \\ -21 & 3 & 24 \\ \end{bmatrix} \newline
= \begin{bmatrix} -7 & -4 & 0 \\ 29 & 7 & -36 \\ \end{bmatrix}
$$
---

## 2.2

Find $x,y,z,t$ where:

$
3\begin{bmatrix}x & y \\ z & t\end{bmatrix} = \begin{bmatrix}x & 6 \\ -1 & 2t\end{bmatrix} + \begin{bmatrix}4 & x + y \\ z + t & 3\end{bmatrix}
$

---
$$
3\begin{bmatrix}x & y \\ z & t\end{bmatrix} = \begin{bmatrix}x+4 & 6+x+y \\ -1+z+t & 2t+3\end{bmatrix} \newline
\Longrightarrow \begin{cases} 3x = x + 4 \\ 3y = 6 + x + y \\ 3z = -1 + z + t \\ 3t = 2t + 3 \end{cases} \Longrightarrow \begin{cases} 2x = 4 \\ 2y = 6 + x \\ 2z = -1 + t \\ t = 3 \end{cases}
\Longrightarrow \begin{cases}x=2 \\ y=4 \\ z=1 \\ t=3\end{cases}
$$
---

## 2.3

Prove $(A+B)+C=A+(B+C)$ and $k(A+B)=kA+kB$ with $A=[a_{ij}]$, $B=[b_{ij}]$, $C=[c_{ij}]$ and $k$ is a scalar.

---
$$
(A+B)+C = [a_{ij}+b_{ij}]+c_{ij} = [a_{ij}+b_{ij}+c_{ij}] = a_{ij}+[b_{ij}+c_{ij}] = A+(B+C)
$$
---
$$
k(A+B) = k[a_{ij}+b_{ij}] = [ka_{ij}+kb_{ij}] = [ka_{ij}]+[kb_{ij}] = kA+kB
$$
---

## 2.10

Prove that $(AB)C = A(BC)$

---
$$
A = [a_{ij}], B=[b_{jk}], C=[c_{kl}] \newline
AB = S = [s_{ik}], BC = T = [t_{jl}] \newline
S = \sum_{j=1}^{m}a_{ij}b_{jk}, T = \sum_{k=1}^{n}b_{jk}c_{kl} \newline
SC = \sum_{k=1}^{n}s_{ik}c_{kl} = \sum_{k=1}^{n}\sum_{j=1}^{m}a_{ij}b_{jk}c_{kl} \newline
AT = \sum_{j=1}^{m}t_{jl}a_{ij} = \sum_{j=1}^{m}\sum_{k=1}^{n}b_{jk}c_{kl}a_{ij} \newline
SC = AT \Longrightarrow (AB)C = A(BC)
$$
---
$$
AB = \begin{bmatrix}
    a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
    a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn} \\
\end{bmatrix} \begin{bmatrix}
    b_{11} & b_{12} & b_{13} & \dots & b_{1n} \\
    b_{21} & b_{22} & b_{23} & \dots & b_{2n} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    b_{n1} & b_{n2} & b_{n3} & \dots & b_{nn} \\
\end{bmatrix} \newline
= \begin{bmatrix}
    \sum_{j=1}^{n}a_{1j}b_{j1} & \sum_{j=1}^{n}a_{1j}b_{j2} & \sum_{j=1}^{n}a_{1j}b_{j3} & \dots & \sum_{j=1}^{n}a_{1j}b_{jn} \\
    \sum_{j=1}^{n}a_{2j}b_{j1} & \sum_{j=1}^{n}a_{2j}b_{j2} & \sum_{j=1}^{n}a_{2j}b_{j3} & \dots & \sum_{j=1}^{n}a_{2j}b_{jn} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    \sum_{j=1}^{n}a_{nj}b_{j1} & \sum_{j=1}^{n}a_{nj}b_{j2} & \sum_{j=1}^{n}a_{nj}b_{j3} & \dots & \sum_{j=1}^{n}a_{nj}b_{jn} \\
\end{bmatrix} \newline
= [\sum_{i=1}^{n}\sum_{j=1}^{n}a_{ij}b_{ji}]
$$
