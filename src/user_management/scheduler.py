import requests
import random
import traceback
from apscheduler.schedulers.blocking import BlockingScheduler
from user_models import User, session


def random_user_sign_in():
    user_id_list = session.query(User.id)
    select_user_id = random.choice(user_id_list)
    try:
        result = requests.post('http://127.0.0.1:12345/user/sign_in/', data={'user_id': select_user_id}, timeout=2).json()
        print(result)
    except:
        print(traceback.format_exc())

def test():
    print('this is a test!')

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(random_user_sign_in, 'interval', seconds=3)
    print('Press Ctrl+C to exit')

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass