import os.path
import matplotlib.pyplot as plt
import numpy
import re

path = "/../data/activity_log"

# os.path.dirname(__file__) gets the absolute path to this file
file = open(os.path.dirname(__file__) + path, 'r')

times = []
online_counts = []
total_counts = []
title = ""

for line in file:
    line_formatted = line
    line_formatted = line_formatted.strip()

    line_formatted = line_formatted.split(", ")

    pattern = r'\d+'

    times.append(line_formatted[4])
    online_counts.append(int(re.findall(pattern, line_formatted[5])[0]))
    total_counts.append(int(re.findall(pattern, line_formatted[6])[0]))
    title = line_formatted[3] + " " + line_formatted[2]

# First Graph

width = 0.3
label_location = numpy.arange(len(times))

fig, ax = plt.subplots(layout='constrained')

# set window title
fig.canvas.manager.set_window_title("Active Member Counts")

# create grouped bars with both online and total member counts
online_bar = ax.bar(label_location, online_counts, width, label="Online")
total_bar = ax.bar(label_location + width, total_counts, width, label="Total")

# display exact number above the bars
ax.bar_label(online_bar, padding=3)
ax.bar_label(total_bar, padding=3)

ax.set_ylabel("Member Count")
ax.set_xlabel("Time")
ax.set_title(title)
ax.legend(loc='upper left', ncols=2)

# sets x tick marks to be times
ax.set_xticks(label_location + width/2, times)

ax.set_ylim(0, max(total_counts) + 50)

plt.show()