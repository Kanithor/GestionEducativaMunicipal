from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into colegios (nombre,telefono,categoria,director) values 
('COLEGIO ECOLÓGICO Y MEDIOAMBIENTAL ANTÚ',225586635,1,'Roxana Díaz Armijo'),
('LICEO POLITÉCNICO CIENCIA Y TECNOLOGÍA',225584253,2,'Alicia Santibáñez Arcos'),
('COLEGIO DE ROBÓTICA Y TECNOLOGÍA ESPERANZA JÓVEN',225210937,0,'Irene Montaño Espinoza'),
('ESCUELA DEPORTIVA NACIONES UNIDAS',225586869,2,'Karina Labbe Bustos'),
('COLEGIO ECOLÓGICO Y MEDIOAMBIENTAL OLOF PALME',225583521,1,'Jaime Olate Ruz'),
('ESCUELA DE ARTES Y CULTURA BOMBERO OSCAR ENCALADA',225583187,1,'Mireya Cordero Venegas'),
('COLEGIO CÍVICO PRE-MILITAR PALESTINO',944059860,0,'Claudia Moragrega'),
('LICEO PORTAL DE LA CISTERNA',225252715,2,'Juan Claudio González Poblete');
"""
cur.execute(sql)

sql ="""
insert into docentes (rut,id_colegio,nombre,telefono,email,direccion,formacion,calificacion) values 
(1111,1,'CRISTIAN FERNANDES GUARDIOLA',999999,'cfg@ed.cl','Calle 1, La Cisterna','Pedagogía en Historia',5.7),
(2222,1,'ROSA ATIENZA GRACIA',999999,'rag@ed.cl','Calle 2, La Cisterna','Pedagogía en Matematicas',5.8),
(3333,1,'AGUSTIN MEDINA QUIROGA',999999,'amq@ed.cl','Calle 3, La Cisterna','Pedagogía en Lenguaje',5.9),
(4444,2,'MARIA ROSARIO BORJA PIÑERO',999999,'mrb@ed.cl','Calle 4, La Cisterna','Pedagogía en Historia',6.2),
(5555,2,'RAUL VALCARCEL PELAEZ',999999,'rvp@ed.cl','Calle 5, La Cisterna','Pedagogía en Matematicas',6.4),
(6666,2,'CARLA MASIP MIRO',999999,'cmm@ed.cl','Calle 6, La Cisterna','Pedagogía en Lenguaje',6.2),
(7777,3,'ROBERTO GAMBOA MEDIAVILLA',999999,'rgm@ed.cl','Calle 7, La Cisterna','Pedagogía en Historia',6.1),
(8888,3,'ANA BELEN RUBIA CASTILLO',999999,'arc@ed.cl','Calle 8, La Cisterna','Pedagogía en Matematicas',6.7),
(9999,3,'MIGUEL SEMPERE HOLGADO',999999,'msh@ed.cl','Calle 9, La Cisterna','Pedagogía en Lenguajes',5.4),
(1211,4,'GLORIA MACHIN PRATS',999999,'gmp@ed.cl','Calle 10, La Cisterna','Pedagogía en Historia',5.5),
(1311,4,'JUAN LUIS CANTARERO FONT',999999,'jcf@ed.cl','Calle 11, La Cisterna','Pedagogía en Matematicas',5.9),
(1411,4,'YOLANDA QUIROGA PINA',999999,'yqp@ed.cl','Calle 12, La Cisterna','Pedagogía en Lenguaje',6.5),
(1511,5,'FRANCISCO GONZALO DE LAS HERAS',999999,'fdh@ed.cl','Calle 13, La Cisterna','Pedagogía en Historia',6.9),
(1611,5,'PATRICIA NAVARRETE TORNERO',999999,'pnt@ed.cl','Calle 14, La Cisterna','Pedagogía en Matematicas',7.0),
(1711,5,'CRISTOBAL BELTRAN MASCARO',999999,'cbm@ed.cl','Calle 15, La Cisterna','Pedagogía en Lenguaje',6.2),
(1811,6,'ELENA BRIZ YUSTE',999999,'eby@ed.cl','Calle 16, La Cisterna','Pedagogía en Historia',6.3),
(1911,6,'HUGO PALACIOS CORONEL',999999,'hpc@ed.cl','Calle 17, La Cisterna','Pedagogía en Matematicas',6.4),
(2111,6,'TERESA VILLAVERDE HUGUET',999999,'tvh@ed.cl','Calle 18, La Cisterna','Pedagogía en Lenguaje',6.1),
(2211,7,'JULIO RIVAS MALAGON',999999,'jrm@ed.cl','Calle 19, La Cisterna','Pedagogía en Historia',5.8),
(2311,7,'CONCEPCION PELAEZ PRIEGO',999999,'cpp@ed.cl','Calle 20, La Cisterna','Pedagogía en Matematicas',5.9),
(2411,7,'GABRIEL HEVIA RODAS',999999,'ghr@ed.cl','Calle 21, La Cisterna','Pedagogía en Lenguaje',6.1),
(2511,8,'NEREA COBO ALBERO',999999,'nca@ed.cl','Calle 22, La Cisterna','Pedagogía en Historia',6.2),
(2611,8,'PEDRO HOYOS GONZALES',999999,'phg@ed.cl','Calle 23, La Cisterna','Pedagogía en Matematicas',6.6),
(2711,8,'BEATRIZ GRAU SACRISTAN',999999,'bgs@ed.cl','Calle 24, La Cisterna','Pedagogía en Lenguaje',6.7);
"""
cur.execute(sql)

sql ="""
insert into niveles (nivel) values 
('NM1'),
('NM2'),
('NM3'),
('NM4');
"""
cur.execute(sql)

sql ="""
insert into cursos (promedio,cantidadEstudiantes,id_colegio,id_nivel) values
(5.7,40,1,1),
(6.1,43,2,1),
(5.4,44,3,1),
(5.9,36,4,1),
(6.8,34,5,1),
(5.3,47,6,1),
(5.2,48,7,1),
(5.8,38,8,1),
(5.6,40,1,2),
(5.5,43,2,2),
(6.8,42,3,2),
(5.8,43,4,2),
(5.1,38,5,2),
(5.2,39,6,2),
(5.9,41,7,2),
(6.1,40,8,2),
(4.8,42,1,3),
(5.6,43,2,3),
(5.7,36,3,3),
(5.8,33,4,3),
(5.5,32,5,3),
(5.6,45,6,3),
(5.7,40,7,3),
(5.8,41,8,3),
(4.8,42,1,4),
(5.6,35,2,4),
(5.7,32,3,4),
(5.8,33,4,4),
(5.5,36,5,4),
(5.6,37,6,4),
(5.7,38,7,4),
(5.8,39,8,4);
"""
cur.execute(sql)

sql ="""
insert into imparte (rut,id_curso,asignatura) values 
(1111,'1','Historia'),(2222,'1','Matemáticas'),(3333,'1','Lenguaje'),
(1111,'9','Historia'),(2222,'9','Matemáticas'),(3333,'9','Lenguaje'),
(1111,'17','Historia'),(2222,'17','Matemáticas'),(3333,'17','Lenguaje'),
(1111,'25','Historia'),(2222,'25','Matemáticas'),(3333,'25','Lenguaje'),

(4444,'2','Historia'),(5555,'2','Matemáticas'),(6666,'2','Lenguaje'),
(4444,'10','Historia'),(5555,'10','Matemáticas'),(6666,'10','Lenguaje'),
(4444,'18','Historia'),(5555,'18','Matemáticas'),(6666,'18','Lenguaje'),
(4444,'26','Historia'),(5555,'26','Matemáticas'),(6666,'26','Lenguaje'),

(7777,'3','Historia'),(8888,'3','Matemáticas'),(9999,'3','Lenguaje'),
(7777,'11','Historia'),(8888,'11','Matemáticas'),(9999,'11','Lenguaje'),
(7777,'19','Historia'),(8888,'19','Matemáticas'),(9999,'19','Lenguaje'),
(7777,'27','Historia'),(8888,'27','Matemáticas'),(9999,'27','Lenguaje'),

(1211,'4','Historia'),(1311,'4','Matemáticas'),(1411,'4','Lenguaje'),
(1211,'12','Historia'),(1311,'12','Matemáticas'),(1411,'12','Lenguaje'),
(1211,'20','Historia'),(1311,'20','Matemáticas'),(1411,'20','Lenguaje'),
(1211,'28','Historia'),(1311,'28','Matemáticas'),(1411,'28','Lenguaje'),

(1511,'5','Historia'),(1611,'5','Matemáticas'),(1711,'5','Lenguaje'),
(1511,'13','Historia'),(1611,'13','Matemáticas'),(1711,'13','Lenguaje'),
(1511,'21','Historia'),(1611,'21','Matemáticas'),(1711,'21','Lenguaje'),
(1511,'29','Historia'),(1611,'29','Matemáticas'),(1711,'29','Lenguaje'),

(1811,'6','Historia'),(1911,'6','Matemáticas'),(2111,'6','Lenguaje'),
(1811,'14','Historia'),(1911,'14','Matemáticas'),(2111,'14','Lenguaje'),
(1811,'22','Historia'),(1911,'22','Matemáticas'),(2111,'22','Lenguaje'),
(1811,'30','Historia'),(1911,'30','Matemáticas'),(2111,'30','Lenguaje'),

(2211,'7','Historia'),(2311,'7','Matemáticas'),(2411,'7','Lenguaje'),
(2211,'15','Historia'),(2311,'15','Matemáticas'),(2411,'15','Lenguaje'),
(2211,'23','Historia'),(2311,'23','Matemáticas'),(2411,'23','Lenguaje'),
(2211,'31','Historia'),(2311,'31','Matemáticas'),(2411,'31','Lenguaje'),

(2511,'8','Historia'),(2611,'8','Matemáticas'),(2711,'8','Lenguaje'),
(2511,'16','Historia'),(2611,'16','Matemáticas'),(2711,'16','Lenguaje'),
(2511,'24','Historia'),(2611,'24','Matemáticas'),(2711,'24','Lenguaje'),
(2511,'32','Historia'),(2611,'32','Matemáticas'),(2711,'32','Lenguaje');
"""
cur.execute(sql)

conn.commit()
cur.close()