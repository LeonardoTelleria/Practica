import os
from contextlib import contextmanager
from urllib.parse import quote_plus #quoteplus codifica caracteres especiales para que sqlalchemis las lea bien

from dotenv import load_dotenv
from sqlalchemy import create_engine #create engine crea el motor de conexon a sql
from sqlalchemy.orm import declarative_base, sessionmaker #session fabrica sesiones de trabajo en la db

load_dotenv()#lee desde un venv

Base = declarative_base() #crea la base de la que heredaran todos los models

def url_database() -> str:
    driver = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")#(
    server = os.getenv("DB_SERVER", "localhost")
    database = os.getenv("DB_NAME", "pulperiasDB") #lee los parametros de entorno
    user = os.getenv("DB_USER", "")
    password = os.getenv("DB_PASSWORD", "")
    trust_cert = os.getenv("DB_TRUST_CERT", "yes") #)

    if user and password:
        odbc_str = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};" #si hay user y contra entonces arma la cadena UID Y PWD
            f"UID={user};"
            f"PWD={password};"
            f"TrustServerCertificate={trust_cert};"
        )
    else:
        odbc_str = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};" #si no hay entonces usa la autenticacion de windows
            f"DATABASE={database};"
            f"Trusted_Connection=yes;"
            f"TrustServerCertificate={trust_cert};"
        )
    return f"mssql+pyodbc:///?odbc_connect={quote_plus(odbc_str)}" #indica a a sqlalchemist que use dialecto de sqlserver con pyodbc


DATABASE_URL = url_database() #guardar conexion

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True, #antes de entregar una conexion de pool, verifica que siga viva. para que al reiniciar ocerrar sqls server se renueve
    pool_size=5, #mantienen hasta 5 conexiones abiertas
    max_overflow=10, #permite 10 extra en picos de demanda
)

SessionLocal = sessionmaker(
    bind=engine, #une la fabricaal sqlserver
    autoflush=False, #evita que alchemi envie cambios a sqlserver antes de tiempo de forma auto
    autocommit=False, #exige confirmar los cambios
    expire_on_commit=False, #evita que los objetos se vacien tras hacer commit
)

@contextmanager #convierte la funcion simple en bloque with getsession as session, para no escribir try/except/commit/rollback/close cada vez que se consulte en sqlserver
def get_session():
    session = SessionLocal()
    try:
        yield session #entrega la sesion abierta al codigo que la usa y cuando termina el bloque with ejecuta el commit o el rollback
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close() #la sesion vuelve al pool y se cierra
