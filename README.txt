####################
#  hashservice.py  #
####################

Requires: flask (pip install flask), curl

Usage:
    export FLASK_APP=hashservice.py (Unix) OR
    set FLASK_APP=hashservice.py (Windows)
    flask run
    curl -X POST -H "Content-Type: application/json" -d '{"message": "<msg>"}' <server_url>/messages
    curl <server_url>/messages/<hash>

