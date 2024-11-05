DROP DATABASE gimnasio_db;
-- Crear la base de datos
CREATE DATABASE gimnasio_db;

-- Usar la base de datos
USE gimnasio_db;

-- Crear la tabla Aparatos
CREATE TABLE Aparatos (
    id_aparato INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Crear la tabla Clientes
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    pago_realizado VARCHAR(255)
);

-- Crear la tabla Recibos
CREATE TABLE Recibos (
    id_recibo INT PRIMARY KEY,
    cliente_id INT,
    mes VARCHAR(20) NOT NULL,
    mensualidad DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id_cliente)
);

-- Crear la tabla Sesiones
CREATE TABLE Sesiones (
    id_sesion INT PRIMARY KEY,
    dia VARCHAR(20) NOT NULL,
    hora TIME NOT NULL,
    cliente_id INT,
    aparato_id INT,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (aparato_id) REFERENCES Aparatos(id_aparato)
);

