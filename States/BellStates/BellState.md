# Bell State

## Definition

$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle
$$

## Schema

```
q0: --H--v--M--
         |
q1: -----*--M--
```

$$
q0 = |0\rangle, q1 = |0\rangle
$$

## Demonstration

### Step 0

```
  Step0
q0: |--H--v--M--
    |     |
q1: |-----*--M--
```

$$
|\psi_0\rangle = |00\rangle
$$

### Step 1

```
       Step1
q0: --H-|-v--M--
        | |
q1: ----|-*--M--
```

$$
|\psi_1\rangle = H|\psi_0\rangle \newline
$$
---
$$
H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \newline
H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \newline
$$
---
$$
H|\psi_0\rangle = H|0\rangle*|0\rangle \newline
H|\psi_0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|0\rangle \newline
H|\psi_0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \newline
\Longrightarrow |\psi_1\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|10\rangle
$$

### Step 2

```
         Step2
q0: --H--v-|-M--
         | |
q1: -----*-|-M--
```

$$
|\psi_2\rangle = CNOT|\psi_1\rangle \newline
CNOT|\psi_1\rangle = CNOT(\frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|10\rangle) \newline
CNOT|\psi_1\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle \newline
\Longrightarrow |\psi_2\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle
$$

### Verification

$$
||\psi|| = \sqrt{(\frac{1}{\sqrt{2}})^2 + (\frac{1}{\sqrt{2}})^2} = 1 \newline
P(0) = (\frac{1}{\sqrt{2}})^2 = \frac{1}{2} \newline
P(1) = (\frac{1}{\sqrt{2}})^2 = \frac{1}{2} \newline
$$
