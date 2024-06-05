

from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del archivo crear_entidades
from crear_entidades import CuentasAhorro

# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,desde el generador de clases de SQLAlchemy sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session de tipo Session, que permite: permitir guardar, eliminar, actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Autor. Se hace uso del método query. all, significa que se obtiene todos los registros
LocalesComida = session.query(CuentasAhorro).all()

# se realiza un proceso iterativo para presentar la información
# de cada objeto.
for cuenta_ahorro in LocalesComida:
    # Acceso a todos los atributos de cuenta_ahorro aqui
    print(f"Número de cuenta: {cuenta_ahorro.numero_cuenta}")
    print(f"Titular: {cuenta_ahorro.nombre_titular}")
    print(f"Saldo: ${cuenta_ahorro.saldo_actual:.2f}")
    print(f"Fecha de apertura: {cuenta_ahorro.fecha_apertura}")
    print("----------------------------")  # Separador entre cuentas  