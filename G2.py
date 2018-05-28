from flask import Flask, request
from psycopg2 import connect, OperationalError


def create_connection(db_name = 'exercise_db'):
    username = "postgres"
    password = "coderslab"
    host = 'localhost'

    try:
        connection = connect(user=username, password=password, host=host, database=db_name)
        return connection

    except OperationalError:
        return None

app = Flask("bilet")

@app.route('/')
def product():
    cnx = create_connection()
    if cnx:
        result = ''
        cursor = cnx.cursor()
        cursor.execute("""
            SELECT id, name, price FROM "order";
        """)
        #używamy fetchall ponieważ w nie możemy skorzystać z cursora
        #do wykonania kolejnego zapytania dopóki go nie opróżnimy
        for order in cursor.fetchall():
            result += "Zamówienie: {} {}<br>".format(order[0], order[1])
            cursor.execute("""
              SELECT * FROM product JOIN order_product ON product.id = order_product.product_id
              WHERE order_product.order.id = {};
            
            """.format(order[0]))
        for product in cursor:
            result += "Produkt: {} {} [} <br>".format(product[0], product[1], product[2])

        cursor.close()
        cnx.close()
        return result


if __name__ == "__main__":
    app.run()