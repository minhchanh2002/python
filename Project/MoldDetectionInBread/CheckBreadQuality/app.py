import os

from flask import Flask, render_template, redirect, request, flash
from werkzeug.utils import secure_filename

from common.utils import allowed_file, UPLOAD_FOLDER, EXPORT_FOLDER
from services.mold_detection_service import MoldDetectionService

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 16MB
app.secret_key = 'PiYCGJcn5JW10cw7qowyEK8tiXU6iDNV'


@app.route("/")
def home():
    return render_template("index.html", view=None)


@app.route('/', methods=['POST'])
def create():
    # check if the post request has the file part
    if 'image' not in request.files:
        flash('Please select image..', category="danger")
        return redirect(request.url)

    file = request.files['image']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('Please select image..', category="danger")
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)

        if os.path.exists(UPLOAD_FOLDER) == False:
            os.mkdir(UPLOAD_FOLDER)

        if os.path.exists(EXPORT_FOLDER) == False:
            os.mkdir(EXPORT_FOLDER)

        file.save(path)

        try:
            # Write process dectection in this function
            view = MoldDetectionService().detect(filename, path)

            flash('Detect image success..', category="success")
            return render_template("index.html", view=view)
        except NameError:
            flash('Detect image failed..', category="danger")

    else:
        flash('Please import image with format: png, jpg, jpeg, webp', category="danger")
        return redirect(request.url)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8000, debug=True)
