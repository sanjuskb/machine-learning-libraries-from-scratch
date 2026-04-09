'''Before scikit learn, understand one truth clearly.

Machine Learning is not about algorithms first.
It is about how data is arranged and given to algorithms.

If data structure is wrong, even the best model will fail.

So the first thing scikit learn teaches you is discipline in data structure.

1 WHAT IS A DATASET IN MACHINE LEARNING

A dataset is a table of past observations.

Each row represents one example.
Each column represents one property of that example.

Example in words
Suppose you want to predict delivery time of a drone.

One row could mean one delivery.
Columns could be distance battery wind speed payload weight.

The value you want to predict is delivery time.

So every dataset always has two logical parts.

Input part
Output part

scikit learn enforces this separation strictly.

2 FEATURES AND TARGET MEANING

In scikit learn language

Features are called X
Target is called y

X means all the information you give to the model.
y means the answer you want the model to learn.

Real meaning

X answers the question
What do I know before prediction

y answers the question
What do I want to predict

Example logic

If you are predicting house price
X could be area number of rooms location
y is the price

Important reasoning

The model never sees the real y during prediction.
It only sees X and tries to guess y.

That is why separating X and y is mandatory.

3 WHY X IS CAPITAL AND y IS SMALL

This is not style. This is meaning.

X is usually a table with many columns.
y is usually a single column.

So by convention

X is written capital because it is a matrix like structure.
y is written small because it is a vector like structure.

This helps you immediately understand the shape of data.

-------------------------------------------------------------------------------------

SUBTOPIC 1
WHAT A DATASET REALLY MEANS IN MACHINE LEARNING

A dataset is not just a table of numbers.
It is a collection of past experiences.

Each row represents one real world event that already happened.
Each column represents one measurable property of that event.

Real meaning
Machine learning learns patterns from past experiences, not rules written by humans.

Example logic
If you want a machine to predict delivery time, you must show it many past deliveries.
Each past delivery is one row.
Distance, wind speed, payload, battery level are properties.

Without past experiences, learning is impossible.
So dataset is the foundation of everything in machine learning.

SUBTOPIC 2
FEATURES X REAL MEANING

Features are the inputs you give to the model.

X represents everything the model is allowed to look at before making a decision.

Think like this
If you are solving a question in an exam, features are the information given in the question.

Real world meaning
Features answer the question
What information is available before prediction

Important logic
The model can only learn relationships between features and output.
If an important feature is missing, the model can never learn that effect.

That is why feature selection matters later.

SUBTOPIC 3
TARGET y REAL MEANING

Target is the correct answer for each past example.

y represents what you want the model to learn to predict.

Think like this
In an exam, target is the answer key.

Real world meaning
Target answers the question
What outcome am I trying to predict

Critical logic
During training, the model compares its guess with y and corrects itself.
During prediction, y is hidden.
The model must rely only on learned patterns.

This is why separating X and y is mandatory.
'''