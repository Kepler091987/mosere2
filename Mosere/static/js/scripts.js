$(document).ready(function () {
    $('#group-students-create').on('change', function() {
        var result = $('#area-students-create');
        var alert = $('#area-students-alert');
        var html;
        if ($(this).val() != 0){
            html ='<input type="number" id="number-students-create" class="form-control form-inline mb-3" placeholder="Ingresa el numero de alumnos que vas a registrar">';
            html +='<button type="button" class="btn btn-info btn-sm" id="btn-quantity-create-student"><i class="fas fa-sign-in-alt"></i> Ingresar</button>';
            result.html(html);
            alert.empty();
        } else {
            html ='<div class="alert alert-danger alert-dismissible fade show" role="alert">';
            html +='<strong>¡Debes Seleccionar un grupo!</strong>';
            html +='<button type="button" class="close" data-dismiss="alert" aria-label="Close">';
            html +='<span aria-hidden="true">&times;</span>';
            html +='</button>';
            html +='</div>';
            alert.html(html);
            result.empty();
        }

    });

    $('#form-create-students').on('click', '#btn-quantity-create-student' ,function () {
        var result = $('#area-students-create');
        var alert = $('#area-students-alert');
        var btn = $('#btn-sign-create-students');
        var quantity = $('#number-students-create').val();
        var html = '';
        if (quantity > 0){
            btn.prop('disabled', false);
            for (var i=0; i<quantity; i++){
                html += '<div class="row mt-2">';
                html += '<div class="col-12 col-md-3"><input type="text" name="names[]" class="form-control mr-2" placeholder="Nombre del estudiante"></div>';
                html += '<div class="col-12 col-md-3"><input type="text" name="firsts[]" class="form-control mr-2" placeholder="Apellido paterno del estudiante"></div>';
                html += '<div class="col-12 col-md-3"><input type="text" name="lasts[]" class="form-control mr-2" placeholder="Apellido materno del estudiante"></div>';
                html += "<div class='col-12 col-md-3'>";
                html +="<div class='row'>";
                html += '<div class="col-12 col-md-8"><input type="text" name="enrollments[]" class="form-control mr-2" placeholder="Matricula"></div>';
                html += "<div class='col-12 col-md-4'>";
                html += "<select class=form-control name='sexs[]' required>";
                html += "<option value='0'>Selecciona el Sexo</option>";
                html += "<option value='1'>Hombre</option>";
                html += "<option value='2'>Mujer</option>";
                html += "</select>";
                html += "</div>";
                html += "</div>";
                html += '</div>';
                html += '</div>';
                result.html(html)
            }
            alert.empty();
        } else {
            html ='<div class="alert alert-danger alert-dismissible fade show" role="alert">';
            html +='<strong>¡Debes Seleccionar una cantidad mayor a 0!</strong>';
            html +='<button type="button" class="close" data-dismiss="alert" aria-label="Close">';
            html +='<span aria-hidden="true">&times;</span>';
            html +='</button>';
            html +='</div>';
            alert.html(html);
        }
    });
    $('#form-create-students').on('submit', function (event) {
        event.preventDefault();
        var btn = $('#btn-sign-create-students');
        btn.prop('disabled', true);
        var result = $('#area-students-create');
        var action = $(this).attr('action');
        var alert = $('#area-students-alert');
        alert.html('<div class="loading"><img src="/public/images/loader.gif" alt="loading" /><br/>Un momento, por favor...</div>');
        var html = '';
        $.ajax(action, {
            type:'POST',
            data: $(this).serialize()
        })
        .fail(function(request, errorType, errorMessage){
            alert.html(errorMessage);
        })
        .done(function(response){
            result.empty();
            alert.html(response);
        });
    });

    $('#form-search-students').on('keyup', '#search-student', function () {
       var result = $('#area-search-students');
        var alert = $('#alert-students-search');
        var action = $('#form-search-students').attr('action');
        result.html('<div class="loading"><img src="/public/images/loader.gif" alt="loading" /><br/>Un momento, por favor...</div>');
        $.ajax(action, {
            type:'POST',
            data: $('#form-search-students').serialize()
        })
            .fail(function(request, errorType, errorMessage){
                alert.html(errorMessage);
            })
            .done(function(response){
                result.html(response);
                // alert.empty();
            });
    });
});





// html ='<div class="alert alert-danger alert-dismissible fade show" role="alert">';
// html +='<strong>¡Debes Seleccionar un grupo!</strong>';
// html +='<button type="button" class="close" data-dismiss="alert" aria-label="Close">';
// html +='<span aria-hidden="true">&times;</span>';
// html +='</button>';
// html +='</div>';
// result.html(html);