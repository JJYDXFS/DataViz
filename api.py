from flask import Flask, request, render_template, jsonify, redirect
from flask_cors import *
import pymysql
import json
import copy

# 指定静态文件目录
app = Flask(__name__,static_url_path='/static/',template_folder='templates')
# 允许跨域访问
CORS(app, resources=r'/*')

# GET
@app.route('/api/get_pm_info', methods=['GET'])
def get_pm_info():
    '''
    get_pm_info
    '''
    # request.args.get 用于获取GET所传参数
    name=request.args.get('name')

    print(name)

    db = pymysql.connect(host="8.131.66.184",user="JJYDXFS",password="618618",database="dviz" )
    cursor = db.cursor()

    sql="""
    select *
    from stat_info
    where stat_info.name = "{}";
    """.format(name)

    cursor.execute(sql)
    data = cursor.fetchall()[0]

    result = {
        "name":data[0],
        "scale":data[1],
        "begin_age":data[2],
        "age":data[3],
        "times":data[4],
        "info":"暂无"
    }

    cursor = db.cursor()

    sql="""
    select info
    from detail_info
    where detail_info.name = "{}";
    """.format(name)

    cursor.execute(sql)
    data = cursor.fetchall()[0]

    result["info"] = data[0]

    db.close()

    return json.dumps({'result':result},ensure_ascii=False)

# 主页
@app.route('/')
def index():
    return "Hi Flask!"

if __name__ == '__main__':
    app.debug=True  # 默认开启debug模式
    # host=0.0.0.0 port=5000
    app.run('0.0.0.0', 5000)