import traceback
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user/user_list/', methods=['GET'])
def user_list():
    page_index = request.args.get('page_index')
    result = {'user_name': page_index, 'user_id': page_index}
    return jsonify(result)

@app.route('/user/add_user/', methods=['POST'])
def add_user():
    if request.method == 'POST':
        age = request.args.get('age')
        name = request.args.get('name')
        sex = request.args.get('sex')
        address = request.args.get('address')
        if not age:
            return jsonify({'res': 'error', 'msg': '请输入年龄'})
        if not name:
            return jsonify({'res': 'error', 'msg': '请输入姓名'})
        if not sex:
            return jsonify({'res': 'error', 'msg': '请输入性别'})
        if not address:
            return jsonify({'res': 'error', 'msg': '请输入地址'})
        try:
            # TODO save user info
            return jsonify({'res': 'ok', 'msg': '添加成功'})
        except:
            print(traceback.format_exc())
            return jsonify({'res': 'error', 'msg': '保存失败'})
    else:
        return jsonify({'res': 'error', 'msg': 'request must be post'})

@app.route('/user/edit_user/', methods=['POST'])
def edit_user():
    if request.method == 'POST':
        age = request.args.get('age')
        name = request.args.get('name')
        sex = request.args.get('sex')
        address = request.args.get('address')
        if not age:
            return jsonify({'res': 'error', 'msg': '请输入年龄'})
        if not name:
            return jsonify({'res': 'error', 'msg': '请输入姓名'})
        if not sex:
            return jsonify({'res': 'error', 'msg': '请输入性别'})
        if not address:
            return jsonify({'res': 'error', 'msg': '请输入地址'})
        try:
            # TODO update user info
            return jsonify({'res': 'ok', 'msg': '修改成功'})
        except:
            print(traceback.format_exc())
            return jsonify({'res': 'error', 'msg': '保存失败'})
    else:
        return jsonify({'res': 'error', 'msg': 'request must be post'})

@app.route('/user/delete_user/', methods=['POST'])
def delete_user():
    pass

@app.route('/user/sign_in_ranking/', methods=['GET'])
def sign_in_ranking_list():
    pass

@app.route('/user/sign_in/', methods=['POST'])
def sign_in():
    pass

if __name__ == '__main__':
    app.run()