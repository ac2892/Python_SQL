# Z02DTWorkspace

Use this repository in GitHub Codespaces

If you are running the codespace for the first time you'll need to check that Sqlite3 is installed in the terminal window to add the local database to the server. If it says its already installed you are good to go, in you need to say yes to install then install it.

*sudo apt update*

*sudo apt install sqlite3*

To check sqlite3 is running and want to view its version run: 

*sqlite3 --version*

In the DB folder there is a test datbase file, you can access this directly using the Sqlite3 interpreter using, you can use same command to create a new database file and it will connect your automatically: 

*cd DB/*

*sqlite3 databasename.db*