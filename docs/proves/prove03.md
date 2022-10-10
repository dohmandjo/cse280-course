# CSE 280 Prove 03

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

**Section**:

**Teacher**:

## Question 1

Negate each of the following logical statements by adding a negation symbol $\neg$, then apply De Morgan's Laws so that each negation symbol $\neg$ immediately prceeds a predicate.  The first one is done for you.

|Predicate|$\neg$ Predicate|
|:-:|:-:|
|$\forall x \forall y \ P(x,y)$|$\exists x \exists y \ \neg P(x,y)$|
|$\exists x \forall y \ P(x,y)$||
|$\exists x \exists y \forall z \ \neg P(x,y,z)$||
|$\forall x \exists y \forall z \ P(x,y,z)$||
|$\exists x \exists y \ (P(x,y) \land Q(x,y))$||
|$\forall x \forall y \exists z \ (P(x,y) \to Q(y,z))$||

## Question 2

Let $E$ be the set of even numbers, and let $P$ be the set of prime numbers.  Find all the values in the set formed by $E \cap P$.

**Answer**:  

## Question 3

Let the following sets be given.  The Universal set for this problem is the set of all students at some univeristy:

* $F$ = the set of all freshmen
* $M$ = the set of all math majors
* $C$ = the set of all CS majors

Translate $(F \cap M) \subseteq C$ into an english sentance.

**Answer**:


## Question 4

For each set described below, list 4 example values that would be in that set.  The first one is done for you.  Remember that $\mathbf{Z}$ represents integers and $\mathbf{Z}^+$ represents positive integers greater than 0.  The set $\mathbf{Q}$ represents rational numbers that can be represented as a fraction $\frac a b$ where $a, b \in \mathbf{Z}$.

|Set|Four Example Values in the Set|
|:-:|:-:|
|$\lbrace x \in \mathbf{Z}^+ \mid x-1 \text{ is a multiple of 7} \rbrace$||
|$\lbrace x \mid x \text{ is a fruit and its skin is normally eaten} \rbrace$||
|$\lbrace x \in \mathbf{Q} \mid \frac 1 x \in \mathbf{Z} \rbrace$||
|$\lbrace 2n \mid n \in \mathbf{Z}, n \lt 0 \rbrace$||
|$\lbrace s \mid s = 1 + 2 + ... + n \text{ for some } n \in \mathbf{Z}^+ \rbrace$||

## Question 5

Let $A = \lbrace 0, 2, 3 \rbrace$, $B = \lbrace 2, 3 \rbrace$, and $C = \lbrace 1, 5, 9 \rbrace$, and the universal set $U = \lbrace 0, 1, 2, ...,  9 \rbrace$.  Determine the resulting sets for the following operations.  The first one is done for you,

|Operation|Resulting Set|
|:-:|:-:|
|$A \cap B$|$\lbrace 2, 3 \rbrace$|
|$A \cup B$||
|$B \cup A$||
|$A \cup C$||
|$A - B$||
|$B - A$||
|$\overline{A}$||
|$\overline{C}$||
|$A \cap C$||
|$A \oplus B$||


## Question 6

In Python, you can create a set using curly braces as follows: `A = {0, 2, 3}`.  You can create any set by using `set()` and you can make a copy of a set by using `set(AnotherSet)`.  You can loop through a set in Python just like a list.  You can add to a set by calling the `add` function, remove from a set by calling the `remove` functionm, and determine if a value is in the set using the `in` operator.  Python provides functions (e.g. `union`, `intersection`, `difference`, `symmetric_difference`) as well as operators (e.g. `&`, `|`, `-`, `^`).  However instead of using these functions and operators, you want to implement `union`, `intersection`, `difference`, `compliment`, and `symmetric_difference` using loops, if statements, and reuse of these functions.  Using the comments below as guidance, implement the functions and test them with the code below.  This can be used to check your answers to the previous problem.

```python
def union(A, B):
    # Start with a new set equivalent to A
    result = set(A)

    # Loop through B to update the result
    # Add your code here

    return result

def intersection(A, B):
    # Start with an empty set
    result = set()

    # Using a loop and if statement with both sets A and B, build the resulting set
    # Add your code here

    return result

def difference(A, B):
    # Start with a new set equivalent to A
    result = set(A)

    # Using a loop and if statement with set B, update the resulting set
    # Add your code here

    return result

def compliment(U, A):
    # U = Universal Set
    # Reuse one of the functions above to implement this function
    # Refer to the definition of compliment we learned in class.
    return None  # Replace None with your code

def symmetric_difference(A, B):
    # Reuse two of the functions above to implement this function.
    # Refer to the definition of symmetric difference we learned
    # in class.
    return None  # Replace None with your code

A={0,2,3}
B={2,3}
C={1,5,9}
U={0,1,2,3,4,5,6,7,8,9}
print(intersection(A,B))
print(union(A,B))
print(union(B,A))
print(union(A,C))
print(difference(A,B))
print(difference(B,A))
print(compliment(U,A))
print(compliment(U,B))
print(intersection(A,C))
print(symmetric_difference(A,B))
```

## Question 7

In Python, you can create sets using "set comprehensions" (which is similar to "list comprehensions").  We read the following $S = \lbrace P(x) \mid x \in D \land C(x) \rbrace$ in English as "$S$ is the set of all values $P(x)$ such that $x$ is an element of the domain set $D$ and satisifies the condition $C(X)$".  We can translate this into Python code as: `S = {P(x) for x in D if C(x)}`.  The function calls `P(x)` and `C(x)` can be other defined function, other defined lambda function, or expressions written directly in the set comprehension.  Additionally, $D$ could be a set defined in a different variable or it could be provided directly in the set comprehension.

Recall the use of the `range(a,b)` function in Python to generate an iterable collections from `a` to `b-1`.

Using the starting code below to create set comprehensions as follows:

|Set ID|Set Builder Notation|
|:-:|:-:|
|Set1|$\lbrace \frac 1 n \mid n \in \lbrace 2, 4, 8, 16 \rbrace \rbrace$|
|Set2|$\lbrace n^2 \mid n \in \lbrace -2, -1, 0, 1, 2 \rbrace \rbrace$|
|Set3|$\lbrace n \mid n \in \mathbf{Z}^+ \land n \text{ is a factor of } 24 \rbrace$|
|Set4|$\lbrace n \mid n \in \mathbf{Z} \land n \ge -10 \land n \le 10 \land n \text { is odd.} \rbrace$|


```python
Set1 = None # Add Set Comprehension Code Here
Set2 = None # Add Set Comprehension Code Here
Set3 = None # Add Set Comprehension Code Here
Set4 = None # Add Set Comprehension Code Here

# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)
```