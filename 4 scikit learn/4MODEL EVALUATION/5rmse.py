from sklearn.metrics import mean_squared_error
import math

actual = [10, 20, 30]
predicted = [12, 18, 25]

mse = mean_squared_error(actual, predicted)
rmse = math.sqrt(mse)

print(rmse)

'''
ROOT MEAN SQUARED ERROR RMSE

---

SUBTOPIC 1
WHY RMSE EXISTS AT ALL

After MSE, we have a problem.

MSE is in squared units.

If time is measured in minutes
MSE is in minutes squared

That is not intuitive for humans.

So RMSE exists to fix this.

RMSE simply takes the square root of MSE.

This brings the error back
to the original unit.

---

SUBTOPIC 2
WHAT RMSE TELLS YOU

RMSE answers this question.

On average
how big is a typical mistake
while still caring more about large errors

So RMSE keeps the benefit of MSE
punishing large mistakes

But expresses the result
in a unit humans understand.

Example logic

RMSE equals 4 minutes

Means
a typical prediction error is around 4 minutes
with big mistakes counted seriously.

This is much easier to reason about
than minutes squared.

---

SUBTOPIC 3
RMSE USING SCIKIT LEARN CODE

```python
from sklearn.metrics import mean_squared_error
import math

actual = [10, 20, 30]
predicted = [12, 18, 25]

mse = mean_squared_error(actual, predicted)
rmse = math.sqrt(mse)

print(rmse)
```

Using previous example

MSE was 11

Square root of 11
is about 3.32

So RMSE equals about 3.32 minutes.

Meaning

A typical error is around 3.3 minutes
with large errors influencing this value strongly.

---

FINAL COMPARISON YOU SHOULD REMEMBER

MAE
average mistake size
treats all errors equally

MSE
average squared mistake
punishes large errors strongly
not human readable

RMSE
square root of MSE
punishes large errors
human readable

---

WHEN TO USE WHAT

Use MAE
when you want simple interpretation

Use MSE
when training models and optimizing

Use RMSE
when reporting performance and caring about large failures

---

STOP HERE

We have completed
evaluation metrics basics.

Reply with one word only.

DONE

Next we will move to
feature scaling
and you will see why KNN and others break without it
----------------------------------------------------------------------------

WHAT DOES TYPICAL ERROR MEAN

Typical error means
a single number that represents
how wrong predictions usually are.

It does NOT mean
every prediction is wrong by exactly that amount.

It means
if you had to describe the overall mistake level
using one number
this is that number.

So when we say

typical error is around 3.3 minutes

we mean

most prediction mistakes are of that order of size
some smaller
some larger

SECOND PART
WHAT DOES LARGE ERRORS INFLUENCING THIS VALUE MEAN

Let us go back to the same example.

Actual values
10
20
30

Predicted values
12
18
25

Individual errors were
2
2
5

Now imagine two situations.

Situation A

Errors are
2
2
2

Situation B

Errors are
2
2
10

Now think carefully.

In both situations
most errors are small.

But in situation B
one error is very large.

RMSE behaves like this.

Situation A
RMSE stays close to 2

Situation B
RMSE increases a lot

Even though only one error became large.

This happens because
squaring makes large errors contribute much more
to the final number.

So that one big mistake
pulls the RMSE upward.

PUTTING BOTH PARTS TOGETHER

So when we say

A typical error is around 3.3 minutes
with large errors influencing this value strongly

It means

3.3 minutes summarizes the overall mistake size
but if there are any big mistakes
they will push this number higher
more than small mistakes would.
'''
