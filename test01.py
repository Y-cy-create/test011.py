from flask import *
app = Flask(__name__)
@app.route('/forcompany')
def page():
    return render_template('forcompany.html')

@app.route('/submit', methods =['POST'])
def submit():
    title = request.values["title"]#把所有對應的值(values)抓出
    area = request.values['area']
    salary = request.values["salary"]
    skill = request.values['skill']
    detail = request.values['detail']

    if title == "資料分析師" and area == "台北市" and salary == '1' and skill == '123' and detail == "123" :
        return "Good!"
    else:
        return "Bad!"

if __name__ == '__main__':
    app.debug = True
    app.run()