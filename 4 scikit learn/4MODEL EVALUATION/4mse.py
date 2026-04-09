from sklearn.metrics import mean_squared_error

actual = [10, 20, 30]
predicted = [12, 18, 25]

mse = mean_squared_error(actual, predicted)
print(mse)


'''PART 4
MEAN SQUARED ERROR MSE

SUBTOPIC 1
WHAT MSE MEANS IN SIMPLE WORDS

MSE means Mean Squared Error.

Ignore the name again and focus on the idea.

MSE answers this question.

On average
how bad are my mistakes
while giving extra importance to big mistakes

So MSE is like MAE
but it punishes large errors more strongly.

This is the key difference.

SUBTOPIC 2
WHY WE SQUARE THE ERRORS

Let us reuse the same example.

Actual values
10
20
30

Predicted values
12
18
25

First get individual errors.

Predicted minus actual gives
2
minus 2
minus 5

Now square each error.

2 squared gives 4
minus 2 squared gives 4
minus 5 squared gives 25

Notice something important.

The large error 5
became much larger after squaring

This is intentional.

Why this matters

In many real systems
a big mistake is much worse than many small mistakes.

Example

Predicting delivery time
being wrong by 30 minutes once
can be worse than being wrong by 3 minutes ten times

MSE captures this idea.

SUBTOPIC 3
MSE USING SCIKIT LEARN CODE

Now see how scikit learn calculates MSE.

from sklearn.metrics import mean_squared_error

actual = [10, 20, 30]
predicted = [12, 18, 25]

mse = mean_squared_error(actual, predicted)
print(mse)


Manual check

Squared errors were
4
4
25

Average of these
4 plus 4 plus 25 divided by 3
which equals 11

So MSE equals 11.

Important observation

MSE is not in original units.
Time was in minutes
but MSE is in minutes squared

This makes MSE harder to interpret directly
but very useful for optimization.

MENTAL SUMMARY

MAE treats all mistakes equally.
MSE punishes large mistakes more.
MSE is sensitive to outliers.
Lower MSE means better model
-------------------------------------------------------------------
.

---

THE CORE QUESTION YOU ARE ASKING

Why do we intentionally make big errors look much bigger
by squaring them
instead of treating all errors equally

What do we gain from this

---

FIRST THINK ABOUT WHAT A MODEL IS TRYING TO DO

A model is trying to adjust itself
so that future predictions are better.

During training
the model looks at errors
and changes itself to reduce those errors.

So error is not just for reporting.
Error is a signal used to improve the model.

---

WHAT HAPPENS IF ALL ERRORS ARE TREATED EQUALLY

This is what MAE does.

MAE says
an error of 3
and an error of 30
are both just errors

Their impact is proportional.

This means
a few very large mistakes
can hide behind many small correct predictions.

The model might think
overall I am doing okay
and ignore those big failures.

---

WHY BIG ERRORS ARE DANGEROUS IN REAL LIFE

Now think practically.

Suppose you run a drone delivery system.

Scenario A

Most deliveries are off by 2 minutes
One delivery is off by 40 minutes

Scenario B

All deliveries are off by 5 minutes

Which system is more dangerous

Scenario A
because one extreme failure can cause
battery drain
customer loss
system breakdown

So big errors must scream louder.

---

WHAT SQUARING ACHIEVES

Squaring does ONE thing.

It makes big errors dominate decision making.

Small errors stay small.
Big errors explode.

This forces the model to focus on
fixing large mistakes first.

That is the purpose.

Not math beauty.
Not statistics.
Engineering safety.

---

WHAT WE ACHIEVE BY SQUARING

By squaring errors
we tell the model this message.

A few large mistakes are unacceptable.
Fix them even if it slightly worsens small ones.

This leads to safer
more stable
more reliable systems.

---

WHY WE CANNOT JUST MANUALLY CHECK BIG ERRORS

Because real datasets have
thousands or millions of predictions.

You need an automatic way
to highlight dangerous failures.

MSE does that automatically.

---

VERY IMPORTANT REALIZATION

MSE is not about human interpretation.
It is about model training behavior.

It changes how the model learns.

That is the key.

---

ONE LINE FINAL ANSWER

Squaring errors forces the model to care much more
about large mistakes
so that dangerous failures are reduced.

---



'''