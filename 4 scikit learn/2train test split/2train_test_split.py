'''
Docstring for 2train test split.2train_test_split
CLEARING THE WORD CONFUSION FIRST

Let us forget machine learning for a moment.

Imagine a simple table written on paper.

Example table in words

Row 1
distance 5
battery 90
time 10

Row 2
distance 10
battery 80
time 20

Now understand each word carefully.

WHAT IS A ROW

A row represents one complete real world event.

In your case
One row means one delivery.

Everything about that delivery is written in the same row.

So
Row equals one example
Row equals one data point
Row equals one past experience

These three words mean the same thing.

WHAT IS A COLUMN

A column represents one type of information.

distance is a column
battery is a column
time is a column

Each column stores the same kind of information for all rows.

WHAT ARE PROPERTIES

Property is a general English word.

It means a measurable characteristic of something.

distance is a property of a delivery
battery is a property of a delivery
time is a property of a delivery

So property equals column in table language.

WHAT ARE FEATURES

Feature is a machine learning word.

Feature means
a property that is used as input to the model.

So

distance is a property
battery is a property

When we decide to use them as inputs
they become features.

Important logic

Not all properties must be features.
But all features are properties.

WHAT IS AN EXAMPLE

Example is one complete case.

One row is one example.

So

example equals row
example equals one delivery
example equals one observation
--------------------------------------------------------------------


Good. This confusion is **normal** and actually a good sign.
We will slow down more and remove every abstraction.

I will NOT assume scikit learn is installed.
I will NOT use new terms without grounding them.
I will ONLY clarify what you asked.

No moving forward. No new topics.

---

PART A
CLEARING THE WORD CONFUSION FIRST

---

Let us forget machine learning for a moment.

Imagine a simple table written on paper.

Example table in words

Row 1
distance 5
battery 90
time 10

Row 2
distance 10
battery 80
time 20

Now understand each word carefully.

---

WHAT IS A ROW

A row represents one complete real world event.

In your case
One row means one delivery.

Everything about that delivery is written in the same row.

So
Row equals one example
Row equals one data point
Row equals one past experience

These three words mean the same thing.

---

WHAT IS A COLUMN

A column represents one type of information.

distance is a column
battery is a column
time is a column

Each column stores the same kind of information for all rows.

---

WHAT ARE PROPERTIES

Property is a general English word.

It means a measurable characteristic of something.

distance is a property of a delivery
battery is a property of a delivery
time is a property of a delivery

So property equals column in table language.

---

WHAT ARE FEATURES

Feature is a machine learning word.

Feature means
a property that is used as input to the model.

So

distance is a property
battery is a property

When we decide to use them as inputs
they become features.

Important logic

Not all properties must be features.
But all features are properties.

---

WHAT IS AN EXAMPLE

Example is one complete case.

One row is one example.

So

example equals row
example equals one delivery
example equals one observation

TARGET IN YOUR CASE

time

This is the target because

It is the value you want to predict
It is the output of the model

So

Target equals time
Target is one column

---


---

PART C
MANUAL TRAIN TEST SPLIT WITHOUT ANY LIBRARY

Pretend we have four examples.

Example 1
Example 2
Example 3
Example 4

We decide
3 examples for learning
1 example for testing

Manually this means

Training set
Example 1
Example 2
Example 3

Testing set
Example 4

This is all train test split means.

No magic. No algorithm.

scikit learn just automates this cleanly and safely.

---

PART D
WHAT train_test_split REALLY IS

train_test_split is just a helper.

It does three things.

It splits rows into two groups.

It keeps feature rows and target values aligned.
here features are distance and battery and time is the target
It shuffles data to avoid bias.

Nothing more.

You do NOT need to install it right now to understand the idea.

---

PART E
WHEN YOU ACTUALLY NEED scikit learn

You only need scikit learn when
you want to train a model.

Right now
we are only building understanding.

---

IMPORTANT SUMMARY

Row example observation data point all mean the same thing.
Column property feature means a type of information.
Feature is a property used as input.
Target is the output you want to predict.
Train test split means hiding some rows for testing.



---

ONE VERY IMPORTANT FINAL CHECK

Number of rows in features
must equal
number of values in target

This ensures

Each example has exactly one correct answer

Your understanding satisfies this rule perfectly.

'''