from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into colegios (id_colegio,nombre,telefono,categoria,director) values 
(1,'COLEGIO ECOLÓGICO Y MEDIOAMBIENTAL ANTÚ',225586635,1,'Roxana Díaz Armijo'),
(2,'LICEO POLITÉCNICO CIENCIA Y TECNOLOGÍA',225584253,2,'Alicia Santibáñez Arcos'),
(3,'COLEGIO DE ROBÓTICA Y TECNOLOGÍA ESPERANZA JÓVEN',225210937,0,'Irene Montaño Espinoza'),
(4,'ESCUELA DEPORTIVA NACIONES UNIDAS',225586869,2,'Karina Labbe Bustos'),
(5,'COLEGIO ECOLÓGICO Y MEDIOAMBIENTAL OLOF PALME',225583521,1,'Jaime Olate Ruz'),
(6,'ESCUELA DE ARTES Y CULTURA BOMBERO OSCAR ENCALADA',225583187,1,'Mireya Cordero Venegas'),
(7,'COLEGIO CÍVICO PRE-MILITAR PALESTINO',944059860,0,'Claudia Moragrega'),
(8,'LICEO PORTAL DE LA CISTERNA',225252715,2,'Juan Claudio González Poblete');
"""
cur.execute(sql)

sql ="""
insert into docentes (rut,id_colegio,nombre,telefono,email,direccion,formacion,asignatura) values 
(1111,1,'CRISTIAN FERNANDES GUARDIOLA',999999,'cfg@ed.cl','Calle 1, La Cisterna','Pedagogía Historia','Historia'),
(2222,2,'ROSA ATIENZA GRACIA',999999,'rag@ed.cl','Calle 2, La Cisterna','Pedagogía Matematicas','Matematicas'),
(3333,3,'AGUSTIN MEDINA QUIROGA',999999,'amq@ed.cl','Calle 3, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(4444,4,'MARIA ROSARIO BORJA PIÑERO',999999,'mrb@ed.cl','Calle 4, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(5555,5,'RAUL VALCARCEL PELAEZ',999999,'rvp@ed.cl','Calle 5, La Cisterna','Pedagogía Historia','Historia'),
(6666,6,'CARLA MASIP MIRO',999999,'cmm@ed.cl','Calle 6, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(7777,7,'ROBERTO GAMBOA MEDIAVILLA',999999,'rgm@ed.cl','Calle 7, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(8888,8,'ANA BELEN RUBIA CASTILLO',999999,'arc@ed.cl','Calle 8, La Cisterna','Pedagogía Matematicas','Matematicas'),
(9999,1,'MIGUEL SEMPERE HOLGADO',999999,'msh@ed.cl','Calle 9, La Cisterna','Pedagogía Matematicas','Matematicas'),
(1211,2,'GLORIA MACHIN PRATS',999999,'gmp@ed.cl','Calle 10, La Cisterna','Pedagogía Historia','Historia'),
(1311,3,'JUAN LUIS CANTARERO FONT',999999,'jcf@ed.cl','Calle 11, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(1411,4,'YOLANDA QUIROGA PINA',999999,'yqp@ed.cl','Calle 12, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(1511,5,'FRANCISCO GONZALO DE LAS HERAS',999999,'fdh@ed.cl','Calle 13, La Cisterna','Pedagogía Historia','Historia'),
(1611,6,'PATRICIA NAVARRETE TORNERO',999999,'pnt@ed.cl','Calle 14, La Cisterna','Pedagogía Matematicas','Matematicas');
"""
cur.execute(sql)

conn.commit()
cur.close()