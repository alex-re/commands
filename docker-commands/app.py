from flask import Flask
import redis


app = Flask(__name__)


@app.route('/')
def say_hello():
    '''
    index page of the app
    '''
    redis_conn = redis.Redis(host='docker-redis-container-name', port=6379, db=0)
    name = redis_conn.get('name')
    return f'Hello {name}\n'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
