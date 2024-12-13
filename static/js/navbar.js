// Pilih semua link navbar
const navLinks = document.querySelectorAll('.navbar .nav-link');

// Tambahkan event listener untuk setiap link navbar
navLinks.forEach(link => {
    link.addEventListener('click', function() {
        // Hapus kelas 'active' dari semua link
        navLinks.forEach(nav => nav.classList.remove('active'));
        // Tambahkan kelas 'active' ke link yang diklik
        this.classList.add('active');
    });
});

document.addEventListener('click', function(event) {
    // Memeriksa apakah klik dilakukan pada card
    const isCard = event.target.closest('.teacher .card');

    if (!isCard) {
        // Jika bukan klik pada card, hapus class 'expanded' dari semua card
        document.querySelectorAll('.teacher .card').forEach(card => card.classList.remove('expanded'));
    }
});

function expandCard(card) {
    // Cek apakah card sudah memiliki class 'expanded'
    if (card.classList.contains('expanded')) {
        // Jika sudah, hapus class 'expanded' untuk menutup card
        card.classList.remove('expanded');
    } else {
        // Jika belum, hapus class 'expanded' dari semua card lain, dan tambahkan ke card yang diklik
        document.querySelectorAll('.teacher .card').forEach(c => c.classList.remove('expanded'));
        card.classList.add('expanded');
    }
}