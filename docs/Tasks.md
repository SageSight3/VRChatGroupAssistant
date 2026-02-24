# Tasks

## To Do
* Look into making graph scrollable when window is small
* Look into storing program data in AppData or Documents. May be necessary for compiling to an executable.
* Possibly switch config.json from having username, to just using email and password.
* Possibly refactor GUI scripts to follow MVC better: gui Convert gui.py to controller.py. Convert data-parser.py to model.py. Convert grapher.py to gui.py or view.py or make a new gui/view script and ahve grapher be a sub-script of it -> Look into Python classes.
* Make a new app.py script for running the GUI
* Begin doing research into making discord bot ON HOLD
* Make script to update version num in all neccessary files?
* Have program create neccessary dirs and files when run, if they don't exist
* Create window for entering target group's basic info (name, short code, discriminator)
* Add buttons to start and stop Rust program
* Add quit all button to GUI -> should close both the gui app and stop the rust program
* Make it so when GUI launches, it will check if the rust program is running, and if it isn't, start it
* Write GUI story board
* Update GUI and maybe rust program also to change their working directories to where they need to be
* Switch log_group_member_counts() to use a BufWriter for updating the log -> not fully neccessary potentially, since log is only updated every hour
* Make it so when program is launched, if any neccessary files or dirs don't exist yet, they'll be created with the necessary info they need
* Possibly change log storage to store logs in dirs based on year with seperate log files for each month -> figure out how selecting a date to get the graph for, would work if implemented -> how would listbox be drawn, if using -> list most recent 30 days maybe? or maybe list entries off selected month and year? could have dropdowns for each, alternative, could have selection box show date options between one date and another
* See if can space bar groups in graph to be better spaces/give the bar labels more room
* Figure out how to distribute project, for version 1.0.0 -> do i need to publish both a release, package, or both? How do I do both of those things, and what do I need to include/do for each
* Look into how to certify distributed release build/cost
* Add about/credits section to GUI -> will need to put LGPLv3 license text here? will also need to include name of LGPL libraries used (PySide6?)? Look into what else needs to be in it -> have contact information in it?
* Add logout functionality -> cookies should be cleared when user logs out
* Refactor auth module to be a struct impl block
* Update backend for case of user enters wrong auth credentials
* Look into how group data would be structured if wanting to use VRCGA, for multiple groups -> how would making and running jobs (like autologgers) for both groups work?, How would switching between multiple groups work?
* Make so instead of needing to search for group, can choose group from user's group list -> may not be pheasible to only list groups where user has a management role
* For actions able to be taken in the group by someone using VRCGA, gray out or hide actions a user's role in the group doesn't allow them to do? -> look into `get_user_all_group_permissions` in the api

## In Progress
* Make GUI
* Create login window and functionality
* Sandbox PySide GUI changing windows -> look into QStackedWidget

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