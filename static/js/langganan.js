function calculateTotal() {
    const plan = document.getElementById("plan");
    const outputElement = document.getElementById("output");
    const discountInfo = document.getElementById("discount-info");
    const Harga = document.getElementById("price");
    const total_harga = document.getElementById("total-price");
  
    // Mendapatkan nilai yang dipilih
    const selectedPaket = plan.value;
  
    if (selectedPaket === "pilih") {
      // Jika pengguna belum memilih paket
      outputElement.innerText = "Anda belum memilih paket berlangganan.";
      total_harga.innerText = "Rp.0";
      Harga.innerText = "Rp.0";
      discountInfo.innerText = "Rp.0";
    } else {
      // Logika harga dan potongan
      let harga = 0;
      let potongan = 0;
  
      if (selectedPaket === "1") {
        harga = 99999;
        potongan = 70000;
      } else if (selectedPaket === "6") {
        harga = 999999;
        potongan = 890000;
      } else if (selectedPaket === "12") {
        harga = 1999999;
        potongan = 1800000;
      }
  
      const total = harga - potongan;
  
      // Menampilkan hasil
      outputElement.innerText = `${selectedPaket} Bulan`;
      Harga.innerText = `Rp.${harga.toLocaleString("id-ID")}`;
      discountInfo.innerText = `Rp.${potongan.toLocaleString("id-ID")}`;
      total_harga.innerText = `Rp.${total.toLocaleString("id-ID")}`;
    }
  }
  