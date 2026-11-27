from sqlalchemy import select
from ..engine import get_session
from ..models.business_type import BusinessType

DEFAULT_BUSINESS_TYPES = [
    {"code": "GROCERY","name": "Pulpería","description": "Venta de productos de consumo diario"},
    {"code": "MINIMARKET","name": "Minimarket","description": "Comercio minorista de productos variados"},
    {"code": "HARDWARE","name": "Ferretería","description": "Venta de herramientas y materiales"},
    {"code": "CLOTHING","name": "Tienda de ropa","description": "Venta de prendas de vestir"},
    {"code": "BOOKSTORE","name": "Librería","description": "Venta de libros y útiles escolares"},
    {"code": "BARBERSHOP","name": "Barbería","description": "Servicios de cuidado personal"},
    {"code": "ENTREPRENEURSHIP","name": "Emprendimiento","description": "Pequeño negocio de actividad diversa"},
    {"code": "OTHER","name": "Otro","description": "Tipo de negocio personalizado"}
]

def seed_business_types() -> None:
    with get_session() as session:
        for type_data in DEFAULT_BUSINESS_TYPES:
            statement = select(BusinessType).where(BusinessType.code == type_data["code"])
            resultado = session.execute(statement)
            existing_type = resultado.scalar_one_or_none()

            if existing_type is None:
                new_type = BusinessType(**type_data)
                session.add(new_type)