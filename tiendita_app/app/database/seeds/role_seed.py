from sqlalchemy import select
from ..engine import get_session
from ..models import Role

DEFAULT_ROLES = [
    {"name": "ADMIN", "description": "Administrador", "scope": "PLATFORM"},
    {"name": "OWNER", "description": "Propietario del negocio", "scope": "BUSINESS"},
    {"name": "EMPLOYEE", "description": "Trabajadores del negocio", "scope": "BUSINESS"}
]

def seed_roles() -> None: #none dice que esta funcion no esta dise;ada para retornar algo util
    with get_session() as session: #agarrar sesion para consultar
        for role_data in DEFAULT_ROLES:
            statement = select(Role).where(Role.name == role_data["name"])
            resultado = session.execute(statement)
            existing_role = resultado.scalar_one_or_none() #escalar retorna el pimer elemento y scalaronefornone retorna un elemento o none o genera un except si hay mas de una fila
            #se puso scalar one or none porque se espera que name sea unico
            if existing_role is None:
                new_role = Role(**role_data) #si la variable es none entonces se crea un nuevo rol
                session.add(new_role) #los ** son una forma simplificada de hacer el diccionario otra vez para cambiar una var


