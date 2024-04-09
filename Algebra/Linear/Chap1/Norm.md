# Norm of a vector

## Definition

$$
\|u\| = \sqrt{u \cdot u} = \sqrt{\sum_{i=1}^n u_i^2}
$$

## Theorem

$|u \cdot v| \leq \|u\|\|v\|$

Proof
$$
|u \cdot v| = |\sum_{i=1}^n u_i v_i| \newline
\leq \sum_{i=1}^n |u_i v_i| \leq \sum_{i=1}^n |u_i| |v_i| \newline
\leq \sum_{i=1}^n \sqrt{u_i^2} \sqrt{v_i^2} = \sum_{i=1}^n \sqrt{u_i^2 v_i^2} \newline
= \sqrt{\sum_{i=1}^n u_i^2 v_i^2} = \sqrt{\sum_{i=1}^n u_i^2} \sqrt{\sum_{i=1}^n v_i^2} \newline
= \|u\|\|v\|
$$

$\|u + u\| \leq \|u\| + \|v\|$

Proof
$$
\|u + u\| = \sum_{i=1}^n (u_i + v_i)^2 \newline
= \sum_{i=1}^n u_i^2 + 2u_i v_i + v_i^2 \newline
= \sum_{i=1}^n u_i^2 + \sum_{i=1}^n 2u_i v_i + \sum_{i=1}^n v_i^2 \newline
= \|u\|^2 + 2u \cdot v + \|v\|^2 \newline
\leq \|u\|^2 + 2|u \cdot v| + \|v\|^2 \newline
$$
