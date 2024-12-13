function showPopup(title) {
    const modal = new bootstrap.Modal(document.getElementById('welcomeModal'));
    const modalTitle = document.getElementById('welcomeModalLabel');
    const modalBody = document.querySelector('.modal-body p');
  
    modalTitle.textContent = `Post Test: ${title}`;
    modalBody.textContent = `Selamat datang di Post Test ${title}. Test ini berisi 10 soal yang nantinya dapat kita ketahui seberapa jauh pengetahuan kita mengenai ${title}. Semoga sukses!`;
  
    modal.show();
  }