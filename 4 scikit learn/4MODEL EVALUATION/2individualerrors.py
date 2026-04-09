actual = [10, 20, 30]
predicted = [12, 18, 25]
errors=[]
for a,p in zip(actual,predicted):
    '''
    WHY zip IS USED HERE

We want to compare
each actual value
with its corresponding predicted value.

zip makes sure
we take matching values together.

Without zip
you would have to manage indexes manually.
    '''
    e=p-a
    errors.append(e)
print()
absolute_errors = []

for a, p in zip(actual, predicted):
    absolute_errors.append(abs(p - a))
    '''
    WHAT abs MEANS

abs means absolute value.

Absolute value means
remove the minus sign.

Examples

abs(2) gives 2
abs(-2) gives 2
abs(-5) gives 5

So abs only keeps the size of the error
not the direction.
----------------------
    '''

print(absolute_errors)


'''

MAE, MSE, RMSE
are NOT meant to show individual errors.

They are meant to summarize errors.

So your observation is right
MAE still gives only one overall number.

That is by design.

WHY METRICS DO NOT SHOW INDIVIDUAL ERRORS

Think of metrics like a report card.

A report card shows
average marks
overall grade

It does NOT show
how many marks you lost in each question.

That does not mean question wise marks do not exist.
It just means the report card is a summary.

Same here.

Individual errors DO exist.
Metrics just summarize them.

WHERE INDIVIDUAL ERRORS ACTUALLY LIVE

Individual errors are simply this.

predicted value minus actual value

That is it.

There is no special machine learning concept here.

HOW TO GET INDIVIDUAL ERRORS STEP BY STEP

Let us use the same example.

actual = [10, 20, 30]
predicted = [12, 18, 25]


Now compute individual errors manually.

errors = []

for a, p in zip(actual, predicted):
    error = p - a
    errors.append(error)

print(errors)


Output will be

[2, -2, -5]


Meaning

First prediction was 2 units higher
Second prediction was 2 units lower
Third prediction was 5 units lower

These are individual errors.

ABSOLUTE INDIVIDUAL ERRORS

If you want absolute mistakes.

absolute_errors = []

for a, p in zip(actual, predicted):
    absolute_errors.append(abs(p - a))

print(absolute_errors)


Output

[2, 2, 5]


These are exactly the values used inside MAE.

MAE just averages these numbers.

CONNECTING MAE TO INDIVIDUAL ERRORS

Internally MAE does this.

Step 1
Compute individual absolute errors

Step 2
Add them all

Step 3
Divide by number of examples

So MAE does NOT hide errors.
It compresses them into one number.

WHEN YOU SHOULD LOOK AT INDIVIDUAL ERRORS

You look at individual errors when

Debugging a model
Finding outliers
Understanding failure cases
Improving features

You look at metrics when

Comparing two models
Reporting performance
Making decisions

Both are needed.

VERY IMPORTANT FINAL LINE

Individual errors tell you
where the model fails.

Metrics tell you
how bad the model is overall.

'''