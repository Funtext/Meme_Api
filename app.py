from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
from reddit_handler import *
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
meme_subreddits = ['memes', 'dankmemes', 'meirl']
@app.route('/')
@cross_origin()
def one_post():
    sub = random.choice(meme_subreddits)
    try:
        re = get_posts(sub, 100)
    except ResponseException:
        return jsonify({
            'status_code': 500,
            'message': 'Internal Server Error'
        })
    r = random.choice(re)
    while not is_img_link(r["url"]):
        r = random.choice(re)
    return jsonify({
        'title': r["title"],
        'url': r["url"],
        'postLink': r["link"],
        'subreddit': sub
    })
@app.route('/<int:count>')
@cross_origin()
def multiple_posts(count):

    if count > 100:
        return jsonify({
            'status_code': 400,
            'message': 'Please ensure the count is less than 100'
        })

    sub = random.choice(meme_subreddits)

    try:
        re = get_posts(sub, 100)

    except ResponseException:
        return jsonify({
            'status_code': 500,
            'message': 'Internal Server Error'
        })

    random.shuffle(re)

    memes = []

    for post in re:
        if len(memes) == count:
            break

        if is_img_link(post['url']):
            temp = {
                'title': post["title"],
                'url': post["url"],
                'postLink': post["link"],
                'subreddit': sub
            }

            memes.append(temp)

    return jsonify({
        'memes': memes,
        'count': len(memes)
    })


@app.route('/<subreddit>')
@cross_origin()
def one_post_from_sub(subreddit):
    try:
        re = get_posts(subreddit, 100)

    except Redirect:
        return jsonify({
            'status_code': 404,
            'message': 'Invalid Subreddit'
        })

    except ResponseException:
        return jsonify({
            'status_code': 500,
            'message': 'Internal Server Error'
        })

    r = random.choice(re)

    while not is_img_link(r["url"]):
        r = random.choice(re)

    return jsonify({
        'title': r["title"],
        'url': r["url"],
        'postLink': r["link"],
        'subreddit': subreddit
    })


@app.route('/<subreddit>/<int:count>')
@cross_origin()
def multiple_posts_from_sub(subreddit, count):

    if count > 100:
        return jsonify({
            'status_code': 400,
            'message': 'Please ensure the count is less than 100'
        })

    try:
        re = get_posts(subreddit, 100)

    except Redirect:
        return jsonify({
            'status_code': 404,
            'message': 'Invalid Subreddit'
        })

    except ResponseException:
        return jsonify({
            'status_code': 500,
            'message': 'Internal Server Error'
        })

    random.shuffle(re)

    memes = []

    for post in re:
        if len(memes) == count:
            break

        if is_img_link(post['url']):
            temp = {
                'title': post["title"],
                'url': post["url"],
                'postLink': post["link"]
            }

            memes.append(temp)

    return jsonify({
        'memes': memes,
        'count': len(memes),
        'subreddit': subreddit
    })

@app.errorhandler(404)
@app.route('/<something>')
def not_found(something):
    return render_template('not_found.html')
