# ae1-1bim-aa2024
Trabajo de recuperación de nota

Base de datos SQLite


CREATE TABLE "Cuentas_Ahorro" (
	"id_cuenta"	INTEGER,
	"numero_cuenta"	VARCHAR(20) NOT NULL UNIQUE,
	"nombre_titular"	VARCHAR(50) NOT NULL,
	"saldo_actual"	NUMERIC NOT NULL,
	"fecha_apertura"	DATE NOT NULL,
  PRIMARY KEY("id_cuenta" AUTOINCREMENT)
	);