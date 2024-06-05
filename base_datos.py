import os
from sqlalchemy import create_engine

# Check database file existence
if not os.path.exists('cuenta_ahorros.db'):
  print("Error: El archivo de base de datos 'cuenta_ahorros.db' no existe.")
  exit(1)

# Create engine with connection options
engine = create_engine(
    'sqlite:///cuenta_ahorros.db',
    pool_size=5,
    connect_args={'check_same_thread': False}
)

try:
    with engine.connect() as connection:
        print("Conexión a la base de datos establecida correctamente.")
except FileNotFoundError as e:
    print(f"Error: El archivo de base de datos no se encontró: {e}")
except OperationalError as e:
    print(f"Error de base de datos: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")