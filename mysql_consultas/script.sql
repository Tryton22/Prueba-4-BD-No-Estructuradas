-- Script SQL para crear la base de datos y tablas para el sistema de reclamos

-- 1. Eliminar la base de datos si ya existe para asegurar una creación limpia
DROP DATABASE IF EXISTS actividad2;

-- 2. Crear la base de datos
CREATE DATABASE actividad2;

-- 3. Usar la base de datos recién creada
USE actividad2;

-- 4. Crear la tabla 'clientes'
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY, -- Clave primaria autoincremental
    nombre VARCHAR(100) NOT NULL,
    rut VARCHAR(12) UNIQUE NOT NULL, -- Asumiendo RUT es único
    direccion VARCHAR(255),
    correo VARCHAR(100) UNIQUE,
    telefono VARCHAR(15)
);

-- 5. Crear la tabla 'reclamo'
CREATE TABLE reclamo (
    id_reclamo INT AUTO_INCREMENT PRIMARY KEY, -- Clave primaria autoincremental
    id_cliente INT NOT NULL, -- Clave foránea que referencia a 'clientes'
    fecha_reclamo DATE NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(50) NOT NULL, -- Ej: 'Pendiente', 'En Proceso', 'Resuelto', 'Cerrado'
    -- Definir la clave foránea
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
        ON DELETE CASCADE -- Si se elimina un cliente, sus reclamos también
        ON UPDATE CASCADE -- Si cambia el id_cliente, se actualiza en reclamo
);

-- 6. Crear la tabla 'respuesta'
CREATE TABLE respuesta (
    id_respuesta INT AUTO_INCREMENT PRIMARY KEY, -- Clave primaria autoincremental
    id_reclamo INT NOT NULL, -- Clave foránea que referencia a 'reclamo'
    fecha_respuesta DATE NOT NULL,
    detalle_respuesta TEXT NOT NULL,
    responsable VARCHAR(100), -- Quién dio la respuesta
    -- Definir la clave foránea
    FOREIGN KEY (id_reclamo) REFERENCES reclamo(id_reclamo)
        ON DELETE CASCADE -- Si se elimina un reclamo, sus respuestas también
        ON UPDATE CASCADE -- Si cambia el id_reclamo, se actualiza en respuesta
);