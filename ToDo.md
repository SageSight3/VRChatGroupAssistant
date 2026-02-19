# To Do

* Make GUI
* Look into making graph scrollable when window is small -> may require GUI framework
* Look into exporting full size matplotlib graphs as images and then having separate guis to move around them?
* Look into embedding matplotlib graphs into other GUI frameworks
* Look into storing program data in AppData or Documents. May be necessary for compiling to an executable.
* Possibly switch config_info from having username, to just using email and password.
* Possibly refactor GUI scripts to follow MVC better: gui Convert gui.py to controller.py. Convert data-parser.py to model.py. Convert grapher.py to gui.py or view.py or make a new gui/view script and ahve grapher be a sub-script of it -> Look into Python classes.
* Make a new app.py script for running the GUI
* Look into making GUI with PySide
* Begin doing research into making discord bot
* Make script to update version num in all neccessary files?
* Have program create neccessary dirs and files when run, if they don't exist
* Create login window and functionality
* Create window for entering target group's basic info (name, short code, discriminator)
* Add buttons to start and stop Rust program
* Add quit all button to GUI -> should close both the gui app and stop the rust program
* Make it so when GUI launches, it will check if the rust program is running, and if it isn't, start it
* Write GUI story board
* Update GUI and maybe rust program also to change their working directories to where they need to be
* Possibly refactor Rust program so that auth module is a submodule
* Switch log_group_member_counts() to use a BufWriter for updating the log -> not fully neccessary potentially, since log is only updated every hour
* Make it so when program is launched, if any neccessary files don't exist yet, they'll be created with the necessary info they need
* Possibly change log storage to store in logs in dirs based on year with seperate log files for each month -> figure out how selecting a date to get the graph for, would work if implemented -> how would listbox be drawn, if using -> list most recent 30 days maybe? or maybe list entries off selected month and year? could have dropdowns for each, alternative, could have listbox show date options between one date and another
* See if can space bar groups in graph to be better spaces/give the bar labels more room
* Create separate doc for tasks list
* Create separate doc for notes
* Create and figure out to how to add VRChat Group Assistant Liscense to project-> look into GPL?
* Figure out why there is error switching to venv for python interpreter
* Look into how to put qt liscense (LGPL) in project for distributed version
* Look into how to embed matplotplot lib figure in a qtwidget -> figure out how to be able to update graph in a widget with a button, also figure out how to add it to a widget's layout

### GUI Brainstorm
* Have arrow buttons to switch between graphs of different days
* Checkboxes to toggle rendering for both online and total member counts
* Have login window and window for group info input
* Have hub for expansion

### Feature Ideas
* Have a graph of discord member counts also
* For every month, calculate average member counts at every time for each day of the week, also have options to display averages for weekdays and weekends

### To Update Version Number
* Update it in config_info, README.md, and Cargo.toml
* Make sure to update version num in release build dir also

### Compiling to executable
* cargo build --release
* python -m PyInstaller <--onedir or --onefile> <--noconsole> <filename.py>

### Implemented GUI Features
* Graph x-axis should be time of day
* Graph y-axis should be member count
* Each graph could be one day
* Graph title will be day of weak and the date
* Have list of buttons, where each button is for a specific date, that when pressed will pop up the active member counts graph for that day. Use the date field in the log entries for this

### To Switch to Venv
* ctrl+shift+p, Python: Select Interpeter, choose the one that says .venv, and switch to cmd or git bash terminal
* In a powershell terminal, change session script perms with the command: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. Then enter command: `.\.venv\Scripts\activate

### To convert .ui file to .py
* pyside6-uic a_file.ui -o ui_a_file.py

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