(function($) {
    "use strict"

    var busqueda = false;

    //Buscar Usuario
    $('#numId').keyup(function(e) {
        e.preventDefault();
        if ($('#numId').val() == '1234' && $('#tipoId').val() == 'CC') {
            $('#primerNombre').val('Radamel');
            $('#primerApellido').val('Falcao');
            $('#correo').val('rfalcao@fcf.com');
            $('#direccion').val('Calle 10 # 25 -58');
            $('#nombreUsuario').val('rfalcao');
            $('#telefono').val('3698745');
            busqueda = true;
        } else {
            $('#primerNombre').val('');
            $('#primerApellido').val('');
            $('#correo').val('');
            $('#direccion').val('');
            $('#nombreUsuario').val('');
            $('#telefono').val('');
            busqueda = false;
        }
    });

    //Eliminar Usuario
    $('#eliminarUsuario').on('click', function(e) {
        e.preventDefault();
        if (busqueda) {
            if (window.confirm("¿Realmente quieres eliminar este usuario?")) {
                $('#tipoId').val('CC');
                $('#numId').val('');
                $('#primerNombre').val('');
                $('#primerApellido').val('');
                $('#correo').val('');
                $('#direccion').val('');
                $('#nombreUsuario').val('');
                $('#telefono').val('');
                busqueda = false;
            }
        } else {
            alert('Primero debe buscar un usuario.');
        }

    });

    //Limpiar Usuario
    $('#limpiarUsuario').on('click', function(e) {
        e.preventDefault();
        $('#tipoId').val('CC');
        $('#numId').val('');
        $('#primerNombre').val('');
        $('#primerApellido').val('');
        $('#correo').val('');
        $('#direccion').val('');
        $('#nombreUsuario').val('');
        $('#telefono').val('');
    });

    //Guardar Usuario
    //Limpiar Usuario
    $('#guardarUsuario').on('click', function(e) {
        e.preventDefault();
        if (busqueda) {
            if ($('#tipoId').val() != '' && $('#numId').val() != '' && $('#primerNombre').val() != '' &&
                $('#primerApellido').val() != '' && $('#correo').val() != '' && $('#direccion').val() != '' &&
                $('#nombreUsuario').val() != '' && $('#telefono').val() != '') {
                alert('Usuario creado exitosamente!');
            } else {
                alert('Todos los campos deben estar diligenciados.');
            }
        } else {
            if ($('#tipoId').val() != '' && $('#numId').val() != '' && $('#primerNombre').val() != '' &&
                $('#primerApellido').val() != '' && $('#correo').val() != '' && $('#direccion').val() != '' &&
                $('#nombreUsuario').val() != '' && $('#telefono').val() != '' && $('#contrasena').val() != '' && $('#repetirContrasena').val() != '') {
                alert('Usuario creado exitosamente!');
            } else {
                alert('Todos los campos deben estar diligenciados.');
            }
        }

    });

    //Comentar
    $('#Comentar').on('click', function(e) {
        e.preventDefault();
        if ($('#Comentar').text() == 'Comentar') {
            if ($('#comentario').val().length > 10) {
                $('.reviews').append('<li><div class="review-heading"><img class="img" src="./img/user.png" alt=""><h5 class="name">Jaime</h5><p class="date">10 OCT 2021, 7:00 AM</p></div><div class="review-body"><p>' + $('#comentario').val() + '</p></div></li>');
                $('#comentarioModal').modal('hide');
            } else {
                alert("El campo comentario debe tener más de 10 caracteres.");
            }
        } else {
            if ($('#comentario').val().length > 10) {
                $('#texto').text($('#comentario').val());
                $('#comentarioModal').modal('hide');
                $('#comentario').val('');
                $('#Comentar').text('Comentar');
            } else {
                alert("El campo comentario debe tener más de 10 caracteres.");
            }
        }
    });

    //Editar comentario
    $('#editar').on('click', function(e) {
        e.preventDefault();
        $('#comentario').val($('#texto').text());
        $('#Comentar').text('Editar');
    });

    //Eliminar Comentario
    $('#eliminar').on('click', function(e) {
        e.preventDefault();
        if (window.confirm("¿Realmente quieres eliminar el comentario?")) {
            $('#delete').remove();
            $('#num_comentarios').text('Comentarios (2)');
        }
    });

    // Mobile Nav toggle
    $('.menu-toggle > a').on('click', function(e) {
        e.preventDefault();
        $('#responsive-nav').toggleClass('active');
    })

    // Fix cart dropdown from closing
    $('.cart-dropdown').on('click', function(e) {
        e.stopPropagation();
    });

    /////////////////////////////////////////

    // Products Slick
    $('.products-slick').each(function() {
        var $this = $(this),
            $nav = $this.attr('data-nav');

        $this.slick({
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplay: true,
            infinite: true,
            speed: 300,
            dots: false,
            arrows: true,
            appendArrows: $nav ? $nav : false,
            responsive: [{
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                    }
                },
            ]
        });
    });

    // Products Widget Slick
    $('.products-widget-slick').each(function() {
        var $this = $(this),
            $nav = $this.attr('data-nav');

        $this.slick({
            infinite: true,
            autoplay: true,
            speed: 300,
            dots: false,
            arrows: true,
            appendArrows: $nav ? $nav : false,
        });
    });

    /////////////////////////////////////////

    // Product Main img Slick
    $('#product-main-img').slick({
        infinite: true,
        speed: 300,
        dots: false,
        arrows: true,
        fade: true,
        asNavFor: '#product-imgs',
    });

    // Product imgs Slick
    $('#product-imgs').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: true,
        centerMode: true,
        focusOnSelect: true,
        centerPadding: 0,
        vertical: true,
        asNavFor: '#product-main-img',
        responsive: [{
            breakpoint: 991,
            settings: {
                vertical: false,
                arrows: false,
                dots: true,
            }
        }, ]
    });

    // Product img zoom
    var zoomMainProduct = document.getElementById('product-main-img');
    if (zoomMainProduct) {
        $('#product-main-img .product-preview').zoom();
    }

    /////////////////////////////////////////

    // Input number
    $('.input-number').each(function() {
        var $this = $(this),
            $input = $this.find('input[type="number"]'),
            up = $this.find('.qty-up'),
            down = $this.find('.qty-down');

        down.on('click', function() {
            var value = parseInt($input.val()) - 1;
            value = value < 1 ? 1 : value;
            $input.val(value);
            $input.change();
            updatePriceSlider($this, value)
        })

        up.on('click', function() {
            var value = parseInt($input.val()) + 1;
            $input.val(value);
            $input.change();
            updatePriceSlider($this, value)
        })
    });

    var priceInputMax = document.getElementById('price-max'),
        priceInputMin = document.getElementById('price-min');

    if (priceInputMax) {
        priceInputMax.addEventListener('change', function() {
            updatePriceSlider($(this).parent(), this.value)
        });
    }

    if (priceInputMin) {
        priceInputMin.addEventListener('change', function() {
            updatePriceSlider($(this).parent(), this.value)
        });
    }

    function updatePriceSlider(elem, value) {
        if (elem.hasClass('price-min')) {
            console.log('min')
            priceSlider.noUiSlider.set([value, null]);
        } else if (elem.hasClass('price-max')) {
            console.log('max')
            priceSlider.noUiSlider.set([null, value]);
        }
    }

    // Price Slider
    var priceSlider = document.getElementById('price-slider');
    if (priceSlider) {
        noUiSlider.create(priceSlider, {
            start: [1, 999],
            connect: true,
            step: 1,
            range: {
                'min': 1,
                'max': 999
            }
        });

        priceSlider.noUiSlider.on('update', function(values, handle) {
            var value = values[handle];
            handle ? priceInputMax.value = value : priceInputMin.value = value
        });
    }

})(jQuery);