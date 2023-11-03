import sqlite3

# import cx_Oracle

DEBUG_ORACLE = False



class CoolBox:
    def __init__(self, name):
        self.name = name
        # Crear un objeto cursor para ejecutar comandos SQL
        # self.cursor = self.databaseCreationOrConnection(self.name)
        self.conn, self.cursor = self.databaseCreationOrConnection()

    # Creacion de la base de datos
    def databaseCreationOrConnection(self):
        if DEBUG_ORACLE == True:
            # Credenciales de conexión
            # dsn = cx_Oracle.makedsn("host", "port", service_name="service_name")
            # username = "tu_usuario"
            # password = "tu_contraseña"

            # Crear una conexión
            # conn = cx_Oracle.connect(username, password, dsn)            
            # cursor = conn.cursor()
            # return conn, cursor
            pass
        else:
            conn = sqlite3.connect(f"{self.name}.db")
            cursor = conn.cursor()
            return conn, cursor

    # creación de la entidad de relación categorias productos
    def creationOfTheProductCategoryRelationshipEntity(self):
        self.cursor.execute("""
            CREATE TABLE Categorias_Productos (
                categoria_code INTEGER NOT NULL,
                producto_code INTEGER NOT NULL,
                PRIMARY KEY (categoria_code, producto_code),
                FOREIGN KEY (categoria_code) REFERENCES Categorias(code),
                FOREIGN KEY (producto_code) REFERENCES Productos(code)
            );
                    """)

    # creación de la entidad de relación producto proveedor
    def creationOfTheProductSupplierRelationshipEntity(self):
        self.cursor.execute("""
            CREATE TABLE Productos_Proveedores (
                producto_code INTEGER NOT NULL,
                proveedor_code INTEGER NOT NULL,
                PRIMARY KEY (producto_code, proveedor_code),
                FOREIGN KEY (producto_code) REFERENCES Productos(code),
                FOREIGN KEY (proveedor_code) REFERENCES Proveedores(code)
            );
                    """)

    # Creacion de la entidad de detalles compras
    def creationOfPurchasingDetails(self):
        self.cursor.execute("""
            CREATE TABLE Detalle_Compra (
                code INTEGER NOT NULL PRIMARY KEY,
                cliente_code INTEGER NOT NULL,
                producto_code INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                fecha DATE NOT NULL,
                monto_total INTEGER NOT NULL,
                FOREIGN KEY (cliente_code) REFERENCES Clientes(code),
                FOREIGN KEY (producto_code) REFERENCES Productos(code)
            );
                    """)

    # Creacion de la entidad de Contactos
    def contactCreation(self):
        self.cursor.execute("""
            CREATE TABLE Contactos (
                code INTEGER NOT NULL PRIMARY KEY,
                cliente_code INTEGER NOT NULL,
                nombre VARCHAR2(50) NOT NULL,
                apellido VARCHAR2(50) NOT NULL,
                telefono VARCHAR(11) NOT NULL,
                correo VARCHAR2(100) NOT NULL,
                FOREIGN KEY (cliente_code) REFERENCES Clientes(code)
            );

                    """)

    # Creacion de la entidad de Categorias
    def categoryCreation(self):
        self.cursor.execute("""
            CREATE TABLE Categorias (
                code INTEGER NOT NULL PRIMARY KEY,
                nombre VARCHAR2(50) NOT NULL,
                descripcion VARCHAR2(100) NOT NULL
            );
                    """)

    # Inserta datos en la tabla Detalle_Compra
    def insertDetalleCompraData(self):
        detalle_compra_data = [
            (1, 1, 1, 10, '2023-11-01', 500),
            (2, 2, 3, 5, '2023-11-02', 250),
            (3, 3, 2, 8, '2023-11-03', 400),
            (4, 4, 5, 12, '2023-11-04', 600),
            (5, 5, 4, 6, '2023-11-05', 300),
            (6, 6, 6, 15, '2023-11-06', 750),
            (7, 7, 9, 4, '2023-11-07', 200),
            (8, 8, 7, 9, '2023-11-08', 450),
            (9, 9, 8, 7, '2023-11-09', 350),
            (10, 10, 10, 20, '2023-11-10', 1000),
            (11, 11, 12, 3, '2023-11-11', 150),
            (12, 12, 11, 14, '2023-11-12', 700),
            (13, 13, 15, 6, '2023-11-13', 300),
            (14, 14, 14, 18, '2023-11-14', 900),
            (15, 15, 13, 11, '2023-11-15', 550),
            (16, 16, 16, 9, '2023-11-16', 450),
            (17, 17, 17, 4, '2023-11-17', 200),
            (18, 18, 20, 13, '2023-11-18', 650),
            (19, 19, 18, 5, '2023-11-19', 250),
            (20, 20, 19, 7, '2023-11-20', 350),
            # Agregar los 10 registros restantes aquí
        ]

        for detalle_compra in detalle_compra_data:
            self.cursor.execute("""
                INSERT INTO Detalle_Compra (code, cliente_code, producto_code, cantidad, fecha, monto_total)
                VALUES (?, ?, ?, ?, ?, ?)
            """, detalle_compra)


    # Inserta datos en la tabla Categorias
    def insertCategoryData(self):
        category_data = [
            (1, 'Electrónica', 'Productos electrónicos de consumo'),
            (2, 'Ropa', 'Ropa y accesorios de moda'),
            (3, 'Hogar', 'Productos para el hogar'),
            (4, 'Deportes', 'Artículos deportivos'),
            (5, 'Alimentación', 'Productos alimenticios'),
            (6, 'Salud y Belleza', 'Productos de salud y belleza'),
            (7, 'Automóviles', 'Piezas y accesorios para automóviles'),
            (8, 'Libros', 'Libros y medios impresos'),
            (9, 'Música', 'Instrumentos y accesorios musicales'),
            (10, 'Juguetes', 'Juguetes y juegos para niños'),
            (11, 'Electrodomésticos', 'Electrodomésticos para el hogar'),
            (12, 'Muebles', 'Muebles y decoración para el hogar'),
            (13, 'Tecnología', 'Productos de tecnología y electrónica'),
            (14, 'Deporte y Aire Libre', 'Equipamiento deportivo y actividades al aire libre'),
            (15, 'Bricolaje y Herramientas', 'Herramientas y suministros de bricolaje'),
            (16, 'Jardín', 'Productos para el jardín y exteriores'),
            (17, 'Oficina', 'Suministros y mobiliario de oficina'),
            (18, 'Mascotas', 'Productos para mascotas'),
            (19, 'Arte y Manualidades', 'Material de arte y productos para manualidades'),
            (20, 'Videojuegos', 'Videojuegos y consolas'),
            (21, 'Joyas', 'Joyas y relojes'),
            (22, 'Viajes', 'Reservas y servicios de viaje'),
            (23, 'Instrumentos Musicales', 'Instrumentos musicales y accesorios'),
            (24, 'Cine y Series', 'Películas y series en formato físico y digital'),
            (25, 'Herramientas de Cocina', 'Utensilios y herramientas de cocina'),
            (26, 'Fotografía', 'Cámaras y equipos de fotografía'),
            (27, 'Bebés', 'Productos para bebés y cuidado infantil'),
            (28, 'Religión', 'Artículos y libros religiosos'),
            (29, 'Belleza y Cuidado Personal', 'Productos de belleza y cuidado personal'),
            (30, 'Artes Escénicas', 'Entradas y productos relacionados con las artes escénicas')
        ]

        for category in category_data:
            self.cursor.execute("""
                INSERT INTO Categorias (code, nombre, descripcion)
                VALUES (?, ?, ?)
                                """, category)


    # Creacion de la entidad de Clientes
    def clientCreation(self):
        self.cursor.execute("""
            CREATE TABLE Clientes (
                code INTEGER NOT NULL PRIMARY KEY,
                nombre VARCHAR2(50) NOT NULL,
                apellido VARCHAR2(50) NOT NULL,
                ruc VARCHAR(11) NOT NULL
            );

                    """)
    # Creacion de la entidad de Productos
    def productCreation(self):
        self.cursor.execute("""
            CREATE TABLE Productos (
                code INTEGER NOT NULL PRIMARY KEY,
                nombre VARCHAR2(50) NOT NULL,
                descripcion VARCHAR2(100) NOT NULL,
                precio_Actual DECIMAL(8, 2) NOT NULL,
                stock INTEGER NOT NULL,
                proveedor_code INTEGER NOT NULL,
                FOREIGN KEY (proveedor_code) REFERENCES Proveedores(code)
            );
                    """)

    # Creacion de la entidad de Proveedores
    def supplierCreation(self):
        self.cursor.execute("""
            CREATE TABLE Proveedores (
                code INTEGER NOT NULL PRIMARY KEY,
                nombre VARCHAR2(50) NOT NULL,
                ruc VARCHAR(11) NOT NULL,
                descripcion VARCHAR2(100) NOT NULL,
                direccion VARCHAR(100) NOT NULL,
                numero_telefono VARCHAR(11) NOT NULL,
                pagina_web VARCHAR2(100) NOT NULL
            );
                    """)
    # Inserta datos en la tabla Categorias_Productos
    def insertCategoriasProductosData(self):
        categorias_productos_data = [
            (1, 1),
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 5),
            (3, 6),
            (4, 7),
            (4, 8),
            (5, 9),
            (5, 10),
            # Agrega las combinaciones de categoría y producto restantes aquí
        ]

        for categoria_producto in categorias_productos_data:
            self.cursor.execute("""
                INSERT INTO Categorias_Productos (categoria_code, producto_code)
                VALUES (?, ?)
            """, categoria_producto)



    # inserta datos de clientes
    def insertCustomerData(self):
        supplier_data = [
            (1, 'Juan', 'Pérez', '12345678901'),
            (2, 'María', 'González', '23456789012'),
            (3, 'Carlos', 'López', '34567890123'),
            (4, 'Ana', 'Martínez', '45678901234'),
            (5, 'Luis', 'Rodríguez', '56789012345'),
            (6, 'Laura', 'Fernández', '67890123456'),
            (7, 'Pedro', 'Sánchez', '78901234567'),
            (8, 'Sofía', 'Díaz', '89012345678'),
            (9, 'Javier', 'Torres', '90123456789'),
            (10, 'Lucía', 'Ramírez', '01234567890'),
            (11, 'Diego', 'Hernández', '11223344556'),
            (12, 'Valentina', 'Gómez', '22334455667'),
            (13, 'Manuel', 'Pérez', '33445566778'),
            (14, 'Carmen', 'López', '44556667789'),
            (15, 'Francisco', 'García', '55667778990'),
            (16, 'Isabel', 'Martínez', '66778899001'),
            (17, 'Andrés', 'Fernández', '77889900112'),
            (18, 'Luisa', 'Sánchez', '88990011223'),
            (19, 'Roberto', 'Díaz', '99001122334'),
            (20, 'Elena', 'Rodríguez', '00112233445')
        ]

        for supplier in supplier_data:
            self.cursor.execute("""
                INSERT INTO Clientes (code, nombre, apellido, ruc)
                VALUES (?, ?, ?, ?)
                                """, supplier)

    # Inserta datos en la tabla Productos_Proveedores
    def insertProductosProveedoresData(self):
        productos_proveedores_data = [
            (1, 1),
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 5),
            (3, 6),
            (4, 7),
            (4, 8),
            (5, 9),
            (5, 10),
            # Agrega las combinaciones de producto y proveedor restantes aquí
        ]

        for producto_proveedor in productos_proveedores_data:
            self.cursor.execute("""
                INSERT INTO Productos_Proveedores (producto_code, proveedor_code)
                VALUES (?, ?)
            """, producto_proveedor)



    # inserta datos de proveedores
    def insertSupplierData(self):

        supplier_data = [

            (1, 'Dell', '12345678901', 'Proveedor de productos electrónicos y computadoras', '123 Main Street', '123-456-7890', 'www.dell.com'),
            (2, 'Apple Inc.', '98765432109', 'Proveedor de dispositivos móviles y computadoras', '456 Elm Street', '987-654-3210', 'www.apple.com'),
            (3, 'HP', '56789012345', 'Proveedor de impresoras y equipos de cómputo', '789 Oak Street', '567-890-1234', 'www.hp.com'),
            (4, 'Samsung Electronics', '34567890123', 'Proveedor de electrónicos y dispositivos móviles', '101 Pine Street', '345-678-9012', 'www.samsung.com'),
            (5, 'Sony', '67890123456', 'Proveedor de electrónicos y equipos de entretenimiento', '222 Cedar Street', '678-901-2345', 'www.sony.com'),
            (6, 'LG Electronics', '45678901234', 'Proveedor de productos electrónicos y electrodomésticos', '333 Maple Street', '456-789-0123', 'www.lg.com'),
            (7, 'Logitech', '78901234567', 'Proveedor de periféricos y accesorios para computadoras', '444 Birch Street', '789-012-3456', 'www.logitech.com'),
            (8, 'NVIDIA', '23456789012', 'Proveedor de tarjetas gráficas y soluciones de gráficos', '555 Walnut Street', '234-567-8901', 'www.nvidia.com'),
            (9, 'Microsoft', '98765432101', 'Proveedor de software y dispositivos tecnológicos', '666 Oak Avenue', '987-654-3210', 'www.microsoft.com'),
            (10, 'Canon', '12345678910', 'Proveedor de cámaras y equipos de imágenes', '777 Elm Avenue', '123-456-7891', 'www.canon.com'),
            (11, 'ASUS', '34567890121', 'Proveedor de computadoras y componentes de hardware', '888 Pine Avenue', '345-678-9012', 'www.asus.com'),
            (12, 'Amazon', '56789012343', 'Proveedor de productos y servicios en línea', '999 Birch Avenue', '567-890-1234', 'www.amazon.com'),
            (13, 'Lenovo', '78901234564', 'Proveedor de computadoras y dispositivos móviles', '1111 Cedar Avenue', '789-012-3456', 'www.lenovo.com'),
            (14, 'JBL', '23456789021', 'Proveedor de equipos de audio y altavoces', '1212 Walnut Avenue', '234-567-8902', 'www.jbl.com'),
            (15, 'AMD', '45678901233', 'Proveedor de procesadores y soluciones de gráficos', '1313 Maple Avenue', '456-789-0123', 'www.amd.com'),
            (16, 'DJI', '98765432122', 'Proveedor de drones y equipos de fotografía aérea', '1414 Oak Drive', '987-654-3212', 'www.dji.com'),
            (17, 'Bose', '12345678932', 'Proveedor de sistemas de audio y auriculares', '1515 Elm Drive', '123-456-7893', 'www.bose.com'),
            (18, 'GoPro', '34567890144', 'Proveedor de cámaras de acción y accesorios', '1616 Pine Drive', '345-678-9014', 'www.gopro.com'),
            (19, 'Dell', '23456789012', 'Proveedor de productos electrónicos y computadoras', '1717 Cedar Drive', '234-567-8901', 'www.dell.com'),
            (20, 'Sony', '56789012341', 'Proveedor de electrónicos y equipos de entretenimiento', '1818 Walnut Drive', '567-890-1234', 'www.sony.com'),
            
            (21, 'Acer', '23456789023', 'Proveedor de computadoras y productos electrónicos', '1919 Oak Drive', '234-567-8902', 'www.acer.com'),
            (22, 'Bose', '56789012345', 'Proveedor de sistemas de audio y auriculares', '2020 Elm Drive', '567-890-1234', 'www.bose.com'),
            (23, 'Canon', '78901234567', 'Proveedor de cámaras y equipos de imágenes', '2121 Pine Drive', '789-012-3456', 'www.canon.com'),
            (24, 'Dell', '34567890122', 'Proveedor de productos electrónicos y computadoras', '2222 Cedar Drive', '345-678-9012', 'www.dell.com'),
            (25, 'ASUS', '45678901234', 'Proveedor de computadoras y componentes de hardware', '2323 Walnut Avenue', '456-789-0123', 'www.asus.com'),
            (26, 'Samsung Electronics', '12345678900', 'Proveedor de electrónicos y dispositivos móviles', '2424 Maple Avenue', '123-456-7890', 'www.samsung.com'),
            (27, 'Microsoft', '56789012349', 'Proveedor de software y dispositivos tecnológicos', '2525 Oak Avenue', '567-890-1234', 'www.microsoft.com'),
            (28, 'Lenovo', '78901234567', 'Proveedor de computadoras y dispositivos móviles', '2626 Elm Avenue', '789-012-3456', 'www.lenovo.com'),
            (29, 'Logitech', '23456789020', 'Proveedor de periféricos y accesorios para computadoras', '2727 Pine Avenue', '234-567-8902', 'www.logitech.com'),
            (30, 'NVIDIA', '34567890125', 'Proveedor de tarjetas gráficas y soluciones de gráficos', '2828 Cedar Avenue', '345-678-9012', 'www.nvidia.com'),
            (31, 'Sony', '45678901237', 'Proveedor de electrónicos y equipos de entretenimiento', '2929 Walnut Drive', '456-789-0123', 'www.sony.com'),
            (32, 'Amazon', '98765432101', 'Proveedor de productos y servicios en línea', '3030 Maple Drive', '987-654-3210', 'www.amazon.com'),
            (33, 'HP', '12345678901', 'Proveedor de impresoras y equipos de cómputo', '3131 Oak Drive', '123-456-7890', 'www.hp.com'),
            (34, 'Apple Inc.', '56789012348', 'Proveedor de dispositivos móviles y computadoras', '3232 Elm Drive', '567-890-1234', 'www.apple.com'),
            (35, 'JBL', '23456789024', 'Proveedor de equipos de audio y altavoces', '3333 Pine Drive', '234-567-8902', 'www.jbl.com'),
            (36, 'Samsung Electronics', '78901234565', 'Proveedor de electrónicos y dispositivos móviles', '3434 Cedar Drive', '789-012-3456', 'www.samsung.com'),
            (37, 'DJI', '34567890126', 'Proveedor de drones y equipos de fotografía aérea', '3535 Walnut Avenue', '345-678-9012', 'www.dji.com'),
            (38, 'Sony', '12345678907', 'Proveedor de electrónicos y equipos de entretenimiento', '3636 Maple Avenue', '123-456-7890', 'www.sony.com'),
            (39, 'HP', '56789012349', 'Proveedor de impresoras y equipos de cómputo', '3737 Oak Avenue', '567-890-1234', 'www.hp.com'),
            (40, 'Logitech', '23456789025', 'Proveedor de periféricos y accesorios para computadoras', '3838 Elm Avenue', '234-567-8902', 'www.logitech.com')
        ]

        for supplier in supplier_data:
            self.cursor.execute("""
                INSERT INTO Proveedores (code, nombre, ruc, descripcion, direccion, numero_telefono, pagina_web)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                                """, supplier)

    # Inserta datos en la tabla Contactos
    def insertContactData(self):
        contact_data = [
            (1, 1, 'Juan', 'Pérez', '1234567890', 'juan.perez@example.com'),
            (2, 2, 'María', 'González', '2345678901', 'maria.gonzalez@example.com'),
            (3, 3, 'Carlos', 'López', '3456789012', 'carlos.lopez@example.com'),
            (4, 4, 'Ana', 'Martínez', '4567890123', 'ana.martinez@example.com'),
            (5, 5, 'Luis', 'Rodríguez', '5678901234', 'luis.rodriguez@example.com'),
            (6, 6, 'Laura', 'Fernández', '6789012345', 'laura.fernandez@example.com'),
            (7, 7, 'Pedro', 'Sánchez', '7890123456', 'pedro.sanchez@example.com'),
            (8, 8, 'Sofía', 'Díaz', '8901234567', 'sofia.diaz@example.com'),
            (9, 9, 'Javier', 'Torres', '9012345678', 'javier.torres@example.com'),
            (10, 10, 'Lucía', 'Ramírez', '0123456789', 'lucia.ramirez@example.com'),
        ]

        for contact in contact_data:
            self.cursor.execute("""
                INSERT INTO Contactos (code, cliente_code, nombre, apellido, telefono, correo)
                VALUES (?, ?, ?, ?, ?, ?)
                                """, contact)


    # Insertamos los datos de los producto en la tabla
    def insertProductData(self):

        # from faker import Faker

        # fake = Faker()

        # for i in range(1, 51):
        #     code = f"000{i}"
        #     nombre = str(fake.name())
        #     descripcion = str(fake.text())
        #     precio_Actual = gen_decimal()
        #     stock = fake.random_int()
        #     proveedor_code = fake.random_int()

        #     print(nombre)

        #     self.cursor.execute("""
        #         INSERT INTO Productos (
        #             code,
        #             nombre,
        #             descripcion,
        #             precio_Actual,
        #             stock,
        #             proveedor_code
        #         ) VALUES (
        #             {}, {}, {}, {}, {}, {}
        #         )
        #     """.format(code, nombre, descripcion, precio_Actual, stock, proveedor_code))

        supplier_data = [
            (1, 'Laptop Dell XPS 13', 'Portátil ultradelgado con procesador i7 y pantalla 4K', 1399.99, 25, 1),
            (2, 'iPhone 13 Pro', 'Teléfono inteligente de Apple con pantalla OLED', 999.99, 30, 2),
            (3, 'Computadora de escritorio HP Pavilion', 'Computadora de escritorio de gama media con procesador i5 y tarjeta gráfica dedicada', 799.99, 50, 3),
            (4, 'Tablet Samsung Galaxy Tab S8', 'Tablet de 11 pulgadas con pantalla AMOLED y S Pen', 699.99, 150, 4),
            (5, 'Monitor LG UltraWide', 'Monitor ultrapanorámico de 34 pulgadas con resolución QHD', 499.99, 10, 5),
            (6, 'Auriculares Sony WH-1000XM4', 'Auriculares inalámbricos con cancelación de ruido', 299.99, 40, 6),
            (7, 'NVIDIA GeForce RTX 3080', 'Tarjeta gráfica para juegos de alta gama', 799.99, 20, 7),
            (8, 'Smart TV Sony BRAVIA X90J', 'Televisor 4K con procesador XR y Android TV', 1199.99, 15, 8),
            (9, 'Portátil ASUS ROG Strix', 'Laptop para juegos con GPU RTX 3060 y pantalla de 144Hz', 1099.99, 35, 9),
            (10, 'Smartphone Google Pixel 6', 'Teléfono Android con cámara avanzada', 799.99, 28, 10),
            (11, 'Teclado Logitech G Pro X', 'Teclado mecánico para juegos con interruptores intercambiables', 129.99, 50, 11),
            (12, 'Impresora HP LaserJet Pro', 'Impresora láser monocromática para oficina', 199.99, 12, 12),
            (13, 'Tableta Wacom Intuos Pro', 'Tableta gráfica con lápiz digital para diseñadores', 299.99, 7, 13),
            (14, 'Silla ergonómica Herman Miller', 'Silla de oficina ergonómica de alta gama', 649.99, 10, 14),
            (15, 'Monitor Dell Ultrasharp', 'Monitor 4K de 27 pulgadas con precisión de color', 549.99, 18, 15),
            (16, 'Cámara Canon EOS R5', 'Cámara sin espejo de alta resolución para fotógrafos profesionales', 3499.99, 5, 16),
            (17, 'Impresora Epson EcoTank', 'Impresora de tanque de tinta con capacidad de alto rendimiento', 299.99, 8, 17),
            (18, 'Laptop Microsoft Surface Laptop 4', 'Laptop ultradelgada con Windows 10', 1099.99, 22, 18),
            (19, 'Altavoces Bose SoundLink Revolve', 'Altavoces Bluetooth portátiles de 360 grados', 199.99, 25, 19),
            (20, 'MacBook Air M2', 'Laptop ultradelgada con el chip M2 de Apple', 999.99, 14, 2),
            (21, 'Cámara Nikon Z6', 'Cámara sin espejo de fotograma completo para entusiastas de la fotografía', 1999.99, 7, 20),
            (22, 'Portátil Acer Aspire 5', 'Laptop con procesador Ryzen 5 y pantalla Full HD', 549.99, 10, 1),
            (23, 'Tarjeta gráfica AMD Radeon RX 6900 XT', 'Tarjeta gráfica de alto rendimiento para juegos', 1499.99, 6, 21),
            (24, 'Smartphone Samsung Galaxy S22', 'Teléfono Android con cámara de 108MP', 1199.99, 30, 4),
            (25, 'Impresora Canon PIXMA', 'Impresora de inyección de tinta para fotografías', 149.99, 12, 22),
            (26, 'Auriculares JBL Quantum', 'Auriculares gaming con sonido envolvente', 89.99, 40, 23),
            (27, 'Router ASUS ROG Rapture', 'Router gaming de alta velocidad con iluminación RGB', 299.99, 10, 9),
            (28, 'Smart TV LG OLED 4K', 'Televisor OLED con resolución 4K y HDR', 1499.99, 22, 24),
            (29, 'Proyector Epson Home Cinema', 'Proyector 4K para cine en casa', 899.99, 7, 17),
            (30, 'Reloj inteligente Apple Watch Series 7', 'Reloj con seguimiento de la salud y pantalla siempre encendida', 399.99, 15, 2),
            (31, 'Monitor Dell UltraSharp', 'Monitor 4K de 32 pulgadas con conectividad USB-C', 699.99, 8, 15),
            (32, 'Impresora HP OfficeJet Pro', 'Impresora de inyección de tinta todo en uno', 249.99, 12, 3),
            (33, 'Cámara Sony Alpha 7 IV', 'Cámara sin espejo de fotograma completo de alta resolución', 2499.99, 5, 6),
            (34, 'Teclado mecánico Corsair K95', 'Teclado para juegos con retroiluminación RGB', 169.99, 14, 25),
            (35, 'Monitor Acer Predator X35', 'Monitor gaming curvo de 35 pulgadas con resolución 4K', 1699.99, 6, 26),
            (36, 'Impresora Brother LaserJet', 'Impresora láser multifunción para pequeñas empresas', 299.99, 9, 27),
            (37, 'Portátil Lenovo ThinkPad X1 Carbon', 'Laptop empresarial ultraligera con pantalla 4K', 1299.99, 11, 28),
            (38, 'Smartphone Google Pixel 5a', 'Teléfono Android asequible con cámara de alta calidad', 399.99, 20, 10),
            (39, 'Silla de oficina Steelcase Leap', 'Silla ergonómica con soporte lumbar ajustable', 499.99, 15, 29),
            (40, 'Monitor Dell S2719DGF', 'Monitor gaming de 27 pulgadas con tasa de actualización de 144Hz', 399.99, 12, 15),
            (41, 'Smart TV Samsung QLED Q70T', 'Televisor QLED 4K con asistentes de voz integrados', 1099.99, 9, 4),
            (42, 'Router TP-Link Archer C4000', 'Router WiFi de alto rendimiento con MU-MIMO', 199.99, 10, 30),
            (43, 'Impresora Epson WorkForce Pro', 'Impresora láser para oficinas con alimentador automático de documentos', 299.99, 8, 17),
            (44, 'Auriculares Skullcandy Crusher Evo', 'Auriculares con bajos ajustables y cancelación de ruido', 149.99, 16, 31),
            (45, 'Monitor BenQ PD2700U', 'Monitor 4K de 27 pulgadas para diseñadores y creativos', 499.99, 14, 32),
            (46, 'Cámara Nikon D780', 'Cámara DSLR de fotograma completo con grabación 4K', 1799.99, 5, 20),
            (47, 'Portátil MSI GS66 Stealth', 'Laptop gaming delgada y potente con pantalla de 300Hz', 1699.99, 7, 33),
            (48, 'Altavoz Sonos Roam', 'Altavoz Bluetooth portátil resistente al agua', 179.99, 18, 34),
            (49, 'Monitor Alienware AW3420DW', 'Monitor gaming curvo de 34 pulgadas con resolución WQHD', 999.99, 8, 36),
            (50, 'Smart TV TCL 4K', 'Televisor 4K con Roku integrado y soporte para HDR', 499.99, 22, 35)
        ]
        for supplier in supplier_data:
            self.cursor.execute("""
                INSERT INTO Productos (code, nombre, descripcion, precio_Actual, stock, proveedor_code)
                VALUES (?, ?, ?, ?, ?, ?)
            """, supplier)

    def schemaMigrateDataTables(self):
        self.insertCustomerData()
        # Insertar datos de los Productos
        self.insertProductData()
        # Insertar datos del proveedor
        self.insertSupplierData()
        # Inserta datos de las categorias
        self.insertCategoryData()
        # Inserta datos de los contactos
        self.insertContactData()
    
        self.insertDetalleCompraData()
        self.insertCategoriasProductosData()
        self.insertProductosProveedoresData()

    # creacion del schema 
    def schemaCreation(self):
        self.clientCreation()
        self.contactCreation()
        self.productCreation()
        self.creationOfPurchasingDetails()
        self.categoryCreation()
        self.supplierCreation()
        self.creationOfTheProductSupplierRelationshipEntity()
        self.creationOfTheProductCategoryRelationshipEntity()

if __name__ == "__main__":
    # Instanciamos y creamaos un nuevo objecto o clase con el argumento name=""
    cool = CoolBox(name="myDatabase")
    # Llamamos a uno de sus metodos
    cool.databaseCreationOrConnection()
    # Crear las entidades y tablas en la db
    cool.schemaCreation()
    # Inserta datos de clientes
    cool.schemaMigrateDataTables()

    # Guardar los cambios en la base de datos
    cool.conn.commit()
    
    # Cerrar la conexión a la base de datos
    cool.conn.close()
