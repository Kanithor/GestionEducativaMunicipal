from app import app
from flask import render_template,request,redirect
from app.configuraciones import *

import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s" %(database,user,passwd))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	sql ="""
	select count(*) from colegios
	"""
	cur.execute(sql)
	colegios  = cur.fetchone()

	sql ="""
	select count(*) from cursos
	"""
	cur.execute(sql)
	cursos  = cur.fetchone()

	sql ="""
	select count(*) from docentes
	"""
	cur.execute(sql)
	docentes  = cur.fetchone()

	sql ="""
	select sum(cantidadEstudiantes) from cursos
	"""
	cur.execute(sql)
	estudiantes  = cur.fetchone()

	sql = """select D.rut,D.nombre,D.formacion,C.nombre, D.calificacion from docentes as D JOIN colegios as C ON D.id_colegio = C.id_colegio ORDER BY (D.calificacion) DESC LIMIT 5"""
	cur.execute(sql)
	top5docentes  = cur.fetchall()

	sql = """select C.director, C.nombre from colegios as C where C.categoria = 2"""
	cur.execute(sql)
	directores  = cur.fetchall()

	sql ="""
	select CU.id_curso,N.nivel,CU.promedio,CO.nombre
	from cursos as CU JOIN colegios as CO ON CU.id_colegio = CO.id_colegio
	JOIN niveles as N ON CU.id_nivel = N.id_nivel ORDER BY(CU.promedio) DESC LIMIT 1
	"""
	cur.execute(sql)
	topcursos  = cur.fetchall()

	return render_template("index.html",colegios=colegios,cursos = cursos,docentes = docentes,estudiantes=estudiantes,top5docentes = top5docentes, directores = directores, topcursos = topcursos)

@app.route('/docentes')
def docentes():
	sql ="""
	select D.rut,D.nombre,D.formacion,C.nombre from docentes as D JOIN colegios as C ON D.id_colegio = C.id_colegio
	"""
	cur.execute(sql)
	docentes  = cur.fetchall()

	sql = """select id_colegio,nombre from colegios"""
	cur.execute(sql)
	colegios  = cur.fetchall()

	return render_template("docentes.html",docentes=docentes,colegios=colegios)


@app.route('/docentes/<rut>')
def docentesrut(rut):
	sql ="""
	select CU.id_curso, N.nivel, CU.promedio, CO.nombre from cursos as CU JOIN imparte as I ON CU.id_curso = I.id_curso JOIN 
	docentes as D ON D.rut = I.rut JOIN niveles as N ON N.id_nivel = CU.id_nivel JOIN colegios as CO ON
	CO.id_colegio = CU.id_colegio where D.rut = %s
	"""%rut
	cur.execute(sql)
	cursosdocentes  = cur.fetchall()
	sql = """select D.rut,CO.nombre,D.nombre,D.telefono,D.email,D.calificacion,D.direccion,
	D.formacion,D.asignatura from docentes as D JOIN colegios as CO ON D.id_colegio = CO.id_colegio where rut = %s"""%rut
	cur.execute(sql)
	docente  = cur.fetchone()

	sql = """select id_colegio,nombre from colegios"""
	cur.execute(sql)
	colegios  = cur.fetchall()

	return render_template("docenteconfig.html",cursosdocentes=cursosdocentes,docente=docente,colegios=colegios)

@app.route('/colegios')
def colegios():
	sql ="""
	select id_colegio, nombre, director, categoria from colegios
	"""
	cur.execute(sql)
	colegios  = cur.fetchall()
	return render_template("colegios.html",colegios=colegios)

@app.route('/colegios/<id>')
def colegiosid(id):
	sql ="""
	select CU.id_curso, N.nivel, CU.promedio, CU.cantidadEstudiantes from cursos as CU JOIN niveles as N ON CU.id_nivel = N.id_nivel
JOIN colegios as CO ON CO.id_colegio = CU.id_colegio where CO.id_colegio = %s
	"""%id
	cur.execute(sql)
	cursoscolegios  = cur.fetchall()

	sql="""select * from colegios where id_colegio = %s"""%id
	cur.execute(sql)
	colegio  = cur.fetchone()

	return render_template("colegioconfig.html",cursoscolegios=cursoscolegios,colegio=colegio)

@app.route('/cursos')
def cursos():
	sql ="""
	select CU.id_curso,N.nivel,CU.cantidadEstudiantes,CU.promedio,CO.nombre
	from cursos as CU JOIN colegios as CO ON CU.id_colegio = CO.id_colegio
	JOIN niveles as N ON CU.id_nivel = N.id_nivel
	"""
	cur.execute(sql)
	cursos  = cur.fetchall()

	sql ="""
	select id_colegio,nombre from colegios
	"""
	cur.execute(sql)
	colegios  = cur.fetchall()

	sql ="""
	select id_nivel,nivel from niveles
	"""
	cur.execute(sql)
	niveles  = cur.fetchall()

	return render_template("cursos.html",cursos=cursos,colegios=colegios,niveles=niveles)

@app.route('/cursos/<id>')
def cursosid(id):
	sql ="""
	select D.rut, D.nombre, D.asignatura from docentes as D JOIN imparte as I ON D.rut = I.rut JOIN cursos as CU
	ON CU.id_curso = I.id_curso where CU.id_curso = %s
	"""%id
	cur.execute(sql)
	docentescurso  = cur.fetchall()

	sql="""select CU.id_curso,N.nivel ,CO.nombre, CU.promedio, CU.cantidadestudiantes  from cursos as CU 
	JOIN niveles as N ON N.id_nivel = CU.id_nivel JOIN colegios as CO ON CO.id_colegio = CU.id_colegio 
	where CU.id_curso = %s"""%id
	cur.execute(sql)
	curso  = cur.fetchone()

	sql ="""
	select id_colegio,nombre from colegios
	"""
	cur.execute(sql)
	colegios  = cur.fetchall()

	sql ="""
	select id_nivel,nivel from niveles
	"""
	cur.execute(sql)
	niveles  = cur.fetchall()

	return render_template("cursoconfig.html",docentescurso=docentescurso,curso=curso,colegios=colegios,niveles=niveles)