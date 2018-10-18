from flask import Flask, render_template
from subprocess import run, PIPE
#from flask import render_template

def run_playbook_to_shutdown_network():
    """
    Run an ansible playbook on disk
    """
    path = '/some/path/dir/disk'
    playbook = run(["python", path], stdout=PIPE)
    response = playbook.stdout
    return response

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html page
    """
   #return 'Hello, World!'
    return render_template('index.html')


@app.route('/shutdown_network', methods=['GET'])
def shutdown_network():
    return run_playbook_to_shutdown_network()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

