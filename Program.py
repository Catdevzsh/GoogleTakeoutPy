## this is a program that backup your youtube files as a mp3 format
import os
import time
## write a program that uses google takeout to backup your youtube account on user input
print("Welcome to youtube backup")
print("Please enter your youtube account name: ")
username = input()
## use the google api to google takeout to backup your youtube account and all viedeos in a zip file with the mp4 format
## install the youtube api system to rosetta terminal and main terminal

## codex for backup format
print("Please enter your youtube password: ")
password = input()
print("Please enter the path to your backup folder: ")
backup_path = input()
print("Please enter the path to your youtube folder: ")
youtube_path = input()
print("Please enter the path to your mp3 folder: ")
mp3_path = input()
print("Please enter the path to your zip folder: ")
zip_path = input()
print("Please enter the path to your mp3 folder: ")
## enter the commands to complete the download using youtube-dl and backup all videos in your google account from youtube api to a zip file
os.system("youtube-dl -u "+ username +" -p "+ password +" --output " + youtube_path +"%(title)s.%(ext)s --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames --write-info-json --write-thumbnail --write-description --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata --ignore-errors --restrict-filenames")
print("Please enter the directory where you want to save your backup: ")
directory = input()
os.system("google-takeout --user " + username + " --output " + directory + " --format mp4")
## use the youtube-dl to backup your youtube account and all viedeos in a zip file with the mp3 format
print("Please enter the directory where you want to save your backup: ")
directory = input()
os.system("youtube-dl --username " + username + " --output " + directory + " --format mp3")
## use the google takeout to backup your youtube account and all viedeos in a zip file with the mp4 format
print("Please enter the directory where you want to save your backup: ")
directory = input()
os.system("google-takeout --user " + username + " --output " + directory + " --format mp4")
print("Backup complete")
print("Thank you for using my program")


## use the python to unzip the backup file
os.system("unzip 1q6g_p6-xvhDZ8CQ2jK9X-gv2s-oW8CzI")
## use the python to move the file to the user input directory
os.system("mv *.mp4 "+username+"/")
## use the python to remove the backup file
os.system("rm 1q6g_p6-xvhDZ8CQ2jK9X-gv2s-oW8CzI")
## use the python to rename the file with the current time
os.system("mv "+username+" "+username+"_"+time.strftime("%Y-%m-%d_%H-%M-%S"))
## use the python to zip the user input directory
os.system("zip -r "+username+".zip "+username+"/")
## use the python to remove the user input directory
os.system("rm -r "+username+"/")
## use the python to move the zip file to the user input directory
os.system("mv "+username+".zip "+username+"/")
## use the python to remove the zip file
os.system("rm "+username+".zip")
print("Your youtube backup is complete")

## (C) Flames LLC 2021