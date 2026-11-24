# tiendita_app

Aplicacion para administrar una tiendita.

## Configuracion

1. Crea un entorno virtual de Python.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Copia `.env.example` como `.env` y completa la configuracion local de SQL Server.
4. Ejecuta la aplicacion con `python -m app.main`.

## Estructura

- `app/core/`: configuracion de la aplicacion.
- `app/database/`: conexion y modelos de datos.
- `app/repositories/`: acceso a datos.
- `app/services/`: logica de negocio.
- `app/ui/`: interfaz grafica.
- `app/api/`: integraciones futuras.
- `tests/`: pruebas.
- `docs/`: documentacion.