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
cuenta2 = CuentasAhorro(numero_cuenta="CA56789", nombre_titular="María Gómez", saldo_actual=500, fecha_apertura=datetime.date(year=2023, month=12, day=2))
cuenta3 = CuentasAhorro(numero_cuenta="CA01257", nombre_titular="Genny Alcivar", saldo_actual=1000, fecha_apertura=datetime.date(year=2022, month=5, day=7))
cuenta4 = CuentasAhorro(numero_cuenta="CA06036", nombre_titular="Aníbal Sánchez", saldo_actual=500, fecha_apertura=datetime.date(year=2021, month=11, day=12))
cuenta5 = CuentasAhorro(numero_cuenta="CA54377", nombre_titular="Rosa Guzmán", saldo_actual=1000, fecha_apertura=datetime.date(year=2000, month=8, day=7))
cuenta6 = CuentasAhorro(numero_cuenta="CA17125", nombre_titular="María Vera", saldo_actual=500, fecha_apertura=datetime.date(year=1999, month=10, day=28))

# Add cities and stadiums to the session

session.add_all([cuenta1, cuenta2, cuenta3, cuenta4, cuenta5, cuenta6])


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