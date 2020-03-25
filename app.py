from flask import Flask, render_template, request , redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'JuSeTech'


mysql=MySQL(app)

app.secret_key = 'mysecretkey'

@app.route("/")
def Inicio():
    return render_template('Inicio.html' )

@app.route("/clientes", methods = ['POST','GET'] )
def Clientes():
    if request.method == 'POST':
        #deve ser corregido para que el post que le llegue guarde los productos
        return redirect(url_for('Productos'))   
    else:
        cur=mysql.connection.cursor()
        cur.execute('select * from Cliente')
        data=cur.fetchall()
        return render_template('clientes.html' , productos = data)


@app.route("/ventas", methods = ['POST','GET'] )
def Ventas():
    if request.method == 'POST':
        #deve ser corregido para que el post que le llegue guarde las ventas
        return redirect(url_for('Productos'))   
    else:
        cur=mysql.connection.cursor()
        cur.execute('select P.nombre_producto,P.tipo_producto,P.marca,I.cantidad_inventario from Productos P left join Inventario I on P.id_producto=I.id_producto;')
        data=cur.fetchall()
        return render_template('ventas.html' , Ventas = data)

@app.route("/compras", methods = ['POST','GET'] )
def Compras():
    if request.method == 'POST':
        #deve ser corregido para que el post que le llegue guarde las compras('Productos') esta mal
        return redirect(url_for('Productos'))   
    else:
        cur=mysql.connection.cursor()
        cur.execute('select P.nombre_producto,P.tipo_producto,P.marca,I.cantidad_inventario from Productos P left join Inventario I on P.id_producto=I.id_producto;')
        data=cur.fetchall()
        return render_template('compra.html' , compras = data)       


@app.route("/ventas-echa")
def Ventas_echa():
    cur=mysql.connection.cursor()
    cur.execute('select P.nombre_producto,P.tipo_producto,P.marca,I.cantidad_inventario from Productos P left join Inventario I on P.id_producto=I.id_producto;')
    data=cur.fetchall()
    return render_template('ventas.html' , Ventas = data)

@app.route('/productos', methods = ['POST','GET'] )
def Productos():
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

@app.route('/edit/<id>',methods = ['POST','GET'] )
def get_producto(id):
    if request.method == 'POST':
        nombre=request.form['nombre']
        tipo=request.form['tipo']
        marca=request.form['marca']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE Productos SET nombre_producto = %s , tipo_producto = %s, marca = %s WHERE id_producto = %s' , (nombre,tipo,marca,id))
        flash('procesador update succefully')
        mysql.connection.commit()
        return redirect(url_for('Productos'))
    else :
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Productos WHERE id_producto = {}'.format(id))
        data = cur.fetchall()
        print (data[0])
        return render_template('edit-productos.html',procesador = data[0])

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