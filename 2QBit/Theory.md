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
|\psi 0> = |0.0>
$$

## Step 1

```
      Step1
0 -- h -|- cnot -- m
        |   |
1 -- x -|-- x -- h -- m
```

$$
\Alpha = |0> \newline
\Beta = |0> \newline
H\Alpha = \frac{1}{\sqrt{2}}(|0> + |1>) = \frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1> \newline
X\Beta = |1> \newline
|\psi 1> = |(\frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1>).1>
$$

## Step 2

```
               Step2
0 -- h -- cnot --|-- m
           |     |
1 -- x --- x ----|- h -- m
```

$$
\Alpha = \frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1> \newline
\Beta = |1> \newline
CNOT(\Alpha, \Beta) = \frac{1}{\sqrt{2}}|0.1> + \frac{1}{\sqrt{2}}|1.0> \newline
|\psi 2> = \frac{1}{\sqrt{2}}|0.1> + \frac{1}{\sqrt{2}}|1.0> \newline
$$

## Step 3

```
                 Step3
0 -- h -- cnot ----|- m
           |       |
1 -- x --- x -- h -|- m
```

$$
|\psi 2> = \frac{1}{\sqrt{2}}|0.1> + \frac{1}{\sqrt{2}}|1.0> \newline
|\psi 3> = H|\psi 2> \newline
\Alpha = \frac{1}{\sqrt{2}}|0.1> \newline
\Beta = \frac{1}{\sqrt{2}}|1.0> \newline
H\Alpha = \frac{1}{\sqrt{2}}|0>H|1> \newline
H\Alpha = \frac{1}{\sqrt{2}}|0>(\frac{1}{\sqrt{2}}|0> - \frac{1}{\sqrt{2}}|1>) \newline
H\Alpha = \frac{1}{\sqrt{2}}(\frac{1}{\sqrt{2}}|0.0> - \frac{1}{\sqrt{2}}|0.1>) \newline
\Longrightarrow H\Alpha = \frac{1}{2}|0.0> - \frac{1}{2}|0.1> \newline
H\Beta = \frac{1}{\sqrt{2}}|1>H|0> \newline
H\Beta = \frac{1}{\sqrt{2}}|1>(\frac{1}{\sqrt{2}}|0> + \frac{1}{\sqrt{2}}|1>) \newline
H\Beta = \frac{1}{\sqrt{2}}(\frac{1}{\sqrt{2}}|1.0> + \frac{1}{\sqrt{2}}|1.1>) \newline
\Longrightarrow H\Beta = \frac{1}{2}|1.0> + \frac{1}{2}|1.1> \newline
|\psi 3> = HA + HB \newline
\Longrightarrow |\psi 3> = \frac{1}{2}|0.0> - \frac{1}{2}|0.1> + \frac{1}{2}|1.0> + \frac{1}{2}|1.1> \newline
$$

---

Probabilities:
$$
P(0.0) = |\frac{1}{2}|^2 = \frac{1}{4} \newline
P(0.1) = |\frac{-1}{2}|^2 = \frac{1}{4} \newline
P(1.0) = |\frac{1}{2}|^2 = \frac{1}{4} \newline
P(1.1) = |\frac{1}{2}|^2 = \frac{1}{4} \newline
$$
