import matplotlib.pyplot as plt
a=[1,2,3,4,5]
b=[2,4,6,8,10]
sizes = [50, 200, 100, 300,250]

plt.scatter(a, b, s=sizes)
plt.xlabel("X position")
plt.ylabel("Y position")
plt.show()
'''

Size of points and what it represents

Size can represent magnitude.

Example meanings:
Speed of drone
Signal strength
Importance of a point
Larger dot means higher value.
Smaller dot means lower value.
----------------------------------------------------------------------------
In scatter plot:
Position answers WHERE
Size answers HOW MUCH

That is the core logic.

Why size exists at all

Each dot already shows location.
But sometimes location alone is not enough.

You may want to show:
Strength
Intensity
Importance
Magnitude

Size is used to encode that extra information.

Simple real life analogy

Imagine a map showing cities.

Dot position shows:
Where the city is

Dot size shows:
Population of the city

Big city = big dot
Small town = small dot

You immediately understand both location and population.

That is the purpose of size.

Now think in drone terms

Imagine drone positions.

Each drone has:
x position
y position
speed

Position shows where drone is.
Speed is extra information.

You cannot add speed as another axis easily.

So:
You use dot size.

Fast drone = big dot
Slow drone = small dot

Another simple example

Imagine sensor readings.

Each sensor has:
Location
Signal strength

Position shows where sensor is.
Signal strength shows how strong reading is.

So:
Strong signal = bigger dot
Weak signal = smaller dot

Very important understanding

Size is NOT mandatory.

Use size only when:
You want to show an extra value
Without adding another axis

If size adds confusion
'''