# Análisis estadístico con Python

Desafíos de estadística resueltos con Python y un proyecto final de riesgo cardiovascular.

## Contenido

| Notebook | Datos | Qué se hace |
|---|---|---|
| desafio_preparacion_datos_graficos | Indicadores de países 2023 (`world-data-2023.csv`) | Limpieza de texto a números, tratamiento de nulos y atípicos (IQR), correlaciones y transformación logarítmica |
| desafio_distribuciones_tlc | Peso de recién nacidos (`baby.csv`) | Ajuste de la distribución normal con histograma y QQ-plot, comparación entre madres fumadoras y no fumadoras, modelo binomial y teorema del límite central con 1.000 muestras simuladas |
| desafio_inferencia_hipotesis | Ingresos de personas (`earnings.csv`) | 12 pruebas t con muestras de 25 datos, intervalos de confianza para una proporción (95 % y 99 %) y comparación de ingresos por género con y sin atípicos |
| desafio_regresion | Medidas de peces (`Fish.csv`) | Creación del volumen, regresión simple y múltiple, modelo por especie y métricas (R², RMSE, MAE) |
| **prueba_estadísticas_probabilidades** (proyecto final) | Datos clínicos de pacientes (`cardio.csv`) | Limpieza e imputación de nulos, atípicos con IQR, pruebas de hipótesis, regresión lineal con entrenamiento y prueba, y regresión logística con SMOTE (accuracy, recall y AUC-ROC) |

## Herramientas

Python, pandas, numpy, matplotlib, seaborn, scipy, statsmodels, scikit-learn e imbalanced-learn.

## Datos

Los archivos de datos fueron provistos en el bootcamp de ciencia de datos de Desafío Latam y se incluyen solo para poder ejecutar los notebooks.
