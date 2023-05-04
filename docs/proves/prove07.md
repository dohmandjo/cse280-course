# CSE 280 Prove 07

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

**Section**:

**Teacher**:

## Question 1

Find the $gcd$ for each of the following by hand using Eulid's Algorithm  Show your work in the tables below.  The first one is done for you.  Add more rows to each table as needed.  You can check your work with a calculator.

**Problem A**: $gcd(43,57)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|43|57|14|
|14|43|1|
|1|14|0|

Answer: 1

**Problem B**: $gcd(39,501)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
||||
||||
||||

Answer: 

**Problem C**: $gcd(110,765)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
||||
||||
||||

Answer: 

**Problem D**: $gcd(443,899)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
||||
||||
||||

Answer: 

## Question 2

Find the $gcd$ for the first three problems from Question 1 using the Extended Eulcid Algorithm to express the answer as a linear combination.  The first one is done for you.

|Problem|$gcd = s*x + t*y$|
|:-:|:-:|
|$gcd(43,57)$|$1 = 4*43 - 3*57$|
|$gcd(39,501)$||
|$gcd(110,765)$||


## Question 3

Find the multiplicative inverse for $x \text{ mod } n$ in the table below.  These numbers are smaller so you don't need to use the Extended Euclidean Algorithm to solve.  You can check your answers by verifying that $sx \text{ mod } n = 1$ where $s$ is the multiplicative inverse you calculated.

|$x$|$n$|Multiplicative Inverse|
|:-:|:-:|:-:|
|2|7||
|5|11||
|7|20||
|3|13||

## Question 4
Use the Extended Euclidean Algorithm to find the multiplicative inverse of $83 \text{ mod } 96$.  You can check your answer by verifying that $s*83 \text{ mod } 96 = 1$ where $s$ is the multiplicative inverse you calculated.  

In your answer, provide both the linear combination of $1 = s*83 + t*96$ and the multiplicative inverse derived from it.

Answers:
* $s = $
* $t = $
* Multiplicative Inverse = 

## Question 5

The python code below implements the Extended Euclidean Algorithm with function `gcd_ext`.  The result of the `gcd_ext(x,y)` function is a 3 element tuple `(r,s,t)` where $r = s*x + t*y$.  For example, `gcd_ext(83,96)` will result in `(1,-37,32)` which represents $1 = -37*86 + 32*96$.

```python
def gcd_ext(x,y):

    (old_r, r) = (x, y)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    while r != 0:
        q = old_r // r
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
        (old_t, t) = (t, old_t - q * t)
    return (old_r, old_s, old_t)
```

Complete the python function `mi` below to calculate the multiplicative inverse of $x \text{ mod } n$ using the `gcd_ext` function above.  As an example, `mi(83,96)` should return a value of 59.  You should return `None` if no multiplicative inverse exists.  You can also check your code on question 4 above.  

```python
def mi(x,n):
    # Put your code here using the gcd_ext function
    pass

print(mi(83,96)) # 59
print(mi(675,210)) # None
```

## Question 6

### Part 1

Create public and private RSA keys by selecting two prime numbers $p$ and $q$ that are less than 1000 (for performance reasons).  Don't select a $p$ and $q$ that we used in the reading or in classroom examples.  Calculate $N$ and $\phi$.  Select a value of $e$ such that $gcd(e,\phi)=1$.  Find the multiplicative identity for $e \text{ mod } \phi$ (called $d$).  You can use the code from question 5 above to find the value of $d$.  

Answers:
* $p = $
* $q = $
* $N = $
* $\phi = $
* $e = $
* $d = $

### Part 2

The values of $N$ and $e$ are the public keys.  The value of $d$ is the private key.  Complete the python code below to encrypt the value $m = 5645$ and then decrypt it again. 

```python
# Put your values from Part 1
p = 
q = 
e = 
N = 
phi = 
d = 

m = 5645
# Write code to encrypt 'm' and display it

# Write code to decrypt it back again and display it.   It should be 5645 again.

```

  
