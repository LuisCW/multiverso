// JS JQuery
$("#planet-list").sortable();

// JS Ajax
$("#check-order").click(function () {
    var planetIds = $("#planet-list").sortable("toArray");
    $.post("/check_order/", { order: planetIds }, function (data) {
        if (data.correct) {
            $("#next-level").prop("disabled", false);
        }
    });
});
