drop database JuSeTech;
create database JuSeTech;
use JuSeTech;


create table Cliente
(id_cliente int   primary key not null,
nombre_cliente varchar(45),
telefono_cliente varchar(45),
direccion_cliente varchar(45),
ciudad_cliente varchar(45),
correo_cliente varchar(45)
);

create table Empleados
(id_empleado int AUTO_INCREMENT primary key not null,
clave varchar(45),
nombre_empleado varchar(45),
telefono_empleado varchar(45),
cargo_empleado varchar(45),
correo_cliente varchar(45)
);

create table Proveedores
(id_proveedor int AUTO_INCREMENT  primary key not null,
nombre_proveedor varchar(45),
tel_proveedor varchar(45)
);

create table Factura
(id_factura int AUTO_INCREMENT  primary key not null,
fecha date,
id_cliente int,
id_empleado int,
constraint fk_cliente_factura foreign key (id_cliente) references Cliente(id_cliente),
constraint fk_Empleados_factura foreign key (id_empleado) references Empleados(id_empleado)
);

create table Compras
(id_compras_factura int AUTO_INCREMENT  primary key not null,
fecha date,
id_empleado int,
id_proveedor int,
constraint fk_proveedores_compras foreign key (id_proveedor) references Proveedores(id_proveedor),
constraint fk_empleado_compras foreign key (id_empleado) references Empleados(id_empleado)
);



create table Productos
(id_producto int AUTO_INCREMENT  primary key not null,
nombre_producto varchar(45),
tipo_producto varchar(45),
marca varchar(45),
valor_unidad float
);

create table Compras_contiene_productos
(id_compras_factura int,
id_empleado int,
id_proveedor int,
id_producto int,
cantidad_compra int,
valor_unidad float,
constraint fk_comprasfac_continene foreign key (id_compras_factura) references Compras(id_compras_factura),
constraint fk_empleado_continene foreign key (id_empleado) references Empleados(id_empleado),
constraint fk_proveedor_contiene foreign key (id_proveedor) references Proveedores(id_proveedor),
constraint fk_producto_contiene foreign key (id_producto) references Productos(id_producto)

);

/*disparador que actualiza inventario cuando se compra algun producto*/
DELIMITER $
create trigger sumar_al_inventario before insert on Compras_contiene_productos for each row begin
update Inventario SET cantidad_inventario=cantidad_inventario + new.cantidad_compra where id_producto=new.id_producto;

END $
DELIMITER ;

create table Factura_contiene_producto
(id_factura int,
id_cliente int,
id_producto int,
cantidad_producto int,
valor_unidad float,
constraint fk_factura_contienep foreign key (id_factura) references Factura(id_factura),
constraint fk_cliente_contienep foreign key (id_cliente) references Cliente(id_cliente),
constraint fk_producto_contienep foreign key (id_producto) references Productos(id_producto)
);


/*disparador que actualiza inventario cuando se vende algun producto*/
DELIMITER $
create trigger restar_al_inventario before insert on Factura_contiene_producto for each row begin
update Inventario SET cantidad_inventario=cantidad_inventario - new.cantidad_producto where id_producto=new.id_producto;

END $
DELIMITER ;

create table Caracteristicas
(id_caracteristicas int AUTO_INCREMENT  primary key not null,
nombre varchar(45)
);

create table Productos_tiene_caracteristicas
(id_producto int,
id_caracteristica int,
constraint fk_productos_tiene foreign key (id_producto) references Productos(id_producto),
constraint fk_caracteristia_tiene foreign key (id_caracteristica) references Caracteristicas(id_caracteristicas)
);


create table Inventario
(id_producto int primary key,
cantidad_inventario int
);

/*disparador que crea los productos en el inventario inventario*/
DELIMITER $
create trigger agregar_al_inventario before insert on Productos for each row begin
insert into Inventario values(new.id_producto,0);
END $
DELIMITER ;


insert into Cliente values (9090,'juan','3193897599','cll 41 N-34-57','bucaramanga','correo');
insert into Cliente values (2132173,'sebastian','3115717400','atalaya','cucuta','corrdfeo');
insert into Cliente values (121232,'camilo','123456','piedecuesta','bucaramanga','corrdfdeo');
insert into Cliente values (434343,'leonardo dallos','4343434','brr la universidad','pegaso','correofd');

insert into Empleados values ('10023','123456','persefone','543343','gerente','correofd');
insert into Empleados values ('20023','123456','lodiba','554333','venedor','correofd');
insert into Empleados values ('20054','123456','narciso','554322','limpieza','correofd');
insert into Empleados values ('20005','cocuyretrix5','luvodipa','5405904','vendedor','correofd');

insert into Proveedores values (55094,'amazon','+12069220880');
insert into Proveedores values (55100,'newegg','+12323343454');
insert into Proveedores values (55044,'tauret computadores','+570316065852,');
insert into Proveedores values (55000,'aliexpress','+00000000');

insert into Productos values (1,'b450m','mobo','asus',54);
insert into Productos values (2,'lpx','RAM','corsair',32);
insert into Productos values (3,'A400','SSD','Kingston',65);


insert into Factura values (1,'2020-03-04',9090,20023);
insert into Factura values (2,'2020-03-01',9090,20023);
insert into Factura values (3,'2020-03-04',2132173,20005);


insert into Compras values (1,curdate(),20023,55100);
insert into Compras values (2,curdate(),20054,55100);




insert into Factura_contiene_producto values (1,9090,1,2,54);
insert into Factura_contiene_producto values (1,9090,2,2,54);

insert into Factura_contiene_producto values (2,9090,1,2,54);
insert into Factura_contiene_producto values (2,9090,2,2,54);



insert into Compras_contiene_productos values (1,20005,55094,1,2,25);
insert into Compras_contiene_productos values (1,20005,55094,3,5,52);