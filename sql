create database JuSeTech;
use JuSeTech;


create table Cliente
(id_cliente int primary key,
nombre_cliente varchar(45),
telefono_cliente varchar(45),
direccion_cliente varchar(45)
);

create table Empleados
(id_empleado int primary key,
clave varchar(45),
nombre_empleado varchar(45),
telefono_empleado varchar(45),
cargo_empleado varchar(45)
);

create table Proveedores
(id_proveedor int primary key,
nombre_proveedor varchar(45),
tel_proveedor varchar(45)
);

create table Factura
(id_factura int,
fecha date,
id_cliente int,
id_empleado int,
primary key(id_factura),
constraint fk_cliente_factura foreign key (id_cliente) references Cliente(id_cliente),
constraint fk_Empleados_factura foreign key (id_empleado) references Empleados(id_empleado)
);

create table Compras
(id_compras_factura int primary key,
fecha date,
id_empleado int,
id_proveedor int,
constraint fk_proveedores_compras foreign key (id_proveedor) references Proveedores(id_proveedor),
constraint fk_empleado_compras foreign key (id_empleado) references Empleados(id_empleado)
);

create table Productos
(id_producto int primary key not null,
nombre_producto varchar(45),
tipo_producto varchar(45),
marca varchar(45)
);

create table Compras_contiene_productos
(id_compras_factura int,
id_empleado int,
id_proveedor int,
id_producto int,
cantidad_compra int,
constraint fk_comprasfac_continene foreign key (id_compras_factura) references Compras(id_compras_factura),
constraint fk_empleado_continene foreign key (id_empleado) references Empleados(id_empleado),
constraint fk_proveedor_contiene foreign key (id_proveedor) references Proveedores(id_proveedor),
constraint fk_producto_contiene foreign key (id_producto) references Productos(id_producto)

);

create table Factura_contiene_producto
(id_factura int,
id_cliente int,
id_producto int,
cantidad_producto varchar(45),
valor_total int,
constraint fk_factura_contienep foreign key (id_factura) references Factura(id_factura),
constraint fk_cliente_contienep foreign key (id_cliente) references Cliente(id_cliente),
constraint fk_producto_contienep foreign key (id_producto) references Productos(id_producto)
);

create table Caracteristicas
(id_caracteristicas int primary key,
nombre varchar(45),
valor varchar(45)
);

create table Productos_tiene_caracteristicas
(id_producto int,
id_caracteristica int,
constraint fk_productos_tiene foreign key (id_producto) references Productos(id_producto),
constraint fk_caracteristia_tiene foreign key (id_caracteristica) references Caracteristicas(id_caracteristicas)
);


create table Inventario
(id_producto int primary key,
cantidad_intentario varchar(45)
);

insert into Cliente values (9090,'juan','3193897599','cll 41 N-34-57');
insert into Cliente values (2132173,'sebastian','3115717400','atalaya');
insert into Cliente values (121232,'camilo','123456','piedecuesta');
insert into Cliente values (434343,'leonardo dallos','4343434','brr la universidad');

insert into Empleados values (10023,'123456','persefone','543343','gerente');
insert into Empleados values (20023,'123456','lodiba','554333','venedor');
insert into Empleados values (20054,'123456','narciso','554322','limpieza');
insert into Empleados values (20005,'cocuyretrix5','luvodipa','5405904','vendedor');

insert into Proveedores values (55094,'amazon','+12069220880');
insert into Proveedores values (55100,'newegg','+12323343454');
insert into Proveedores values (55044,'tauret computadores','+570316065852,');
insert into Proveedores values (55000,'aliexpress','+00000000');


insert into Factura values (1,'2020-03-04',9090,20023);
insert into Factura values (2,'2020-03-01',9090,20023);
insert into Factura values (3,'2020-03-04',2132173,20005);


insert into Compras values (213,curdate(),20023,55100);
insert into Compras values (111,curdate(),20054,55100);
