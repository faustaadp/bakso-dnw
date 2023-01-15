const cards = document.querySelectorAll('.card');

cards.forEach(card => {
    card.addEventListener('click', (event) => {
        // Mendapatkan id transaksi dari data attribute
        const transaksiId = card.getAttribute('data-transaksi-id');
        // Redirect ke halaman detail transaksi dengan id transaksi yang didapat
        window.location.href = `/kasir/detail/${transaksiId}`;
    });
});

const transaksiCards = document.querySelectorAll('.card');
  transaksiCards.forEach(function(card) {
    // jika status transaksi sudah bayar, tampilkan card tersebut
    if (card.querySelector('.status-box').textContent == "Belum Bayar") {
        card.classList.remove("hidden");
        card.style.visibility = "visible";
    } else {
         // jika tidak, sembunyikan card tersebut
         card.classList.add("hidden");
         card.style.visibility = "hidden";
    }
    });

// get element tombol pending dan selesai
const pendingBtn = document.querySelector('#pending');
const selesaiBtn = document.querySelector('#selesai');
const pendingBtn2 = document.querySelector('#pending2');
const selesaiBtn2 = document.querySelector('#selesai2');

// tambahkan event listener pada tombol pending
pendingBtn.addEventListener('click', function() {
    pendingBtn2.classList.add("active")
    selesaiBtn2.classList.remove("active")
  // looping untuk setiap card transaksi
  const transaksiCards = document.querySelectorAll('.card');
  transaksiCards.forEach(function(card) {
    // jika status transaksi belum bayar, tampilkan card tersebut
    if (card.querySelector('.status-box').textContent == "Belum Bayar") {
        card.classList.remove("hidden");
        card.style.visibility = "visible";
        
    } else {
      // jika tidak, sembunyikan card tersebut
      card.classList.add("hidden");
      card.style.visibility = "hidden";
      
    }
  });
});

// tambahkan event listener pada tombol selesai
selesaiBtn.addEventListener('click', function() {
    selesaiBtn2.classList.add("active")
    pendingBtn2.classList.remove("active")
  // looping untuk setiap card transaksi
  const transaksiCards = document.querySelectorAll('.card');
  transaksiCards.forEach(function(card) {
    // jika status transaksi sudah bayar, tampilkan card tersebut
    if (card.querySelector('.status-box').textContent == "Sudah Bayar") {
        card.classList.remove("hidden");
        card.style.visibility = "visible";
        
    } else {
         // jika tidak, sembunyikan card tersebut
         card.classList.add("hidden");
         card.style.visibility = "hidden";
         
    }
    });
});

    
    