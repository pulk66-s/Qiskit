# Find the invert of a NxN matrix

This is an algorith that can invert any $N \times N$ matrix named $A$. It is based on the Gauss-Jordan elimination method. The algorithm is as follows:

1. Create a matrix $M$ of size $N \times 2N$ where the first $N$ columns are the original matrix and the last $N$ columns are the identity matrix. $M=[A, I]$
2. Reduce to the Echelon form the matrix $M$. If you have a degenerate row, then the original matrix is not invertible.
3. Transform the echelon matrix expression into canonical form. This is done by reducing all the pivot elements to 1 and all the elements above and below the pivot elements to 0.
4. Now you should have the matrix $M=[I, B]$. B is the inverse of the original matrix $A$.

## Example

Let's take the $3 \times 3$ matrix $M = \begin{bmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{bmatrix}$

### Step 1

$M = \begin{bmatrix} 1 & 0 & 2 & 1 & 0 & 0 \\ 2 & -1 & 3 & 0 & 1 & 0 \\ 4 & 1 & 8 & 0 & 0 & 1 \end{bmatrix}$

### Step 2

$
M = \begin{bmatrix}
    1 & 0 & 2 & 1 & 0 & 0 \\
    2 & -1 & 3 & 0 & 1 & 0 \\
    4 & 1 & 8 & 0 & 0 & 1 
\end{bmatrix} \sim \begin{bmatrix}
    1 & 0 & 2 & 1 & 0 & 0 \\
    0 & -1 & -1 & -2 & 1 & 0 \\
    0 & 1 & 0 & -4 & 0 & 1 
\end{bmatrix} \sim \begin{bmatrix}
    1 & 0 & 2 & 1 & 0 & 0 \\
    0 & -1 & -1 & -2 & 1 & 0 \\
    0 & 0 & -1 & -6 & 1 & 1 
\end{bmatrix}
$

### Step 3

$
M = \begin{bmatrix}
    1 & 0 & 2 & 1 & 0 & 0 \\
    0 & -1 & -1 & -2 & 1 & 0 \\
    0 & 0 & -1 & -6 & 1 & 1 
\end{bmatrix} \sim \begin{bmatrix}
    1 & 0 & 2 & 1 & 0 & 0 \\
    0 & -1 & 0 & 4 & 0 & -1 \\
    0 & 0 & -1 & -6 & 1 & 1 
\end{bmatrix} \sim \begin{bmatrix}
    1 & 0 & 2 & 1 & 0 & 0 \\
    0 & 1 & 0 & -4 & 0 & 1 \\
    0 & 0 & 1 & 6 & -1 & -1 
\end{bmatrix} \sim \begin{bmatrix}
    1 & 0 & 0 & -11 & 2 & 2 \\
    0 & 1 & 0 & -4 & 0 & 1 \\
    0 & 0 & 1 & 6 & -1 & -1 
\end{bmatrix}
$

### Step 4

$
M = \begin{bmatrix}
    \begin{bmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
    \end{bmatrix} &
    \begin{bmatrix}
        -11 & 2 & 2 \\
        -4 & 0 & 1 \\
        6 & -1 & -1
    \end{bmatrix}
\end{bmatrix} \newline
\Longrightarrow B = \begin{bmatrix}
    -11 & 2 & 2 \\
    -4 & 0 & 1 \\
    6 & -1 & -1
\end{bmatrix} = A^{-1}
$


### Verification

$
A = \begin{bmatrix}
    1 & 0 & 2 \\
    2 & -1 & 3 \\
    4 & 1 & 8
\end{bmatrix} \newline
A^{-1} = \begin{bmatrix}
    -11 & 2 & 2 \\
    -4 & 0 & 1 \\
    6 & -1 & -1
\end{bmatrix} \newline
AA^{-1} = \begin{bmatrix}
    1 & 0 & 2 \\
    2 & -1 & 3 \\
    4 & 1 & 8
\end{bmatrix} \begin{bmatrix}
    -11 & 2 & 2 \\
    -4 & 0 & 1 \\
    6 & -1 & -1
\end{bmatrix} = \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
\end{bmatrix} = I
$
