# Changelog

# master  

## v7.5.2  

### New features  
- add lots of command.  
- support powershell.  
- support custom environment.  
- support transport environ across between two environ assemblage.  

### Changes

* default execute shell root is in <User's source root>/UserShell.  
* pymake export2 command can export separate env, +basic, +custom env to a file.  
* lots of shortcut to pymake command.     

## v6.0.0

###New features

* support export environ variable
* update environ .json data structure.

###Changes

* you can execute command in bash file or use pymake execute command.
* you can execute command in one bash file but multi environment and consume little energy

----
## v5.0.0

###New features

* support change source root

###Changes

* you can install pymake to anywhere and collect all config file to another one place.

----
## v1.0.0

###New features

* support cmake

###Changes

* add 'source' command to support multi computers.

###Bugs fixed

* fix 'list-path' command adding new item to 'add-to-dev'
