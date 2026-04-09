'''
POLYNOMIAL REGRESSION
PART 1

SUBTOPIC 1
WHY LINEAR REGRESSION FAILS AND WHY WE NEED POLYNOMIAL REGRESSION

Linear Regression can only draw a straight line.

But many real world relationships are curved.

Example thinking

At small distance
time increases slowly

At medium distance
time increases faster

At very large distance
time increases very fast due to safety limits and battery constraints

This is not a straight relationship.
This is a curve.

Linear Regression cannot bend.
So it underfits.

Polynomial Regression exists to allow bending.

It lets the model learn curves instead of forcing straight lines.

SUBTOPIC 2
WHAT POLYNOMIAL REGRESSION REALLY IS

Important truth first

Polynomial Regression is still Linear Regression.

This sounds strange, but it is true.

The only difference is
we create extra features from existing ones.

Example

Original feature
distance

Polynomial features
distance
distance squared
distance cubed

Now the model can combine these
to form a curve.

So Polynomial Regression is not a new algorithm.
It is Linear Regression with transformed features.

SUBTOPIC 3
DEGREE AND WHAT IT MEANS

Degree controls how flexible the curve is.

Degree 1
Straight line
This is normal Linear Regression

Degree 2
Simple curve
Can bend once

Degree 3
More complex curve
Can bend more

Higher degree
More flexibility
More risk of overfitting

Important intuition

Low degree
model is too rigid

High degree
model becomes too sensitive to noise

So degree is a balance knob.
'''
