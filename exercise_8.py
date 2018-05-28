from flask import Flask, request

app = Flask(__name__)
contacts = {}

def get_html():
    form = """
       <form method = "POST">
           <label>
               Name:
               <input name="contactName">
           </label>
           <label>
               Phone:
               <input name="contactNo">
           </label>
           <input type="submit">
       </form>
       """
    contacts_table = "<table>"
    for contactName, contactNo in contacts.items():
        contacts_table += """
           <tr>
               <td>{}</td>
               <td>{}</td>
           </tr>
           """.format(contactName, contactNo)
    return contacts_table + "<br/>" + form

@app.route('/', methods=['GET', 'POST'])
def phone_book():

    if request.method == 'GET':
        return get_html()
    else:
        contactName = str(request.form["contactName"])
        contactNo = str(request.form["contactNo"])
        contacts[contactName] = contactNo
        return get_html()


if __name__ == "__main__":
    app.run()


