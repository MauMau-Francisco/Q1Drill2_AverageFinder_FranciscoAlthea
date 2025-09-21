from pyscript import document

def generate_message(event):
    

    # strings
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # if user left empty
    if not name:
        name = "Blank"
    if not age:
        age = "Blank"
    if not school:
        school = "Blank"

    # escape codes
    profile = f""" Student Profile:
Name\n: \"{name}\"
Age\n:\t{age}
School\n: {school}

Info:
{name} is currently {age} years old and studies at {school}.\nThis produced message was extracted from the input fields and\npresented using PyScript in Python for a multiline string.\
"""

    # display the result inside the <div id="output">
    document.getElementById("output").innerHTML = profile