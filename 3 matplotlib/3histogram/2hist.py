import matplotlib.pyplot as plt

data = [10, 12, 15, 15, 18, 20, 22, 22, 22, 25, 30]

plt.hist(data, bins=5)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram using Frequency")

plt.show()

'''
What this does:
It groups values into ranges
It counts how many values fall in each range
It draws bars for those counts
--------------------------------------------------------------------------
I will explain slowly and deeply, in two parts only:

Why we give only one list and still get y axis

What bins really are, with real logic

No symbols. No shortcuts.

Part 1
Why histogram needs only ONE list

This is the most important thing to understand.

First compare with line and scatter plot

Line plot
You give x and y
Because you already KNOW both values

Example
Time is x
Distance is y

Scatter plot
You give x and y
Because each point already has two values

Histogram is different

In histogram
You do NOT already know y values

You only have raw data.

Example
Sensor errors
Exam marks
ML loss values

You only know the values themselves.

So what does histogram do internally

Histogram does this internally step by step:

Step 1
Take the data list

Example
10, 12, 15, 15, 18, 20, 22, 22, 22, 25, 30

Step 2
Divide the value range into bins

Step 3
Count how many values fall in each bin

That count is the y axis.

So answer to your question

Yes
The y axis frequency is calculated automatically

You never give y values
Histogram computes them for you

That is the whole purpose of histogram.

Very important mental rule

Line and scatter
You provide both x and y

Histogram
You provide only data
Histogram creates y for you

Part 2
What bins REALLY mean

This is where most confusion happens.

First understand range

Look at your data again

Minimum value is 10
Maximum value is 30

So the full range is from 10 to 30

Now what does bins do

Bins means
How many parts you split this range into

Example
bins equals 5

That means
Split 10 to 30 into 5 equal ranges

Example bins logic

Range 10 to 30
Total width is 20

If bins is 5
Each bin width is about 4

So bins look like this conceptually

10 to 14
14 to 18
18 to 22
22 to 26
26 to 30

Now frequency calculation

Histogram checks each value

10 goes to first bin
12 goes to first bin
15 goes to second bin
15 goes to second bin
18 goes to second or third depending on edge
And so on

It counts how many values fall in each bin

That count becomes bar height.

Why bins matter so much

Few bins
Everything looks lumped together
You lose detail

Too many bins
Bars look random and noisy

Correct bins
You see real distribution shape
---------------------------------------------------------------------
First important truth

Bins equals 4 does NOT mean:
You will clearly see 4 separate labeled boxes on the x axis.

Histogram does not label bins explicitly by default.

That is why it feels confusing.

What bins equals 4 ACTUALLY means

When you say bins equals 4, matplotlib does this internally:

It finds the minimum value

It finds the maximum value

It divides the full range into 4 equal ranges

These ranges exist internally.
They are not clearly printed on the graph.

Why you cannot easily see 4 parts

Because of three reasons:

Bars touch each other

Bin boundaries are not labeled

X axis shows continuous values, not bin ranges

So visually it looks like one continuous shape.

But internally, counting is still happening in 4 bins.

Very important mental shift

Histogram is NOT about seeing bins clearly.

Histogram is about seeing:
Where values are concentrated
Where values are rare

Bins are just a tool to make that visible.

How to mentally identify bins from a graph

You do this in your head, not by looking for boxes.

Step 1
Look at minimum and maximum on x axis

Example:
10 to 30

Step 2
If bins equals 4, divide range mentally

Total range is 20
20 divided by 4 equals 5

So bins are roughly:

10 to 15
15 to 20
20 to 25
25 to 30

Now look at bar heights around those regions.

That is how engineers read histograms.

Why matplotlib does not draw clear bin borders

Because histogram is meant for:
Understanding distribution shape
Not exact numeric boundaries

If it drew heavy borders and labels:
Graph would become cluttered.

Key rule to lock in your mind

Bins control counting
Not visual boxes

Histogram is an approximation tool, not a precise table
'''