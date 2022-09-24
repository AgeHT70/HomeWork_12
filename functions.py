import json
import logging


def load_data(filename: str) -> list[dict]:
    """
    Loads data from json-file.
    :param filename: name of json-file
    :return: list of dictionaries with data
    """
    with open(filename, encoding='UTF-8') as file:
        data = json.load(file)
    return data


def search_by_word(path: str, word: str) -> list[dict]:
    """

    :param path:
    :param word:
    :return:
    """

    result = [post for post in load_data(path) if word.lower() in post['content'].lower()]
    return result


def add_post_to_json(filename: str, post: dict) -> None:
    """
    Add post to json
    Rewrite json
    :param filename:
    :param post: new post
    :return: None
    """
    posts: list = load_data(filename)
    posts.append(post)
    write_to_json(filename, posts)


def write_to_json(filename: str, posts: list) -> None:
    """
    Rewrite json file
    :param filename:
    :param posts: list with all posts
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)


def check_extension(filename: str) -> bool:
    """
    Check is extension is available
    :param filename: Name of check file
    :return: True if available else False
    """
    if filename.split(".")[1] not in ("jpeg", "png", "jpg"):
        return False
    return True


loger = logging.getLogger("project_loger")
loger.setLevel(logging.INFO)
loger_handler = logging.FileHandler("log.log")
loger_formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
loger_handler.setFormatter(loger_formatter)
loger.addHandler(loger_handler)
