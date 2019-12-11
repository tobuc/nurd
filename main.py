from app import app
from app import reviewQueue
from bad_word_check import bad_word_check
from db_config import mysql
from flask import jsonify
from flask import request
import time


def insertdb(review):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _name = review['name']
        _email = review['email']
        _productId = review['productid']
        _review = review['review']
        sql = "INSERT INTO productreview(ReviewerName,EmailAddress,ProductID,Comments,Rating) VALUES('%s', '%s', %s, '%s',%s)" % (
            _name, _email, _productId, _review, "0")
        print(sql)
        cursor.execute(sql)
        conn.commit()
        rev_id = cursor.lastrowid
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return {"success": "true", "reviewID": rev_id}


@app.route('/api/reviews', methods=['POST'])
def curl_listen():
    retval = {}
    try:
        _json = request.json
        print(_json)
        if _json['name'] and _json['email'] and _json['productid'] and _json['review'] and request.method == 'POST':
            retval = insertdb(_json)
        else:
            return not_found()
    except Exception as e:
        return not_found()
    job = reviewQueue.enqueue(bad_word_check, request.json)
    print(f"Task ({job.id}) added to queue at {job.enqueued_at}")
    return retval


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(500)
def internal_server_error(error=None):
    message = {
        'status': 500,
        'message': 'Internal Server Error: ' +request.url,
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
