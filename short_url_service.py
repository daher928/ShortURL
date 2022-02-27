"""
   Short URL service implementation
   Author: Daher Daher
   Date and Time: 26 Feb 2021 14:49
"""

from flask import Flask, request, jsonify, url_for
from werkzeug.utils import redirect

from memory_store import InMemoryStore
from short_url_utils import ShortUrlGenerator

service = Flask(__name__)
service.config['DATABASE'] = 'in_memory_store'

db = InMemoryStore()  # key=shortUrl, val=originalUrl
short_url_generator = ShortUrlGenerator(prefix="http://shrt.url")

"""
   POST API for encoding (shortening) a new URL
   POST request structure example:
    {
        'url': 'https://blog.hexa3d.io/posts/the-underlying-motivations-of-nft-trading'
    }
    
    response:
    {
        'message': 'created',
        'short_url': 'http://shrt.url/0'
    }
"""
@service.route('/encode', methods=['POST'])
def encode():
    if 'url' not in request.json:
        return jsonify(message='missing url', short_url="none"), 400

    url = request.json['url']
    short_url = short_url_generator.generate_next_shortest_url()

    db.set(short_url, url)
    return jsonify(message='created', short_url=short_url), 201

"""
   GET API for decoding a short URL
    Get request structure example:
        GET http://localhost:5000/decode?short_url=http://shrt.url/0
    
    response:
    {
        'original_url': 'https://blog.hexa3d.io/posts/the-underlying-motivations-of-nft-trading'
    }
"""
@service.route('/decode', methods=['GET'])
def decode():
    if 'short_url' not in request.args:
        return jsonify(original_url='missing short_url'), 400

    short_url = request.args.get('short_url')
    try:
        original_url = db.get(short_url)
        return jsonify(original_url=original_url), 200
    except Exception:
        return jsonify(original_url='unrecognized short URL'), 200  # return OK since it is not a server or client error


if __name__ == '__main__':
    service.run()
