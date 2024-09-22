import os
import shutil

UPLOAD_FOLDER = os.path.join('static', 'upload')
EXPORT_FOLDER = os.path.join('static', 'export')
ALLOWED_EXTENSIONS = {'mp4'}


def allowed_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def copy_file(src, dst):
    shutil.copy2(src, dst)
