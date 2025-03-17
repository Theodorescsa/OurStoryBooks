var pages = document.getElementsByClassName('page');
    for (var i = 0; i < pages.length; i++) {
      var page = pages[i];
      if (i % 2 === 0) {
        page.style.zIndex = (pages.length - i);
      }
    }

    document.addEventListener('DOMContentLoaded', function() {
      for (var i = 0; i < pages.length; i++) {
        pages[i].pageNum = i + 1;
        pages[i].onclick = function() {
          if (this.pageNum % 2 === 0) {
            this.classList.remove('flipped');
            this.previousElementSibling.classList.remove('flipped');
          } else {
            this.classList.add('flipped');
            this.nextElementSibling.classList.add('flipped');
          }
        }
      }
    });
    
    document.addEventListener('DOMContentLoaded', function () {
      // Chuyển nền tối
      const darkModeBtn = document.getElementById('toggle-dark-mode');
      darkModeBtn.addEventListener('click', function () {
          document.body.classList.toggle('dark-mode'); 
      });
  
      // Chọn nhạc và phát nhạc
      const musicUpload = document.getElementById('music-upload');
      const chooseMusicBtn = document.getElementById('choose-music');
      const audioPlayer = document.getElementById('audio-player');
      const volumeUp = document.getElementById('volume-up');
      const volumeDown = document.getElementById('volume-down');
  
      chooseMusicBtn.addEventListener('click', function () {
          musicUpload.click(); 
      });
  
      musicUpload.addEventListener('change', function (event) {
          const file = event.target.files[0];
          if (file) {
              const objectURL = URL.createObjectURL(file);
              audioPlayer.src = objectURL;
              audioPlayer.style.display = 'block';
              audioPlayer.play();
          }
      });
  
      // Tăng giảm âm lượng
      volumeUp.addEventListener('click', function () {
          if (audioPlayer.volume < 1.0) {
              audioPlayer.volume = Math.min(audioPlayer.volume + 0.1, 1.0);
          }
      });
  
      volumeDown.addEventListener('click', function () {
          if (audioPlayer.volume > 0.0) {
              audioPlayer.volume = Math.max(audioPlayer.volume - 0.1, 0.0);
          }
      });
  });
  document.addEventListener('DOMContentLoaded', function () {
    const bookmarkBtn = document.getElementById('bookmark-btn');

    // Lắng nghe sự kiện đánh dấu trang
    bookmarkBtn.addEventListener('click', function () {
        let currentPageElement = null;

        // Duyệt qua tất cả các trang từ cuối đến đầu để tìm trang flipped cuối cùng
        for (let i = pages.length - 1; i >= 0; i--) {
            if (pages[i].classList.contains('flipped') && pages[i].getAttribute('data-id') !== 'bia') {
                currentPageElement = pages[i];
                break;
            }
        }

        // Nếu không có trang flipped thì hiển thị thông báo
        if (!currentPageElement) {
            alert("❌ Không tìm thấy trang hiện tại!");
            return;
        }

        // Lấy ID của trang hiện tại
        const currentPage = currentPageElement.getAttribute('data-id');
        console.log("Trang hiện tại có ID:", currentPage);

        if (!currentPage) {
            alert("❌ Không tìm thấy ID của trang hiện tại!");
            return;
        }

        const token = document.querySelector('#token').textContent; // Lấy token từ hidden field
        const user = getUserIdFromToken(token); // Lấy user từ token, nếu cần
        if (currentPage === null) {
          alert("❌ Không tìm thấy trang hiện tại!");
          return;
      }
        // Gửi AJAX request để đánh dấu trang
        fetch('/home-api/reading-sessions/bookmark/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({
                user_id: user,  // Truyền user vào
                page: currentPage  // Truyền page id vào
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("📌 Đã đánh dấu trang tại trang " + currentPage);
            } else {
                alert("❌ Trang đã được đánh dấu rồi!");
            }
        })
        .catch(error => console.error("Lỗi:", error));
    });

    // Hàm lấy CSRF token từ cookie Django
    function getCSRFToken() {
        let csrfToken = null;
        document.cookie.split(';').forEach(cookie => {
            if (cookie.trim().startsWith('csrftoken=')) {
                csrfToken = cookie.trim().substring('csrftoken='.length);
            }
        });
        return csrfToken;
    }

    // Hàm lấy ID user từ token nếu có
    function getUserIdFromToken(token) {
        // Giải mã token (JWT) để lấy thông tin người dùng (tùy vào cấu trúc token của bạn)
        // Bạn có thể dùng thư viện như `jwt-decode` nếu cần thiết
        // Ví dụ:
        const decodedToken = JSON.parse(atob(token.split('.')[1])); // Giải mã JWT
        return decodedToken.user_id; // Giả sử user_id có trong payload của token
    }
});
