import os
from flask import Flask, render_template, redirect, request, flash
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import tensorflow as tf
from common.utils import allowed_file, UPLOAD_FOLDER, EXPORT_FOLDER
from services.human_pose_detection_service import HumanPoseDetectionService

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 16MB
app.secret_key = 'PiYCGJcn5JW10cw7qowyEK8tiXU6iDNV'

@app.route("/")
def home():
    return render_template("index.html", view=None)

@app.route('/', methods=['POST'])
def create():
    # check if the post request has the file part
    if 'video' not in request.files:
        flash('Please select a video..', category="danger")
        return redirect(request.url)

    file = request.files['video']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('Please select a video..', category="danger")
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)

        if not os.path.exists(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)

        if not os.path.exists(EXPORT_FOLDER):
            os.mkdir(EXPORT_FOLDER)

        file.save(path)

        try:
            # Use HumanPoseDetectionService to predict the action in the video
            human_pose_service = HumanPoseDetectionService()
            view = human_pose_service.predict_single_action(filename, path, seq_length=30)  # Adjust seq_length as needed

            flash('Video processed successfully..', category="success")
            return render_template("index.html", view=view)
        except Exception as e:
            flash(f'Video processing failed: {str(e)}', category="danger")
            return redirect(request.url)  # Ensure a response is returned

    else:
        flash('Please upload a video with a valid format.', category="danger")
        return redirect(request.url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)