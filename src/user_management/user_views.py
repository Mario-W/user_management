from flask import Flask, request, jsonify
from manage import app
from user_handler import UserHandler
from copy import deepcopy

@app.route('/user/user_list/', methods=['GET'])
def user_list():
    page_index = request.args.get('page_index')
    user_handler = UserHandler()
    users = user_handler.get_user_list(page_index) if page_index else user_handler.get_user_list()
    return jsonify({'res': 'ok', 'data': [{
                                              'id': user.id,
                                              'name': user.name,
                                              'age': user.age,
                                              'sex': user.sex,
                                              'address': user.address,
                                          } for user in users]})

@app.route('/user/add_user/', methods=['POST'])
def add_user():
    if request.method == 'POST':
        data = deepcopy(request.json) if request.is_json else deepcopy(request.form)
        user_handler = UserHandler()
        result, result_msg = user_handler.add_user(data)
        if not result:
            return jsonify({'res': 'error', 'msg': result_msg})
        else:
            return jsonify({'res': 'ok', 'msg': result_msg})
    else:
        return jsonify({'res': 'error', 'msg': 'request must be post'})

@app.route('/user/edit_user/', methods=['POST'])
def edit_user():
    if request.method == 'POST':
        data = deepcopy(request.json) if request.is_json else deepcopy(request.form)
        user_id = data.get('user_id')
        user_handler = UserHandler()
        result, result_msg = user_handler.edit_user(user_id, data)
        if not result:
            return jsonify({'res': 'error', 'msg': result_msg})
        else:
            return jsonify({'res': 'ok', 'msg': result_msg})
    else:
        return jsonify({'res': 'error', 'msg': 'request must be post'})

@app.route('/user/delete_user/', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        data = deepcopy(request.json) if request.is_json else deepcopy(request.form)
        user_id = data.get('user_id')
        user_handler = UserHandler()
        result, result_msg = user_handler.delete_user(user_id)
        if not result:
            return jsonify({'res': 'error', 'msg': result_msg})
        else:
            return jsonify({'res': 'ok', 'msg': result_msg})
    else:
        return jsonify({'res': 'error', 'msg': 'request must be post'})

@app.route('/user/sign_in_ranking/', methods=['GET'])
def sign_in_ranking_list():
    page_index = request.args.get('page_index')
    user_handler = UserHandler()
    user_count_list = user_handler.get_sign_in_ranking_list(page_index) if page_index else \
        user_handler.get_sign_in_ranking_list()
    return jsonify({'res': 'ok', 'data': user_count_list})

@app.route('/user/sign_in/', methods=['POST'])
def sign_in():
    if request.method == 'POST':
        data = deepcopy(request.json) if request.is_json else deepcopy(request.form)
        user_id = data.get('user_id')
        user_handler = UserHandler()
        result, result_msg = user_handler.sign_in(user_id)
        if not result:
            return jsonify({'res': 'error', 'msg': result_msg})
        else:
            return jsonify({'res': 'ok', 'msg': result_msg})
    else:
        return jsonify({'res': 'error', 'msg': 'request must be post'})

if __name__ == '__main__':
    app.run()