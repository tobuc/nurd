from flask import Flask
import redis
from rq import Queue
app = Flask(__name__)

r= redis.Redis()
reviewQueue = Queue(connection=r)
notificationQueue = Queue(connection=r)

