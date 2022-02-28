import json


def load_data():
    with open('data/data.json', encoding='utf8') as f:
        data = json.load(f)
    return data


def load_comments():
    with open('data/comments.json', encoding='utf8') as f:
        comments = json.load(f)
    return comments


def get_post(uid):
    posts = load_data()
    for post in posts:
        if post['pk'] == uid:
            return post
    return None


def get_comment(uid):
    post_comments = []
    comments = load_comments()
    for comment in comments:
        if comment['post_id'] == uid:
            post_comments.append(comment)
    return post_comments


def delete_repetition(my_list):
    return list({d['pk']: d for d in my_list}.values())


def search_post(req):
    post_search = []
    posts = load_data()
    if req:
        req = req.split()
        for post in posts:
            post_content_word = post['content'].replace('!', "").replace(',', "").replace('.', "")
            post_content_word = post_content_word.split()
            if len(req) > 1:
                for idx in range(len(req)):
                    if req[idx] in post_content_word:
                        post_search.append(post)
        return delete_repetition(post_search)
    else:
        return posts


def search_user_post(username):
    post_search = []
    posts = load_data()
    for post in posts:
        if username == post['poster_name']:
            post_search.append(post)
    return delete_repetition(post_search)