from sqlalchemy.orm import sessionmaker  # Import sessionmaker
from base_datos import engine  # Import engine
from sqlalchemy import create_engine
from crear_entidades import CuentasAhorro


# Create a session maker
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

# Create a session
session = Session()

# Example local de comida data

cuenta1 = CuentasAhorro(numero_cuenta="CA12345", nombre_titular="Juan Pérez", saldo_actual=1000.00, fecha_apertura=datetime.date(year=2024, month=6, day=4))
cuenta2 = CuentasAhorro(numero_cuenta="CA56789", nombre_titular="María Gómez", saldo_actual=500.00, fecha_apertura=datetime.date(year=2023, month=12, day=21))




# Add cities and stadiums to the session

session.add_all([cuenta1, cuenta2])


try:
    session.commit()
    print("Cuentas de ahorro almacenadas correctamente en la base de datos.")
except Exception as e:
    print(f"Error al almacenar datos: {e}")
    session.rollback()


# Close the session
session.close()