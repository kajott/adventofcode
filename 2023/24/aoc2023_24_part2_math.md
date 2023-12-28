# Mathematical Solution of the AoC 2023/24 Part 2 Problem

_(originally provided by [@chschu](https://github.com/chschu), converted to Markdown with LaTeX math by [@kajott](https://github.com/kajott))_

Variables used here:
- $\overrightarrow{p_i}$ = initial position of hailstone number _i_ **[known]**
- $\overrightarrow{v_i}$ = velocity of hailstone number _i_ **[known]**
- $t_i$ = time of collision between the rock and hailstone number _i_ **[unknown]**
- $\overrightarrow{p_R}$ = initial position of the rock **[unknown]**
- $\overrightarrow{v_R}$ = velocity of the rock **[unknown]**

The basic equation for a rock-hailstone collision is:

$$
\overrightarrow{p_i} + t_i \cdot \overrightarrow{v_i} =
\overrightarrow{p_R} + t_i \cdot \overrightarrow{v_R}
$$

Rearranging for $t_i$:

$$
(\overrightarrow{p_i} - \overrightarrow{p_R}) = -t_i \cdot
(\overrightarrow{v_i} - \overrightarrow{v_R})
$$

Note that $(\overrightarrow{p_i} - \overrightarrow{p_R})$ and $(\overrightarrow{v_i} - \overrightarrow{v_R})$ are identical, up to a scale factor of $-t_i$. This means that those two vectors are **parallel**, and parallel vectors have a cross product of zero:

$$
(\overrightarrow{p_i} - \overrightarrow{p_R}) \times
(\overrightarrow{v_i} - \overrightarrow{v_R}) = \overrightarrow{0}
$$

Expanding the cross product:

$$
(\overrightarrow{p_i} \times \overrightarrow{v_i}) -
(\overrightarrow{p_i} \times \overrightarrow{v_R}) -
(\overrightarrow{p_R} \times \overrightarrow{v_i}) +
(\overrightarrow{p_R} \times \overrightarrow{v_R}) =
\overrightarrow{0}
$$

Note the following:
- sub-term $(\overrightarrow{p_i} \times \overrightarrow{v_i})$ is known for each hailstone _i_
- sub-term $(\overrightarrow{p_i} \times \overrightarrow{v_R})$ is unknown, but linear with respect to $v_R$
- sub-term $(\overrightarrow{p_R} \times \overrightarrow{v_i})$ is unknown, but linear with respect to $p_R$
- sub-term $(\overrightarrow{p_R} \times \overrightarrow{v_R})$ is unknown, not linear, but it's identical for all hailstones

With one hailstone alone, we can't do much. Let's add another one:

$$
\begin{align*}
(\overrightarrow{p_i} \times \overrightarrow{v_i}) -
(\overrightarrow{p_i} \times \overrightarrow{v_R}) -
(\overrightarrow{p_R} \times \overrightarrow{v_i}) +
(\overrightarrow{p_R} \times \overrightarrow{v_R}) & =
 \overrightarrow{0} \quad (\text{hailstone } i) \\
(\overrightarrow{p_j} \times \overrightarrow{v_j}) -
(\overrightarrow{p_j} \times \overrightarrow{v_R}) -
(\overrightarrow{p_R} \times \overrightarrow{v_j}) +
(\overrightarrow{p_R} \times \overrightarrow{v_R}) & =
 \overrightarrow{0} \quad (\text{hailstone } j)
\end{align*}
$$

Subtracting these two equations gives:

$$
(\overrightarrow{p_i} \times \overrightarrow{v_i}) -
(\overrightarrow{p_j} \times \overrightarrow{v_j}) -
(\overrightarrow{p_i} \times \overrightarrow{v_R}) +
(\overrightarrow{p_j} \times \overrightarrow{v_R}) -
(\overrightarrow{p_R} \times \overrightarrow{v_i}) +
(\overrightarrow{p_R} \times \overrightarrow{v_j}) =
 \overrightarrow{0}
$$

(Note how conveniently the problematic term $(\overrightarrow{p_R} \times \overrightarrow{v_R})$ disappears!)

Move the terms around, especially moving $(\overrightarrow{p_i} \times \overrightarrow{v_i})$ and $(\overrightarrow{p_j} \times \overrightarrow{v_j})$ to the right, as these are constant for each hailstone _i_:

$$
(\overrightarrow{p_j} \times \overrightarrow{v_R}) -
(\overrightarrow{p_i} \times \overrightarrow{v_R}) +
(\overrightarrow{p_R} \times \overrightarrow{v_j}) -
(\overrightarrow{p_R} \times \overrightarrow{v_i}) =
(\overrightarrow{p_j} \times \overrightarrow{v_j}) -
(\overrightarrow{p_i} \times \overrightarrow{v_i})
$$

Move the $\overrightarrow{p_R}$ in its cross products to the right; this means that we need to swap the signs (or, since they have opposite signs, the order) of $\overrightarrow{v_j}$ and $\overrightarrow{v_i}$ too:

$$
(\overrightarrow{p_j} \times \overrightarrow{v_R}) -
(\overrightarrow{p_i} \times \overrightarrow{v_R}) +
(\overrightarrow{v_i} \times \overrightarrow{p_R}) -
(\overrightarrow{v_j} \times \overrightarrow{p_R}) =
(\overrightarrow{p_j} \times \overrightarrow{v_j}) -
(\overrightarrow{p_i} \times \overrightarrow{v_i})
$$

Now bracket $\overrightarrow{p_R}$ and $\overrightarrow{v_R}$, and assign the remaining vectors new names:

```math
       \underbrace{(\overrightarrow{v_i} - \overrightarrow{v_j})}_{\overrightarrow{A}}
\times \underbrace{\overrightarrow{p_R}}_{\overrightarrow{P}} +
       \underbrace{(\overrightarrow{p_j} - \overrightarrow{p_i})}_{\overrightarrow{B}}
\times \underbrace{\overrightarrow{v_R}}_{\overrightarrow{V}} =
       \underbrace{(\overrightarrow{p_j} \times \overrightarrow{v_j}) -
                   (\overrightarrow{p_i} \times \overrightarrow{v_i})}_{\overrightarrow{C}}
```

At this point, $\overrightarrow{A}$, $\overrightarrow{B}$ and $\overrightarrow{C}$ are known, as they are directly derived from the parameters of hailstones _i_ and _j_. $\overrightarrow{P}$ and $\overrightarrow{V}$ are the unknowns we're trying to solve for.

Switch to component notation, resolving the cross products:

```math
\begin{align*}
A_y P_z - A_z P_y + B_y V_z - B_z V_y = C_x \\
A_z P_x - A_x P_z + B_z V_x - B_x V_z = C_y \\
A_x P_y - A_y P_x + B_x V_y - B_y V_x = C_z
\end{align*}
```

The same thing can be written in matrix notation by looking for the coefficients of all components of $\overrightarrow{V}$ and $\overrightarrow{P}$ in each equation:

```math
\begin{pmatrix}
   0 & -A_z &  A_y &    0 & -B_z &  B_y \\
 A_z &    0 & -A_x &  B_z &    0 & -B_x \\
-A_y &  A_x &    0 & -B_y &  B_x &    0
\end{pmatrix} \cdot \begin{pmatrix}
P_x \\ P_y \\ P_z \\ V_x \\ V_y \\ V_z
\end{pmatrix} = \begin{pmatrix}
C_x \\ C_y \\ C_z
\end{pmatrix}
```

Now this looks a lot like a system of linear equations, but it's underconstrained &ndash; we only have three equations for six unknowns. However, since the unknowns $\overrightarrow{P}$ and $\overrightarrow{V}$ are the same for every hailstone and only $\overrightarrow{A}$, $\overrightarrow{B}$ and $\overrightarrow{C}$ change for each pair of hailstones, we can just add **another, different pair of hailstones** (or just swap hailstone _j_ with another hailstone _k_) with new derived parameters $\overrightarrow{A'}$, $\overrightarrow{B'}$ and $\overrightarrow{C'}$ to get another set of three equations:

```math
\begin{pmatrix}
    0 &  -A_z &   A_y &     0 &  -B_z &   B_y \\
  A_z &     0 &  -A_x &   B_z &     0 &  -B_x \\
 -A_y &   A_x &     0 &  -B_y &   B_x &     0 \\
    0 & -A'_z &  A'_y &     0 & -B'_z &  B'_y \\
 A'_z &     0 & -A'_x &  B'_z &     0 & -B'_x \\
-A'_y &  A'_x &     0 & -B'_y &  B'_x &     0
\end{pmatrix} \cdot \begin{pmatrix}
P_x \\ P_y \\ P_z \\ V_x \\ V_y \\ V_z
\end{pmatrix} = \begin{pmatrix}
C_x \\ C_y \\ C_z \\ C'_x \\ C'_y \\ C'_z
\end{pmatrix}
```

This is a perfectly standard system of six linear equations with six unknowns, and it can be solved using any standard algorithm like [Gaussian Elimination](https://en.wikipedia.org/wiki/Gaussian_elimination).
