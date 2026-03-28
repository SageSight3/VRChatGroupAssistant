# Features Doc for pre-1.0.0

Note: The app and backend run independently from each other. In future, there will be controls to start and stop the backend from the app, and the app will start the backend when launched, if the backend isn't already running. It will also have an alternative `full quit` button, that will close both the app and the backend, if wanted.

### Backend (Rust) - Implemented
* Attempts login with stored cookies from config file. Prompts user for auth credentials, if fails, as well as 2fa, if needed.
* Takes basic group info as input and queries VRChat API to find a target group and gets its group id
* Queries VRChat API at the start of every hour, and logs how many members in the target group are are online, and the size of the target group. Logs -1 for both counts if the query fails. Helpful for figuring out what geographical demogrpahics exist within your group, for the purpsoes of event planning and better accomodating group member time availability. Logs can be found in the [`activity log`](../data/activity_log).

## App - Implemented
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
* Query api every 10 to 20 minutes, or so during meetups, to track peak players at the meet, and when it was most active -> can also maybe use this to figure out who are the group meetup's regular attendees?
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
* Clearer management of group role permissions, would have clear distinction between between management and member perms
* In the event of multiple people using the same app on the same machine, or someone's account getting comprimised, for sensitive group logs (like moderation logs), maybe encrypt sensitive logs using the permissions needed to access those logs and the group's id, and make them only decryptable/readable in the app? Would need encryption to complex enough to dissuade bad actors from trying to break it.
* **Checking User Group Perms and Membership Status**
    * First, check membership status, then, if status is valid (user is in group), check perms
    * **Checking For a Specific Group**
        * **When:**
            * User changes selected group in app to that group
            * User attempts to take an action that directly involves querying the VRChat API (ex. making a group post) -> analytics tools shouldn't fall under this, as they would be querying the API automatically, and just displaying aggregated data from locally stored logs 
        * WIP Check all perms for all groups listed in app for a user on an interval/when querying the VRChat API for that group, in general
* First Degree groups graph -> Should display target group in center with links to other groups it's members are in (have configureable parameters for how. ex. for group to be represented on graph, at least 5% of target group members must be in it). Should also show links between represented mutual groups if significant number of members in target group are in multiple of them. (ex. in target group a, a significant fraction of members are in both groups b and group c, so there's a link between groups b and c), can have graphs for active members and all
* Frontend model should update dates list when new entries are added to the app's analytics logs
* List which group staff members are online in VRChat/on VRChat's website, maybe show if they're on discord, as well, if set up
* Automatically give members of a group who have verified their 18+ with VRChat a role to allow them to be pinged exclusively for adult only events -> As of 03/23/2026, VRChat's group post system doesn't have an option to only ping members who are verified 18+, meaning groups would need to have to make a unique role and assign it to members over 18, manually, to ping them, if they need to for some reason.
* Any action that requires the API to be queried should pop up a window saying that the backend service needs to be running for the action to work, if the backend is stopped
* GUI should have page showing group description?

### GUI Brainstorm
* Have arrow buttons to switch between graphs of different days
* Checkboxes to toggle rendering for both online and total member counts
* Have login window and window for group info input
* Have hub for expansion
* **Pages:**
    * Login -> use recovery code button should be hidden, as well, when using an OTP code for 2fa
    * 2fa
    * App -> info bar at top with selected group dropdown (placeholder text could say "Group Select..."), a refresh button (will get new list of available groups user can select and refresh all group info) -> when group selection changes, all group info should refresh to change to the newly selected group
        * Home -> buttons to start, stop, and restart backend, logout button, delete logs button, quit all button (prompt for user confirmation before quitting), basic info info: selected group size, user roles in selected group, backend status, is the group in the autologger, group name, group short code and discriminator
        * About -> LGPL, app description, other license info
        * Group Analytics (auto logger) - Should display something if selected group isn't set up with autologger
            * Add Group Button -> button to add new group to VRCGA auto-logger -> List should be empty by default -> if a group is added, should refresh all group info, after a group is added, button should change to `Remove Group` button
            * Remove Group Button -> button to remove a group from VRCGA auto-logger (have subwindow to prompt for confirmation) -> if a group is removed, button should change to `Add Group` button
            * Next to Add/Remove Group Button - display if autologger is enabled for the selected group
            * Dropdown to select analytic being viewed
                * Online Member Counts
                    * Date selection box
                    * Selection between viewing member counts or percents in graph
                    * Show graph button
                    * Option to show graph in new window
                    * Graph widget
                    * Arrow buttons to cycle between graphs of different days -> date selection should update, when button is pushed, graph shouldn't change if selected date is earliest or most recent available
                * Meetup Activity
                    * WIP
* WIP

### Model Data
* Selected group
    * Group id
    * Name
    * Short code and discriminator (formatted how they are in VRChat)
* User roles in selected group
* User perms in selected group
* Backend status -> is backend running or stopped
* Current Graph Data
    * Percents?
    * Online Counts
    * Total Counts
* Dates
* sessionExists -> is there an existing logged in VRCGA session
* Current appOuterWidget
* showCloseDialogs -> should show app closing dialogs if a close event is activated for it's gui's main widget

### Model Signals
* requiresEmail2fa
* requiresAuth2fa
* loginFailed
* twoFactorAuthFailed
* onlineCountsGraphDataChanged
* datesListChanged

### Config Data
* App name
* App version
* Session cookies (clear, if user logs out)
* Users Info
    * Username
    * User id
* Auto-logger groups
* WIP
    

### GUI Pages
* Login - Put 2fa and login in same widget -> (will implement later, due to potential method/overhead considerations on how app frontend will communicate with backend)
* App
    * Player Count Tracker
    * About - about tab should have app version in it (change Licenses tab to Credits tab)
    * Autologger controls -> for now maybe instead have menu bar that opens a subwindow with controls?
        * Buttons to start and stop backend
        * Should report backend status (running, not running)
        * backend logs
    * Menu
        * Autologger Controls
            * Start
            * Stop
            * Restart (should be grayed out if autologger isn't running)
            * Open Logs Folder
            * View Error Logs
            * Clear Groups (future)
        * Clear Cookies
        * Quit -> should open dialog for confirmation, should inform user that the backend will close also
    * If frontend is closed, but backend isn't, a dialog window should open, informing the user that the backend is still running, should also provide option to quit backend
    * Menu bar should also display status of autologger
    * Button to open about page should also be in menu bar -> should open as a subwindow/dialog
    * Settings Page
        * Clear cookies button
        * Show app close/close backend service dialog on app close
        * Quit backend service on app close