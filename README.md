# VRChat Group Assistant

VRChat Group Assistant is an app and backend to help with running a VRChat group, by providing analytics tools for identifying geogrpahical demographics within your group's member base to better understand what times of the day, your group is most active, and other tools for streamlining group moderation, event planning, and more, with possible future features including announcement, moderation, and log syncing with a discord server, if your group has one. See **[Features](docs/Features.md)** for more info.

# Instructions
VRChat Group Assistant, at present not create a config file for you automatically, which you will need to make manually, following the steps below.

While this will change in future, for now, you will need to start the backend and app individually, from each other.

### Make App Config File
As of version 0.8.0, the basic info VRChat Group Assistant uses to run has been unified under one file in the app backend's main working directory, `config.json`. See example: [config_guide.json](config_guide.json)

To make the config file, create a new file called `config.json` in the main the app's main directory, `VRChatGroupAssistant`, copy and paste over the everything from `config_guide.json`, and replace all the fields in `basicGroupInfo`. No other field needs to be changed. 

Alternatively, just replace the necessary info in config_guide.json and remove the `-guide` from the file name. 

### Finding Your Group's Basic Info
Your group's short code and discriminator is the group code you can find under your group's name in it's description on VRChat or VRChat's website. It'll look like `ACODE.####`.

**On VRChat**
![Group Short Code and Discriminator on VRChat](assets/GroupCodeVRC.png)

**On VRChat's Website**
![Group Short Code and Discriminator on VRChat's Website](assets/GroupCodeVRCWebsite.png)

The short code is everything on the left of the `.`, and the discriminator is the numbers.

---
In future, I intend to make it so you can enter your authentication config info and group info through a GUI.

# Licensing
VRChat Group Assistant uses primarily `PySide6` for it's GUI under the open source license, [LGPLv3](licenses/python/pyside6/LICENSE). In abidance with it, you can find instructions on how to install PySide6 in the [pyside-pyside-setup repo on github](https://github.com/qtproject/pyside-pyside-setup/blob/dev/README.pyside6.md), part of the [Qt Project](https://github.com/qtproject).

VRChat Group Assistant also uses the python package, `mplcursors`, for its graphs. [Find it here.](https://github.com/anntzer/mplcursors)

---

VRChat Group Assistant is not endorsed by VRChat and does not reflect the views or opinions of VRChat or anyone officially involved in producing or managing VRChat properties. VRChat and all associated properties are trademarks or registered trademarks of VRChat Inc. VRChat © VRChat Inc.