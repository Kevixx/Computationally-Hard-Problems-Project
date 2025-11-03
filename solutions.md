# `SuperStringWithExpansion` Problem

---

### b) Test Case Analysis - **Bozhidar**

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

### c) Formal Language Description - **Bozhidar**

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

### d) Decision to Optimization Algorithm Conversion - **Pinac**

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

### e) NP Membership - **Pinac**

As mentioned in the question, the problem is a decision problem. Let R be interpreted from Random Bits. We define the certificate $R$. as a sequence of choices for $r_1 \in R_1, \dots, r_m \in R_m$. Since each $R_j$ is finite and listed in the input, we can encode the choice of each $r_j$ by an index into $R_j$ (requiring $O(\log |R_j|)$ bits per $j$). As $|R_j| \leq n$ (bounded by input size) and $m \leq n$, the total length of $R$ is $O(m \log n) = O(n \log n)$, which is polynomial in $n$.

The algorithm $A(X, R)$ is as follows (deterministic verifier, where $R$ is randomized):

1. First, we'll parse R to pull out the selected choices r1​,…,rm​ based on the indices provided. If any index doesn't match up with its corresponding Rj, we simply output NO.
2. For each $i = 1$ to $k$:
   - Compute the expansion $e(t_i)$ by replacing every occurrence of $\gamma_j$ in $t_i$ with $r_j$, leaving symbols from $\Sigma$ unchanged.
   - Check if $e(t_i)$ is a substring of $s$
3. If all $k$ expansions are substrings of $s$, output YES; otherwise, output NO.

If $X$ is a YES-instance, there exists at least one sequence $r_1, \dots, r_m$ such that all $e(t_i)$ are substrings of $s$. The corresponding $R$ (encoding those choices) makes $A(X, R) =$ YES, so $\Pr[A(X, R) = \text{YES}] > 0$ at least one good $R$ out of $2^{O(n \log n)}$.
If $X$ is a NO-instance, no such sequence exists, so for all $R$, $A(X, R) =$ NO, hence $\Pr[A(X, R) = \text{NO}] = 1$.

### f) NP-Completeness - **Bozhidar**

> Show that `SuperStringWithExpansion (SWE)` is NP-complete. As reference problem you have to select a problem from the list of NP-complete problems given below. Note that there may be many different approaches to prove NP-completeness.

To show that `SWE` is NP-complete, two conditions must be satisfied:

1. Prove that `SWE` is in NP ( $P \in NP$ ) (proven in part _e_).
2. Prove that a NP-complete problem $P_c$ can be transformed through reduction to `SWE` in polynomial time  $P_c \leq_p P$.

For the proof we choose `1-In-3-SATISFIABILITY (1-In-3-SAT)` because of its similarity to `SWE`.

#### Problem: [1-In-3-Satisfiability]

**Input:** A set of clauses $C = \lbrace c_1,...,c_k  \rbrace$ over $n$ boolean variables $x_1,...,x_n$, where every clause contains exactly three literals.

**Output:** YES if there is a satisfying assignment such that every clause has exactly one true literal, i.e., if there is an assignment $a: \lbrace x_1,...,x_n \rbrace \to \lbrace 0,1  \rbrace$ such that every clause $c_j$ is satisfied and no clause has two or three satisfied literals, and NO otherwise.


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

- For every clause $c_i = (l_{i1} \lor l_{i2} \lor l_{i3})$, a template string is created $t_i = \Gamma(l_{i1}) \Gamma(l_{i2}) \Gamma(l_{i3})$ where $\Gamma(l) = Y_j$ if $l = x_j$ and $\Gamma(l) = Y_j'$ if $l = \neg x_j$.

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

### g) Algorithm Design **Kevin**

Design an algorithm which receives an input to `SuperStringWithExpansion` in the general format given above (not restricted to .SWE format) and always gives the correct answer, i.e., which always stops and determines whether the input instance is a YES or NO instance. The algorithm is allowed to have exponential worst-case running time (i.e. bounded by $2^{p(n)}$, where $n$ is the size of the input and $p$ some polynomial), but should contain some heuristic elements that allow for faster execution on certain types of instances. For example, a heuristic may be used to quickly identify cases where the answer must be NO. Describe in natural language how the algorithm works, prove its correctness and running time, and explain the heuristic elements.

When you later implement the algorithm (part i) below), you have to restrict its inputs to .SWE files. If the instance is a NO-instance (including the input is malformed, i.e., does not comply with .SWE format), your algorithm must output NO. If it is a YES-instance, your algorithm has to construct a solution $r_1,...,r_m$ and output the solution. The format of the output should then only be a list of lines in the format $\gamma_i : r_i$, where $\gamma_i$ is an upper-case letter and $r_i$ the chosen element of $R_i$, for example (not a solution to test01.SWE):

```
A:a
B:b
C:c
D:d
E:e
```

1. Input Parsing

Read .SWE file from standard input (later in i)).
Parse:

First line: $k \in \mathbb{N}$, number of patterns.
Second line: $s \in \Sigma^*$, target string.
Next $k$ lines: patterns $t_1, \dots, t_k \in (\Sigma \cup \Gamma)^*$.
Remaining lines: for each $\gamma_j \in \Gamma$, line $\gamma_j : r_{j1}, r_{j2}, \dots$.

Tokenization rule: Consecutive lowercase letters form a single token (e.g., dd → one token).

1. Preprocessing
For each pattern $t_i$:

Split into tokens: lowercase sequences and uppercase letters are separate.
Build $\text{options}[i][j]$: list of possible expansions for token $j$ in pattern $i$.

If token is lowercase string $w$, then $\text{options}[i][j] = [w]$.
If token is $\gamma \in \Gamma$, then $\text{options}[i][j] = R_\gamma$.
If unknown → empty list → immediate NO.

Let $P_i$ = number of tokens in pattern $i$, $|R_\gamma|$ = size of expansion set.

3. Backtracking Search (per pattern)
For each pattern $t_i$, solve:

Find assignment $r_1, \dots, r_{P_i}$ such that $e(t_i) = r_1 \cdots r_{P_i}$ is a substring of $s$.

Backtracking procedure:
```python
      backtrack(idx, current_string, path):
          if idx == len(tokens):
              if current_string in s:  # substring check
                  record path

              return
          for choice in options[idx]:
              new_str = current_string + choice

              if s.find(new_str) == -1:  # early pruning
                  continue

              backtrack(idx + 1, new_str, path + [choice])

              if found: early exit (first solution)
```            
Heuristic Pruning (Key Optimization):

At each step, after appending a choice, check if the prefix so far appears anywhere in $s$ using str.find().
If not → prune entire branch → avoids expanding impossible paths.
This is sound (no valid solution missed) and effective when $s$ is short or patterns grow quickly.

4. Sequential Processing

Process patterns one at a time.
If any pattern has no valid expansion → return NO.
Otherwise, collect the first valid assignment per uppercase token across all patterns.

5. Output

If all patterns succeed: output lines $\gamma: r$ for each chosen expansion of $\gamma$.
Else: output NO.

**Correctness Proof**

Soundness:

Only record a path if the fully expanded string is a substring of $s$ (checked explicitly). All expansions respect $R_j$.
Completeness:
Backtracking explores all combinations of expansions. Early pruning only skips prefixes not in $s$, but any valid full string must have all prefixes in $s$ → no valid solution is missed.

Termination:

Finite search space → terminates.

**Running Time (Worst Case)**

Let:

$n = |s| + \sum |t_i| + \sum |R_j|$ = total input size.

$d = \max_j |R_j|$, maximum expansion set size.

$\ell = \max_i$ (number of tokens in $t_i$).

Then for one pattern: $O(d^\ell)$ calls, each doing $O(n)$ substring check → $O(d^\ell \cdot n)$.
Total: $k$ patterns →
$$T(n) \leq k \cdot d^\ell \cdot n = O(2^{p(n)})$$
since $\ell \leq n$, $d \leq n$, $k \leq n$ → exponential, but allowed.

**Heuristic Elements**

Prefix pruning:
- s.find(current + choice) → eliminates impossible paths early.
- First-solution early exit: stop after finding one valid expansion per pattern.
- Process patterns sequentially: fail fast on first unsatisfiable pattern.

These make the algorithm fast in practice on small/structured instances (e.g., test01.SWE), despite worst-case exponential.

### h) Runtime Analysis - **Kevin**

Analyze the worst-case running time of the algorithm with respect to the general input format.

Worst-Case Running Time (General Input)
Let:

$s \in \Sigma^*$: target string, $n_s = |s|$

$k$: number of patterns $t_1, \dots, t_k$

$t_i \in (\Sigma \cup \Gamma)^*$: $\newline$
each pattern, let $ n_t = \sum_{i=1}^k |t_i|$

$\Gamma = \{\gamma_1, \dots, \gamma_m\}$, $R_j \subseteq \Sigma^*$:$\newline$
finite expansion sets

$n_R = \sum_{j=1}^m |R_j|$:$\newline$ total number of expansion strings

Total input size:
$$n = n_s + n_t + n_R$$

For pattern $t_i$:

Split into tokens:<br/>
consecutive lowercase letters → one token;<br>uppercase → one token.$\newline$

Let $\ell_i$ = number of tokens in $t_i$

Let:

$d = \max_j |R_j|$ = maximum expansion set size<br>

Then number of possible expansions of $t_i$:
$$\prod_{\text{variable tokens}} |R_\gamma| \leq d^{\ell_i} \leq d^n$$

Each node: $O(n_s)$ time for find().<br>
Total per pattern: $O(d^n \cdot n_s)$
Over $k \leq n$ patterns:
$$T(n) = O(k \cdot d^n \cdot n_s) = O(n \cdot d^n \cdot n) = O(n^2 \cdot d^n)$$
Since $d \geq 2$ possible,
$$T(n) \in O(2^{p(n)})\ \text{for some polynomial } p$$
Conclusion: Exponential in input size, as required.

### i) Implementation **Kevin** and **Pinac**

Implement the algorithm you developed in Part g). It has to be able to read inputs in .SWE format from standard input (not as a command line argument) and, as described in g), it must always solve the corresponding problem correctly by outputting a solution (or NO if no solution is possible) to standard output. It is important to use only standard input and standard output for communication, i.e., the program must not require additional command-line arguments or user interaction to read from a file etc. Failing to do so will reduce your score.

We expect you to test your code on the instances published on DTU Learn as well as on other instances. If your code does not solve all tests test01.SWE–test06.SWE on DTU Learn, you should try to improve it. The teachers will take into account the total number of solved test instances (not necessarily limited to the ones on Learn) for the final score you receive for this whole assignment.

Implemented code can be found in path `/code-group-17/code-group-17.py`

---
