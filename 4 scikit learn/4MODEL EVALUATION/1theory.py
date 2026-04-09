'''
Docstring for 4MODEL EVALUATION.1theory

SUBTOPIC 1
WHAT EVALUATION REALLY MEANS

Evaluation means checking how good your model is at guessing.

Training tells the model what to learn.
Evaluation checks whether learning actually worked.

Without evaluation
you are just hoping the model is good.

With evaluation
you know how good or bad it is.

So evaluation is not optional.
It is proof of learning.

SUBTOPIC 2
WHY TESTING DATA IS NECESSARY

During training
the model sees correct answers.

So it can adjust itself to fit those answers.

If you test on the same data
you are not testing intelligence
you are testing memory.

That is useless.

Testing data is data the model has never seen before.

So when a model performs well on testing data
it means it has learned patterns
not memorized examples.

This is the only honest test.

SUBTOPIC 3
WHAT WE ARE ACTUALLY MEASURING

When we evaluate a model
we are measuring the difference between

what the model predicted
and
what actually happened.

This difference is called error.

Smaller error means better model.
Larger error means worse model.

All evaluation methods
are just different ways of measuring error.

Nothing more
-----------------------------------------------------------------------------
EVALUATION IN MACHINE LEARNING
PART 2
UNDERSTANDING model.score

SUBTOPIC 1
WHAT model.score MEANS IN LINEAR REGRESSION

When you call

model.score(X_test, y_test)

scikit learn automatically uses a specific evaluation method.

For Linear Regression
score means R squared score.

R squared answers this question.

How much of the change in output
can be explained by the inputs.

So score is not checking right or wrong exactly.
It is checking how well the pattern fits overall.

Important idea

score does NOT compare one prediction at a time.
It measures overall goodness of fit.

SUBTOPIC 2
WHAT R SQUARED ACTUALLY TELLS YOU

R squared value lies between minus infinity and 1.

But focus on this range for now.

If score is close to 1
Model explains most of the variation
Predictions follow real trend well

If score is close to 0
Model is no better than random guessing

If score is negative
Model is very bad
Worse than guessing average

Real meaning example

Score equals 0.9
Means 90 percent of variation in time
is explained by distance and battery

Score equals 0.2
Means inputs explain very little

SUBTOPIC 3
WHY score ALONE IS NOT ENOUGH

This is very important.

A model can have a good score
but still make bad predictions.

Why this happens

Score averages behavior
It hides individual large errors

Example

Most predictions are close
One prediction is very wrong

Score may still look good
But that one wrong prediction may be unacceptable in real life.

So score tells trend quality
not exact error size.

That is why later we use
MAE
MSE
RMSE
(
MAE
Mean Absolute Error

MSE
Mean Squared Error

RMSE
Root Mean Squared Error
)

But not yet. One step at a time.

CODE
SEE score IN ACTION AGAIN

score = model.score(X_test, y_test)
print("R squared score:", score)


What you should think when you see this number

This number tells
how well inputs explain output overall
{
how well inputs explain output overall

This sentence is abstract.
So let us convert it into plain thinking.

SUBTOPIC 1
WHAT DOES EXPLAIN OUTPUT REALLY MEAN

Look at your problem again.

Inputs
distance and battery

Output
time

Explaining output means this

When distance and battery change
does time change in a predictable way

If yes
then inputs explain output well

If no
then inputs explain output poorly

Example

If longer distance almost always means more time
then distance explains time

If battery level has no clear effect on time
then battery explains time poorly

So explanation means
how strongly inputs control the outpu
}
not whether each prediction is perfect.

MENTAL SUMMARY

score is a high level evaluation
It checks overall fit
It does not show individual mistakes

Think of it like
overall exam percentage
not question wise marks
-----------------------------------------------------------------------------
WHY THIS IS NOT ENOUGH IN REAL LIFE

Now think practically.

Suppose your model predicts delivery time.

Actual time
30 minutes

Predicted time
60 minutes

This is a big mistake.

But if other predictions are good
the overall score may still look high.

That is dangerous.

Because in real life
one big mistake can cause failure

That is why we later measure

How wrong predictions are
in actual numbers

That is where MAE MSE RMSE come in.

They do not care about trends.
They care about mistake size
'''
