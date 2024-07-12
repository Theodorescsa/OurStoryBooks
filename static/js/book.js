$(document).ready(function () {

    // var audio = new Audio('../images/bookssound.mp3');
    $('.books').animate({
        left:"19%",
        opacity:1
    },3200)
    $('.all-box').animate({
        marginRight:0,
        top:"-30px",
        opacity:1
    },3200)
    $('.books').find("a").hover(
        function () {
            $(this).find("img").animate({
                width: "33%",
            }, 300);
            // audio.play();
        },
        function () {
            $(this).find("img").animate({
                width: "30%",
            }, 300);
            // audio.pause();
            // audio.currentTime = 0; 
        }
    );
    $.ajax({
        type: "get",
        url: "http://127.0.0.1:8000/book_api/?format=json",
        dataType: "json",
        success: function (response) {
            console.log(response)
            element = response[0]
            $(".books").prepend(
                `
                <a href="./bookdetail.html" class="grimm">
                <img src="${element.book_image}" alt="">
                </a>
                `
            );
             // var audio = new Audio('../images/bookssound.mp3');
    $('.books').animate({
        left:"19%",
        opacity:1
    },3200)
    $('.all-box').animate({
        marginRight:0,
        top:"-30px",
        opacity:1
    },3200)
    $('.books').find("a").hover(
        function () {
            $(this).find("img").animate({
                width: "33%",
            }, 300);
            // audio.play();
        },
        function () {
            $(this).find("img").animate({
                width: "30%",
            }, 300);
            // audio.pause();
            // audio.currentTime = 0; 
        }
    );
        }
    });
});