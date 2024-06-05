from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date




from base_datos import engine

Base = declarative_base()


class CuentasAhorro(Base):
    __tablename__ = "Cuentas_Ahorro"  # Table name for your savings accounts

    id_cuenta = Column(Integer, primary_key=True)  # Unique identifier
    numero_cuenta = Column(String(20), unique=True, nullable=False)  # Account number (unique)
    nombre_titular = Column(String(50), nullable=False)  # Account holder name
    saldo_actual = Column(  Integer, nullable=False)  # Current balance with decimals
    fecha_apertura = Column(Date, nullable=False)  # Date account was opened

    def __str__(self):
        return f"Cuenta Ahorro No.: {self.numero_cuenta} - Titular: {self.nombre_titular} - Saldo: ${self.saldo_actual:.2f}"
    

  


  
