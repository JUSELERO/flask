from flask import Flask, render_template, request , redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'juse'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'JuSeTech'


mysql=MySQL(app)

app.secret_key = 'mysecretkey'

@app.route("/")
def Inicio():
    return render_template('Inicio.html' )




@app.route("/index")
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM procesadores')
    data=cur.fetchall()

    return render_template('index.html' , procesadores = data)

@app.route("/ventas")
def Ventas():
    return render_template('ventas.html')


@app.route("/ventas-echa")
def Ventas_echa():
    cur=mysql.connection.cursor()
    cur.execute('select P.nombre_producto,P.tipo_producto,P.marca,I.cantidad_inventario from Productos P left join Inventario I on P.id_producto=I.id_producto;')
    data=cur.fetchall()
    return render_template('ventas.html' , Ventas = data)


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
    else:
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM Productos')
        data=cur.fetchall()
        return render_template('productos.html' , productos = data)

@app.route('/delete/<string:id>')
def delete_producto(id):
    cur = mysql.connection.cursor()
    cur.execute(f'DELETE FROM Productos WHERE id_producto = {id}')
    mysql.connection.commit()
    flash('contact delet succesfully')
    return redirect(url_for('Productos'))

@app.route('/edit/<id>')
def get_producto(id):
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
    else :
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM procesadores WHERE id = {}'.format(id))
        data = cur.fetchall()
        print (data[0])
        return render_template('edit-procesador.html',procesador = data[0])

#Inicio de sesion
@app.route("/Sesion")
def Sesion():
    return render_template('sesion.html')

#Crear Usuario
@app.route("/crear-usuario", methods = ['POST','GET'])
def Crear_usuario():
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
    else:
        return render_template('crear-usuario.html')

if __name__=='__main__':
    app.run(port = 3000)