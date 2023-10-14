$$
|\psi> = (3 + i)|0> + (1 - 2i)|1> \newline
$$
---
$$
||\psi>| = |3 + i|^2 + |1 - 2i|^2 \newline
||\psi>| = \sqrt{3^2 + 1^2}^2 + \sqrt{1^2 + (-2)^2}^2 \newline
||\psi>| = \sqrt{10}^2 + \sqrt{5}^2 \newline
||\psi>| = 15 \newline
\Longrightarrow ||\psi>| = \sqrt{15} \newline
$$
---
Normalize a qubit:
$$
\alpha = 3 + i, \beta = 1 - 2i \newline
$$
---
$$
\alpha n = \frac{\alpha}{\sqrt{|\alpha|^2 + |\beta|^2}{}} \newline
\beta n = \frac{\beta}{\sqrt{|\alpha|^2 + |\beta|^2}{}} \newline
$$
---
Application:
$$
\alpha n = \frac{3+i}{\sqrt{|3 + i|^2 + |1 - 2i|^2}{}} \newline
\alpha n = \frac{3+i}{\sqrt{\sqrt{3^2+1^2}^2 + \sqrt{1^2+(-2)^2}^2}}\newline
\Longrightarrow \alpha n = \frac{3+i}{\sqrt{15}} = \frac{3\sqrt{15}}{15} + \frac{\sqrt{15}}{15}i \newline
\beta n = \frac{1 - 2i}{\sqrt{|3 + i|^2 + |1 - 2i|^2}{}} \newline
\beta n = \frac{1-2i}{\sqrt{\sqrt{3^2+1^2}^2 + \sqrt{1^2+(-2)^2}^2}} \newline
\Longrightarrow \beta n = \frac{1-2i}{\sqrt{15}} = \frac{\sqrt{15}}{15} - \frac{2\sqrt{15}}{15}i
$$
---
Verification:
$$
|\psi> = (\frac{3\sqrt{15}}{15} + \frac{\sqrt{15}}{15}i)|0> + (\frac{\sqrt{15}}{15} - \frac{2\sqrt{15}}{15}i)|1> \newline
||\psi>| = |\frac{3\sqrt{15}}{15} + \frac{\sqrt{15}}{15}i|^2 + |\frac{\sqrt{15}}{15} - \frac{2\sqrt{15}}{15}i|^2 \newline
||\psi>| = (\sqrt{(\frac{3\sqrt{15}}{15})^2+(\frac{\sqrt{15}}{15})^2})^2 + (\sqrt{(\frac{\sqrt{15}}{15})^2+(-\frac{2\sqrt{15}}{15})^2})^2 \newline
||\psi>| = (\frac{3\sqrt{15}}{15})^2+(\frac{\sqrt{15}}{15})^2 + (\frac{\sqrt{15}}{15})^2+(-\frac{2\sqrt{15}}{15})^2 \newline
||\psi>| = \frac{9 * 15}{15 * 15} + \frac{15}{15 * 15} + \frac{15}{15 * 15} + \frac{4 * 15}{15 * 15} \newline
||\psi>| = \frac{9}{15} + \frac{1}{15} + \frac{1}{15} + \frac{4}{15} \newline
||\psi>| = \frac{15}{15} \newline
\Longrightarrow ||\psi>| = 1 \newline
$$
