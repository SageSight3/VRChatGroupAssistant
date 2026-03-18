# Creating an App Navigation Menu - WIP

have nav and app focus (where main app contents will be) be in a splitter layout together

Unless wanting to make collapsable widgets, make sure childrenCollapsible in QSpliiter is false (unchecked in QT Designer)

set max size for either veritical or horizontal, to constrain their size policy when the window's opened for the first time, or resized.

change layout spacings, as wanted for wanted appearence

### For Nav
Use push buttons with spacers to put compact them in the right space. If nav items have sub items, have them hidden by default, and only unhide them, if their respective nav item is selected