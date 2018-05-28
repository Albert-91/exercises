from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def postal_code():
    form = """
    <form method = "POST">
        <input name="code">
        <input type="submit">
    </form>
    """
    if request.method == 'GET':
        return form
    else:
        code = request.form["code"]
        parts = code.split('-')
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 3:
            return "Kod niepoprawny"
        else:
            return "Kod poprawny"

if __name__ == "__main__":
    app.run()


