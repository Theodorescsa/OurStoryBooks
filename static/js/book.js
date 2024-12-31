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
                width: "27%",
            }, 300);
            // audio.play();
        },
        function () {
            $(this).find("img").animate({
                width: "25%",
            }, 300);
            // audio.pause();
            // audio.currentTime = 0; 
        }
    );
    var token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxMTQ5NTAyLCJpYXQiOjE3MjExNDU5MDIsImp0aSI6IjdkOGM4ZDk0Njc1OTQ3NTBiYmRmNjdlNTA2M2QyMzc0IiwidXNlcl9pZCI6MX0.XIzjeiozBKWAGuLj1BkFeSD7M8N2U_PEGCdXm8_0P50"
    $.ajax({
        type: "get",
        url: "http://127.0.0.1:8000/book_api/",
        dataType: "json",
        headers: {
            "Authorization": "Bearer " + token
        },
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
    var audio = new Audio('/static/images/bookssound.mp3');
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
            audio.play();
        },
        function () {
            $(this).find("img").animate({
                width: "30%",
            }, 300);
            audio.pause();
            audio.currentTime = 0; 
        }
    );
        }
    });
});