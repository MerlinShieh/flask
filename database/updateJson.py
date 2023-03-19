import traceback
import json


def select(username):
    with open(r'user.json', 'r') as f:
        user_json: dict = json.loads(f.read())
        try:
            return user_json.get(username, False)
        except:
            print('method error')
            traceback.print_exc()
            return False


def insert(username=None, passwd=None):
    if not username or not passwd:
        print('username or passwd is empty !')
        return False
    with open(r'user.json', 'r') as f:
        user_json: dict = json.loads(f.read())
        if user_json.get(username, False):
            return False
        else:
            user_json[username] = passwd
    with open(r'user.json', 'w') as f:
        f.write(json.dumps(user_json))
        return True


if __name__ == '__main__':
    print(select('Merlin'))
    print(insert('mersin', '123'))
