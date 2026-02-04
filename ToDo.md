# To Do

* Make GUI
* Look into setting up activity logger to run on pc startup or on a schedule through linux crob or windows task scheduler
* Look into making graph scrollable when window is small -> may require GUI framework
* Look into exporting full size matplotlib graphs as images and then having separate guis to move around them?
* Look into embedding matplotlib graphs into other GUI frameworks
* Look into storing program data in AppData or Documents. May be necessary for compiling to an executable.
* Possibly switch config_info from having username, to just using email and password.
* Possibly refactor GUI scripts to follow MVC better: gui Convert gui.py to controller.py. Convert data-parser.py to model.py. Convert grapher.py to gui.py or view.py or make a new gui/view script and ahve grapher be a sub-script of it -> Look into Python classes.
* Make a new app.py script for running the GUI
* Look into making GUI with PySide
* Add weekday to date selection labels
* Begin doing research into making discord bot
* Make script to update version num in all neccessary files?
* Have program create neccessary dirs and files when run, if they don't exist
* Create login window
* Refactor storage files into a single config file? -> possibly in JSON
* Create window for entering target group's basic info (name, short code, discriminator)

### GUI Brainstorm
* Have buttons to switch between graphs of different days
* Each graph could be one day
* Checkboxes to toggle rendering for both online and total member counts
* Graph title will be day of weak and the date
* Graph x-axis should be time of day
* Graph y-axis should be member count
* Graph should have different bars to signify times the program wasn't running
* Have login window and window for group info input
* Have hub for expansion
* Have list of buttons, where each button is for a specific date, that when pressed will pop up the active member counts graph for that day. Use the date field in the log entries for this
* Update group_info log_member_counts() to log 0 for both online and total counts if querying API fails

### Feature Ideas
* Have a graph of discord member counts also

### To Update Version Number
* Update it in config_info, README.md, and Cargo.toml
* Make sure to update version num in release build dir also

### Compiling to executable
* cargo build --release
* python -m PyInstaller <--onedir or --onefile> <--noconsole> <filename.py>

## Done
* Added better error handling for if querying member counts fails
* Add scroll wheel to temporary GUI?
* Update main.rs to print program version num when run