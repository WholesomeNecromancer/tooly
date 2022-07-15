#! tooly.py
from tryst import Tryst

import importlib

from flask import Flask, request, jsonify
app = Flask(__name__)

# A RESTful API exposing toolshed apps for more user-friendly access via Postman, etc.

@app.route("/")
def index():
    return "# TODO: implement index."

@app.route("/<string:tool>", methods=['GET'])
def use_tool(tool):
    # TODO: here we implement trying to load/run the tool
    # extract configuration information and inputs from the incoming payload
    # capture the output of the tool and include it in the response payload
    # easy peasy.
    # suppose we could try with tryst.py itself
    # try to load the tool
    importlib.import_module(tool)
    # get access to the tool's main()
    toolmain = getattr(tool, "main")
    # get inputs from request body
    requestbody = request.json
    # now call toolman and capture outputs
    tooltryst = Tryst()
    toolmain(tooltryst, requestbody["args"])

    return jsonify(tooltryst.outputbuffer)

    # return tool + " requested!"

if __name__ == "__main__":
    app.run()
