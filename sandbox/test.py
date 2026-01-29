import os.path
import matplotlib.pyplot as plt
import numpy
import matplotlib.widgets as widgets
import re

path = "/../data/activity_log"

# os.path.dirname(__file__) gets the absolute path to this file
log_file = open(os.path.dirname(__file__) + path, 'r')

times = []
online_counts = []
total_counts = []
title = ""
    
log_file_entries = list(map(lambda log_entry: log_entry.strip().split(", "), log_file.readlines()))

# the element at index 2 in an entry is the date it was logged
# target_date_entries = list(filter(lamda entry: entry[2] == <a_date>, log_file_entries))

for entry in log_file_entries:
    times.append(entry[4]) # element at index 4 of entry is time

    pattern = r'\d+' # regexing to isolate member count values from their labels
    # element at index 5 of entry is online member count
    online_counts.append(int(re.findall(pattern, entry[5])[0])) 
    # element at index 6 of entry is group total member count
    total_counts.append(int(re.findall(pattern, entry[6])[0]))

    # element at index 3 is day of the week, element at index 2
    title = entry[3] + " " + entry[2]

# Graph Data

# First Graph

width = 0.3
label_location = numpy.arange(len(times))

fig, ax = plt.subplots(figsize=(12, 5))

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
plt.xticks(rotation=70)

ax.set_ylim(0, max(total_counts) + 50)

fig.subplots_adjust(bottom=0.3)

# make slider to scroll through times
time_slider_axis = fig.add_axes([0.25, 0.1, 0.65, 0.03])
time_slider = widgets.Slider(time_slider_axis, "", -1, 7, valinit=-1)

def slider_update(val):
    pos = time_slider.val
    ax.axis([pos, pos+24, 0, max(total_counts) + 50])
    fig.canvas.draw_idle()

time_slider.on_changed(slider_update)

slider_update(0)
plt.show()

log_file.close()