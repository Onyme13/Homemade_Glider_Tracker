"""Flask app that serve map localy for the map display in GUI_tkinter.py"""
from flask import Flask, send_file, abort
import os


app = Flask(__name__)

@app.route('/tiles/<int:z>/<int:x>/<int:y>.png')
def get_tile(z,x,y):
    #filename = f'tiles_Grey/{z}/{x}/{y}.png'
    filename = f'tiles_OSM/{z}/{x}/{y}.png'
    if os.path.exists(filename):
        return send_file(filename, mimetype='image/png')
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
