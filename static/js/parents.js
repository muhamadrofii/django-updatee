function filterVideos(category) {
    var videos = document.querySelectorAll('.video-card');
    videos.forEach(function(video) {
      if (video.getAttribute('data-category') === category || category === 'all') {
        video.style.display = 'block';
      } else {
        video.style.display = 'none';
      }
    });
  }