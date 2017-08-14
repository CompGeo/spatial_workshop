# spatial_workshop


on a Mac/ linux machine:

Install Flask:

in a terminal:
```
pip install flask

```

To run the Flask server:

in a terminal:
navigate to the directory containing app.py

```
$ FLASK_APP=app.py flask run
```

If hyou have issues, check out the documentation here:
http://docs.python-guide.org/en/latest/



on a Windows machine:

Install Flask:

in a cmd window:

```
pip install flask

```

Note: if Windows can't find 'pip', you may need to add it or python to the path. 
If python is on the path, you may need to install pip if you have an old python install. 
Check here for correctly installing python on Windows: 
python2: http://docs.python-guide.org/en/latest/starting/install/win/
python3: http://docs.python-guide.org/en/latest/starting/install3/win/

To run the Flask server:

make sure that python and flask are on the path.

start menu
look for “advanced system settings”
'Environment Variables' button
look for 'Path'
'Edit...' button

For Windows 7 & 8: 
if the path is not there
* append the full paths to python and 'Scripts\', preceded by a semi-colon
(path is just a single long string)

For Windows 10:
if the paths are not there:
* add the full path to python
* add the full path to 'Scripts\'

each path is a separate value.

You can set the environment variable "FLASK_APP" in the same dialog or on the command line.
```
set FLASK_APP=app.py
```

Then

```
flask run

```
