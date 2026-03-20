# Notes

### To Update Version Number
* Make sure it's up to date in `cargo.toml`, `config.json`, `config-guide.json`, and `constants.rs`
* Make sure to update version num in release build dir also

### To Switch to Venv
* ctrl+shift+p, Python: Select Interpeter, choose the one that says .venv, and switch to cmd or git bash terminal
* In a powershell terminal, change session script perms with the command: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. Then enter command: `.\.venv\Scripts\activate`

### To convert `.ui` file to `.py`
* `pyside6-uic a_file.ui -o ui_a_file.py`
* to stop Qt from attempting to auto-connect slots to matching signals, add the option `-a` or `--no-auto-connection`
    * Qt's auto-connection is done by calling `QMetaObject.connectSlotsByName()` in a ui's auto-generated file
    * It will trigger for all slots with names prefixed with `on_` that also have the `@Slot()` decorator
* https://doc.qt.io/qt-6/uic.html

### Convert resources.qrc to resources_rc.py
* When using a resources.qrc file with Pyside6, the resources file must also be converted to a python file 
* `pyside6-rcc a_file.qrc -o your_file_rc.py`

### Making a Release for Distribution
* When making a release, make sure to include `READEME.md` and the `licenses` dir with it.

### Build Process
* Make sure it's up to date in `cargo.toml`, `config.json`, `config-guide.json`, and `constants.rs`
* **Frontend**
    * convert necessary `.ui` files to `.py` files
    * if building release:
        * Compile to an executable with PyInstaller: `python -m PyInstaller <--onedir or --onefile> <--noconsole> <filename.py>`
* **Backend**
    * if building release:
        * use command `cargo build --release`, compiles to release profile executable, instead of debug
* if building release:
    * make sure everything is up to date in release build dir, also

### PySide6 Note
* You don't need a main window

### License Requirements in GUI
* Credits tab
    * Have link to VRCGA's git repo
    * Have LGPLv3 listed for PySide
    * Attribute Flaticon for images from it
    
### Sorted Group Permissions
* **Management**
    * Manage Group Member Data
    * Manage Group Data
    * View Audit log
    * Manage Group Roles
    * Manage Group Default Role
    * Assign Group Roles
    * Manage Group Bans
    * Remove Group Members
    * Moderate Group Instances
    * Manage Group Instances
* **Member**
    * View All Members
    * Manage Group Announcement
    * Manage Group Calendar
    * Link Instances and Events
    * Manage Group Galleries
    * Manage Group Invites
    * Group Instance Queue Priority
    * Create Age Gated Instances
    * Create Group Public Instances
    * Create Group+ Instances
    * Create Members-Only Group Instances
    * Role-Restrict Members-Only Instances
    * Portal to Group+ Instances
    * Unlocked Portal to Group+ Instances
    * Join Group Instances