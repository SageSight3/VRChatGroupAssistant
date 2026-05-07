# Possible Task Ideas

This list is less so target tasks to complete, and more of an ideas list thats more do them if can get to them. There isn't time sensitivity on these, though some should be done sooner than later, if they're going to be.

* Refactor model to be multiple sub models -> each may need its own model backend interlayer and abstract interlayer
* Refactor gui to not rely on a central controller, maybe have each view have a controller
* Switch to using sqlite3 db for storing group data
* Refactor backend service into struct-impl blocks
* Refactor subview weidgets to inehrit from an abstract widget class -> can enforce requirement for methods like setup_connections() and set_launch_state()
* Review Tasks and reorganize
* Sort docs better
* Move brainstorms out of Features to their own doc
* Move old docs to a pre-1.0.0 dir
* Write documentation for methods
* Move sandbox to it's own git repo
* Finish unfinished patterns
* Create contribution guide
* Implement group selection feature and multiple group analytics logging
* Clean up file structure
* Implementing other VRCGA Features
* Create a dedciated doc for issues
* Refactor frontend methods privacy to be more consistent with their data's privacy
* Refactor out duplicate code
* Look into making graph scrollable when window is small
* Make script to update version num in all neccessary files?
* For actions able to be taken in the group by someone using VRCGA, gray out or hide actions a user's role in the group doesn't allow them to do? -> look into `get_user_all_group_permissions` in the api
* Maybe have app check for discord perms, as well
* Refactor auth module to be a struct impl block
* Look into finding a better way to organize tasks/docs
    * maybe look into using spreadsheets
* Design database for refactoring log storage to an sqlite3 db
* What should happen if a user loses management perms for or leaves/gets removed from a group? -> delete all data associated with that group, should there be a revert functionality, may not be able to be made truly secure, without a server element to the group's use of VRCGA or VRCGA directly
* Begin doing research into making discord bot ON HOLD
* Move database access to service, and have service pass results to frontend?
    * Have all config and database queiries happen throguh the service?
* Make so search query in Online Counts Tracker Date selection is saved and loaded back in, even if selection changes or user clicks off selection box
* Look into how group data would be structured if wanting to use VRCGA, for multiple groups -> how would making and running jobs (like autologgers) for both groups work?, How would switching between multiple groups work? How would a user choose what groups they want to use VRCGA to help manage?
* Refine Group Selection
    * Make so instead of needing to search for group, can choose group from user's group list -> may not be pheasible to only list groups where user has a management role -> look into get_group_permissions
* Add forgot password button to login GUI
* have autologger session error logs be written to a file
    * log errors to file
    * set up error log view in GUI
* May not be necessary, with intention to switch to a sqlite3 database post first release
    * Switch log_group_member_counts() to use a BufWriter for updating the log -> not fully neccessary potentially, since log is only updated every hour -> 
    * In modelbackendinterlay/dataparser, refactor log path to be parsed from app cofig
* !!! Change group auto logger queries, to first check and make sure app user requesting is allowed to (has a management role in the group)
* Add option to settings to have VRCGA Service launch on pc startup, at least for Windows