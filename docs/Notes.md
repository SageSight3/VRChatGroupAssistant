# Notes

### To Update Version Number
* Update it in config_info, README.md, and Cargo.toml
* Make sure to update version num in release build dir also

### Compiling to executable
* cargo build --release
* python -m PyInstaller <--onedir or --onefile> <--noconsole> <filename.py>

### To Switch to Venv
* ctrl+shift+p, Python: Select Interpeter, choose the one that says .venv, and switch to cmd or git bash terminal
* In a powershell terminal, change session script perms with the command: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. Then enter command: `.\.venv\Scripts\activate

### To convert .ui file to .py
* pyside6-uic a_file.ui -o ui_a_file.py

### Making a Release
* When making a release, make sure to include `READEME.md` and the `licenses` dir with it.
