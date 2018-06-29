from app import app
from flask import render_template,request,redirect
from app.configuraciones import *

import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s" %(database,user,passwd))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
	prueba = "hola"
	return render_template("index.html",prueba=prueba)

@app.route('/docentes')
def docentes():
	sql ="""
	select D.rut,D.nombre,D.formacion,C.nombre from docentes as D JOIN colegios as C ON D.id_colegio = C.id_colegio
	"""
	cur.execute(sql)
	docentes  = cur.fetchall()
	return render_template("docentes.html",docentes=docentes)

@app.route('/colegios')
def colegios():
	sql ="""
	select nombre, director, categoria from colegios
	"""
	cur.execute(sql)
	colegios  = cur.fetchall()
	return render_template("colegios.html",colegios=colegios)

@app.route('/cursos')
def cursos():
	sql ="""
	select CU.id_curso,N.nivel,CU.cantidadEstudiantes,CU.promedio,CO.nombre
	from cursos as CU JOIN colegios as CO ON CU.id_colegio = CO.id_colegio
	JOIN niveles as N ON CU.id_nivel = N.id_nivel
	"""
	cur.execute(sql)
	cursos  = cur.fetchall()
	return render_template("cursos.html",cursos=cursos)

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
	if request.method == 'POST':
		comentario =  request.form['comentarios']
		print(comentario)
		sql = """ insert into comentarios  
		(post_id,usuario_id,creado,comentario) 
		values (%s,1,now(),'%s' ) """%(post_id,comentario)
		cur.execute(sql)
		conn.commit()

	sql ="""
	select id,titulo,texto from posts where id = %s
	"""%post_id
	print(sql)
	cur.execute(sql)
	post  = cur.fetchone()

	sql ="""
	select id,nombre from categorias,categorias_posts 
	where categorias_posts.categoria_id = categorias.id 
	and post_id = %s 
	"""%(post_id)
	print(sql)
	cur.execute(sql)
	categorias  = cur.fetchall()

	sql ="""
	select comentarios.id,nombre,apellido,comentario
	
	from usuarios,comentarios 
	where comentarios.usuario_id = usuarios.id 
	and post_id = %s order by id desc
	"""%(post_id)
	print(sql)
	cur.execute(sql)
	comentarios  = cur.fetchall()
	return render_template("post.html",post= post,categorias=categorias,comentarios= comentarios) 


@app.route('/comentario/<id>', methods=['GET', 'POST'])
def comentario(id):
	if request.method == 'POST':
		comentario =  request.form['comentarios']
		print(comentario)
		sql = """ update comentarios  set comentario = '%s'
		where id = %s """%(comentario,id)
		cur.execute(sql)
		conn.commit()


	sql ="""
	select comentarios.id,nombre,apellido,comentario
	
	from usuarios,comentarios 
	where comentarios.usuario_id = usuarios.id 
	and comentarios.id = %s order by id desc
	"""%(id)
	print(sql)
	cur.execute(sql)
	comentario  = cur.fetchone()
	return render_template("comentario.html",comentario= comentario) 


@app.route('/borrar/<id>', methods=['GET', 'POST'])
def borrar(id):


	sql ="""
		delete from comentarios where id = %s
	"""%(id)
	print(sql)
	cur.execute(sql)
	conn.commit()
	return  redirect(request.referrer)


