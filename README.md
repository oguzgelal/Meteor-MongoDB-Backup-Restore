MongoDB Backup/Restore Script for Meteor
==========

These are two simple scripts you can use to backup and restore your **Mongo** database of your **Meteor** application. 

# Usage
Copy these to where you want to store your backups. The location doesn't have to be where your project is, it could ve anywhere on your computer. 

##### To backup
While you are in the directory where the folders are, run :
```sh
./backup.py <meteor_app_url> <meteor_password>
```
And the script will create a new folder **backup-day\_month\_year-hour\_min\_secs** and under that folder, there will be another folder **your_app**. All your backups will be under your_app.

##### To restore
While you are in the directory where the folders are, run :
```sh
./restore.py <meteor_app_url> <meteor_password> <backup_dir>
```
The backup directory that you should restore from is **your_app** folder.