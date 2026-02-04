# VRChat Group Activity Assistant

# Current Features
* Logs online player counts every hour to help figure out when your group's members are most active, for the sake of planning meetups and other events. Once you run the program, the the logs will be able to be found in [`data/activity_log`](data/activity_log)

# Instructions
This repo does not include the `config_info` file for your authentication config, or the `target_group` file for the basic information related to the group you are using this program for. Both of these will need to be made for the program to work.

Once the program is running, it can be stopped by hitting `ctrl-c`.

### Make config_info File
To make the config file, make a new file called `config_info` in the `storage` directory, and add the following three lines:

```
VRCUsernameOrEmail
ObfuscatedPassword
VRChatGroupAssistant/0.6.2 email@address.com
```

**Note**: Line order does matter.

To obfuscate your password, temporarily add these lines to `main` or another rust program

```rust
let pw = "YourPasswordHere".to_string();
println!("{}", modules::util::obfuscate_text(&pw));
```
Then run the program and your obfuscated password to the right line in `config_info`.

If you use a different program, make sure to copy and paste the `obfuscate_text()` function definition from the util module to the other program for it to work, and change the call to it, as needed. You can find obfuscate_text()'s definition in [modules/util.rs](src/modules/util.rs).

Also, you can change `obfuscate_text()` obfuscates your password to whatever you want. Just make sure to make the respective changes to `deobfuscate_text()` in the same file, so the program can still pass the right password to VRChat's API.

**Disclaimer**: This obfuscation is not meant to be a secure form of password encryption. It is only there, because I wasn't comfortable with having a VRChat account password in plain text sitting in a file, since I like to screenshare as I develop code, as well as for concerns over potential Windows Recall or similar features.

### Make target_group File
Make a file called `target_group` in the `storage` directory. Then add these lines in order:

```
GroupName
GroupShortCode
GroupDiscriminator
```

Your group's short code and discriminator is the group code you can find under your group's name in it's description on VRChat or VRChat's website. It'll look like `ACODE.####`.

**On VRChat**
![Group Short Code and Discriminator on VRChat](assets/GroupCodeVRC.png)

**On VRChat's Website**
![Group Short Code and Discriminator on VRChat's Website](assets/GroupCodeVRCWebsite.png)

The short code is everything on the left of the `.`, and the discriminator is the numbers.

---
In future, I intend to make it so you can enter your authentication config info and group info through a GUI, and possibly make the password obfuscation more secure.