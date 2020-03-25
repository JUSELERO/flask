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

@app.route("/clientes", methods = ['POST','GET'] )
def Clientes():
    if request.method == 'POST':
        #si se le llama con metodo POST insertara un valor a la tabla Clientes
        cedula=request.form['cedula']
        nombre=request.form['nombre']
        telefono=request.form['telefono']
        ciudad=request.form['ciudad']
        direccion= request.form['direccion']
        correo= request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Cliente( id_cliente,nombre_cliente, telefono_cliente, direccion_cliente, ciudad_cliente, correo_cliente) VALUES (%s,%s,%s,%s,%s,%s)' , (cedula,nombre,telefono,ciudad,direccion,correo))
        flash('procesador update succefully')
        mysql.connection.commit()
        return redirect(url_for('Clientes')) #devuelve la llamada para que le envien a la pagina la consulta de la base
    else:
        #si se le llama simplemente , enviara la consulta para renderizarla en la paginal
        cur=mysql.connection.cursor()
        cur.execute('select * from Cliente')
        data=cur.fetchall()
        return render_template('clientes.html' , productos = data)


@app.route("/ventas", methods = ['POST','GET'] )
def Ventas():
    if request.method == 'POST':
        id_vendedor = request.form['id_vendedor']        
        id_cliente = request.form['id_cliente']
        id_producto = request.form.getlist('id_producto[]')
        cantidad = request.form.getlist('cantidad[]')
        precio = request.form.getlist('precio[]')

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Factura (fecha,id_cliente,id_empleado) VALUES (curdate(),%s,%s)',(id_cliente,id_vendedor))
        mysql.connection.commit()

        id_factura = cur.lastrowid

        for i,id in enumerate(id_producto):
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO Factura_contiene_producto (id_factura,id_cliente,id_producto,cantidad_producto,valor_unidad) VALUES (%s,%s,%s,%s,%s)',(id_factura,id_cliente,id_producto[i],cantidad[i],precio[i]))
            mysql.connection.commit()

        flash('Good job')
        return redirect(url_for('Ventas'))   
    else:
        cur=mysql.connection.cursor()
        cur.execute('select P.nombre_producto,P.tipo_producto,P.marca,I.cantidad_inventario,P.valor_unidad from Productos P left join Inventario I on P.id_producto=I.id_producto;')
        data=cur.fetchall()
        return render_template('ventas.html' , Ventas = data)

@app.route("/compras", methods = ['POST','GET'] )
def Compras():
    if request.method == 'POST':
        id_vendedor = request.form['id_vendedor']        
        id_cliente = request.form['id_cliente']
        id_producto = request.form.getlist('id_producto[]')
        cantidad = request.form.getlist('cantidad[]')
        precio = request.form.getlist('precio[]')

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Compras (fecha,id_empleado,id_proveedor) VALUES (curdate(),%s,%s)',(id_vendedor,id_cliente))
        mysql.connection.commit()

        id_factura = cur.lastrowid

        for i,id in enumerate(id_producto):
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO Compras_contiene_productos (id_compras_factura,id_empleado,id_proveedor,id_producto,cantidad_compra,valor_unidad) VALUES (%s,%s,%s,%s,%s,%s)',(id_factura,id_vendedor,id_cliente,id_producto[i],cantidad[i],precio[i]))
            mysql.connection.commit()
        flash('Good job')

        return redirect(url_for('Compras'))   
    else:
        cur=mysql.connection.cursor()
        cur.execute('select P.nombre_producto,P.tipo_producto,P.marca,I.cantidad_inventario from Productos P left join Inventario I on P.id_producto=I.id_producto;')
        data=cur.fetchall()
        return render_template('compra.html' , compras = data)       

@app.route('/productos' , methods = ['POST','GET'] )
def Productos():
    if request.method == 'POST':
        om= request.form['om']   
        nombre = request.form['nombre']        
        marca = request.form['marca']
        tipo= request.form['tipo']
        precio= request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Productos (id_producto,nombre_producto,tipo_producto,marca,valor_unidad) VALUES (%s,%s,%s,%s,%s)' , (om,nombre,tipo,marca,precio))
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
        precio= request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE Productos SET nombre_producto = %s , tipo_producto = %s, marca = %s, valor_unidad = %s WHERE id_producto = %s' , (nombre,tipo,marca,precio,id))
        flash('procesador update succefully')
        mysql.connection.commit()
        return redirect(url_for('Productos'))
    else :
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Productos WHERE id_producto = {}'.format(id))
        data = cur.fetchall()
        print (data[0])
        return render_template('edit-productos.html',procesador = data[0])

@app.route('/edit-cliente/<id>',methods = ['POST','GET'] )
def Get_clientes(id):
    if request.method == 'POST':
        nombre=request.form['nombre']
        telefono=request.form['telefono']
        ciudad=request.form['ciudad']
        direccion= request.form['direccion']
        correo= request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE Cliente SET nombre_cliente = %s , telefono_cliente= %s, direccion_cliente = %s, ciudad_cliente = %s, correo_cliente = %s WHERE id_cliente= %s' , (nombre,telefono,ciudad,direccion,correo,id))
        flash('procesador update succefully')
        mysql.connection.commit()
        return redirect(url_for('Clientes'))
    else :
        cur = mysql.connection.cursor()
       # cur.execute(f'DELETE FROM Cliente WHERE id_cliente = {id}')  codigo para elimina (NO QUEDA EN USO) 
        cur.execute('SELECT * FROM Cliente WHERE id_cliente = {}'.format(id))
        data = cur.fetchall()
        print (data[0])
        return render_template('edit-cliente.html',procesador = data[0])


@app.route('/empleados', methods = ['POST','GET'] )
def Empleados():
    if request.method == 'POST':
        om= request.form['om']   
        nombre = request.form['nombre']  
        telefono=request.form['telefono']      
        cargo = request.form['cargo']
        correo= request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Empleados (id_empleado,clave,nombre_empleado,telefono_empleado,cargo_empleado,correo_cliente) VALUES (%s,%s,%s,%s,%s,%s)' , (om,correo,nombre,telefono,cargo,correo))
        mysql.connection.commit()
        flash('Good job')
        return redirect(url_for('Empleados'))
    else:
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM Empleados')
        data=cur.fetchall()
        return render_template('empleados.html' , productos = data)


@app.route('/edit-empleado/<id>',methods = ['POST','GET'] )
def Get_empleados(id):
    if request.method == 'POST':
        om= request.form['om']   
        nombre = request.form['nombre']  
        telefono=request.form['telefono']      
        cargo = request.form['cargo']
        correo= request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE Empleados SET id_empleado = %s , nombre_empleado = %s , telefono_empleado= %s, cargo_empleado = %s, correo_cliente = %s WHERE id_empleado= %s' , (om,nombre,telefono,cargo,correo,id))
        flash('procesador update succefully')
        mysql.connection.commit()
        return redirect(url_for('Empleados'))
    else :
        cur = mysql.connection.cursor()
       # cur.execute(f'DELETE FROM Cliente WHERE id_cliente = {id}')  codigo para elimina (NO QUEDA EN USO) 
        cur.execute('SELECT * FROM Empleados WHERE id_empleado = {}'.format(id))
        data = cur.fetchall()
        print (data[0])
        return render_template('edit-empleado.html',procesador = data[0])

@app.route('/proveedores', methods = ['POST','GET'] )
def Proveedores():
    if request.method == 'POST':
        om= request.form['om']   
        nombre = request.form['nombre']  
        telefono=request.form['telefono']      
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Proveedores (id_proveedore,nombre_proveedor,tel_proveedor) VALUES (%s,%s,%s)' , (om,nombre,telefono))
        mysql.connection.commit()
        flash('Good job')
        return redirect(url_for('Proveedores'))
    else:
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM Proveedores')
        data=cur.fetchall()
        return render_template('proveedores.html' , productos = data)

@app.route('/edit-proveedor/<id>',methods = ['POST','GET'] )
def Get_proveedores(id):
    if request.method == 'POST':
        om= request.form['om']   
        nombre = request.form['nombre']  
        telefono=request.form['telefono']      
        cur = mysql.connection.cursor()
        cur.execute('UPDATE Proveedores SET id_proveedor = %s , nombre_proveedor = %s , tel_proveedor= %s WHERE id_proveedor= %s' , (om,nombre,telefono,id))
        flash('procesador update succefully')
        mysql.connection.commit()
        return redirect(url_for('Proveedores'))
    else :
        cur = mysql.connection.cursor()
       # cur.execute(f'DELETE FROM Cliente WHERE id_cliente = {id}')  codigo para elimina (NO QUEDA EN USO) 
        cur.execute('SELECT * FROM Proveedores WHERE id_proveedor = {}'.format(id))
        data = cur.fetchall()
        print (data[0])
        return render_template('edit-proveedor.html',procesador = data[0])






###### bet ###############################################

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
    app.run(debug=True, host='192.168.1.56',port=80)
