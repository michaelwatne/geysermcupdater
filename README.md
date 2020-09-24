# Geyser MC Auto Updater
An auto-updater for GeyserMC. 
This is designed for you to be able to automatically check and download for updates when your GeyserMC-Activated Minecraft server starts up!

*This is still in its beta stage and potential bugs may be applicable.*

**This has been tested for Geyser Spigot and has not yet been tested on other versions!**

## PREREQUISITES
**Main Requirements**

[GeyserMC](https://geysermc.org/)

[Minecraft Java](https://www.minecraft.net/en-us/download/server)

**On Linux**

curl, wget

**On Windows**

Powershell

## HOW TO USE
**On Linux**

1) Download autoupdater_linux.sh in the root of your java-server folder or insert this code into your startup script:

```bash
#!/bin/bash

#####GEYSER SPIGOT UPDATER#####


###Section 1 - Sets file parameters###

#This will store the data of the build number. We recommend leaving this as is
#geyser.bld should be located inside the java-server directory.
buildfile=$(echo geyser.bld)

#This is your plugin file.
pluginfile=$(echo Geyser-Spigot.jar)

#this is your plugin directory. We strongly suggest leaving this as-is. Plugins
#are normally stored in its own directory of your java-server.
plugindir=$(echo plugins)


###Section 2 - Downloads and checks to see if Geyser Spigot is at the latest build###
echo Checking is Geyser-Spigot is latest...
sleep 3

#Gets timestamp data from JSON file.
#Do not change this unless you know what you're doing!
#If you get a 404 error, contact the developers
updatever=$(curl https://ci.nukkitx.com/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/buildNumber)

#Compares the update version. Do not change this
currentver=$(cat $buildfile)
if [ "$updatever" == "$currentver" ]
then
echo Geyser-Spigot is currently the latest version
sleep 5
else
echo A new version is available
sleep 2

#makes a backup of your pluginfile.
echo Backing up...
sleep 2
mv $plugindir/$pluginfile $pluginfile.backup

#downloads newest update
echo Downloading latest update...
wget -O $plugindir/$pluginfile https://ci.nukkitx.com/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/spigot/target/Geyser-Spigot.jar

echo $updatever > $buildfile
echo Download complete.
sleep 3
fi

###ENTER ANYTHING ELSE YOU NEED TO START THE SERVER NORMALLY###

```

2) Update the following to meet your needs:

`buildfile=$(echo geyser.bld)`, 
`pluginfile=$(echo Geyser-Spigot.jar)`, 
`plugindir=$(echo plugins)`

3) Add any additional code to run your server, such as server startup, backup commands, and more

4) Start the program and you're done!


**On Windows**

1) Download autoupdater_windows.ps1 in the root of your java-server folder or insert this code into your startup script:

```powershell
<#
GEYSER SPIGOT UPDATER
#>


<#
##Section 1 - Sets file parameters###
#>

<#
#This will store the data of the build number. We recommend leaving this as is
geyser.bld should be located inside the java-server directory.
#>
Set-Variable -Name "buildfile" -Value "geyser.bld"

<#
This is your plugin file.
#>
Set-Variable -Name "pluginfile" -Value "Geyser-Spigot.jar"

<#
this is your plugin directory. We strongly suggest leaving this as-is. Plugins
are normally stored in its own directory of your java-server.
#>
Set-Variable -Name "plugindir" -Value "plugins"

<#
##Section 2 - Downloads and checks to see if Geyser Spigot is at the latest build##
#>
echo "Checking is Geyser-Spigot is latest..."
sleep 3

<# Gets timestamp data from JSON file.
Do not change this unless you know what you're doing!
If you get a 404 error, contact the developers#>
$updatever = (Invoke-RestMethod -Uri https://ci.nukkitx.com/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/buildNumber )

<# Compares the update version. Do not change this #>
$currentver = (Get-Content $buildfile)
if ( $currentver -eq $updatever ) {
echo "Geyser-Spigot is currently the latest version"
sleep 5
} else {
echo "A new version is available"
sleep 2

<# makes a backup of your pluginfile. #>
echo "Backing up..."
sleep 2
Move-Item -path $plugindir\$pluginfile -Destination $plugindir\$pluginfile.backup -Force

<# downloads newest update #>
echo "Downloading latest update..."
$url = "https://ci.nukkitx.com/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/spigot/target/Geyser-Spigot.jar"
$output = "$plugindir\$pluginfile"
Invoke-WebRequest -Uri $url -OutFile $output
echo $updatever > $buildfile
echo "Download complete."
sleep 3
}

<#
##ENTER ANYTHING ELSE YOU NEED BELOW TO START THE SERVER NORMALLY##
#>
```

2) Update the following to meet your needs:

`Set-Variable -Name "buildfile" -Value "geyser.bld"`

`Set-Variable -Name "pluginfile" -Value "Geyser-Spigot.jar"`

`Set-Variable -Name "plugindir" -Value "plugins"`

3) Add any additional code to run your server, such as server startup, backup commands, and more

4) Start the program and you're done!

*GeyserMC belongs to their original developers and this project is not in any way owned by GeyserMC, therefore it is not warranted. Use at your own risk*
