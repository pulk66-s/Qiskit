# Angles

## Cos

$cos(\theta) = \frac{u \cdot v}{\|u\|\|v\|}$

$\theta$ is the angle between $u$ and $v$.

Proof
---
On a triangle the cosinus is equal to the adjacent side divided by the hypotenuse.

We have a triangle formed by $u$, $v$ and the projection of $u$ onto $v$.

$
cos(\theta) = \frac{adj}{hyp} \newline
adj = \|proj(u, v)\|, hyp = \|u\| \newline
\Longrightarrow cos(\theta) = \frac{\|proj(u, v)\|}{\|u\|} \newline
proj(u, v) = \frac{u \cdot v}{\|v\|^2}v \newline
\Longrightarrow cos(\theta) = \frac{\|\frac{u \cdot v}{\|v\|^2}v\|}{\|u\|} \newline
cos(\theta) = \frac{\frac{\|u \cdot v\|}{\|v\|^2}\|v\|}{\|u\|} \newline
cos(\theta) = \frac{\frac{\|u \cdot v\|}{\|v\|}}{\|u\|} \newline
cos(\theta) = \frac{1}{\|u\|}\frac{\|v\|}{\|u \cdot v\|} \newline
cos(\theta) = \frac{\|v\|}{\|u\|\|u \cdot v\|} \newline
cos(\theta) = \frac{u \cdot v}{\|u\|\|v\|}
$

