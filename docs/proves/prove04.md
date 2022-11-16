# CSE 280 Prove 04

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

**Section**:

**Teacher**:

## Question 1

Let $A=\lbrace 0, 2, 3 \rbrace$, $B=\lbrace 2, 3 \rbrace$, and $C=\lbrace 1, 4\rbrace$ and let the universal set $U=\lbrace 0, 1, 2, 3, 4 \rbrace$.  List the element pairs for each of the following cartesian products using these sets.  The first one is done for you.

|Cartesian Product|Answer|
|:-:|:-:|
|$A \times B$|$\lbrace (0,2), (0,3), (2,2), (2,3), (3,2), (3,3) \rbrace$|
|$B \times A$||
|$A \times B \times C$||
|$A \times \overline{A}$||
|$B^2$||

## Question 2

Which pairs (there may one pair or more than one pair) of the following sets are pairwise disjoint:

* $A =$ The set of all even numbers.
* $B =$ The set of all odd numbers.
* $C =$ The set of all non-negative powers of 2.

Hint: Make a list of numbers that are in each of these sets.

**Answer**: 

## Question 3

List all of the partitions  (how many ways can we split according to the rules) of the set $A = \lbrace a, b, c \rbrace$.

**Answer**: 


## Question 4

For each of these functions, determine if they are well-defined, one-to-one, and/or onto.  Put "Yes" or "No" in the appropriate columns.  For the first 4 problems, let $A=\lbrace 1,2,3,4 \rbrace$ and $B=\lbrace a, b, c, d \rbrace$.  For the last 4 functions written in the format $f(x)=$ you may find it helpful to graph the function on [Desmos](https://www.desmos.com/).  The first one is done for you.

|Function|Well-Defined|One-to-One|Onto|
|:-:|:-:|:-:|:-:|
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,b),(3,c),(4,d) \rbrace$|Yes|Yes|Yes|
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,a),(3,b),(4,d) \rbrace$||||
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,b),(3,c) \rbrace$||||
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,b),(2,c),(3,a),(4,a) \rbrace$||||
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^3-x$||||
|$f : \mathbf{Z} \to \mathbf{Z}, \text{ where } f(x) = -x+2$||||
|$f : \mathbf{Z}^+ \to \mathbf{Z}^+, \text{ where } f(x) = \lceil \frac {n}{2} \rceil$|||
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = \frac{5}{x-5}$||||
|$f : \lbrace x \in \mathbf{R} : x \ne 5 \rbrace, \text{ where } f(x) = \frac{5}{x-5}$||||

## Question 5

Explain why $f : \mathbf{R} \to \mathbf{R} \text{ where } f(x) = x^2$ is a well defined funtion but is niether one-to-one nor onto (with counterexamples as needed).

**Answer**:  
* Is Well Defined because ...
* Not One-to-One because ...
* Not Onto because ...

## Question 6

Find the inverse of each of the following functions, calculate $f(3)$, and then calculate the composition of $(f^{-1} \circ f)(3)$ (which will prove that you have found the correct inverse).

|Domain|$f(x)$|$f^{-1}(x)$|$f(3)$|$(f^{-1} \circ f)(3)$
|:-:|:-:|:-:|:-:|:-:|
|$f : \mathbf{R} \to \mathbf{R}$|$2x+3$||||
|$f : \lbrace x \in \mathbf{R} : x \gt 0 \rbrace \to \mathbf{R}$|$3^x$||||
|$f : \lbrace x \in \mathbf{R} : x \ge -2 \rbrace \to \mathbf{R}^+$|$x^2-2$||||


## Question 7

Create lambda functions to implement the following functions that have domain of $\mathbf{R}$ and co-domain of $\mathbf{R}$:

* $f_1(x) = x^3+x^2+x+1$
* $f_2(x) = 3x+5$
* $f_3(x) = \frac{x(x+1)}{2}$

The test code below will use the lambda functions to generate the set of all $(X, f(X))$ where $X=\lbrace x \in \mathbf{Z} : -5 \le x \le 5 \rbrace$:

```python
f1 = None # Put your lambda code here
f2 = None # Put your lambda code here
f3 = None # Put your lambda code here

domain = range(-5,6)
f1_points = {(x,f1(x)) for x in domain}
f2_points = {(x,f2(x)) for x in domain}
f3_points = {(x,f3(x)) for x in domain}

# Expected results below may be sorted differently
print(f1_points)
# {(3, 40), (-1, 0), (4, 85), (2, 15), (5, 156), (-2, -5), (-5, -104), (1, 4), (-4, -51), (-3, -20), (0, 1)}
print(f2_points)
# {(-5, -10), (-1, 2), (5, 20), (3, 14), (1, 8), (2, 11), (-3, -4), (0, 5), (4, 17), (-2, -1), (-4, -7)}
print(f3_points)
# {(0, 0.0), (-1, 0.0), (-3, 3.0), (1, 1.0), (3, 6.0), (4, 10.0), (2, 3.0), (-4, 6.0), (5, 15.0), (-2, 1.0), (-5, 10.0)}
```

