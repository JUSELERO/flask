from flask import Flask, render_template, request , redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pcsoluciones'
mysql=MySQL(app)

app.secret_key = 'mysecretkey'
@app.route("/")
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM procesadores')
    data=cur.fetchall()

    return render_template('index.html' , procesadores = data)



@app.route('/add_procesadores' , methods = ['POST'] )
def add_procesadores():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cores = request.form['cores']
        marca = request.form['marca']
        frecuencia = request.form['frecuencia']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO procesadores (nombre,cores,marca,frecuencia) VALUES (%s,%s,%s,%s)' , (nombre,cores,marca,frecuencia))
        mysql.connection.commit()
        flash('Good job')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM  procesadores WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('contact delet succesfully')
    return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_procesador(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM procesadores WHERE id = {0}'.format(id))
    data = cur.fetchall()
    print (data[0])
    return render_template('edit-procesador.html',procesador = data[0])

@app.route('/update/<id>', methods =['POST'])
def get_procesador_edit(id):
    if request.method == 'POST':
        nombre=request.form['nombre']
        cores=request.form['cores']
        marca=request.form['marca']
        frecuencia=request.form['frecuencia']
    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE procesadores 
    SET nombre = %s,
    cores = %s,
    marca = %s,
    frecuencia = %s 
    WHERE id = %s
    """,(nombre,cores,marca,frecuencia,id))
    flash('procesador update succefully')
    mysql.connection.commit()
    return redirect(url_for('Index'))


if __name__=='__main__':
    app.run(port= 3000,debug=True)