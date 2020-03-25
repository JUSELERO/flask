$(document).ready(function (e) {
    var html ='<div id=child class="form-row"><input name="id_producto[]" type="text" class="mb-4 form-control col"placeholder="id producto"><div class="col-3"><input name="cantidad[]" type="text" class="mb-4 form-control col"placeholder="cantidad"></div><div class="col-3"><input name="precio[]" type="text" class="mb-4 form-control col"placeholder="precio"></div></div>'

    $("#add").click(function (e) {
        $("#myconte").append(html);
    });

    $("#add2").click(function (e) {
        $("#myconte #child:last-child").remove();
    });
});

