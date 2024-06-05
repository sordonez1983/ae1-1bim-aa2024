from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import CuentasAhorro

# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# Obtener todos los registros de la entidad Autor.
# Se hace uso del método query.
# order_by, permite ordenar la búsqueda, con base
# a las propiedades de la entidad
lista_cuentas_ahorro = session.query(CuentasAhorro).order_by(CuentasAhorro.saldo_actual.desc()).all()

# La variable lista_autores, tendrá un listado de objetos de tipo Autor
# ordenados por la propiedad edad de la entidad

# se realiza un proceso iterativo para presentar la información
# de cada objeto.

print("\nCuentas de ahorro por saldo (mayor a menor):")
for cuenta_ahorro in lista_cuentas_ahorro:
    print(f"Nombre: {cuenta_ahorro.nombre_titular}")
    print(f"Saldo: ${cuenta_ahorro.saldo_actual:.2f}")
    print("----------------------------")