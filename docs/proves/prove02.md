# CSE 280 Prove 02

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

**Section**:

**Teacher**:

## Question 1

## Question 1

Complete the following truth table to show that $A \equiv B$ (logically equivalent) where

$A : p \to \neg (q \land r)$

$B : \neg (p \land q \land r)$

|$p$|$q$|$r$|$q \land r$|$\neg (q \land r)$|$A: p \to \neg (q \land r)$|$p \land q \land r$|$B: \neg (p \land q \land r)$|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|T|T|T||||||
|T|T|F||||||
|T|F|T||||||
|T|F|F||||||
|F|T|T||||||
|F|T|F||||||
|F|F|T||||||
|F|F|F||||||

## Question 2

Determine if the following propositions written in English are True or False (the first one is done for you):

|Proposition|True or False|
|-|-|
|If $2+2=4$, then pigs can fly.|False|
|If $2+7=5$, then Elvis is alive.||
|If pigs can fly, then dogs can't fly.||
|$2+1=3$ if and only if $1+2=3$.||
|$1+2=3$ if and only if $3+1=6$.||
|$1+3=2$ if and only if the earth is flat.||
|$1 \lt 2$ if an only if $2 \lt 3$.||

## Question 3

Using the following predicates where the domain of $x$ is the set of all people:

$P(x) = x \text{ is older than 21}$

$S(x) = x \text{ is a student}$

express the following propositions in English senteneces (the first two are done for you):

|Proposition|English Sentence|
|-|-|
|$\exists x \ P(x)$|There exists a person who is older than 21.|
|$\forall x \ P(x)$|All people are older than 21.|
|$\exists x \ \neg P(x)$||
|$\forall x \ \neg P(x)$||
|$\exists x \ S(x)$||
|$\forall x \ S(x)$||
|$\neg \exists x \ S(x)$||
|$\exists x \ \neg S(x)$||
|$\neg \forall x \ \neg S(x)$||
|$\forall x \ \neg S(x)$||

## Question 4

Using the following predicates where the domain of $x$ is the set of all people:

$F(x) = x \text{ is my friend}$

$C(x) = x \text{ is cool}$

$S(x) = x \text{ is a student}$

$N(x) = x \text{ is from Nepal}$

identify which of the following english sentences match to each proposition (the first one is done for you).  Each sentence matches to one of the propositions in the table.

* All people are students and from Nepal.
* All of my friends are cool.
* Some of my friends are cool.
* Some student is from Nepal.
* Someone is my friend and is cool.
* All students are from Nepal.
* Everyone is a friend and is cool.
* Some students are from Nepal.

|Proposition|English Sentence|
|-|-|
|$\forall x \ (F(x) \to C(x))$|All of my friends are cool.|
|$\exists x \ (F(x) \land C(x))$||
|$\forall x \ (F(x) \land C(x))$||
|$\exists x \ (F(x) \to C(x))$||
|$\forall x \ (S(x) \to N(x))$||
|$\exists x \ (S(x) \to N(x))$||
|$\forall x \ (S(x) \land N(x))$||
|$\exists x \ (S(x) \land N(x))$||

## Question 5

Evaluate the following propositions to be True or False given that the domain of $x$ is the following integers: $\lbrace -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 \rbrace$:

|Proposition|True or False|
|-|-|
|$\forall x \ (x \text{ is odd})$||
|$\exists x \ (x \text{ is odd})$||
|$\forall x \ (x \text{ is negative})$||
|$\exists x \ (x \text{ is negative})$||
|$\forall x \ (x^2 \ge 0)$||
|$\exists x \ (x^2 \ge 0)$||
|$\exists x \ (x + x = 1)$||
|$\exists x \ (x + 2 = 1)$||

## Question 6

Translate the following statements into logical expressoins using quantifiers (e.g. $\forall \ \exists$), operators/connectives (e.g. $\land \lor \neg \to$), and the following predicates (where the domain of $x$ is the set of all people):

$C(x) = \text{ is a critic.}$

$P(x) = \text{ is perfect.}$

$F(x) = \text{ is your friend.}$

The first one is done for you.

|English Sentence|Proposition|
|-|-|
|Everyone is a critic.|$\forall x \ C(x)$|
|No one is perfect.||
|At least one of your friends is perfect.||
|All of your friends are critics.||
|Everyone is both your friend and a critic.||

## Question 7

The DeMorgan laws can be useful to simplify conditional logic in software.  The following predicates are implemented in the three functions below.  Apply the De Morgan law to each predicate and write the code for the simplified predicate.  The test code verifies that you applied De Morgan correctly.

Predicate 1: $\neg (p \land \neg q)$

Predicate 2: $\neg (\neg p \lor \neg q \lor \neg r)$

Predicate 3: $\neg (p \lor \neg (\neg q \land r))$

```python
def predicate1(p, q):
    # Original Predicate
    return not(p and not q)

def predicate1_demorgan(p,q):
    # Predicate after applying DeMorgan
    # Put your code here
    pass

def predicate2(p, q, r):
    # Original Predicate
    return not(not p or not q or not r)

def predicate2_demorgan(p, q, r):
    # Predicate after applying DeMorgan
    # Put your code here
    pass

def predicate3(p, q, r):
    # Original Predicate
    return not(p or not(not q and r))

def predicate3_demorgan(p, q, r):
    # Predicate after applying DeMorgan
    # Put your code here
    pass

def truth_table_2_vars(function):
    print(f"{function.__name__}")
    print(f"{'p':<8}{'q':<8}{'ANS':<8}")
    print("----------------------------------------")
    rows = [(p,q) for p in (True, False) 
                  for q in (True, False)]    
    for p, q in rows:
        ans = function(p,q)
        print(f"{p!s:<8}{q!s:<8}{ans!s:<8}")
    print()

def truth_table_3_vars(function):
    print(f"{function.__name__}")
    print(f"{'p':<8}{'q':<8}{'r':<8}{'ANS':<8}")
    print("----------------------------------------")
    rows = [(p,q,r) for p in (True, False) 
                    for q in (True, False)
                    for r in (True, False)]
    for p, q, r in rows:
        ans = function(p,q,r)
        print(f"{p!s:<8}{q!s:<8}{r!s:<8}{ans!s:<8}")
    print()

# These two tables should be the same
truth_table_2_vars(predicate1)
truth_table_2_vars(predicate1_demorgan)

# These two tables should be the same
truth_table_3_vars(predicate2)
truth_table_3_vars(predicate2_demorgan)

# These two tables should be the same
truth_table_3_vars(predicate3)
truth_table_3_vars(predicate3_demorgan)
```