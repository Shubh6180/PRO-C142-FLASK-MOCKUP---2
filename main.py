from storage import all_articles, liked_articles, not_liked_articles
from demographic import output
from content_filtering import get_recommendations
from flask import Flask, jsonify, request

app = Flask('__name__')

@app.route("/get-article")
def get_article():
    movie_data = {
        "url": all_articles[0][12],
        "title": all_articles[0][13],
        "text": all_articles[0][14],
        "lang": all_articles[0][15],
        "total_events": all_articles[0][16]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-article")
def popular_article():
    article_data = []
    for i in output:
        data = {
            'url': i[0],
            'title': i[1],
            'text': i[2],
            'lang': i[3],
            'total_events': i[4],
        }
        article_data.append(data)
    return jsonify({
        'data': article_data,
        'message': 'success'
    })

@app.route("/recommended-article")
def recommended_article():
    all_recommended = []
    for liked_article in liked_articles:
        recommended = get_recommendations(liked_article[17])
        for data in recommended:
            all_recommended.append(data)
    article_data = []
    for i in all_recommended:
        data = {
            'url': i[0],
            'title': i[1],
            'text': i[2],
            'lang': i[3],
            'total_events': i[4],
        }
        article_data.append(data)
    return jsonify({
        'data': article_data,
        'message': 'success'
    })

if __name__ == "__main__":
    app.run(debug=True)