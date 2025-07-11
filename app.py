from flask import Flask, render_template, request
from scanners import port_scanner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        scan_type = request.form.get('scan_type')
        target = request.form.get('target')

        if scan_type == 'port':
            result = port_scanner.scan(target)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
