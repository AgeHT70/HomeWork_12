from flask import Blueprint, render_template, request
from config import POST_PATH
from functions import search_by_word, loger
from json import JSONDecodeError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search/')
def page_search():
    search_word = request.args.get('s')
    try:
        posts = search_by_word(POST_PATH, search_word)
        loger.info(f"Search by {search_word}")
    except FileNotFoundError:
        return "File Not Found"
    except JSONDecodeError:
        return "Can`t convert to JSON"
    else:
        return render_template('post_list.html', posts=posts, search_word=search_word)


