from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
Create table colegios(
	id_colegio int NOT NULL,
	nombre varchar(50),
	telefono int,
	categoria int,
	director varchar(100),
	PRIMARY KEY (id_colegio)
);
"""

cur.execute(sql)


sql ="""
Create table docentes(
	rut int NOT NULL,
	id_colegio int,
	nombre varchar(50),
	telefono int,
	email varchar(50),
	calificacion float4,
	direccion varchar(100),
	formacion varchar(100),
	asignatura varchar(100),
	PRIMARY KEY (rut),
	FOREIGN KEY (id_colegio) REFERENCES colegios(id_colegio)
);
"""

cur.execute(sql)

sql ="""
Create table niveles(
	id_nivel int NOT NULL,
	nivel varchar(50),
	PRIMARY KEY (id_nivel)
);
"""

cur.execute(sql)

sql ="""
Create table cursos(
	id_curso int NOT NULL,
	promedio float4,
	cantidadEstudiantes int,
	id_colegio int,
	id_nivel int,
	PRIMARY KEY (id_curso),
	FOREIGN KEY (id_colegio) REFERENCES colegios(id_colegio),
	FOREIGN KEY (id_nivel) REFERENCES niveles(id_nivel)
);
"""

cur.execute(sql)

sql ="""
Create table imparte(
	rut int,
	id_curso int,
	FOREIGN KEY (rut) REFERENCES docentes(rut),
	FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);
"""

cur.execute(sql)

conn.commit()
cur.close()
conn.close()