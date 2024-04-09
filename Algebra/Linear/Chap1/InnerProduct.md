# Inner product

## Definition

### Rn

$$
a \cdot b = \sum_{i=1}^n a_i b_i\newline
a, b \in \mathbb{R}^n
$$

## Properties

$
(u + v) \cdot w = u \cdot w + v \cdot w
$

Proof
$$
(u + v) \cdot w = \sum_{i=1}^{n} (u_i + v_i) * w_i \newline
= \sum_{i=1}^{n} u_i w_i + \sum_{i=1}^{n} v_i w_i \newline
= u \cdot w + v \cdot w
$$

$(ku) \cdot v = k(u \cdot v)$

Proof
$$
(ku) \cdot v = \sum_{i=1}^{n} (ku_i) * v_i \newline
= k \sum_{i=1}^{n} u_i v_i \newline
= k(u \cdot v)
$$

$u \cdot v = v \cdot u$

Proof
$$
u \cdot v = \sum_{i=1}^n u_i v_i \newline
= \sum_{i=1}^n v_i u_i \newline
= v \cdot u
$$

$u \cdot u \geq 0, u \cdot u = 0 \iff u = 0$

Proof
$$
u = (u_1, u_2, \dots, u_n) \newline
u \cdot u = \sum_{i=1}^n u_i^2 \newline
u_i^2 \geq 0 \newline
u \cdot u \geq 0 \newline

u \cdot u = 0 \iff u_i^2 = 0 \iff u_i = 0 \newline
$$

## Exercices

$$
u = (1, 2, 3, 4), v = (6, k, -8, 2) \newline
u \cdot v = 0 \newline
u \cdot v = 1 * 6 + 2 * k + 3 * (-8) + 4 * 2 \newline
u \cdot v = 6 + 2k - 24 + 8 \newline
2k = -6 + 24 - 8 = 10 \newline
k = 5 \newline
\Longrightarrow u \cdot v = 0 \iff k = 5
$$
