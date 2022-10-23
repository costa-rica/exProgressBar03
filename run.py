from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/add_apple2', methods=['GET', 'POST'])
def add_apple_2():
    if request.method == 'POST':
        print(request.method)
        print(request.files)
        filesize = request.cookies.get('filesize')
        # file = request.files['files']
        print(f"Filesize: {filesize}")
        # print(file)

        # res = make_response(jsonify({"message": f"{file.filename} uploaded"}), 200)
        # return res
    return render_template('add_apple.html')

if __name__ == '__main__':
    app.run()