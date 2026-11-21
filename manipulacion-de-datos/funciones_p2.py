
import pandas as pd
# 1. funcion filtrar por fechas
def filtrar_por_fecha(df, columna_fecha, fecha_inicio, fecha_fin):
    """
    Filtra un DataFrame por un rango de fechas.
    """
    # Convertir la columna a datetime
    df[columna_fecha] = pd.to_datetime(df[columna_fecha])

    # Aplicar filtro de rango
    df_filtrado = df[
        (df[columna_fecha] >= fecha_inicio) &
        (df[columna_fecha] <= fecha_fin)
    ]
    return df_filtrado


# 2. funcion para generar reportes
def generar_reporte(df, filas, columnas, valores, medida):
    """
    Genera un reporte tipo tabla dinámica.
    """
    # Creamos una tabla dinámica con los parámetros entregados
    reporte = df.pivot_table(
        index=filas,
        columns=columnas,
        values=valores,
        aggfunc=medida,
        fill_value=0
    )
    
    # Devolvemos el reporte
    return reporte

# 3. funcion para guardar df´s
def escribir_en_db(df, tabla, engine, if_exists="replace"):
    """
    Guarda un DataFrame en PostgreSQL.
    """
    # Guardamos el DataFrame como tabla en PostgreSQL
    df.to_sql(
        tabla,
        con=engine,
        if_exists=if_exists,
        index=False
    )
    # Mensaje de confirmación
    print(f"Tabla '{tabla}' guardada con éxito.")