from .engine import Base, engine
from . import models
from .seeds.role_seed import seed_roles
from .seeds.business_type_seed import seed_business_types

#bind es el motor o conexion que usara
def init_db() -> None:
    Base.metadata.create_all(bind=engine) #iniciar la  base de datos
    seed_roles() #crear tablas faltantes
    seed_business_types()

if __name__ == "__main__":
    init_db()