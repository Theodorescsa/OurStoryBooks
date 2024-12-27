$(document).ready(function () {
    let book_id = $("#book_id").text()
    let access_token = $("#access_token").text()
    $.ajax({
        type: "get",
        url: `/book_api/${book_id}/`,
        dataType: "json",
        headers: {
            "Authorization": `Bearer ${access_token}` 
        },
        success: function (response) {
            let element = response
            console.log('response',response)
            $(".reviews-read").before(
                `
                <img src='${element.book_image}' alt=''>
                <p><span>${element.bookname}</span>${element.description}</p>
                `
            );
          
        },
        error: function (xhr, status, error) {
            console.error("Error: ", status, error);
        }
    });
});
