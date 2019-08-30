# questionare
A questionare website for TNMOC

# dependencies
this repository requires
python 3, available from https://python.org, the latest stable version of python is recomended
python also has to be added to PATH
django 2, again the latest stable version is recommended

# setup
as a database is not included in the repository, a database must be constructed.
this can be done by running the following commands or make on unix machines:
the following commands are run from the root directory 
cd Questionare
manage.py migrate
manage.py loaddata queations.json

# invocation
unfortunately a production server isn't included yet however django comes bundled with a web server
this server can be run by running
manage.py runserver 0.0.0.0:80
in the directory Questionare
