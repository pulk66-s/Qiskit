## Application de la porte d'Hadamar

$$|\psi> = i|0> + (2 + i)|1>$$
$$H|\psi> = iH|0> + (2 + i)H|1>$$
$$H|\psi> = \frac{i}{\sqrt{2}}(|0> + |1>) + \frac{(2 + i)}{\sqrt{2}}(|0> - |1>)$$
$$H|\psi> = \frac{i|0>}{\sqrt{2}} + \frac{i|1>}{\sqrt{2}} + \frac{(2 + i)|0>}{\sqrt{2}} - \frac{(2 + i)|1>}{\sqrt{2}}$$
$$H|\psi> = \frac{i|0> + i|1> + (2 + i)|0> - (2 + i)|1>}{\sqrt{2}}$$
$$H|\psi> = \frac{(2 + 2i)|0> - (2 + 2i)|1>}{\sqrt{2}}$$
$$H|\psi> = \frac{(2 + 2i)}{\sqrt{2}}|0> - \frac{(2 + 2i)}{\sqrt{2}}|1>$$
$$H|\psi> = (\frac{2}{\sqrt{2}} + \frac{2}{\sqrt{2}}i)|0> - (\frac{2}{\sqrt{2}} + \frac{2i}{\sqrt{2}})|1>$$

## Hadammar for different values

### H |0>
---
$$H|0> = \frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1>$$
$$\Longrightarrow |H|0>|^2 = (\frac{1}{\sqrt{2}})^2 + (\frac{1}{\sqrt{2}})^2 = 1$$

### H |1>
---
$$H|1> = \frac{1}{\sqrt{2}}|0> - \frac{1}{\sqrt{2}}|1>$$
$$\Longrightarrow |H|1>|^2 = (\frac{1}{\sqrt{2}})^2 + (\frac{-1}{\sqrt{2}})^2 = 1$$

### H |PSI>
---

$$H|\psi> = \frac{\alpha}{\sqrt{2}}(|0> + |1>) + \frac{\beta}{\sqrt{2}}(|0> - |1>)$$
$$H|\psi> = \frac{\alpha}{\sqrt{2}}|0> + \frac{\alpha}{\sqrt{2}}|1> + \frac{\beta}{\sqrt{2}}|0> - \frac{\beta}{\sqrt{2}}|1>$$
$$H|\psi> = \frac{\alpha + \beta}{\sqrt{2}}|0> + \frac{\alpha - \beta}{\sqrt{2}}|1>$$
$$\Longrightarrow P|0> = \frac{\alpha + \beta}{\sqrt{2}}, P|1> = \frac{\alpha - \beta}{\sqrt{2}}$$

# Differents gates

## X gate (NOT)

$$X|0> = |1>$$
$$X|1> = |0>$$
$$|\psi> = \alpha|0> + \beta|1> \newline \Longrightarrow X|\psi> = \alpha X|0> + \beta X|1>$$
$$X|\psi> = \beta|0> + \alpha|1>$$

$$
X = \begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
\newline
|0> = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, |1> = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\newline
X|1> = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0*0+1*1 \\ 1*0+0*1 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = |0>\newline
X|0> = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0*1+1*0 \\ 1*1+0*0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |1> \newline
X|\psi> = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \begin{pmatrix} 0*\alpha+1*\beta \\ 1*\alpha+0*\beta \end{pmatrix} = \begin{pmatrix} \beta \\ \alpha \end{pmatrix} \newline
$$



## Hadammar gate

$$|\psi> = \alpha|0> + \beta|1> \Longrightarrow H|\psi> = \alpha H|0> + \beta H|1>$$
$$H|0> = \frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1>$$
$$H|1> = \frac{1}{\sqrt{2}}|0> - \frac{1}{\sqrt{2}}|1>$$

$$\Longrightarrow H|\psi> = \frac{\alpha}{\sqrt{2}}|0> + \frac{\alpha}{\sqrt{2}}|1> + \frac{\beta}{\sqrt{2}}|0> - \frac{\beta}{\sqrt{2}}|1>$$
$$\Longrightarrow H|\psi> = \frac{\alpha+\beta}{\sqrt{2}}|0> + \frac{\alpha-\beta}{\sqrt{2}}|1>$$

$$
H = \begin{pmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{pmatrix} \newline
H|0> = \begin{pmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}}*1+\frac{1}{\sqrt{2}}*0 \\ \frac{1}{\sqrt{2}}*1-\frac{1}{\sqrt{2}}*0 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix} = \frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1> \newline
H|1> = \begin{pmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}}*0+\frac{1}{\sqrt{2}}*1 \\ \frac{1}{\sqrt{2}}*0-\frac{1}{\sqrt{2}}*1 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \end{pmatrix} = \frac{1}{\sqrt{2}}|0> - \frac{1}{\sqrt{2}}|1> \newline
H|\psi> = \begin{pmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}}*\alpha+\frac{1}{\sqrt{2}}*\beta \\ \frac{1}{\sqrt{2}}*\alpha-\frac{1}{\sqrt{2}}*\beta \end{pmatrix} = \begin{pmatrix} \frac{\alpha+\beta}{\sqrt{2}} \\ \frac{\alpha-\beta}{\sqrt{2}} \end{pmatrix} = \frac{\alpha+\beta}{\sqrt{2}}|0> + \frac{\alpha-\beta}{\sqrt{2}}|1> \newline
$$


### Example

$$|\psi> = \frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1>$$
---
$$H|\psi> = \frac{1}{\sqrt{2}}H|0> + \frac{1}{\sqrt{2}}H|1> = \frac{1}{\sqrt{2}}(\frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1>) + \frac{1}{\sqrt{2}}(\frac{1}{\sqrt{2}}|0> - \frac{1}{\sqrt{2}}|1>)$$
Naive method
$$\Longrightarrow H|\psi> = \frac{1}{\sqrt{2}} * \frac{1}{\sqrt{2}}(|0> + |1>) + \frac{1}
{\sqrt{2}} * \frac{1}{\sqrt{2}}(|0> - |1>)$$
$$\Longrightarrow H|\psi> = \frac{1}{2}(|0> + |1>) + \frac{1}{2}(|0> - |1>)$$
$$\Longrightarrow H|\psi> = \frac{1}{2}|0> + \frac{1}{2}|1> + \frac{1}{2}|0> - \frac{1}{2}|1>$$
$$\Longrightarrow H|\psi> = |0>$$
---
Using formula method
$$\Longrightarrow H|\psi> = \frac{\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}}{\sqrt{2}}|0> + \frac{\frac{1}{\sqrt{2}}-\frac{1}{\sqrt{2}}}{\sqrt{2}}|1>$$
$$\Longrightarrow H|\psi> = \frac{\frac{2}{\sqrt{2}}}{\sqrt{2}}|0> = \frac{\frac{2\sqrt{2}}{2}}{\sqrt{2}}|0> = \frac{\sqrt{2}}{\sqrt{2}}|0>$$
$$\Longrightarrow H|\psi> = |0>$$

---

### Resume

$$H|0> = \frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1>, P(0) = |\frac{1}{\sqrt{2}}|^2 = \frac{1}{2}, P(1) = |-\frac{1}{\sqrt{2}}|^2 = \frac{1}{2}$$
$$H|1> = \frac{1}{\sqrt{2}}|0> - \frac{1}{\sqrt{2}}|1>, P(0) = |\frac{1}{\sqrt{2}}|^2 = \frac{1}{2}, P(1) = |-\frac{1}{\sqrt{2}}|^2 = \frac{1}{2}$$
$$H|\psi> = \frac{\alpha+\beta}{\sqrt{2}}|0> + \frac{\alpha-\beta}{\sqrt{2}}|1>$$
$$\Longrightarrow P(0) = |\frac{\alpha+\beta}{\sqrt{2}}|^2 = \frac{(\alpha+\beta)^2}{2} \newline \Longrightarrow P(1) = |\frac{\alpha-\beta}{\sqrt{2}}|^2 = \frac{(\alpha-\beta)^2}{2}$$

## Y gate

$$Y|0> = i|1>$$
$$Y|1> = -i|0>$$
$$
Y = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix} \newline
Y|0> = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix} \begin{pmatrix}1 \\ 0\end{pmatrix} = \begin{pmatrix}0*1+-i*0 \\ i*1+0*0\end{pmatrix} = \begin{pmatrix}0 \\ i\end{pmatrix} = i|1> \newline
Y|1> = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix} \begin{pmatrix}0 \\ 1\end{pmatrix} = \begin{pmatrix}0*-i+-i*1 \\ i*0+0*1\end{pmatrix} = \begin{pmatrix}-i \\ 0\end{pmatrix} = -i|0> \newline
Y|\psi> = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix} \begin{pmatrix}\alpha \\ \beta\end{pmatrix} = \begin{pmatrix}0*\alpha+-i*\beta \\ i*\alpha+0*\beta\end{pmatrix} = \begin{pmatrix}-i\beta \\ i\alpha\end{pmatrix} = i\alpha|1> - i\beta|0> \newline
$$

## Z gate

$$Z|0> = |0>$$
$$Z|1> = -|1>$$

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \newline
Z|0> = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1*1+0*0 \\ 0*1+-1*0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = |0> \newline
Z|1> = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1*0+0*1 \\ 0*0+-1*1 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix} = -|1> \newline
Z|\psi> = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \begin{pmatrix} 1*\alpha+0*\beta \\ 0*\alpha+-1*\beta \end{pmatrix} = \begin{pmatrix} \alpha \\ -\beta \end{pmatrix} = \alpha|0> - \beta|1> \newline
$$