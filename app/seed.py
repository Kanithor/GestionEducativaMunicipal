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
(2222,1,'ROSA ATIENZA GRACIA',999999,'rag@ed.cl','Calle 2, La Cisterna','Pedagogía Matematicas','Matematicas'),
(3333,1,'AGUSTIN MEDINA QUIROGA',999999,'amq@ed.cl','Calle 3, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(4444,2,'MARIA ROSARIO BORJA PIÑERO',999999,'mrb@ed.cl','Calle 4, La Cisterna','Pedagogía Historia','Historia'),
(5555,2,'RAUL VALCARCEL PELAEZ',999999,'rvp@ed.cl','Calle 5, La Cisterna','Pedagogía Matematicas','Matematicas'),
(6666,2,'CARLA MASIP MIRO',999999,'cmm@ed.cl','Calle 6, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(7777,3,'ROBERTO GAMBOA MEDIAVILLA',999999,'rgm@ed.cl','Calle 7, La Cisterna','Pedagogía Historia','Historia'),
(8888,3,'ANA BELEN RUBIA CASTILLO',999999,'arc@ed.cl','Calle 8, La Cisterna','Pedagogía Matematicas','Matematicas'),
(9999,3,'MIGUEL SEMPERE HOLGADO',999999,'msh@ed.cl','Calle 9, La Cisterna','Pedagogía Lenguajes','Lenguajes'),
(1211,4,'GLORIA MACHIN PRATS',999999,'gmp@ed.cl','Calle 10, La Cisterna','Pedagogía Historia','Historia'),
(1311,4,'JUAN LUIS CANTARERO FONT',999999,'jcf@ed.cl','Calle 11, La Cisterna','Pedagogía Matematicas','Matematicas'),
(1411,4,'YOLANDA QUIROGA PINA',999999,'yqp@ed.cl','Calle 12, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(1511,5,'FRANCISCO GONZALO DE LAS HERAS',999999,'fdh@ed.cl','Calle 13, La Cisterna','Pedagogía Historia','Historia'),
(1611,5,'PATRICIA NAVARRETE TORNERO',999999,'pnt@ed.cl','Calle 14, La Cisterna','Pedagogía Matematicas','Matematicas'),
(1711,5,'CRISTOBAL BELTRAN MASCARO',999999,'cbm@ed.cl','Calle 15, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(1811,6,'ELENA BRIZ YUSTE',999999,'eby@ed.cl','Calle 16, La Cisterna','Pedagogía Historia','Historia'),
(1911,6,'HUGO PALACIOS CORONEL',999999,'hpc@ed.cl','Calle 17, La Cisterna','Pedagogía Matematicas','Matematicas'),
(2111,6,'TERESA VILLAVERDE HUGUET',999999,'tvh@ed.cl','Calle 18, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(2211,7,'JULIO RIVAS MALAGON',999999,'jrm@ed.cl','Calle 19, La Cisterna','Pedagogía Historia','Historia'),
(2311,7,'CONCEPCION PELAEZ PRIEGO',999999,'cpp@ed.cl','Calle 20, La Cisterna','Pedagogía Matematicas','Matematicas'),
(2411,7,'GABRIEL HEVIA RODAS',999999,'ghr@ed.cl','Calle 21, La Cisterna','Pedagogía Lenguaje','Lenguaje'),
(2511,8,'NEREA COBO ALBERO',999999,'nca@ed.cl','Calle 22, La Cisterna','Pedagogía Historia','Historia'),
(2611,8,'PEDRO HOYOS GONZALES',999999,'phg@ed.cl','Calle 23, La Cisterna','Pedagogía Matematicas','Matematicas'),
(2711,8,'BEATRIZ GRAU SACRISTAN',999999,'bgs@ed.cl','Calle 24, La Cisterna','Pedagogía Lenguaje','Lenguaje');
"""
cur.execute(sql)

sql ="""
insert into niveles (id_nivel,nivel) values 
(1,'NM1'),
(2,'NM2'),
(3,'NM3'),
(4,'NM4');
"""
cur.execute(sql)

sql ="""
insert into cursos (id_curso,promedio,cantidadEstudiantes,id_colegio,id_nivel) values
(1,5.7,40,1,1),
(2,6.1,43,2,1),
(3,5.4,44,3,1),
(4,5.9,36,4,1),
(5,6.8,34,5,1),
(6,5.3,47,6,1),
(7,5.2,48,7,1),
(8,5.8,38,8,1),
(9,5.6,40,1,2),
(10,5.5,43,2,2),
(11,6.8,42,3,2),
(12,5.8,43,4,2),
(13,5.1,38,5,2),
(14,5.2,39,6,2),
(15,5.9,41,7,2),
(16,6.1,40,8,2),
(17,4.8,42,1,3),
(18,5.6,43,2,3),
(19,5.7,36,3,3),
(20,5.8,33,4,3),
(21,5.5,32,5,3),
(22,5.6,45,6,3),
(23,5.7,40,7,3),
(24,5.8,41,8,3),
(25,4.8,42,1,4),
(26,5.6,35,2,4),
(27,5.7,32,3,4),
(28,5.8,33,4,4),
(29,5.5,36,5,4),
(30,5.6,37,6,4),
(31,5.7,38,7,4),
(32,5.8,39,8,4);
"""
cur.execute(sql)

sql ="""
insert into imparte (rut,id_curso) values 
(1111,'1'),(2222,'1'),(3333,'1'),(1111,'9'),(2222,'9'),(3333,'9'),(1111,'17'),(2222,'17'),(3333,'17'),
(1111,'25'),(2222,'25'),(3333,'25'),

(4444,'2'),(5555,'2'),(6666,'2'),(4444,'10'),(5555,'10'),(6666,'10'),(4444,'18'),(5555,'18'),(6666,'18'),
(4444,'26'),(5555,'26'),(6666,'26'),

(7777,'3'),(8888,'3'),(9999,'3'),(7777,'11'),(8888,'11'),(9999,'11'),(7777,'19'),(8888,'19'),(9999,'19'),
(7777,'27'),(8888,'27'),(9999,'27'),

(1211,'4'),(1311,'4'),(1411,'4'),(1211,'12'),(1311,'12'),(1411,'12'),(1211,'20'),(1311,'20'),(1411,'20'),
(1211,'28'),(1311,'28'),(1411,'28'),

(1511,'5'),(1611,'5'),(1711,'5'),(1511,'13'),(1611,'13'),(1711,'13'),(1511,'21'),(1611,'21'),(1711,'21'),
(1511,'29'),(1611,'29'),(1711,'29'),

(1811,'6'),(1911,'6'),(2111,'6'),(1811,'14'),(1911,'14'),(2111,'14'),(1811,'22'),(1911,'22'),(2111,'22'),
(1811,'30'),(1911,'30'),(2111,'30'),

(2211,'7'),(2311,'7'),(2411,'7'),(2211,'15'),(2311,'15'),(2411,'15'),(2211,'23'),(2311,'23'),(2411,'23'),
(2211,'31'),(2311,'31'),(2411,'31'),

(2511,'8'),(2611,'8'),(2711,'8'),(2511,'16'),(2611,'16'),(2711,'16'),(2511,'24'),(2611,'24'),(2711,'24'),
(2511,'32'),(2611,'32'),(2711,'32');
"""
cur.execute(sql)

conn.commit()
cur.close()