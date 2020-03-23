from flask import Flask, render_template, request , redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'JuSeTech'
mysql=MySQL(app)

app.secret_key = 'mysecretkey'

@app.route("/Sesion")
def Sesion():
    return render_template('sesion.html')

@app.route("/crear-usuario")
def Crear_usuario():
    return render_template('crear-usuario.html')

@app.route("/Crear-usuario-final", methods = ['POST'])
def Crear_usuario_final():
    if request.method == 'POST':
        cedula= request.form['cedula']
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        tipo = request.form['tipo']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (cedula,nombre,correo,clave,tipo) VALUES (%s,%s,%s,%s,%s)' , (cedula,nombre,correo,clave,tipo))
        mysql.connection.commit()
        flash ('Good job')
    return redirect(url_for('Crear_usuario'))

Crear_usuario_final
@app.route("/")
def Inicio():
    return render_template('Inicio.html' )




@app.route("/index")
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM procesadores')
    data=cur.fetchall()

    return render_template('index.html' , procesadores = data)

@app.route("/productos")
def Productos():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM Productos')
    data=cur.fetchall()

    return render_template('productos.html' , productos = data)

@app.route('/add_producto' , methods = ['POST'] )
def add_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']        
        marca = request.form['marca']
        tipo= request.form['tipo']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Productos (nombre_producto,tipo_producto,marca) VALUES (%s,%s,%s)' , (nombre,tipo,marca))
        mysql.connection.commit()
        flash('Good job')
        return redirect(url_for('Productos'))



@app.route('/add_procesadores' , methods = ['POST'] )
def add_procesadores():
    if request.method == 'POST':
        nombre = request.form['nombre']        
        marca = request.form['marca']
        tipo= request.form['tipo']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO producto (nombre_producto,tipo_producto,marca) VALUES (%s,%s,%s)' , (nombre,tipo,marca))
        mysql.connection.commit()
        flash('Good job')
        return redirect(url_for('Productos'))

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