from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('files/' + file.filename)
    return jsonify({
        'status': 'success',
        'message': 'File uploaded successfully'
    })

if __name__ == '__main__':
    app.run(debug=True)
