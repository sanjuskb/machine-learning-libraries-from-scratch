'''
Docstring for 2train test split.1theory
SUBTOPIC 1
WHY WE NEED TRAIN TEST SPLIT

The main goal of machine learning is not to remember data.
The goal is to predict correctly on new unseen data.

If a model learns using all available data and is tested on the same data, it can cheat.
Cheating here means memorization.

Real world logic

If you give a student the question paper and answer key together
and then ask how well the student performs
the score is meaningless.

Same thing happens in machine learning.

So we divide data into two parts.

Training data
Used to teach the model

Testing data
Used to check whether learning is real

This separation is the foundation of honest machine learning.

SUBTOPIC 2
WHAT TRAIN TEST SPLIT ACTUALLY DOES

train_test_split takes your prepared X and y and divides them into four parts.

X_train
y_train
X_test
y_test

Real meaning

X_train and y_train are used to learn patterns.
X_test and y_test are kept hidden during learning.

After training is complete
the model is tested using X_test
and compared against y_test

This simulates the future
where answers are unknown.


'''