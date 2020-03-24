$(document).ready(function (e) {
    var html ='<div id="child" class="form-row"><select name=producto[] class="browser-default custom-select mb-4 col-8"><option value="" disabled>Producto</option><option value="1" selected>Ram</option><option value="2">HDD</option></select><div class="col-4"><input name="cantidad[]" type="text" id="defaultRegisterFormFirstName" class="form-control col"placeholder="First name"></div></div>'

    $("#add").click(function (e) {
        $("#myconte").append(html);
    });

    $("#add2").click(function (e) {
        $("#myconte #child:last-child").remove();
    });
});

