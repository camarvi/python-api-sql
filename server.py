from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, json

from class_zonasbasicas import zonasbasicas
from class_centros import centros


app = Flask(__name__)

app.secret_key = "frjkfjierjklsjk5343"

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Funcionando"})

@app.route('/zonas', methods=['GET'])
def html_zonas():
    lzonas = zonasbasicas()
    listado_zonas = lzonas.listado_zonas()
    json_zonas = []
    
    for zona in listado_zonas:
        elemento_zona={
           'cod' : zona[0], 
           'zbs' : zona[1].strip()
        }
        json_zonas.append(elemento_zona)
        
    return jsonify({"zonas_basicas" : json_zonas, "message": "Listado ZonasBasicas"})

@app.route('/centros_zbs/<id>', methods = ['GET'])
def centros_zbs(id):
    valor_recibido = id
    lcentros = centros('',valor_recibido,'')
    lista_centros = lcentros.centrosugc()
   
    return jsonify({
        "centros_ugc" : [{"cod": x[0], "zbs": x[1].strip(), "nombre": x[2].strip()} for x in lista_centros]
    })


#-----------  AÑADIR UN NUEVO CENTRO   --------------------------------------------

@app.route('/nuevocentro', methods=['POST'])
def addCentro():
    new_centro = centros(request.json['cod_cen'],request.json['cod_zbs'],request.json['nombre']) 
    new_centro.nuevo_centro()
    return jsonify({"message":"centro agregado"})

#----------------------------------------------------------------------------------

@app.route('/delete_centro/<string:cod_cen_delete>', methods=['DELETE'])
def deleteCentro(cod_cen_delete):
    try:
        d_centro = centros(cod_cen_delete,'','')
        d_centro.elimina_centro()
        return jsonify({"message":"Centro Eliminado"})
    except:
        return jsonify({"message":"Error al borrar el centro", "centro": cod_cen_delete})
    

'''
@app.route("/cuentas/", endpoint="nueva_cuenta", methods=["POST"])
def new_account():
    from flask import request
    json = request.get_json()
    email = json.get("email")
    name = json.get("name")
    new_user = Cuenta()
    new_user.name = name
    new_user.email = email
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"id": new_user.id}), 201


'''

'''
#--------------         ELIMINAR UN PRODUCTO ---------------------
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    ProductFoundDelete = [product for product in products if product['name'] == product_name]
    if (len(ProductFoundDelete) >0 ):
        products.remove(ProductFoundDelete[0])
        return jsonify({
            "message" : "Product Delete", 
            "products": products
            })

    return jsonify({"message" : "Product Not Found, not delete"})
#------------------------------------------------------------------------------
'''


if __name__ == '__main__':
    app.run(port=8000, debug = True)

