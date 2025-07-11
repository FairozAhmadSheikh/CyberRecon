from flask import Flask, render_template, request
from scanners import port_scanner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        scan_type = request.form.get('scan_type')
        target = request.form.get('target')