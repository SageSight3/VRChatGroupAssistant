# Current Features

### Backend (Rust)
* Attempts login with stored cookies and login info from config file. Prompts 2fa, if fails
* Takes basic group info as input and queries VRChat API to find a target group and gets its group id
* Queries VRChat API at the start of every hour, and logs how many members in the target group are are online, and the size of the target group. Logs -1 for both counts if the query fails

## App
* Parses activity log data, treats all -1 counts as 0, and returns parsed data in a configurable dictionary
* Generates a list of every unique date in the activity log
* Retrieves app name and version info from config file
* View features:
    * Selection box of all dates in activity log.
    * `Graph Member Counts` button displays bar graph, for selected date in dates list, showing online vs total member counts at every hour. Graph is titled with date and day of the week
    * `Graph Member Counts as Percents` button displays bar graph, for selected date in dates list, showing percent of all group members online at every hour. Graph is titled with date and day of the week
    * `Refresh Dates` button refreshes dates list with most recent date data from activity log. May implement automatic refresh at the start of every day, for if the app is open  multiple days. May still be kept after that, for atypical cases where the list of dates in the activity log may change (ex. loading a backup log).

# Ideas

### Feature Ideas
* Have a graph of discord member counts also
* For every month, calculate average member counts at every time for each day of the week, also have options to display averages for weekdays and weekends

### GUI Brainstorm
* Have arrow buttons to switch between graphs of different days
* Checkboxes to toggle rendering for both online and total member counts
* Have login window and window for group info input
* Have hub for expansion