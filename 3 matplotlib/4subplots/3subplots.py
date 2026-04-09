import matplotlib.pyplot as plt

# data
x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]

# create first subplot
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title("Drone 1 Distance")
plt.ylabel("Distance")#when rows are 2 and column is 1 it means x axis is of same for both plots so no need to write xlabel for both plots

# create second subplot
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title("Drone 2 Distance")
plt.xlabel("Time")
plt.ylabel("Distance")

# fix spacing between subplots

plt.tight_layout() #to  get rid of overlapping of texts

plt.show()

#-------------------------------------------------------------------------------

x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]

# create first subplot
plt.subplot(1,2, 1)
plt.plot(x, y1)
plt.title("Drone 1 Distance")
plt.xlabel("Time")#when rows are 1 and columns are 2 it means y axis is of same for both plots so no need to write ylabel for both plots

# create second subplot
plt.subplot( 1,2, 2)
plt.plot(x, y2)
plt.title("Drone 2 Distance")
plt.xlabel("Time")
plt.ylabel("Distance")

# fix spacing between subplots

plt.tight_layout() #to  get rid of overlapping of texts

plt.show()
'''

We will cover only these 3 sub topics:

Subplot positions and numbering

Sharing axes between subplots

Fixing spacing issues

After this, I will stop and wait.

Subplot positions and numbering

Once you decide the grid,
each subplot gets a position number.

Positions are counted:
Left to right
Top to bottom

Example grid:
2 rows
2 columns

Positions look like this:

Position 1 Position 2
Position 3 Position 4

So:

subplot(2, 2, 1) means top left
subplot(2, 2, 2) means top right
subplot(2, 2, 3) means bottom left
subplot(2, 2, 4) means bottom right

This numbering never changes.

Sharing axes between subplots

Sometimes you want both plots to use the same scale.

Example:
Compare two drones distance vs time

If x axis scale is different,
comparison becomes misleading.

You can share axes so both plots use same limits.

Basic idea:
Same x axis
Same y axis

This makes visual comparison correct.

Important logic:
Sharing axis does NOT merge plots
It only syncs their scales

Fixing spacing issues between subplots

Sometimes titles or labels overlap.

This happens because:
Subplots are placed tightly by default.

Matplotlib provides a simple solution.

After creating all subplots,
you tell matplotlib to adjust spacing automatically.

This improves readability.

Logic:
Let matplotlib manage spacing
Instead of you guessing margins

Mental summary for subplots so far

Decide grid once
Choose positions correctly
Share axes for fair comparison
Fix spacing for clean visual
'''