$(document).ready(function () {
    $.ajax({
        type: "get",
        url: "../data/detailbook.json",
        dataType: "json",
        success: function (response) {
            element = response[0]
            $(".reviews-read").before(
                `
                <img src='${element.bookimage}' alt=''>
                <p><span>${element.titlecontent}</span>${element.content}</p>
                `
            );
        }
    });
});