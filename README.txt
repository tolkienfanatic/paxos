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


####################
#    findpair.py   #
####################

Usage:
    python findpair.py prices.txt <amount>

i.e:
    python findpair.py prices.txt 2000


####################
#    replaceX.py   #
####################

Usage:
    python replaceX.py <xstring>

i.e.:
    python replaceX.py X0101010X