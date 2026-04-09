'''
Docstring for 7text and annotations.4text_vs_annotation

Text says: “Highest point”

Annotation says: “THIS is the highest point”T

he difference is not how they look by default
The difference is what they are capable of

Think like this:

text = writing words on the graph

annotation = writing words about a specific point

What plt.text really is

plt.text(x, y, "message")

Means:

Write this message at these coordinates
Nothing more

It does NOT know:

which data point you mean

what it is describing

It is just text placed on the graph.

What plt.annotate really is

plt.annotate("message", xy=(x, y))

Means:

This message refers to THIS point

Even if it looks like text,
internally matplotlib knows:

which point it belongs to

This matters later.
------------------------------------------

The REAL difference is NOT placement

The difference is attachment

This is the key idea.

Text is manually placed

Text says:

“Put these words at this position”

It does not know:

which data point it refers to

whether that point moves or changes

If the data changes, text stays where you put it.

Annotation is logically attached

Annotation says:

“These words belong to THIS data point”

Even if:

the plot is resized

axis limits change

the point moves

The annotation tracks the point.

That is the core difference.

Very important mental model

Text = absolute position
Annotation = relative to data poin

'''