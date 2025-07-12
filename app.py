from flask import Flask, render_template, request
from scanners import port_scanner, subdomain_enum

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    scan_type = ''
    if request.method == 'POST':
        scan_type = request.form.get('scan_type')
        target = request.form.get('target')

        if scan_type == 'port':
            result = port_scanner.scan(target)
        elif scan_type == 'subdomain':
            result = subdomain_enum.enumerate_subdomains(target)

    return render_template('index.html', result=result, scan_type=scan_type)

if __name__ == '__main__':
    app.run(debug=True)
