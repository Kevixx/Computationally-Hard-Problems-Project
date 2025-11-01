# `SuperStringWithExpansion` Problem

---

## Problem Statement

**Problem:** [`SuperStringWithExpansion`]

### Input:
- **a)** 2 disjoint alphabets called $\Sigma$ and $\Gamma = \lbrace \gamma_1,\dots,\gamma_m \rbrace$,
- **b)** a string $s \in \Sigma^{\ast}$,
- **c)** $k$ strings $t_1,...,t_k \in (\Sigma \cup \Gamma)^{\ast}$,
- **d)** and subsets $R_1,...,R_m \subseteq \Sigma^{\ast}$, all being of finite size.

### Output:
**YES** if there is a sequence of words $r_1 \in R_1, r_2 \in R_2,...,r_m \in R_m$ such that for all $i \in \lbrace 1,...,k  \rbrace$ the so-called expansion $e(t_i)$ is a substring of $s$; the expansion $e(\gamma_j)$ of the $j$-th letter $\gamma_j \in \Gamma$, $1 \leq j \leq m$, is defined by $e(\gamma_j) := r_j$, and the expansion $e(t)$ of a whole string $t \in (\Sigma \cup \Gamma)^{\ast}$ is obtained by replacing all letters from $\Gamma$ appearing within $t$ by their expansions. Otherwise output **NO**.

---

## Formal Definitions

### Substring:
We say that $v = v_1v_2 \cdots v_{\ell_v}$ is a substring of $w = w_1w_2 \cdots w_{\ell_w}$ if there is a $j$, $1 \leq j \leq \ell_w - \ell_v + 1$, such that for all $k = 1,2,...,\ell_v$ we have $v_k = w_{j+k-1}$.

### String Replacement:
Replacing the $i$-th letter $v_i$ of the string $v = v_1v_2 \cdots v_{\ell_v}$ by the string $w = w_1w_2 \cdots w_{\ell_w}$ results in the string $v_1v_2 \cdots v_{i-1}w_1w_2 \cdots w_{\ell_w}v_{i+1}v_{i+2} \cdots v_{\ell_v}$.

---

## SWE File Format

Problem instances on the alphabets $\Sigma = \lbrace a,b,...,z  \rbrace$, $\Gamma \subseteq \lbrace A,B,...,Z  \rbrace$ are given as text files in the following SWE format:

The file is an ASCII file consisting of lines separated by the line-feed symbol; besides the line-feed, the only allowed characters in the file are numbers $\lbrace 0,1,...,9  \rbrace$, lower-case letters ($\Sigma$), upper-case letters ($\Gamma$), the colon (`:`), and the comma symbol (`,`).

### Format Structure:
1. The first line contains the number $k$`
2. The second line contains the string $s$
3. The following $k$ lines contain the strings $t_1,...,t_k$
4. The last lines (at most 26) start with a letter $\gamma_j \in \Gamma$ followed by a colon and the contents of the set $R_j$ belonging to the letter, where the elements of the set are separated by commas

### Example: test01.SWE
```
4
abdde
ABD
DDE
AAB
ABd
A:a,b,c,d,e,f,dd
B:a,b,c,d,e,f,dd
C:a,b,c,d,e,f,dd
D:a,b,c,d,e,f,dd
E:aa,bd,c,d,e
```

---

## Tasks

### a) Problem Understanding
Read and understand the problem. You do not have to comment on this in the report.

### b) Test Case Analysis
Determine whether the answer for `test01.SWE` is YES or NO and justify your solution.

- For the answer to be YES, all of the expansions must be substrings of `abdde`. 
- For the answer to be NO, at least one expansion must not be a substring of `abdde`.

Analyze the expansions of each string $t_i$:
1. For $t_1 = ABD$, valid expansions are:
   - `a` + `b` + `d` = `abd`
   - `a` + `b` + `dd` = `abdd`
   - `b` + `d` + `d` = `bdd`
   - `b` + `dd` + `e` = `bdde`
   - `d` + `d` + `e` = `dde`
    
2. For $t_2 = DDE$, valid expansions are:
   - `a` + `b` + `d` = `abd`
   - `b` + `d` + `d` = `bdd`
   - `b` + `dd` + `e` = `bdde`
   - `d` + `d` + `e` = `dde`

3. For $t_3 = AAB$, valid expansions are:
   - `a` + `b` + `d` = `abd`
   - `a` + `b` + `dd` = `abdd`
   - `b` + `d` + `d` = `bdd`
   - `b` + `dd` + `e` = `bdde`
   - `d` + `d` + `e` = `dde`

4. For $t_4 = ABd$, valid expansions are:
    - `a` + `b` + `d` = `abd`
    - `b` + `d` + `d` = `bdd`





### c) Formal Language Description
Describe the formal language that we use in the .SWE file format to represent inputs to `SuperStringWithExpansion` and describe how to solve the word problem for a word over the underlying alphabet. Note that every formal language is defined over a single alphabet only.

$$
\Pi_{file}​= \lbrace 0,…,9,a,…,z,A,…,Z,:, (',' coma) \rbrace ,
$$

Let:
- $D$ be a subset of $\Pi_{file}$ such that $D$ contains only digits $D\subset \Pi_{file} = \lbrace 0,...,9  \rbrace$
- $\Sigma$ be a subset of $\Pi_{file}$ such that $\Sigma$ contains only lower-case letters $\Sigma\subset \Pi_{file} = \lbrace a,...,z  \rbrace$
- $\Gamma$ be a subset of $\Pi_{file}$ such that $\Gamma\subset \Pi_{file} = \lbrace A,...,Z  \rbrace$

The formal language $L_{SWE}$ is defined as follows:

$$
L_{SWE} = \lbrace w \in \Pi_{file}^{\ast} | w = l_1 l_2 ... l_n, l_1 \in D^+, l_2 \in \Sigma^{\ast}, l_3,...,l_{k+2} \in (\Sigma \cup \Gamma)^{\ast}, l_{k+3},...,l_m \in \Gamma : R_j, R_j \subseteq \Sigma^{\ast}  \rbrace
$$

Where:
- $l_1$ is the first line containing the number $k$
- $l_2$ is the second line containing the string $s$
- $l_3,...,l_{k+2}$ are the following $k$ lines containing the strings $t_1,...,t_k$
- $l_{k+3},...,l_m$ are the last lines starting with a letter $\gamma_j \in \Gamma$ followed by a colon and the contents of the set $R_j$ belonging to the letter, where the elements of the set are separated by commas. The last lines should be at most 26 lines, thus $m - (k-3) \leq 26$.

### d) Decision to Optimization Algorithm Conversion
1. First we call the decision algorithm $A_d$ using the given inputs. If $A_d$ returns NO, then return $A_o$ outputs NO.
2. If the output is YES, initialize an empty list for, that we append the solution to. Process the $\gamma_j$ in order from $j = 1$ to $m$. (First For Loop)
3. Now we iterate over $r \in R_j$, create a reduced instance: (Second For Loop)
  - Replace every occurrence of $\gamma_j$ in each $t_i$ (for $i = 1$ to $k$) with the string $r$, producing new strings $t_i'$.
  - Remove $\gamma_j$ from $\Gamma$, producing $\Gamma'$.
  - Remove $R_j$ from the list of subsets, keeping $R_{j+1}, \dots, R_m$.
  - The string $s$ remains unchanged
  - Call $A_d$ on this reduced instance as follows: 
  
  $$
  (s, t_1', \dots, t_k', \Gamma', R_{j+1}, \dots, R_m)
  $$ 
  
  If $A_d$ outputs YES, fix $r_j = r$, append it to the solution list, update the current instance to this reduced one (e.g set $t_i = t_i'$ for all $i$, $\Gamma = \Gamma'$, and remove $R_j$), and proceed to $j+1$ (Continue to the First For Loop).
  - If $A_d$ outputs NO, Continue the Second Loop.
4. After fixing all $r_1$ to $r_m$, output the solution list in the required format (or NO if the initial check failed).

Note: Since the current instance is a YES instance at the start, there exists at least one $r \in R_j$ for which the reduced instance is a YES. Therefore, such an $r$ will be found.

Correctness: If the original input is a NO, $A_o$ correctly outputs NO, as seen on the 1st step. If YES, each fixation preserves the YES property, as we only choose $r$ where the reduced instance remains YES. At the end, with no $\gamma$ left, the fully expanded $t_i$ are substrings of $s$, so the sequence remains a valid solution.
Running time: Let $n$ be the input size (total bits to describe $s$, all $t_i$, and all $R_j$). The number of $A_d$ calls is at most $\sum_{j=1}^m |R_j|$, which is $O(n)$ since each element in each $R_j$ contributes $\Omega(1)$ to $n$. For each call, building the reduced instance takes time $O(n)$ in the best case, but up to $O(n^2)$ in the worst case (scanning and replacing in $t_i$, where new lengths are $O(n)$ ). Over all calls, total time is $O(n^2)$ excluding $A_d$ calls, which is polynomial. With each $A_d$ call counting as 1 step, $A_o$ runs in polynomial time.

### e) NP Membership
Show that `SuperStringWithExpansion` is in NP.

### f) NP-Completeness
> Show that `SuperStringWithExpansion (SWE)` is NP-complete. As reference problem you have to select a problem from the list of NP-complete problems given below. Note that there may be many different approaches to prove NP-completeness.

To show that `SWE` is NP-complete, two conditions must be satisfied:
1. Prove that `SWE` is in NP ( $P \in NP$ ) (proven in part _e_).
2. Prove that a NP-complete problem $P_c$ can be transformed through reduction to `SWE` in polynomial time  $P_c \leq_p P$.

For the proof we choose `1-In-3-SATISFIABILITY (1-In-3-SAT)` because of its similarity to `SWE`.

### Construction
The construct requires a polynomial-time reduction $T$ that maps any instance of `1-In-3-SAT` to an instance of `SWE` such that the original instance is satisfiable if and only if the constructed instance is a YES-instance.

Let an instance of `1-In-3-SAT` ( $K'$ ) be given by a set of $k$ clauses $C = \lbrace c_1,...,c_k  \rbrace$ over $n$ boolean variables $l_1,...,l_n$, where every clause contains exactly three literals. Each literal is either a $x_j$ or $\neg x_j$.

An instance of `SWE` ( $K'$ ) is constructed  as follows:
- Alphabet $\Sigma = \lbrace t, f, @  \rbrace$ where $t$ represents true, $f$ false, and $@$ is a separator ('# ' unavailable in math equations).
- Alphabet $\Gamma = \lbrace Y_1, Y_1', Y_2, Y_2', ..., Y_n, Y_n'  \rbrace$ where $Y_j$ represents $x_j$ and $Y_j'$ represents $\neg x_j$. There are $2n$ symbols in total.
- For every symbol in $\Gamma$, there is a corresponding set $R_i$ defined as follows for $i = 1 \text{ to } n$:
  
``` math
   R_i = \lbrace t, f \rbrace \\
   R_i' = \lbrace t, f \rbrace
```

- For every clause $c_i = (l_{i1} \lor l_{i2} \lor l_{i3})$, a template string is created$t_i = \Gamma(l_{i1}) \Gamma(l_{i2}) \Gamma(l_{i3})$ where $\Gamma(l) = Y_j$ if $l = x_j$ and $\Gamma(l) = Y_j'$ if $l = \neg x_j$.

   - For example, for the clause $C_1 = (x_1 \lor \neg x_2 \lor x_3)$, the corresponding template would be $t_1 = Y_1\;Y_2'\;Y_3$.



The string $s$ should follow the rule that every 3-letter words over $\lbrace t, f \rbrace$ contains at most one $t$ (true) (`1-In-3-SAT`). the string $s$ can include any of the following substrings: `tff`, `ftf`, `fft`. In addition, since there is a relation between the variables (regular variable and its negation), the string $s$ should include the consistency substrings `tf`, `ft` for each variable $x_j$ to ensure that both $Y_j$ and $Y_j'$ cannot be true at the same time.

The string $s$ can be constructed compactly as 

$$
   s=\text{tf@ft@tff@ftf@fft}.
$$

### Proof
To prove the correctness, we must show that the `1-In-3-SAT` instance is satisfiable if and only if the constructed `SWE` instance has a "YES" answer.

( $\Longrightarrow$ ) If $\Phi$ has a 1-in-3 satisfying assignment $a$, define for each variable $x_i$ the expansions

- $e(Y_i)=T$ iff $a(x_i)=\text{true}$,
- $e(Y_i')=F$ (the opposite value).

Then each consistency template $Y_iY_i'$ expands to either $tf$ or $ft$ (both present in $s$). Each clause template expands to one of $tff$, $ftf$, or $fft$ (exactly one literal true), all present in $s$. Hence every template expansion is a substring of $s$.

( $\Longleftarrow$ ) Conversely, if there exist expansions for all $\Gamma$-symbols such that every template expansion is a substring of $s$, then every consistency template $Y_iY_i'$ must expand to $tf$ or $ft$ (because $tt$ and $ff$ are absent from $s$). Thus $e(Y_i)\neq e(Y_i')$ for all $i$. Define the assignment $a$ by $a(x_i)=\text{true}$ iff $e(Y_i)=T$. Since every clause template expands to one of $tff$, $ftf$, or $fft$ (the only valid combinations), each clause has exactly one true literal under $a$. Therefore $\Phi$ is 1-in-3 satisfiable.

Complexity. The construction uses $O(n+k)$ symbols/templates and runs in polynomial time. Since `SWE` is in NP (verification is polynomial-time), this reduction proves NP-hardness and hence NP-completeness.


---
### g) Algorithm Design
Design an algorithm which receives an input to `SuperStringWithExpansion` in the general format given above (not restricted to .SWE format) and always gives the correct answer, i.e., which always stops and determines whether the input instance is a YES or NO instance. The algorithm is allowed to have exponential worst-case running time (i.e. bounded by $2^{p(n)}$, where $n$ is the size of the input and $p$ some polynomial), but should contain some heuristic elements that allow for faster execution on certain types of instances. For example, a heuristic may be used to quickly identify cases where the answer must be NO. Describe in natural language how the algorithm works, prove its correctness and running time, and explain the heuristic elements.

When you later implement the algorithm (part i) below), you have to restrict its inputs to .SWE files. If the instance is a NO-instance (including the input is malformed, i.e., does not comply with .SWE format), your algorithm must output NO. If it is a YES-instance, your algorithm has to construct a solution $r_1,...,r_m$ and output the solution. The format of the output should then only be a list of lines in the format $\gamma_i : r_i$, where $\gamma_i$ is an upper-case letter and $r_i$ the chosen element of $R_i$, for example (not a solution to test01.SWE):

```
A:a
B:b
C:c
D:d
E:e
```

### h) Runtime Analysis
Analyze the worst-case running time of the algorithm with respect to the general input format.

### i) Implementation
Implement the algorithm you developed in Part g). It has to be able to read inputs in .SWE format from standard input (not as a command line argument) and, as described in g), it must always solve the corresponding problem correctly by outputting a solution (or NO if no solution is possible) to standard output. It is important to use only standard input and standard output for communication, i.e., the program must not require additional command-line arguments or user interaction to read from a file etc. Failing to do so will reduce your score.

We expect you to test your code on the instances published on DTU Learn as well as on other instances. If your code does not solve all tests test01.SWE–test06.SWE on DTU Learn, you should try to improve it. The teachers will take into account the total number of solved test instances (not necessarily limited to the ones on Learn) for the final score you receive for this whole assignment.

---

## Submission Requirements

You have to submit exactly three files to the corresponding assignment on DTU Learn. Replace XX with your group number:

- **`report-group-17.pdf`**: A PDF file with your solutions to the theoretical (non-programming) parts of this project
- **`code-group-17.zip`**: The full source code of your implementation as a ZIP file; the top level of the zip file should contain the root of the project, i.e. not a single directory that contains the root of the project (hint: zip the files/directories in the root of the project, not the directory containing the whole project)
- **`readme-group-17.txt`**: An instruction how to compile and run your implementation as a text file

> **Important:** Do not duplicate files, in particular, do not include the report and readme file in the zip archive.

### Accepted programming languages:
Java, C, C++ and Python. If you prefer other languages, you have to contact the teachers. Note that the latest version submitted before the deadline will be evaluated. We reserve the right to deduce points if you do not comply with the above guidelines, including conventions for file types, file structures and names, which are case sensitive.

### Grading weights:
The three blocks **[b)–f)]**, **[g),h)]**, and **[i)]** have approximately weights of **50%**, **25%**, and **25%**, respectively, in the grading. Please state in your report the division of labor, i.e., describe the contributions of the individual group members.

---

## List of NP-complete Problems to Choose From

### Problem: [PartitionInto3-Sets]

**Input:** A sequence $X = (x_1,x_2,...,x_{3n})$ of $3n$ natural numbers, and a natural number $B$, such that $(B/4) < x_i < (B/2)$ for all $i \in \lbrace 1,2,...,3n  \rbrace$ and $\sum_{i=1}^{3n} x_i = nB$.

**Output:** YES if $X$ can be partitioned into $n$ disjoint sets $X_1,X_2,...,X_n$ such that for all $j \in \lbrace 1,2,...,n  \rbrace$ one has $\sum_{x \in X_j} x = B$.

---

### Problem: [1-In-3-Satisfiability]

**Input:** A set of clauses $C = \lbrace c_1,...,c_k  \rbrace$ over $n$ boolean variables $x_1,...,x_n$, where every clause contains exactly three literals.

**Output:** YES if there is a satisfying assignment such that every clause has exactly one true literal, i.e., if there is an assignment $a: \lbrace x_1,...,x_n \rbrace \to \lbrace 0,1  \rbrace$ such that every clause $c_j$ is satisfied and no clause has two or three satisfied literals, and NO otherwise.

---

### Problem: [MinimumCliqueCover]

**Input:** An undirected graph $G = (V,E)$ and a natural number $k$.

**Output:** YES if there is clique cover for $G$ of size at most $k$. That is, a collection $V_1,V_2,...,V_k$ of not necessarily disjoint subsets of $V$, such that each $V_i$ induces a complete subgraph of $G$ and such that for each edge $\lbrace u,v \rbrace \in E$ there is some $V_i$ that contains both $u$ and $v$. NO otherwise.

---

### Problem: [Graph-3-Coloring]

**Input:** An undirected graph $G = (V,E)$.

**Output:** YES if there is a 3-coloring of $G$ and NO otherwise. A 3-coloring assigns every vertex one of 3 colors such that adjacent vertices have different colors.

---

### Problem: [Longest-Common-Subsequence]

**Input:** A sequence $w_1,w_2,...,w_n$ of strings over an alphabet $\Sigma$ and a natural number $B$.

**Output:** YES if there is a string $x$ over $\Sigma$ of length $B$ which is a subsequence of all $w_i$. The answer is NO otherwise.

**Formal definition:** We say that $x = x_1x_2 \cdots x_{\ell_x}$ is a subsequence of $w = w_1w_2 \cdots w_{\ell_w}$ if there is a strictly increasing sequence of indices $i_j$, $1 \leq j \leq \ell_x$, such that for all $j = 1,2,...,\ell_x$ we have $x_j = w_{i_j}$.

---

### Problem: [MinimumRectangleTiling]

**Input:** An $n \times n$ array $A$ of non-negative numbers, positive integers $k$ and $B$.

**Output:** YES if there is a partition of $A$ into $k$ non-overlapping rectangular sub-arrays such that the sum of the entries every sub-array is at most $B$. NO otherwise.

---

### Problem: [Minimum Graph Transformation]

**Input:** Undirected graphs $G_1 = (V_1,E_1)$, $G_2 = (V_2,E_2)$ and an integer $k > 0$.

**Output:** YES if there is a transformation of order $k$ that makes $G_1$ isomorphic to $G_2$, and NO otherwise. A transformation of order $k$ removes $k$ existing edges from $E_1$ and then adds $k$ new edges to $E_1$.

---

### Problem: [MinimumDegreeSpanningTree]

**Input:** A graph $G = (V,E)$ and an integer $k$.

**Output:** YES if there is a spanning tree $T$ in which every node has degree at most $k$; NO otherwise.

---

**End of Exercise Project 1**
