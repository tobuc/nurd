from notification_process import notification_process
from app import notificationQueue
from datetime import datetime
BAD_WORDS = ["fee", "nee", "cruul", "leent"]


def bad_word_check(review):
    f = open("bad_word_check.txt", "a")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f.write("Review saved succesfully and checking for bad words " + "name: " + review['name'] + " email: " + review['email'] + " product id: " +
            review['productid'] + " review: " + review['review']+" Current Time= "+current_time+ "\n")
    f.close()
    for x in BAD_WORDS:
        if x in review['review']:
            notificationQueue.enqueue(notification_process, review, True)
            return True
    notificationQueue.enqueue(notification_process, review,False)
    return False
