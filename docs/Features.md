# Current Features

Note: The app and backend run independently from each other. In future, there will be controls to start and stop the backend from the app, and the app will start the backend when launched, if the backend isn't already running. It will also have an alternative `full quit` button, that will close both the app and the backend, if wanted.

### Backend (Rust)
* Attempts login with stored cookies from config file. Prompts user for auth credentials, if fails, as well as 2fa, if needed.
* Takes basic group info as input and queries VRChat API to find a target group and gets its group id
* Queries VRChat API at the start of every hour, and logs how many members in the target group are are online, and the size of the target group. Logs -1 for both counts if the query fails. Helpful for figuring out what geographical demogrpahics exist within your group, for the purpsoes of event planning and better accomodating group member time availability. Logs can be found in the [`activity log`](../data/activity_log).

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

### Feature Ideas/Proposals - DISCORD FEATURES ON HOLD
* Have a graph of discord member counts also
* For every month, calculate average member counts at every time for each day of the week, also have options to display averages for weekdays and weekends
* Query api every two minutes, or so during meetups, to track peak players at the meet, and when it was most active -> can also maybe use this to figure out who are the group meetup's regular attendees?
* Maybe can see if can automatically add weekly/monthly/etc. events to the group's VRChat/discord calendars
* Sync logs between discord and VRChat -> logging vrchat logs to discord could also keep logs from further back than VRChat's website displays
* Better case and suggestions storage/management -> You can already set up decent systems in discord, so may be somewhat redundant, could be helpful if creating a ticket system for reports and suggestions. People would need to actively use the ticket system. Possible ideas include:
    * Ability to assign specific staff members to a case, and ping them about it
    * Allow members to request and ping specific staff members to help with a report they're making, even if they'd like to make it anonymously
    * Enable group members to make reports and submit evidence anonymously
    * Enable group members to make anonymous suggestions
    * Ability to more clearly designate certain situations as lower or higher priority
    * If a member is temporarily banned, track the ban, and ping staff members when it becomes time for the ban to be lifted.
    * Dedicated ban appeal system that banned members can access, even if not in the discord or vrchat group anymore -> could limit access to only members that have been banned and are allowed to appeal.
    * Can track the number of appeals a group member, past, or present, has made/attempted -> could automatically revoke their permission to appeal, if group has a cap on number of allowed attempts, could also not allow appeals, if member hasn't waited long enough since their last appeal, if having a minimum duration between appeals
    * Centralized list of banned members -> can also state ban type (permanent or temporary) and if a member is allowed to appeal
    * If wanting to implement a strike system, can track number of strikes a member has, and set how long each strike should last
        * May also allow automatic moderation actions that will be taken if a member reaches a certain number of strikes
* Sync moderation actions between discord and VRChat
* Make it so announcements sent to the discord can automatically be posted to the VRC group, if needed (ex. meetup announcements, group changes, etc.)
* Ping or dm meetup hosts ahead of when they need to send out their meetup announcements, to remind them, in case they forget, or lost track of time -> could also give more time for meetup hosts to find backup host, if they can't make it
* Have more organized list of group members (maybe wouldn't be as prone to some of the search bugs there is on VRChat's website)
* Have a vrchat account, similar to what furality has, that can invite group members to instances not under the group -> could be helpful if hosting larger events or collab meets with other groups
* Group member birthday tracker -> Could automatically create a post wishing Happy Birthday to members who want it, when their birthday rolls around
* Unique event features
* Staff member hiatus tracker -> could also have tracker to see how long a staff member has been active on staff without a hiatus, also could log reasons for the hiatus, could notify staff when another staff member goes on hiatus, and welcome that staff member back when they come back, could allow for hiatuses to be set to specific durations or indefinite, could automatically ping the staff member going on hiatus, and ask if they want to notify the whole group, as well as the staff about it
* Staff member check-in system -> could automatically put a staff member on hiatus, if they miss too many check ins, could also ping staff members if they've missed too many check-ins
* Ping staff if a larger than average number of members join the vrchat group or discord at a time, in case a group's staff would want to take action, if needed (ex. ensure it's not a bot wave, close group temporarily, if there are concerns over managability, etc.)
* Track group growth over time
* Automatically ping staff when a member is given a staff role
* Implement training tools to help staff members in training?
    * mentor assignment
    * mock/dummy moderation actions and logs for situations in-training staff members handle, that full staff members can review or execute on
* Can be used for multiple groups

### GUI Brainstorm
* Have arrow buttons to switch between graphs of different days
* Checkboxes to toggle rendering for both online and total member counts
* Have login window and window for group info input
* Have hub for expansion