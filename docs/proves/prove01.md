# CSE 280 Prove 01

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**:

**Section**:

**Teacher**:

## Question 1

Identify (with an "X") whether each statement is either a proposition or non-propisition.  The first two are done for you:

|Statement|Proposition|Non-Propisition|
|:-:|:-:|:-:|
|I got an A in CSE 280|X||
|Hello!||X|
|The hose has a leak.|||
|The wind speed is greater than 30 miles per hour.|||
|Close the window.|||
|The window is closed.|||
|Are you graduating this semester?|||

## Question 2

Let $p$ be the proposition "I studied." and $q$ be the proposition "I got an A on the test."  Express the following symbolic propositions in English (the first one is done for you):

1. $p \land q$ : I studied and I got an A on the test.
2. $\neg p \land q$ :
3. $p \land \neg q$ :
4. $\neg p \land \neg q$ :
5. $p \lor q$ :
6. $\neg p \lor q$ :
7. $p \lor \neg q$ :
8. $\neg p \lor \neg q$ :

## Question 3

Complete the following truth tables (the first one is done for you):

1. $p \land q$

|$p$|$q$|$p \land q$|
|:-:|:-:|:-:|
|T|T|T|
|T|F|F|
|F|T|F|
|F|F|F|

2. $p \lor q$

|$p$|$q$|$p \lor q$|
|:-:|:-:|:-:|
|T|T||
|T|F||
|F|T||
|F|F||

3. $\neg p \lor q$

|$p$|$q$|$\neg p$|$\neg p \lor q$|
|:-:|:-:|:-:|:-:|
|T|T|||
|T|F|||
|F|T|||
|F|F|||

4. $p \land \neg q$

|$p$|$q$|$\neg q$|$p \land \neg q$|
|:-:|:-:|:-:|:-:|
|T|T|||
|T|F|||
|F|T|||
|F|F|||

5. $p \land (q \lor \neg r)$

|$p$|$q$|$r$|$\neg r$|$q \lor \neg r$|$p \land (q \lor \neg r)$|
|:-:|:-:|:-:|:-:|:-:|:-:|
|T|T|T||||
|T|T|F||||
|T|F|T||||
|T|F|F||||
|F|T|T||||
|F|T|F||||
|F|F|T||||
|F|F|F||||

6. $p \lor \neg (\neg q \land \neg r)$

|$p$|$q$|$r$|$\neg q$|$\neg r$|$\neg q \land \neg r$|$\neg (\neg q \land \neg r)$|$p \lor \neg (\neg q \land \neg r)$|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|T|T|T||||||
|T|T|F||||||
|T|F|T||||||
|T|F|F||||||
|F|T|T||||||
|F|T|F||||||
|F|F|T||||||
|F|F|F||||||

## Question 4

There is another operator called exclusive or which uses the operator symbol $\oplus$.  It is like the traditional $\lor$ but it excludes the case where both $p$ and $q$ are True.  This operator is used frequently in electronics.  The truth table for $p \oplus q$ is given below:

|$p$|$q$|$p \oplus q$|
|:-:|:-:|:-:|
|T|T|F|
|T|F|T|
|F|T|T|
|F|F|F|

There is no built-in python function that implements exclusive or.  Implement the `xor` function below using the `and`, `or`, and `not` operators.  If you want to use a different programming language, you will need to modify the test code to support your language choice.

```python
def xor(p, q):
    # Your code here
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

truth_table_2_vars(xor)
```