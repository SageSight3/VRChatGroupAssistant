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
* Design database for refactoring log storage to an sqlite3 db
* What should happen if a user loses management perms for or leaves/gets removed from a group? -> delete all data associated with that group, should there be a revert functionality, may not be able to be made truly secure, without a server element to the group's use of VRCGA or VRCGA directly
* Begin doing research into making discord bot ON HOLD