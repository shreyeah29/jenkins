from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.form['data']
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
