home = {
    urlbase: 'https://uninorteequipo3.pythonanywhere.com/',
    // urlbase: 'https://127.0.0.1',
    uSuperAdmin: 1,
    uAdmin: 2,
    uCliente: 3,
    ref: null
}
urlRest = {
    urlgetproductos: home.urlbase + '/productos',
    urlconnect: home.urlbase + '/connect',
    urlgetListaDeseos: home.urlbase + '/listadeseos/',
    urlgetListaUsuarios: home.urlbase + '/adminUser'
}

servicios = {

    getproductos: function() {
        localStorage.Deseados = 0;

        $.ajax({
            type: "GET",
            url: urlRest.urlgetproductos,
            async: true,
            dataType: "json",
            success: function(data) {
                $("#list-productos").html("");
                for (var i = 0; i < data.length; i++) {

                    newProducto =
                        '<a href="/producto"><div id="carousel-example-generic' + i + '" class="carousel slide col-md-2" data-ride="carousel" data-interval="false">' +
                        '   <div style="height:60px;"><h4>' + data[i].Nombre + '</h4></div>' +
                        '   <span class="heart">Agregar a la lista de deseos' +
                        '   <i class="' + (data[i].Deseado == "true" ? 'heart-on' : '') + ' fa fa-heart"></i></span>' +
                        '   <ol class="carousel-indicators">' +
                        '       <li data-target="#carousel-example-generic' + i + '" data-slide-to="0" class="active"></li>' +
                        '       <li data-target="#carousel-example-generic' + i + '" data-slide-to="1"></li>' +
                        '       <li data-target="#carousel-example-generic' + i + '" data-slide-to="2"></li>' +
                        '	</ol>' +
                        '   <div class="carousel-inner" role="listbox">';

                    for (var j = 0; j < data[i].Imagenes.length; j++) {

                        newProducto += '<div class="item ' + (j == 0 ? "active" : "") + '">' +
                            '    <img src="' + data[i].Imagenes[j] + '" alt="...">' +
                            '    <div class="carousel-caption"></div>' +
                            '</div>';
                    }

                    newProducto +=
                        '   </div>' +
                        '   <a class="left carousel-control" href="#carousel-example-generic' + i + '" role="button" data-slide="prev">' +
                        '   	<span class="glyphicon glyphicon-chevron-left icon-prev" aria-hidden="true"></span>' +
                        '   	<span class="sr-only">Previous</span>' +
                        '   </a>' +
                        '   <a class="right carousel-control" href="#carousel-example-generic' + i + '" role="button" data-slide="next">' +
                        '   	<span class="glyphicon glyphicon-chevron-right icon-next" aria-hidden="true"></span>' +
                        '   	<span class="sr-only">Next</span>' +
                        '   </a>' +
                        '   <form>' +
                        '       <p class="clasificacion">' +
                        '           <input id="radio1" type="radio" name="estrellas" value="5">' +
                        '           <label for="radio1">★</label>' +
                        '           <input id="radio2" type="radio" name="estrellas" value="4">' +
                        '           <label for="radio2">★</label>' +
                        '           <input id="radio3" type="radio" name="estrellas" value="3">' +
                        '           <label for="radio3" class="votado">★</label>' +
                        '           <input id="radio4" type="radio" name="estrellas" value="2">' +
                        '           <label for="radio4" class="votado">★</label>' +
                        '           <input id="radio5" type="radio" name="estrellas" value="1">' +
                        '           <label for="radio5" class="votado">★</label>' +
                        '       </p>' +
                        '   </form>' +
                        '   <span class="s-precio">$ ' + data[i].Precio + '</span>' +
                        '   <a href="#" class="s-producto-comentarios">' + data[i].Comentarios + ' comentarios</a>' +
                        '   <div class="btn-del-edit-prod">' +
                        '       <button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#formEditar">Editar</button>' +
                        '       <button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#formEliminar">Eliminar</button>' +
                        '   </div>' +
                        '</div></a>';

                    $("#list-productos").append(newProducto);
                    if (data[i].Deseado == "true")
                        localStorage.Deseados = parseInt(localStorage.Deseados) + 1;

                    $('#carousel-example-generic' + i + ' .heart').on("click", function(e) {
                        event.preventDefault();
                        // agregar o quitar de la lista de deseos 
                        $("i", this).toggleClass("heart-on");
                        $(".qty").html($(".heart-on").toArray().length);
                    })
                }
                $(".qty").html(localStorage.Deseados);
            },
            error: function(e) {

            },
        });
    },

    getconnect: function() {
        $.ajax({
            type: "GET",
            url: urlRest.urlconnect,
            async: true,
            dataType: "json",
            success: function(data) {
                localStorage.userRef = data.ref;
                localStorage.tUser = data.tipoUser;
                if (data.tipoUser == home.uSuperAdmin)
                    $("#crear-producto").show();

            },
            error: function(e) {

            },
        });
    },

    getListaDeseos: function() {
        debugger
        $.ajax({
            type: "POST",
            data: JSON.stringify({ "UserRef": localStorage.userRef }),
            url: urlRest.urlgetListaDeseos,
            async: true,
            dataType: "json",
            success: function(data) {
                localStorage.Deseados = 0;
                $("#list-productos").html("");
                for (var i = 0; i < data.length; i++) {

                    newProducto =
                        '       <div id="carousel-example-generic' + i + '" class="carousel slide col-md-2" data-ride="carousel" data-interval="false">' +
                        '		<div style="height:60px;"><h4>' + data[i].Nombre + '</h4></div>' +
                        '		<span>Agregar a la lista de deseos</span>' +
                        '		<a href="" class="heart ' + (data[i].Deseado == "true" ? 'heart-on' : '') + ' fa fa-heart"></a>' +
                        '		<ol class="carousel-indicators">' +
                        '			<li data-target="#carousel-example-generic' + i + '" data-slide-to="0" class="active"></li>' +
                        '			<li data-target="#carousel-example-generic' + i + '" data-slide-to="1"></li>' +
                        '			<li data-target="#carousel-example-generic' + i + '" data-slide-to="2"></li>' +
                        '		</ol>' +
                        '		    <div class="carousel-inner" role="listbox">';

                    for (var j = 0; j < data[i].Imagenes.length; j++) {

                        newProducto += '			    <div class="item ' + (j == 0 ? "active" : "") + '">' +
                            '			        <img src="' + data[i].Imagenes[j] + '" alt="...">' +
                            '			        <div class="carousel-caption"></div>' +
                            '			    </div>';
                    }

                    newProducto +=
                        '		    </div>' +

                        '		' +
                        '		<a class="left carousel-control" href="#carousel-example-generic' + i + '" role="button" data-slide="prev">' +
                        '			<span class="glyphicon glyphicon-chevron-left icon-prev" aria-hidden="true"></span>' +
                        '			<span class="sr-only">Previous</span>' +
                        '		</a>' +
                        '		<a class="right carousel-control" href="#carousel-example-generic' + i + '" role="button" data-slide="next">' +
                        '			<span class="glyphicon glyphicon-chevron-right icon-next" aria-hidden="true"></span>' +
                        '			<span class="sr-only">Next</span>' +
                        '    	</a>' +
                        '		<form>' +
                        '			<p class="clasificacion">' +
                        '			  <input id="radio1" type="radio" name="estrellas" value="5">' +
                        '			  <label for="radio1">★</label>' +
                        '			  <input id="radio2" type="radio" name="estrellas" value="4">' +
                        '			  <label for="radio2">★</label>' +
                        '			  <input id="radio3" type="radio" name="estrellas" value="3">' +
                        '			  <label for="radio3" class="votado">★</label>' +
                        '			  <input id="radio4" type="radio" name="estrellas" value="2">' +
                        '			  <label for="radio4" class="votado">★</label>' +
                        '			  <input id="radio5" type="radio" name="estrellas" value="1">' +
                        '			  <label for="radio5" class="votado">★</label>' +
                        '			</p>' +
                        '		  </form>' +
                        '		<span class="s-precio">$ ' + data[i].Precio + '</span>' +
                        '		<a href="#" class="s-producto-comentarios">' + data[i].Comentarios + ' comentarios</a>' +
                        '       <div class="btn-del-edit-prod">' +
                        '       <button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#formEditar">Editar</button>' +
                        '       <button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#formEliminar">Eliminar</button>' +
                        '        </div>' +
                        '	</div>';

                    $("#list-productos").append(newProducto);
                    if (data[i].Deseado == "true")
                        localStorage.Deseados = parseInt(localStorage.Deseados) + 1;

                }
                $(".qty").html(localStorage.Deseados);

            },
            error: function(e) {

            },
        });
    },

    getListaUsuarios: function() {
        debugger
        $.ajax({
            type: "POST",
            data: JSON.stringify({ "UserRef": localStorage.userRef }),
            url: urlRest.urlgetListaUsuarios,
            async: true,
            dataType: "json",
            success: function(data) {
                localStorage.Deseados = 0;
                $("#list-usuarios").html("");
                for (var i = 0; i < data.length; i++) {

                    newUsuario =
                        '<table class="table">'+
                        '<tr>'+
                        '<th scope="col">ID</th>'+
                        '<th scope="col">Nombre</th>'+
                        '<th scope="col">Apellido</th>'+
                        '<th scope="col">Identificacion</th>'+
                        '<th scope="col">Dirección</th>'+
                        '<th scope="col">Telefono</th>'+
                        '<th scope="col">Correo</th>'+
                        '<th scope="col">Rol</th>'+
                        '</tr>'+
                        '<tr>'+
                        '<td scope="row">' + data[i].id + '</td>'
                        '<td>' + data[i].primer_nombre + '</td>'
                        '<td>' + data[i].segundo_nombre + '</td>'
                        '<td>' + data[i].no_id + '</td>'
                        '<td>' + data[i].direccion + '</td>'
                        '<td>' + data[i].telefono + '</td>'
                        '<td>' + data[i].correo + '</td>'
                        '<td>' + data[i].rol + '</td>'
                        '</tr>'+
                        '</table>';
                }
            },
            error: function(e) {
            },
        });
    },
}

home.eventElement = {
    /* onClick_ListaDeseos: function(){
        event.preventDefault();
        servicios.getListaDeseos();                       
    }  */
}