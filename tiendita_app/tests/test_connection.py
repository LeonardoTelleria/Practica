from sqlalchemy import text
from app.database.engine import get_session

with get_session() as session:
    resultado = session.execute(text('SELECT 1'))
    print(resultado.scalar_one())