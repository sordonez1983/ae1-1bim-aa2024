import datetime  # Import datetime module
from sqlalchemy.orm import sessionmaker  # Import sessionmaker
from base_datos import engine  # Import engine
from crear_entidades import CuentasAhorro


# Create a session maker
Session = sessionmaker(bind=engine)


# Create a session
session = Session()

# Example local de comida data

cuenta1 = CuentasAhorro(numero_cuenta="CA12345", nombre_titular="Juan Pérez", saldo_actual=1000, fecha_apertura=datetime.date(year=2024, month=6, day=4))
cuenta2 = CuentasAhorro(numero_cuenta="CA56789", nombre_titular="María Gómez", saldo_actual=500, fecha_apertura=datetime.date(year=2023, month=12, day=21))



# Add cities and stadiums to the session

session.add_all([cuenta1, cuenta2])


try:
    session.commit()
    print("Cuentas de ahorro almacenadas correctamente en la base de datos.")
except SQLAlchemyError as e:
    print(f"Error de SQLAlchemy: {e}")
    session.rollback()
except DatabaseError as e:
    print(f"Error de base de datos: {e}")
    session.rollback()
except Exception as e:
    print(f"Error inesperado: {e}")
    session.rollback()


# Close the session
session.close()