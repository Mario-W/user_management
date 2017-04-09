import traceback
from manage import redis_instance
from user_models import User, session

class UserHandler(object):

    def __init__(self):
        pass

    def _check_data(self, data):
        age = data.get('age')
        name = data.get('name')
        sex = data.get('sex')
        address = data.get('address')
        if not age:
            return False, '请输入年龄'
        if not name:
            return False, '请输入姓名'
        if not sex:
            return False, '请输入性别'
        if not address:
            return False, '请输入地址'
        if not isinstance(age, int):
            return False, '年龄格式不正确'
        if not sex in ['男', '女', '未知']:
            return False, '性别不正确'
        return True, {'age': age, 'name': name, 'sex': sex, 'address': address}

    def add_user(self, data):
        result, msg = self._check_data(data)
        if not result:
            return result, msg
        user_obj = c
        try:
            session.add(user_obj)
            session.commit()
            return True, '添加成功'
        except:
            print(traceback.format_exc())
            return False, '添加失败'

    def edit_user(self, user_id, data):
        user_obj = User.query.filter_by(id=user_id).first()
        if not user_obj:
            return False, '找不到该用户'
        data = {
            'name': data.get('name', user_obj.name),
            'age': data.get('age', user_obj.age),
            'sex': data.get('sex', user_obj.sex),
            'address': data.get('address', user_obj.address),
        }
        result, msg = self._check_data(data)
        if not result:
            return result, msg
        try:
            # user_obj._sa_instance_state.committed_state.update(msg)
            msg['id'] = user_obj.id
            user_obj = User(**msg)
            session.merge(user_obj)
            session.commit()
            return True, '修改成功'
        except:
            print(traceback.format_exc())
            return False, '修改失败'

    def delete_user(self, user_id):
        user_obj = User.query.filter_by(id=user_id).first()
        if not user_obj:
            return False, '找不到该用户'
        try:
            session.delete(user_obj)
            return True, '删除成功'
        except:
            return False, '删除失败'

    def get_user_list(self, page_index=0):
        page_count = 20
        if not isinstance(page_index, int):
            return []
        user_list = User.query.all()
        if not page_index:
            return user_list
        else:
            return user_list[(page_index-1)*page_count: page_index*page_count]

    def sign_in(self, user_id):
        try:
            redis_instance.incr('user_{}'.format(str(user_id)))
            return True, '成功'
        except:
            print(traceback.format_exc())
            return False, '失败'

    def get_sign_in_ranking_list(self, page_index=0):
        page_count = 20
        if not isinstance(page_index, int):
            return []
        user_list = User.query.all()
        result = [{
            'user_id': user.id,
            'user_name': user.name,
            'sign_in_count': redis_instance.get('user_{}'.format(user.id)) if redis_instance.get(
                'user_{}'.format(user.id)) else 0
                  } for user in user_list]
        if not page_index:
            return result
        else:
            return result[(page_index - 1) * page_count: page_index * page_count]