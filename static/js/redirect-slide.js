$(document).ready(function () {
    $("#redirect-background1").animate({
        left: "-700px",
        opacity:0

    }, 2000, function() {
        $(this).css("display", "none");
    });

    $("#redirect-background2").animate({
        right: "-700px",
        opacity:0
    }, 2000, function() {
        $(this).css("display", "none");
    });
});