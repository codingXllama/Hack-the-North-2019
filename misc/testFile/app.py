import os
from flask import Flask, render_template, request


# initializing the app
app = Flask(__name__)

# Locating the root of the app file
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# Setting the main page to route to the upload.html page
@app.route('/')
def index():
    return render_template('upload.html')


# routing the upload method
@app.route("/upload", methods=['POST'])
def upload():
    # getting the current location of the newly uploaded item
    target = os.path.join(APP_ROOT, 'UPLOADS/')
    print(target)

    # if the path does not contain the target directory
    if not os.path.isdir(target):
        os.mkdir(target)

    # going through each file from the file list: requst.files.getlist("file")
    for file in request.files.getlist("file"):
        # print(file)

        # setting the file name
        filename = file.filename
        # creating the destination of newly uploaded file
        destination = "/".join([target, filename])
        # print(destination)

        # saving the file
        file.save(destination)

    return render_template("base.html")


# to run the app
if __name__ == "__main__":
    app.run(port=4555, debug=True)
