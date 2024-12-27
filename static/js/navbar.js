$(document).ready(function () {
    var currentUrl = window.location.href;
    console.log("Current URL: " + currentUrl);
    var newWindowWidth = $(window).width();
    var newWindowHeight = $(window).height();
    $('#navbar-li-ul1').css("left", `${newWindowWidth * 0.18}px`);  
    $('#navbar-li-ul2').css("left", `${newWindowWidth * 0.043}px`); 
    $('#navbar-li-ul3').css("left", `${newWindowWidth * 0.457}px`); 
    $(".navbar-li:not(.active)").on("mouseover", function () {
        $(this).css("background-color", "rgb(0, 150, 224)");
        $(this).find("img").css("display", "block");
        $(this).find("a").css("margin-top", "0px");
        $(this).find("ul").css("display", "block");
    });
    $(".navbar-li:not(.active)").on("mouseout", function () {
        $(this).css("background-color", "");
        $(this).find("img").css("display", "none");
        $(this).find("ul").css("display", "none");
        // $(this).find("a").css("margin-top", "18px");
    });
    $(".navbar-li.active").on("mouseover", function () {
        $(this).find("ul").css("display", "block");
    });

    $(".navbar-li.active").on("mouseout", function () {
        $(this).find("ul").css("display", "none");
    });

    $(".animation").css("top", '100px');

    $(window).resize(function() {
        var newWindowWidth = $(window).width();
        var newWindowHeight = $(window).height();
        // alert(newWindowHeight)
        // alert(newWindowWidth)

        $('#navbar-li-ul1').css("left", `${newWindowWidth * 0.18}px`);  // 18% of the width
        $('#navbar-li-ul2').css("left", `${newWindowWidth * 0.243}px`); // 24.3% of the width
        $('#navbar-li-ul3').css("left", `${newWindowWidth * 0.457}px`); // 45.7% of the width

        var top = $(".slideshow-background").height() * 0.10;
        $(".animation").css("top", `${top}px`);
    });

    $(window).resize();
    $("#navbar-li-menu").siblings("ul").css("display", "none");

    $("#navbar-li-menu").on("click", function () {
        $(this).siblings("ul").slideToggle(1000);
    });
    console.log($(".navbar-li"))
    let parts = currentUrl.split('/');
    let targetPart = parts[parts.length - 2];
    console.log(targetPart);
    switch (targetPart) {
        case "":
            $(".navbar-li").removeClass("active")
            $("#home").addClass("active");
            break;
        case "books":
            $(".navbar-li").removeClass("active")
            $("#books").addClass("active");
            break;
        case "videos&photos":
            $(".navbar-li").removeClass("active")
            $("#videos_photos").addClass("active");
            break;
        case "find-adam":
            $(".navbar-li").removeClass("active")
            $("#findadam").addClass("active");
            break;
        case "resources":
            $(".navbar-li").removeClass("active")
            $("#resources").addClass("active");
            break;
        case "news_announ":
            $(".navbar-li").removeClass("active")
            $("#news_announcements").addClass("active");
            break;
        case "about_us":
            $(".navbar-li").removeClass("active")
            $("#aboutadam").addClass("active");
            break;
        case "write_adam":
            $(".navbar-li").removeClass("active")
            $("#writetoadam").addClass("active");
            break;
        default:
            break;
    }
});
