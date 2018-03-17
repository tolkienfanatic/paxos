from flask import Flask, request, jsonify
from hashlib import sha256

app = Flask("hash")
# we use this to store messages
message_map = {}

# Just in case
@app.route("/")
def hello():
    return "Hi, this is a small hashing service"

# Posts a message to the server and returns the sha256 hash
@app.route("/messages", methods=["POST"])
def post_message():
    # pick up the posted json content
    content = request.json

    h = sha256()
    # update the hash with the message from our json
    h.update(content["message"])

    # get the (hex) digest of the message, hex is import or things
    hex_d = h.hexdigest()

    # add the message to our map
    message_map[hex_d] = content["message"]
    return jsonify(digest=hex_d)

# Input: sha256 hash
# Output: If  the hash is stored, return the original message. If not, return 404
@app.route("/messages/<hash>", methods=["GET"])
def get_message(hash):
    # Check if the hash is stored, if yes, return the message
    if hash in message_map:
        return jsonify(message=message_map[hash])
    # If the hash is not stored, return a sensible error message and 404
    else:
        return jsonify(err_msg="Message not found"), 404

