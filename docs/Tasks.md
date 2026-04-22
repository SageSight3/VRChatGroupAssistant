# Tasks for 1.0.0

## To Do
* Look into making graph scrollable when window is small
* Possibly refactor GUI scripts to follow MVC better: gui Convert gui.py to controller.py. Convert data-parser.py to model.py. Convert grapher.py to gui.py or view.py or make a new gui/view script and ahve grapher be a sub-script of it -> Look into Python classes.
* Begin doing research into making discord bot ON HOLD
* Make script to update version num in all neccessary files?
* Add buttons to start and stop Rust program
* Add quit all button to GUI -> should close both the gui app and stop the rust program
* Make it so when GUI launches, it will check if the rust program is running, and if it isn't, start it
* Arrow buttons to GUI for switching between graphs
* Update GUI and maybe rust program also to change their working directories to where they need to be
* Switch log_group_member_counts() to use a BufWriter for updating the log -> not fully neccessary potentially, since log is only updated every hour
* Make it so when program is launched, if any neccessary files or dirs don't exist yet, they'll be created with the necessary info they need -> make an install wizard?
* See if can space bar groups in graph to be better spaces/give the bar labels more room
* Figure out how to distribute project, for version 1.0.0 -> do i need to publish both a release, package, or both? How do I do both of those things, and what do I need to include/do for each
* Look into how to certify distributed release build/cost
* Add logout functionality -> cookies should be cleared when user logs out
* Refactor auth module to be a struct impl block
* Update backend for case of user enters wrong auth credentials
* Look into how group data would be structured if wanting to use VRCGA, for multiple groups -> how would making and running jobs (like autologgers) for both groups work?, How would switching between multiple groups work? How would a user choose what groups they want to use VRCGA to help manage?
* Refine Group Selection
    * Create window for entering target group's basic info (name, short code, discriminator)
    * **OR**
    * Make so instead of needing to search for group, can choose group from user's group list -> may not be pheasible to only list groups where user has a management role -> look into get_group_permissions
* For actions able to be taken in the group by someone using VRCGA, gray out or hide actions a user's role in the group doesn't allow them to do? -> look into `get_user_all_group_permissions` in the api
* !!! Change group auto logger queries, to first check and make sure app user requesting is allowed to (has a management role in the group)
* Look into how to have a python app communicate with a rust app
* Look into switching logs to being stored in sqlite3 db
* Maybe have app check for discord perms, as well
* Look into finding a better way to organize tasks/docs
* Implement login window functionality
* put loginButton in a horizontal layout so it can be given a maximum size while kept centered in the view
* have autologger session error logs be written to a file
    * log errors to file
    * set up error log view in GUI
* Review Tasks and reorganize
* Look into protobufs (protocol buffers) for interapplication communication
* Store app config and database in Documents or AppData
    * Look into storing program data in AppData or Documents.
* Add show password button to app gui login screen
* Frontend
    * implement 'don't ask again' functionality for close app dialog
    * implement cookie clearing oif user logs out of app
    * implement checking if 2fa is required for when user login credentials are accepted in login screen
    * implement passing login info to backend
    * implement getting backend status and displaying it in main app widget in gui
    * implement start, stop, restart, and refresh data button functionality in main app widget in gui
    * *Once GUI is initially implemented, go through each screen/app page and implement missing functionality*
    * VRCGA Servuce status in GUI should update if the service quits unexpectedly
        * Should also update, if is unable to query VRChat API, for whatever reason (like API Outage, bad internet connection, etc.)
    * add remember me checkbox and functionality to login
* In modelbackendinterlay/dataparser, refactor log path to be parsed from app cofig

## In Progress
* Make GUI
    * Player Count Tracker Page -> remove graph button, graph should update whenever selection changes or graph as percents is checked -> move all three to one graph, that could toggle on and off, if checked in controls? make sure pushing an arrow button updates the date selection also
    * Login Widget
        * Login
        * Two Factor Auth
    * App Container
        * Navigation
        * About Page
            * * Add about/credits section to GUI -> will need to put LGPLv3 license text here? will also need to include name of LGPL libraries used (PySide6?)? Look into what else needs to be in it -> have contact information in it?
        * App Content
            * Analytics Page
                * Online Counts Tracker
                    * Model hooked into GUI classes, write graph widget
* What should happen if a user loses management perms for or leaves/gets removed from a group? -> delete all data associated with that group, should there be a revert functionality, may not be able to be made truly secure, without a server element to the group's use of VRCGA or VRCGA directly
* Design database for refactoring log storage to an sqlite3 db

## Done
* Update group_info log_member_counts() to log 0 for both online and total counts if querying API fails
* Added better error handling for if querying member counts fails
* Added scrollbar to dates listbox in temporary GUI
* Update main.rs to print program version num when run
* Refactor storage files into a single config file? -> possibly in JSON
* Figure out how to find and close a specific process from a python script
* Add weekday to date selection labels
* Change grapher.py to graph x bars without the log entries, and assign data to each xtick, based on log entry timestamps
* Look into setting up activity logger to run on pc startup or on a schedule through linux cron jobs or windows task scheduler
* Create separate doc for tasks list
* Create separate doc for notes
* Figure out why there is error switching to venv for python interpreter
* !!! Figure out what needs to be done for licensing the project's packages I need to include liscenses in a distributed release: vrchatapi, tokio, reqwest, url, tokio-cron-scheduler, chrono, serde_json, pyside6, matplotlib
* Look into how source code from an LGPL library needs to be included with the project? Does it need to be provided with the release, or just in the Repo? Can it just be instructions on where to find it, or does it need to be the source code directly?
* Look into how to embed matplotplot lib figure in a qtwidget -> figure out how to be able to update graph in a widget with a button, also figure out how to add it to a widget's layout
* Look into making GUI with PySide
* Create and figure out to how to add VRChat Group Assistant Liscense to project-> as of 02/20/2026, has MIT License
* Move constants to constants.rs, refactor other modules to use new constants module -> app name and version should still come from app config, where needed, to be sure they're up to date
* Refactor auth.rs to request username and password from user first time they log in and use a user agent defined in a config file -> Have config file with user agent compiled into backend binaries -> user agent in constants.rs
* Removed need to store auth credentials. User auth credentials are no longer saved.
* Figure out how custom widgets for app pages will be maintained, since pyside6-uic overrides them havomg init methods, parents, and inheriting from QWidget
* Sandbox PySide GUI changing windows -> look into QStackedWidget
* GUI
    * Login
        * Add back arrow to 2fa widget -> should go back to previous verification method if set to use recovery code, and back to login window, if in initial 2fa state
* Refactor online counts tracker data to be a list where each element holds onto the data for one day in the frontend's model > will be more consistent with how days are stored, also may be better for future feature implementations and debugging
    * will need to refactor abstract interlayer and model backend interlayer to do so