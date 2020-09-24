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