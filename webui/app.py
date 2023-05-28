# app.py
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)

# 文件上传目录
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 限制图片大小（最大为16MB）
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
# 支持的文件
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS



# 判断文件名是否是我们支持的格式
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

# index
@app.route('/index', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

# team
@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template("team.html")

# aiphoto
@app.route('/aiphoto', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('aiphoto.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)