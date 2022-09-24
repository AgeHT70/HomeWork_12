from flask import Blueprint, render_template, request
from config import UPLOAD_FOLDER, POST_PATH
from functions import check_extension, add_post_to_json, loger

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def page_post():
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    content: str = request.form["content"]
    picture = request.files.get("picture")

    filename = picture.filename

    if not check_extension(filename):
        loger.info(f"{filename} is not a picture")
        return "Not available file format,<br>Please upload JPEG or PNG"

    try:
        picture.save(UPLOAD_FOLDER + filename)
    except Exception:
        loger.error(f"Error with uploading file {filename}")
        return "Error with uploading file"

    post = {
        "pic": "/uploads/images/" + filename,
        "content": content
    }
    add_post_to_json(POST_PATH, post)

    return render_template("post_uploaded.html", post=post)
