from dataclasses import dataclass

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'some random data'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_crud_db'

mysql = MySQL(app)


@app.route('/')
def dashboard():
    cursor = mysql.connection.cursor()


    cursor.execute("SELECT COUNT(*) FROM biscuit_tbl")
    total_items = cursor.fetchone()[0]


    cursor.execute("SELECT COUNT(*) FROM biscuit_tbl WHERE Quantity Received <= 5")
    low_stock_count = cursor.fetchone()[0]


    cursor.execute("SELECT Name of Biscuit, Price FROM biscuit_tbl ORDER BY id DESC LIMIT 2")
    recent_items = cursor.fetchall()

    cursor.close()
    print(total_items, low_stock_count, recent_items)
    return render_template(
        'dashboard.html',
        total_items=total_items,
        low_stock_count=low_stock_count,
        recent_items=recent_items
    )



@app.route('/create')
def create_page():
    return render_template('create.html')


@app.route('/add', methods=['POST'])
def add_biscuits():
    if request.method == "POST":
        Name_of_Biscuit = request.form['name_of_biscuit']
        Price = request.form['price']
        Quantity_Received = request.form['quantity']
        Expiry_Date = request.form['expiry_date']
        Batch_Number = request.form['batch_no']
        Biscuit_Subtype = request.form['biscuit_subtype']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO biscuit_tbl (Name of Biscuit, Price, Quantity Received, Expiry Date, Batch Number, Biscuit Subtype) VALUES (%s, %s, %s, %s, %s,%s)",
            (Name_of_Biscuit, Price, Quantity_Received, Expiry_Date, Batch_Number, Biscuit_Subtype))

        mysql.connection.commit()
        return redirect(url_for('dashboard'))


@app.route('/inventory')
def view_inventory():
    search_query = request.args.get('search', '')

    cursor = mysql.connection.cursor()

    if search_query:
        query = "SELECT * FROM biscuit_tbl WHERE Item_name LIKE %s"
        cursor.execute(query, ('%' + search_query + '%',))
    else:
        query = "SELECT * FROM biscuit_tbl"
        cursor.execute(query)

    biscuit = cursor.fetchall()
    return render_template('inventory.html', biscuits=biscuit, search_query=search_query)


@app.route('/edit/<int:id>', methods=['GET'])
def edit_item(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM biscuit_tbl WHERE id = %s", (id,))
    biscuit = cursor.fetchone()
    return render_template('update.html', biscuit=biscuit)


@app.route('/update/<int:id>', methods=['POST'])
def update_item(id):
    Name_of_Biscuit = request.form['name_of_biscuit']
    Price = request.form['price']
    Quantity_Received = request.form['Quantity_Received']
    Expiry_Date = request.form['Expiry_Date']
    Batch_Number = request.form['Batch_no']
    Biscuit_Subtype = request.form['biscuit_subtype']

    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE biscuit_tbl
        SET Name_of_Biscuit = %s, Price = %s, Quantity_Received = %s, Expiry_Date = %s, Batch_Number = %s, Biscuit_Subtype = %s
        WHERE id = %s
    """, (Name_of_Biscuit, Price, Quantity_Received, Expiry_Date, Batch_Number,Biscuit_Subtype, id))
    mysql.connection.commit()
    return redirect(url_for('view_inventory'))


@app.route('/update')
def update_list():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM biscuit_tbl")
    biscuit = cursor.fetchall()
    return render_template('update_list.html', biscuit=biscuit)

@app.route('/delete')
def delete_page():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM biscuit_tbl")
    biscuit = cursor.fetchall()
    cursor.close()
    return render_template('delete.html', biscuit=biscuit)


@app.route('/delete<int:id>', methods=['POST'])
def delete_utensil(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM biscuit_tbl WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('view_inventory'))


if __name__ == '__main__':
    app.run(debug=True, port = 4996)
    app.run(debug = True)
