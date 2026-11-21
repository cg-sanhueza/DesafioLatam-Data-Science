# Manipulación de datos con pandas

| Notebook | Datos | Qué se hace |
|---|---|---|
| desafio_analisis_ventas_regionales | Ventas regionales de EE. UU. (Excel) | Unión de 5 hojas con merge validado, tiempos de entrega, margen bruto, comisiones por tramos y margen neto por equipo de ventas |
| prueba_manipulacion_de_datos | Base de datos classicmodels en PostgreSQL | Lectura de tablas con SQLAlchemy, unión de pedidos, clientes y productos, ventas y ganancias, top 10 de clientes y productos de 2005 y escritura de resultados en la base |

`funciones_p2.py` contiene las funciones auxiliares que usa el segundo notebook: filtrar por fecha, generar reportes y guardar resultados en PostgreSQL.

## Herramientas

Python, pandas, SQLAlchemy y PostgreSQL.

## Datos

Los archivos de datos fueron provistos en el bootcamp de ciencia de datos de Desafío Latam y se incluyen solo para poder ejecutar los notebooks.

Para ejecutar el segundo notebook se necesita PostgreSQL con la base `classicmodels` instalada, y reemplazar `TU_CONTRASEÑA` en la conexión por la clave propia. La base de datos no se incluye en el repositorio.
