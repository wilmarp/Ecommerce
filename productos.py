def getProductosList():
    return [
    {"ProductoID":1, "Nombre":"Clasico Standar", "Calificacion": 5, "Precio": 50000, "Comentarios": 6582, "Deseado": "true", "Imagenes": ["/static/img/product01.png","/static/img/product01.png"]},
    {"ProductoID":2, "Nombre":"Tenis Ultraboost 21", "Calificacion": 4, "Precio": 799900, "Comentarios": 695, "Deseado": "false", "Imagenes": ["/static/img/product02.png","/static/img/product02.png"]},
    {"ProductoID":3, "Nombre":"Tenis Grand Court", "Calificacion": 5, "Precio": 559000, "Comentarios": 6582, "Deseado": "true", "Imagenes": ["/static/img/product03.png","/static/img/product03.png"]},
    {"ProductoID":4, "Nombre":"Guayos Predator Freak.3 Terreno Firme", "Calificacion": 3, "Precio": 48900, "Comentarios": 548, "Deseado": "false", "Imagenes": ["/static/img/product04.png","/static/img/product04.png"]},
    {"ProductoID":5, "Nombre":"Chanclas Adilette Aqua (UNISEX)", "Calificacion": 2, "Precio": 189000, "Comentarios": 8484, "Deseado": "false", "Imagenes": ["/static/img/product05.png","/static/img/product05.png"]},
    {"ProductoID":6, "Nombre":"ULTRABOOST 21", "Calificacion": 4, "Precio": 95100, "Comentarios": 2158, "Deseado": "true", "Imagenes": ["/static/img/product06.png","/static/img/product06.png"]},
    {"ProductoID":7, "Nombre":"SUPERNOVA + M", "Calificacion": 3, "Precio": 255410, "Comentarios": 210, "Deseado": "false", "Imagenes": ["/static/img/product07.png","/static/img/product07.png"]},
    {"ProductoID":8, "Nombre":"Copa Sense.3 Turf", "Calificacion": 5, "Precio": 236000, "Comentarios": 518, "Deseado": "false", "Imagenes": ["/static/img/product08.png","/static/img/product08.png"]},
    {"ProductoID":9, "Nombre":"McCarten Simpsons Left Handers Rule", "Calificacion": 3, "Precio": 691000, "Comentarios": 5481, "Deseado": "false", "Imagenes": ["/static/img/product09.png","/static/img/product09.png"]},
    {"ProductoID":10, "Nombre":"Adilette Comfort", "Calificacion": 4, "Precio": 520000, "Comentarios": 5187, "Deseado": "true", "Imagenes": ["/static/img/product01.png"]},
    {"ProductoID":11, "Nombre":"adidas Performance Coreracer", "Calificacion": 4, "Precio": 650000, "Comentarios": 5184, "Deseado": "false", "Imagenes": ["/static/img/product02.png"]},
    {"ProductoID":12, "Nombre":"Royal County Of Berkshire Polo Club", "Calificacion": 4, "Precio": 251000, "Comentarios": 961, "Deseado": "false", "Imagenes": ["/static/img/product03.png"]}    
    ]

def getProductosDeseadosList():
    return [
    {"ProductoID":1, "Nombre":"Clasico Standar", "Calificacion": 5, "Precio": 50000, "Comentarios": 6582, "Deseado": "true", "Imagenes": ["/static/img/product01.png","/static/img/product01.png"]},
    {"ProductoID":3, "Nombre":"Tenis Grand Court", "Calificacion": 5, "Precio": 559000, "Comentarios": 6582, "Deseado": "true", "Imagenes": ["/static/img/product03.png","/static/img/product03.png"]},
    {"ProductoID":6, "Nombre":"ULTRABOOST 21", "Calificacion": 4, "Precio": 95100, "Comentarios": 2158, "Deseado": "true", "Imagenes": ["/static/img/product06.png","/static/img/product06.png"]},
    {"ProductoID":10, "Nombre":"Adilette Comfort", "Calificacion": 4, "Precio": 520000, "Comentarios": 5187, "Deseado": "true", "Imagenes": ["/static/img/product01.png"]}
    ]


def getFiltrosProductosSexo(sexo):

    if sexo == 1 :
        return [
            {"ProductoID":1, "Nombre":"Clasico Standar", "Calificacion": 5, "Precio": 50000, "Comentarios": 6582, "Deseado": "true", "Imagenes": ["/static/img/product01.png","/static/img/product01.png"]},
            {"ProductoID":2, "Nombre":"Tenis Ultraboost 21", "Calificacion": 4, "Precio": 799900, "Comentarios": 695, "Deseado": "false", "Imagenes": ["/static/img/product02.png","/static/img/product02.png"]},
            {"ProductoID":3, "Nombre":"Tenis Grand Court", "Calificacion": 5, "Precio": 559000, "Comentarios": 6582, "Deseado": "true", "Imagenes": ["/static/img/product03.png","/static/img/product03.png"]},
            {"ProductoID":4, "Nombre":"Guayos Predator Freak.3 Terreno Firme", "Calificacion": 3, "Precio": 48900, "Comentarios": 548, "Deseado": "false", "Imagenes": ["/static/img/product04.png","/static/img/product04.png"]},
            {"ProductoID":8, "Nombre":"Copa Sense.3 Turf", "Calificacion": 5, "Precio": 236000, "Comentarios": 518, "Deseado": "false", "Imagenes": ["/static/img/product08.png","/static/img/product08.png"]}
        ]    
    elif sexo == 2:
        return [
            {"ProductoID":5, "Nombre":"Chanclas Adilette Aqua (UNISEX)", "Calificacion": 2, "Precio": 189000, "Comentarios": 8484, "Deseado": "false", "Imagenes": ["/static/img/product05.png","/static/img/product05.png"]},
            {"ProductoID":6, "Nombre":"ULTRABOOST 21", "Calificacion": 4, "Precio": 95100, "Comentarios": 2158, "Deseado": "true", "Imagenes": ["/static/img/product06.png","/static/img/product06.png"]},
            {"ProductoID":7, "Nombre":"SUPERNOVA + M", "Calificacion": 3, "Precio": 255410, "Comentarios": 210, "Deseado": "false", "Imagenes": ["/static/img/product07.png","/static/img/product07.png"]},
        ]
    elif sexo == 3:
        return [
            {"ProductoID":9, "Nombre":"McCarten Simpsons Left Handers Rule", "Calificacion": 3, "Precio": 691000, "Comentarios": 5481, "Deseado": "false", "Imagenes": ["/static/img/product09.png","/static/img/product09.png"]},
            {"ProductoID":10, "Nombre":"Adilette Comfort", "Calificacion": 4, "Precio": 520000, "Comentarios": 5187, "Deseado": "true", "Imagenes": ["/static/img/product01.png"]},
            {"ProductoID":11, "Nombre":"adidas Performance Coreracer", "Calificacion": 4, "Precio": 650000, "Comentarios": 5184, "Deseado": "false", "Imagenes": ["/static/img/product02.png"]},
            {"ProductoID":12, "Nombre":"Royal County Of Berkshire Polo Club", "Calificacion": 4, "Precio": 251000, "Comentarios": 961, "Deseado": "false", "Imagenes": ["/static/img/product03.png"]}    
        ]