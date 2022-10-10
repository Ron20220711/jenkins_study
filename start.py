from application import create_app

app = create_app("development")


@app.route('/', methods=['POST','GET'])
def hello_world():
    return "aaa"


if __name__ == '__main__':
    app.run(debug=True)
