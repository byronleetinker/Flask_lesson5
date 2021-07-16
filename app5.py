from flask import Flask, render_template, request

app = Flask(__name__)


#
# @app.route('/')
# def log():
#     return render_template('login1.html')
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['userpass']
#     if username == "Byron Lee" and password == "1234":
#         return "Welcome %s" % username + request.method
#     else:
#         return "Error in logging in" + request.method


@app.route('/')
def shopping():
    return render_template('shoppinglist.html')


@app.route('/items', methods=['POST', 'GET'])
def items():
    if request.method == 'POST':
        result = request.form
        return render_template('showitems.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
