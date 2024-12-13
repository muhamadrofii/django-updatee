function filterNews(category) {
    var news = document.querySelectorAll('.news-card');
    news.forEach(function(news) {
        if (news.getAttribute('data-category') === category || category === 'all') {
            news.style.display = 'block';
        } else {
            news.style.display = 'none';
        }
        });
    }