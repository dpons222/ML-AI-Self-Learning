# %% [markdown]
# # Introduction to Linear Algebra

# %% [markdown]
# ## What is Linear Algebra?
# Linear algebra is the branch of mathematics that deals with vectors, vector spaces (also known as linear spaces), linear transformations, and systems of linear equations. It forms the foundation for many areas in science and engineering, including computer graphics, machine learning, quantum physics, and more.
# 
# In essence, linear algebra provides tools to model and solve problems involving linear relationships, where variables are related by linear equations.
# 
# ## Why Learn Linear Algebra?
# Linear algebra has a wide range of applications:
# - **Machine Learning & AI:** Algorithms like linear regression, neural networks, and PCA (Principal Component Analysis) heavily rely on linear algebra.
# - **Computer Graphics:** Graphics are created through transformations, which are represented using matrices and vectors.
# - **Physics and Engineering:** Physical phenomena, such as forces, fields, and transformations, are often modeled using linear algebra.
# 
# By mastering linear algebra, you'll gain a strong mathematical foundation useful in numerous fields.
# 
# ## Fundamental Concepts in Linear Algebra
# Here's an outline of the key topics we'll cover:
# 1. **Vectors** - Understand what vectors are, their properties, and operations like addition and scalar multiplication.
# 2. **Matrices** - Introduction to matrices, matrix operations, and their use in solving systems of equations.
# 3. **Linear Transformations** - Learn about functions that map vectors to other vectors in a linear way.
# 4. **Vector Spaces** - Explore spaces formed by vectors, including concepts of basis and dimension.
# 5. **Eigenvalues and Eigenvectors** - Essential concepts for understanding matrix transformations and diagonalization.
# 6. **Orthogonality and Projections** - Understand perpendicular vectors, projections, and how they apply to least-squares solutions.
# 7. **Determinants** - Learn about determinants and their importance in determining matrix invertibility and transformations.
# 
# This roadmap will help you build a solid foundation in linear algebra, one step at a time.
# 
# ---
# 
# In the next section, we'll dive into **Vectors**, beginning with definitions and operations.
# 

# %% [markdown]
# # Vectors and Vector Operations

# %% [markdown]
# ## What is a Vector?
# A **vector** is an object that has both **magnitude** (size) and **direction**. Vectors are often used to represent quantities such as displacement, velocity, or force in physics and engineering, and they’re also fundamental in fields like computer science and machine learning.
# 
# In linear algebra, we represent vectors as ordered lists of numbers (coordinates) that define their position in space. Here’s an example of a vector in two-dimensional (2D) space:
# 
# $$
# \mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}
# $$
# 
# This vector, **v**, has components 3 and 4, representing its position along the x-axis and y-axis.

# %% [markdown]
# ### Notation
# Vectors are typically denoted by bold letters (e.g., **v**) or letters with an arrow on top (e.g., $\vec{v}$). For simplicity, we’ll use bold notation here.

# %% [markdown]
# ## Types of Vectors
# 1. **Column Vectors**: These are vectors represented in a vertical format:
#    $$
#    \mathbf{v} = \begin{bmatrix} 3 \\ 4 \\ 5 \end{bmatrix}
#    $$
# 
# 2. **Row Vectors**: These are represented in a horizontal format:
#    $$
#    \mathbf{w} = \begin{bmatrix} 3 & 4 & 5 \end{bmatrix}
#    $$
# 
# 3. **Zero Vector**: A vector where all elements are zero, often represented as **0**.
#    - Example in 3D: $$\mathbf{0} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
# 
# 4. **Unit Vector**: A vector with a magnitude of 1. It’s often used to represent direction.
# 
# ---

# %% [markdown]
# ## Vector Operations

# %% [markdown]
# ### 1. Vector Addition
# To add two vectors, add their corresponding components. If **a** = $\begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$ and **b** = $\begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$, then:
# 
# $$
# \mathbf{a} + \mathbf{b} = \begin{bmatrix} a_1 + b_1 \\ a_2 + b_2 \end{bmatrix}
# $$
# 
# **Example**:
# $$
# \begin{bmatrix} 2 \\ 3 \end{bmatrix} + \begin{bmatrix} 1 \\ 4 \end{bmatrix} = \begin{bmatrix} 3 \\ 7 \end{bmatrix}
# $$

# %% [markdown]
# ### 2. Scalar Multiplication
# In scalar multiplication, a vector is multiplied by a scalar (a single number), scaling its magnitude without changing its direction.
# 
# If **c** is a scalar and **v** = $\begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$, then:
# 
# $$
# c \cdot \mathbf{v} = \begin{bmatrix} c \cdot v_1 \\ c \cdot v_2 \end{bmatrix}
# $$
# 
# **Example**:
# $$
# 3 \cdot \begin{bmatrix} 2 \\ 5 \end{bmatrix} = \begin{bmatrix} 6 \\ 15 \end{bmatrix}
# $$

# %% [markdown]
# ### 3. Vector Subtraction
# Vector subtraction is similar to addition but subtracts the components instead. Given **a** = $\begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$ and **b** = $\begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$, we find **a** - **b** by:
# 
# $$
# \mathbf{a} - \mathbf{b} = \begin{bmatrix} a_1 - b_1 \\ a_2 - b_2 \end{bmatrix}
# $$
# 
# **Example**:
# $$
# \begin{bmatrix} 5 \\ 7 \end{bmatrix} - \begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}
# $$
# 
# ---

# %% [markdown]
# ## Magnitude of a Vector
# The **magnitude** or **length** of a vector **v** = $\begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$ in 2D space is calculated using the Pythagorean theorem:
# 
# $$
# |\mathbf{v}| = \sqrt{v_1^2 + v_2^2}
# $$
# 
# **Example**:
# For **v** = $\begin{bmatrix} 3 \\ 4 \end{bmatrix}$,
# $$
# |\mathbf{v}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
# $$
# 
# ---

# %% [markdown]
# ## Vector Dot Products
# 
# An important vector operation in linear algebra is the **dot product**. The dot product takes two vectors of equal dimensions and returns a single scalar value by summing the products of the vectors' corresponding components. This can be written out formulaically as:
# 
# $$ \mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i $$

# %% [markdown]
# ### Example of Dot Product
# 
# Let’s calculate the dot product of the vectors 
# 
# $$
# \mathbf{a} = \begin{bmatrix} 3 \\ 2 \\ -3 \end{bmatrix} 
# $$
# and 
# $$
# \mathbf{b} = \begin{bmatrix} 0 \\ -3 \\ -6 \end{bmatrix}
# $$

# %% [markdown]
# #### Step-by-step Calculation
# 
# 1. **Identify the components**:
#    - For vector $ \mathbf{a} $: 
#      - $ a_1 = 3 $, $ a_2 = 2 $, $ a_3 = -3 $
#    - For vector $ \mathbf{b} $: 
#      - $ b_1 = 0 $, $ b_2 = -3 $, $ b_3 = -6 $
# 
# 2. **Apply the dot product formula**:
# 
#    $$
#    \mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i = a_1 b_1 + a_2 b_2 + a_3 b_3
#    $$
# 
#    Substituting in the values:
# 
#    $$
#    \mathbf{a} \cdot \mathbf{b} = (3 \cdot 0) + (2 \cdot -3) + (-3 \cdot -6)
#    $$
# 
# 3. **Calculate each term**:
#    - $ 3 \cdot 0 = 0 $
#    - $ 2 \cdot -3 = -6 $
#    - $ -3 \cdot -6 = 18 $
# 
# 4. **Sum the results**:
#    $$
#    \mathbf{a} \cdot \mathbf{b} = 0 - 6 + 18 = 12
#    $$

# %% [markdown]
# #### Final Result
# 
# The dot product of $ \mathbf{a} $ and $ \mathbf{b} $ is 
# 
# $$
# \mathbf{a} \cdot \mathbf{b} = 12
# $$
# 
# ---

# %% [markdown]
# ## Unit Vector
# A **unit vector** has a magnitude of 1 and is used to indicate direction. To find the unit vector $\hat{\mathbf{v}}$ of any vector **v**, divide each component by the vector's magnitude:
# 
# $$
# \hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}
# $$
# 
# **Example**:
# For **v** = $\begin{bmatrix} 3 \\ 4 \end{bmatrix}$ with $|\mathbf{v}| = 5$,
# $$
# \hat{\mathbf{v}} = \frac{1}{5} \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}
# $$
# 
# ---

# %% [markdown]
# This section covers basic vector operations essential for understanding further topics in linear algebra. Each operation lays the foundation for working with more complex objects, such as matrices and transformations.

# %% [markdown]
# # Systems of Linear Equations

# %% [markdown]
# ## Introduction
# A **system of linear equations** is a collection of one or more linear equations involving the same variables. The aim is to find values of the variables that satisfy all equations in the system. Solving systems of linear equations has wide-ranging applications in fields like engineering, physics, economics, and computer science.

# %% [markdown]
# ### Example of a System of Linear Equations
# Consider the following system of equations:
# $$
# \begin{cases}
# 2x + 3y = 8 \\
# x - y = -1
# \end{cases}
# $$
# 
# Here, we have two equations with two variables, $x$ and $y$. We’ll find the values of $x$ and $y$ that satisfy both equations simultaneously.
# 
# ---

# %% [markdown]
# ## Types of Solutions
# 1. **Unique Solution**: The system has exactly one solution.
# 2. **No Solution**: The system has no solution (the lines are parallel).
# 3. **Infinitely Many Solutions**: The system has an infinite number of solutions (the lines overlap).
# 
# ---

# %% [markdown]
# ## Methods of Solving Systems of Linear Equations

# %% [markdown]
# ### 1. Substitution Method
# 1. Solve one equation for one variable in terms of the other.
# 2. Substitute this expression into the other equation.
# 3. Solve for the remaining variable, then back-substitute to find the other variable.

# %% [markdown]
# #### Example
# Consider:
# $$
# \begin{cases}
# x + 2y = 5 \\
# 3x - y = 4
# \end{cases}
# $$
# 
# 1. **Solve the first equation for $x$**:
#    $$
#    x = 5 - 2y
#    $$
# 
# 2. **Substitute into the second equation**:
#    $$
#    3(5 - 2y) - y = 4
#    $$
#    Expanding gives:
#    $$
#    15 - 6y - y = 4
#    $$
#    Simplifying yields:
#    $$
#    15 - 7y = 4 \implies -7y = -11 \implies y = \frac{11}{7}
#    $$
# 
# 3. **Back-substitute $y = \frac{11}{7}$ into $x = 5 - 2y$**:
#    $$
#    x = 5 - 2 \cdot \frac{11}{7} = 5 - \frac{22}{7} = \frac{35 - 22}{7} = \frac{13}{7}
#    $$
# 
# **Solution**: $x = \frac{13}{7}$, $y = \frac{11}{7}$.
# 
# ---

# %% [markdown]
# ### 2. Elimination Method
# 1. Multiply equations if necessary to align the coefficients of one variable.
# 2. Add or subtract equations to eliminate that variable.
# 3. Solve the resulting equation for the remaining variable.

# %% [markdown]
# #### Example
# Solve:
# $$
# \begin{cases}
# 2x + 3y = 8 \\
# 4x - 3y = 2
# \end{cases}
# $$
# 
# 1. **Add the equations to eliminate $y$**:
#    $$
#    (2x + 3y) + (4x - 3y) = 8 + 2
#    $$
#    Simplifying gives:
#    $$
#    6x = 10 \implies x = \frac{10}{6} = \frac{5}{3}
#    $$
# 
# 2. **Substitute $x = \frac{5}{3}$ back into the first equation**:
#    $$
#    2\left(\frac{5}{3}\right) + 3y = 8
#    $$
#    Simplifying yields:
#    $$
#    \frac{10}{3} + 3y = 8
#    $$
#    Converting $8$ to a fraction:
#    $$
#    3y = 8 - \frac{10}{3} = \frac{24 - 10}{3} = \frac{14}{3}
#    $$
#    Thus:
#    $$
#    y = \frac{14}{9}
#    $$
# 
# **Solution**: $x = \frac{5}{3}$, $y = \frac{14}{9}$.
# 
# ---

# %% [markdown]
# ### 3. Matrix Method (Augmented Matrices)
# For larger systems, we can use an **augmented matrix** and apply **Gaussian elimination** or **Gauss-Jordan elimination** to solve the system.
# 
# Consider:
# $$
# \begin{cases}
# x + y = 3 \\
# 2x - y = 1
# \end{cases}
# $$

# %% [markdown]
# #### Steps
# 1. **Write as an augmented matrix**:
#    $$
#    \begin{bmatrix} 1 & 1 & | & 3 \\ 2 & -1 & | & 1 \end{bmatrix}
#    $$
# 
# 2. **Eliminate $x$ from the second row**:
#    - Replace Row 2 with $ \text{Row 2} - 2 \times \text{Row 1} $:
#    $$
#    \begin{bmatrix} 1 & 1 & | & 3 \\ 0 & -3 & | & -5 \end{bmatrix}
#    $$
# 
# 3. **Solve for $y$ in Row 2**:
#    $$
#    -3y = -5 \implies y = \frac{5}{3}
#    $$
# 
# 4. **Substitute $y = \frac{5}{3}$ back into Row 1**:
#    $$
#    x + frac{5}{3} = 3 \implies x = 3 - frac{5}{3} = frac{9 - 5}{3} = frac{4}{3}
#    $$
# 
# **Solution**: $x = \frac{4}{3}$, $y = \frac{5}{3}$.
# 
# ---

# %% [markdown]
# ## Practice Problems
# 1. Solve using substitution:
#    $$
#    \begin{cases}
#    3x + 2y = 12 \\
#    x - 4y = -2
#    \end{cases}
#    $$
# 
# 2. Solve using elimination:
#    $$
#    \begin{cases}
#    4x + 3y = 24 \\
#    2x - 3y = -6
#    \end{cases}
#    $$
# 
# 3. Solve using matrix methods:
#    $$
#    \begin{cases}
#    5x + 2y = 8 \\
#    3x - y = 1
#    \end{cases}
#    $$

# %% [markdown]
# 
# 
# This concludes the introduction to systems of linear equations and solving them using substitution, elimination, and matrix methods.
# 

# %% [markdown]
# %% [markdown]
# # Matrix Operations
# Matrix operations are essential for manipulating and solving systems of equations, as well as for transforming data in various applications like computer graphics and machine learning. Below are the fundamental matrix operations you'll encounter.
#
# %% [markdown]
# ## 1. Matrix Addition
# To add two matrices of the same dimensions, simply add their corresponding elements.
#
# If **A** and **B** are two matrices of size $m \times n$:
#
# $$
# \mathbf{C} = \mathbf{A} + \mathbf{B} \implies c_{ij} = a_{ij} + b_{ij}
# $$
#
# **Example**:
#
# $$
# \mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} \implies \mathbf{C} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}
# $$

# %% [markdown]
# ## 2. Matrix Subtraction
# Similar to addition, matrix subtraction is performed by subtracting corresponding elements of two matrices of the same size.
#
# If **A** and **B** are two matrices of size $m \times n$:
#
# $$
# \mathbf{C} = \mathbf{A} - \mathbf{B} \implies c_{ij} = a_{ij} - b_{ij}
# $$
#
# **Example**:
#
# $$
# \mathbf{A} = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \implies \mathbf{C} = \begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix}
# $$

# %% [markdown]
# ## 3. Scalar Multiplication
# To multiply a matrix by a scalar, multiply each element of the matrix by that scalar.
#
# If **A** is a matrix and **c** is a scalar:
#
# $$
# \mathbf{B} = c \cdot \mathbf{A} \implies b_{ij} = c \cdot a_{ij}
# $$
#
# **Example**:
#
# $$
# c = 2, \quad \mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \implies \mathbf{B} = \begin{bmatrix} 2 & 4 \\ 6 & 8 \end{bmatrix}
# $$

# %% [markdown]
# ## 4. Matrix Multiplication
# Matrix multiplication is more complex than addition or subtraction. To multiply two matrices, the number of columns in the first matrix must equal the number of rows in the second matrix. The result is a new matrix where each element is the dot product of a row from the first matrix and a column from the second matrix.
#
# If **A** is an $m \times n$ matrix and **B** is an $n \times p$ matrix, then the product **C** is an $m \times p$ matrix:
#
# $$
# \mathbf{C} = \mathbf{A} \cdot \mathbf{B} \implies c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
# $$
#
# **Example**:
#
# $$
# \mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} \implies \mathbf{C} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
# $$

# %% [markdown]
# ## 5. Transpose of a Matrix
# The transpose of a matrix is obtained by flipping it over its diagonal, switching the row and column indices of each element.
#
# If **A** is an $m \times n$ matrix:
#
# $$
# \mathbf{A}^T = \begin{bmatrix} a_{11} & a_{21} & \cdots & a_{m1} \\ a_{12} & a_{22} & \cdots & a_{m2} \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n} & a_{2n} & \cdots & a_{mn} \end{bmatrix}
# $$
#
# **Example**:
#
# $$
# \mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \implies \mathbf{A}^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
# $$

# %% [markdown]
# ## 6. Inverse of a Matrix
# The inverse of a square matrix **A** is denoted as **A**⁻¹ and satisfies the equation:
#
# $$
# \mathbf{A} \cdot \mathbf{A}^{-1} = \mathbf{I}
# $$
#
# where **I** is the identity matrix. Not all matrices have inverses; a matrix must be square and have a non-zero determinant to have an inverse.
#
# **Example**:
# For a 2x2 matrix:
#
# $$
# \mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies \mathbf{A}^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
# $$

# %% [markdown]
# ## Conclusion
# Understanding matrix operations is crucial for working with data in various scientific and engineering applications. Mastery of these operations will enable you to solve complex systems of equations and perform transformations effectively.



# %% [markdown]
# # Determinants

# %% [markdown]
# # Vector Spaces and Subspaces

# %% [markdown]
# # Basis and Dimension

# %% [markdown]
# # Linear Transformations

# %% [markdown]
# # Eigenvalues and Eigenvectors

# %% [markdown]
# # Orthogonality and Orthogonal Bases

# %% [markdown]
# # Applications and Advanced Topics


