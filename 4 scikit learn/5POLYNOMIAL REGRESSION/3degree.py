'''
POLYNOMIAL REGRESSION
PART 3
VISUAL INTUITION AND CHOOSING DEGREE

---

SUBTOPIC 1
WHAT UNDERFITTING AND OVERFITTING LOOK LIKE VISUALLY

Imagine plotting distance on x axis and time on y axis.

Case 1
Straight line on curved data

The line cannot bend.
It misses most points.
Errors are large everywhere.

This is underfitting.

Case 2
Very wiggly curve touching every point

The curve bends sharply to pass through all training points.
Training error becomes almost zero.
But the curve is unstable.

This is overfitting.

Case 3
Smooth curve following general trend

The curve bends gently.
It does not touch every point.
But it follows the overall pattern.

This is good fitting.

Underfitting means model is too simple.
Overfitting means model is too complex.



---

SUBTOPIC 2
WHAT DEGREE REALLY CONTROLS

Degree controls how flexible the curve is.

Degree 1
Straight line
No bending

Degree 2
Single smooth curve
Can bend once

Degree 3
More flexible curve
Can bend more

Higher degree
Very flexible
High risk of learning noise

Important logic

Increasing degree increases model capacity.
More capacity means more ability to fit data.
Too much capacity means memorization.

So degree is not about accuracy only.
It is about stability and generalization.

---

SUBTOPIC 3
HOW TO CHOOSE DEGREE SAFELY IN PRACTICE

There is no magic number.

The safe process is this.

Step 1
Start with degree 1
Check error on test data

Step 2
Increase degree to 2
Check test error

Step 3
Increase degree to 3
Check test error again

What you will usually see

Training error always decreases
Test error decreases at first
Then starts increasing

The degree where test error is minimum
is the best degree.

This is how we avoid overfitting.

This logic applies to every ML model
not just Polynomial Regression.

---

MENTAL SUMMARY

Linear Regression is degree 1.
Polynomial Regression increases degree.
Degree controls flexibility.
Too low degree underfits.
Too high degree overfits.
Best degree balances both.

---
'''