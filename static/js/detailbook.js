$(document).ready(function () {
    let book_id = $("#book_id").text()
    let access_token = $("#access_token").text()
    $.ajax({
        type: "get",
        url: `/home-api/books/${book_id}/`,
        dataType: "json",
        headers: {
            "Authorization": `Bearer ${access_token}` 
        },
        success: function (response) {
            let element = response;
            console.log('response', response);
        
            // Giới hạn số ký tự cho description
            const maxLength = 500; // Số ký tự tối đa
            let description = element.description;
            if (description.length > maxLength) {
                description = description.substring(0, maxLength) + "..."; // Cắt chuỗi và thêm "..."
            }
        
            $(".button-container").before(
                `
                <img src='${element.book_image}' alt=''>
                <p><span>${element.bookname}--</span>${description}</p>
                `
            );
        },
        
        error: function (xhr, status, error) {
            console.error("Error: ", status, error);
        }
    });
});
