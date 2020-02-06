import json

# converts lines of a file to python dictionary
def file_to_dict(read_lines):
    string = ""
    for line in read_lines:
        string += line
    return json.loads(string)