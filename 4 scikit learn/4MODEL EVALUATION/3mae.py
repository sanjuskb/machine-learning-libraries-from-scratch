from sklearn.metrics import mean_absolute_error

actual = [10, 20, 30]
predicted = [12, 18, 25]

mae = mean_absolute_error(actual, predicted)
print(mae)
'''
SUBTOPIC 1
WHAT MAE MEANS IN SIMPLE WORDS

MAE means Mean Absolute Error.

Ignore the name for a moment.

MAE answers one simple question.

On average
how much is my model wrong

Not percentage
Not trend
Actual units

If you are predicting time in minutes
MAE is also in minutes.

So MAE tells you
the average mistake size.

This is why MAE is very practical.

SUBTOPIC 2
LOGIC BEHIND MAE STEP BY STEP

Suppose these are real times and predicted times.

Actual times
10
20
30

Predicted times
12
18
25

Now calculate error for each example.

Example 1
Predicted 12
Actual 10
Error is 2

Example 2
Predicted 18
Actual 20
Error is 2

Example 3
Predicted 25
Actual 30
Error is 5

We do not care if prediction is higher or lower.
We only care how far it is.

That is why it is called absolute error.

Now take average of these errors.

Errors are
2
2
5

Average error
2 plus 2 plus 5 divided by 3
which equals 3

So MAE equals 3.

Meaning
On average
the model is wrong by 3 minutes.

That is all MAE means.
----------------------------------------------------
in the above code 
This will print
3.0

Which matches our manual calculation.

Important meaning

MAE directly tells you
average mistake size
in real units

This is why engineers love MAE.


'''