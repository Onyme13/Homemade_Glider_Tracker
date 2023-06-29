import flask


app = flask.Flask(__name__)

@app.route('/tiles/<int:z>/<int:x>/<int:y>.png')
def get_tile(z,x,y):
    filename = f'tiles_Grey/{z}/{x}/{y}.png'
    print(x,y,z)
    return flask.send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
