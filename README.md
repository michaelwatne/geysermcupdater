# Geyser MC Auto Updater
An auto-updater for GeyserMC. 
This is designed for you to be able to automatically check and download for updates when your GeyserMC-Activated Minecraft server starts up!

*This is still in its beta stage and potential bugs may be applicable.*

## PREREQUISITES
**Main Requirements**

[GeyserMC](https://geysermc.org/), [Minecraft Java](https://www.minecraft.net/en-us/download/server)
[Python 2.7.15](https://www.python.org/downloads/release/python-2715/)

Gitpython Module for Python `pip2 install gitpython`
Requests Module for Python `pip2 install requests`

## HOW TO USE

1) Download the contents of the git repository to the root of your java-server folder

2) Edit the JSON file to meet your needs:

**Under GeyserMcInfo**
- Under Version, set it to your geyser version (Use Lowercase! Important!)
    Acceptable options: bungeecord | spigot | sponge | standalone | velocity
- Under location, set it to the name and directory of your plugin. If you're using the standalone, just set it to geyser.jar (or whatever you have the filename at)
- Under download file, this should be the same as the location name. Do not include `plugins/`

**Under ServerInfo**
- Under startup-script, set this to whatever your startup script is
- If you want to be prompted before the auto-updater downloads an update, set it to yes. Otherwise, set it to no.
- If you want to be prompted before the geyser-updater downloads an update, set it to yes. Otherwise, set it to no.

**Under DynamicInfo**
Do not change these. These update automatically.

4) Start the program and you're done!


*GeyserMC belongs to their original developers and this project is not in any way owned by GeyserMC, therefore it is not warranted. Use at your own risk*

## Please report any issues you have! This is a new release and hopefully there isn't any bugs!
