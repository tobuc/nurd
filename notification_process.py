import time
from datetime import datetime
def notification_process(review,hasBadWord):
    time.sleep(1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("notification_history.txt", "a")
    if hasBadWord:
        f.write(
            "Review is inappropriate " + "name: " + review['name'] + " email: " + review['email'] + " product id: " +
            review['productid'] + " review: " + review['review'] +" Current Time= "+current_time+ "\n")
    else:
        f.write(
            "Mail function is called. Review is appropriate " + "name: " + review['name'] + " email: " + review['email'] + " product id: " +
            review['productid'] + " review: " + review['review'] +" Current Time= "+current_time+ "\n")
    f.close()