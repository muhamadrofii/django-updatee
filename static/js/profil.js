            const itemDetailModal = document.querySelector('#item-detail-modal');
            const itemDetailButtons = document.querySelectorAll('.item-detail-button');

            itemDetailButtons.forEach((btn) => {
                btn.onclick = (b) => {
                itemDetailModal.style.display = 'flex';
                b.preventDefault();
                };
            })

            // Klik Tombol Close di Modal Box
            document.querySelector('.modal .close-icon').onclick = (b) => {
                itemDetailModal.style.display = 'none';
                b.preventDefault();
            }

            // perbatasan

            
            // function selectProfilePicture(imgElement) {
            //     // Mendapatkan URL gambar yang dipilih
            //     const selectedImageUrl = imgElement.src;

            //     // Mengubah gambar profil di bagian atas dengan gambar yang dipilih
            //     const profilePicture = document.getElementById('selectedProfilePicture');
            //     profilePicture.src = selectedImageUrl;

            //     // Menyembunyikan gambar (jika ada) dan menampilkan gambar profil yang dipilih
            //     profilePicture.style.display = 'block';

            //     // Menyimpan URL gambar ke localStorage
            //     localStorage.setItem('profilePicture', selectedImageUrl);

            //     // Menutup modal setelah gambar dipilih
            //     const modal = document.getElementById('imageModal');
            //     const modalInstance = bootstrap.Modal.getInstance(modal); // Bootstrap Modal instance
            //     modalInstance.hide();
            // }
            window.onload = function() {
                // const profilePicture = document.getElementById('selectedProfilePicture');
                // const savedProfilePicture = localStorage.getItem('profilePicture');

                    

                
                // if (savedProfilePicture) {
                //     profilePicture.src = savedProfilePicture;
                //     profilePicture.style.display = 'block';  // Menampilkan gambar profil yang tersimpan
                // }
            };
            