from flask import Flask, render_template, request, redirect, url_for,flash
from dao.CiudadDao import CiudadDao
from dao.PaisDao import PaisDao

app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/inicio')
def inicio():
    return "hola mundo desde el backend"

# endpoint o ruta
@app.route('/contacto')
def contacto():
    return "<h3>Introduciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')






@app.route('/ciudades-index')
def ciudades_index():
    #creacion de la instancia de ciudaddao
    ciudadDao = CiudadDao()
    lista_ciudades = ciudadDao.getCiudades()
    return render_template('ciudades/ciudades-index.html', lista_ciudades=lista_ciudades)



@app.route('/ciudades')
def ciudades():
    return render_template('ciudades/ciudades.html')



@app.route('/guardar-ciudad', methods=['POST'])
def guardarCiudad():
    ciudad = request.form.get('txtDescripcion').strip()
    if ciudad == None or len(ciudad) < 1:
       # mostrar un mensaje al usuario
       flash('Debe escribir algo en la descripcion', 'warning')
    
       # redireccionar a la vista ciudades
       return redirect(url_for('ciudades'))
    
    ciudaddao = CiudadDao()
    ciudaddao.guardarCiudad(ciudad.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista ciudades 
    return redirect(url_for('ciudades_index'))

@app.route('/ciudades_editar/<id>')
def ciudadesEditar(id):
    ciudaddao = CiudadDao()
    return render_template('ciudades/ciudades_editar.html', ciudad=ciudaddao.getCiudadById(id))

@app.route('/actualizar-ciudad', methods=['POST'])
def actualizarCiudad():
    id = request.form.get('txtIdCiudad')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('ciudadesEditar', id=id))

    # actualizar
    ciudaddao = CiudadDao()
    ciudaddao.updateCiudad(id, descripcion.upper())

    return redirect(url_for('ciudades_index'))

@app.route('/ciudades-eliminar/<id>')
def ciudadesEliminar(id):
    ciudaddao = CiudadDao()
    ciudaddao.deleteCiudad(id)
    return redirect(url_for('ciudades_index'))













@app.route('/paises-index')
def paises_index():
    #creacion de la instancia de ciudaddao
    paisDao = PaisDao()
    lista_paises = paisDao.getPaises()
    return render_template('paises/paises-index.html', lista_paises=lista_paises)

@app.route('/paises')
def paises():
    return render_template('paises/paises.html')

@app.route('/guardar-pais', methods=['POST'])
def guardarPais():
    pais = request.form.get('txtDescripcion').strip()
    if pais == None or len(pais) < 1:
       # mostrar un mensaje al usuario
       flash('Debe escribir algo en la descripcion', 'warning')
    
       # redireccionar a la vista ciudades
       return redirect(url_for('paises'))
    
    paisdao = PaisDao()
    paisdao.guardarPais(pais.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista ciudades 
    return redirect(url_for('paises_index'))


@app.route('/paises_editar/<id>')
def paisesEditar(id):
    paisdao = PaisDao()
    return render_template('paises/paises_editar.html', pais=paisdao.getPaisById(id))

@app.route('/actualizar-pais', methods=['POST'])
def actualizarPais():
    id = request.form.get('txtIdPais')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('paisesEditar', id=id))

    # actualizar
    paisdao = PaisDao()
    paisdao.updatePais(id, descripcion.upper())

    return redirect(url_for('paises_index'))



@app.route('/paises-eliminar/<id>')
def paisesEliminar(id):
    paisdao = PaisDao()
    paisdao.deleteCiudad(id)
    return redirect(url_for('paises_index'))








@app.route('/guardar-mascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNombreMascota')
    return f"Ya llego tu mascota <strong>{nombreMascota}</strong> al servidor"


# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)