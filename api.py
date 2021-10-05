from flask import jsonify
def json_test():
    return jsonify(test_dict)


test_dict = {
    "name" : "Ben Johnson",
    "year" : 2021,
    "class" : "CSCI 223"
}