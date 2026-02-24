# Notes

### To Update Version Number
* Make sure it's up to date in `cargo.toml`, `config.json`, `config-guide.json`, and `constants.rs`
* Make sure to update version num in release build dir also

### To Switch to Venv
* ctrl+shift+p, Python: Select Interpeter, choose the one that says .venv, and switch to cmd or git bash terminal
* In a powershell terminal, change session script perms with the command: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. Then enter command: `.\.venv\Scripts\activate`

### To convert `.ui` file to `.py`
* `pyside6-uic a_file.ui -o ui_a_file.py`

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