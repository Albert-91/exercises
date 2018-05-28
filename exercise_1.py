from flask import Flask, request
from math import factorial
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def numbers():
    form = """
    <form method="POST">
        <input name = "n">
        <input type = "submit">
    </form>
    """
    if request.method == "GET":
        return form
    else:
        n = int(request.form["n"])
        html = """
        <table>
            <tr>
                <td>{}
            </tr>
        </table>
        <table>
            <tr>
                <td>{}
            </tr>
        </table>
        <table>
            <tr>
                <td>{}
            </tr>
        </table>
        """
        return html.format(2 ** n, n ** n, factorial(n))

if __name__ == "__main__":
    app.run()


