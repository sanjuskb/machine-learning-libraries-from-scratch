import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]

# first plot
plt.plot(x, y1)
plt.title("Plot 1")
plt.savefig("plot1.png")
plt.clf()

# second plot
plt.plot(x, y2)
plt.title("Plot 2")
plt.savefig("plot2.png")
plt.show()
'''

Saving multiple plots correctly

When you create more than one plot in a program,
each plot must be saved separately.

Important rule:
Save AFTER creating the plot
Save BEFORE clearing or showing the next plot




Here:
clf clears the previous plot
Each plot is saved correctly

Common savefig mistakes

Mistake 1:
Calling savefig after show

Once show is called,
the figure may be closed.
Then savefig may save a blank image.

Mistake 2:
Overwriting files unintentionally

Saving with same filename
will replace the old image.

Mistake 3:
Forgetting folder existence

If folder does not exist,
savefig will fail.

Clean savefig workflow (important habit)

Professional workflow:

Create plot
Add labels and title
Set axis and grid
Save plot
Show plot
Clear figure

This avoids:
Overlapping plots
Wrong saves
Messy output

Mental summary for savefig

Save before show
Clear between plots
Name files carefully

'''
