# Theory explanation

## Schema

```
0 -- h -- cnot -- m
           |
1 -- x --- x -- h -- m
```

## Step 0

```
 Step0
0 -|- h -- cnot -- m
   |        |
1 -|- x --- x -- h -- m
```

$$
|\psi_0\rangle = |00\rangle
$$

## Step 1

```
      Step1
0 -- h -|- cnot -- m
        |   |
1 -- x -|-- x -- h -- m
```

$$
|\psi_0\rangle = |00\rangle \newline
|\psi_1\rangle = H|0\rangle*X|0\rangle \newline
H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \newline
X|0\rangle = |1\rangle \newline
\Longrightarrow |\psi_1\rangle = (\frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle)|1\rangle \newline
|\psi_1\rangle = \frac{1}{\sqrt{2}}|0\rangle|1\rangle + \frac{1}{\sqrt{2}}|1\rangle|1\rangle \newline
|\psi_1\rangle = \frac{1}{\sqrt{2}}|01\rangle + \frac{1}{\sqrt{2}}|11\rangle \newline
$$

## Step 2

```
               Step2
0 -- h -- cnot --|-- m
           |     |
1 -- x --- x ----|- h -- m
```

$$
\Alpha = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle \newline
\Beta = |1\rangle \newline
CNOT(\Alpha, \Beta) = \frac{1}{\sqrt{2}}|01\rangle + \frac{1}{\sqrt{2}}|10\rangle \newline
|\psi_2\rangle = \frac{1}{\sqrt{2}}|01\rangle + \frac{1}{\sqrt{2}}|10\rangle \newline
$$

## Step 3

```
                 Step3
0 -- h -- cnot ----|- m
           |       |
1 -- x --- x -- h -|- m
```

$$
|\psi_2\rangle = \frac{1}{\sqrt{2}}|01\rangle + \frac{1}{\sqrt{2}}|10\rangle \newline
|\psi_3\rangle = \frac{1}{\sqrt{2}}|0\rangle*H|1\rangle + \frac{1}{\sqrt{2}}|1\rangle*H|0\rangle \newline
$$
---
$$
H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \newline
H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \newline
$$
---
$$
\Longrightarrow |\psi_3\rangle = \frac{1}{\sqrt{2}}|0\rangle*\frac{1}{\sqrt{2}}(|0\rangle-|1\rangle) + \frac{1}{\sqrt{2}}|1\rangle*\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle) \newline
|\psi_3\rangle = \frac{1}{2}|0\rangle*(|0\rangle-|1\rangle)+\frac{1}{2}|1\rangle*(|0\rangle+|1\rangle) \newline
|\psi_3\rangle = \frac{1}{2}(|00\rangle-|01\rangle+|10\rangle+|11\rangle) \newline
\Longrightarrow |\psi_3\rangle = \frac{1}{2}|00\rangle+\frac{1}{2}|10\rangle+\frac{1}{2}|01\rangle+\frac{1}{2}|11\rangle \newline
$$
---

Probabilities:
$$
P(00) = |\frac{1}{2}|^2 = \frac{1}{4} \newline
P(01) = |\frac{-1}{2}|^2 = \frac{1}{4} \newline
P(10) = |\frac{1}{2}|^2 = \frac{1}{4} \newline
P(11) = |\frac{1}{2}|^2 = \frac{1}{4} \newline
$$
