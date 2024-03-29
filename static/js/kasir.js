$(document).ready(function() {
  // Menjumlahkan semua subtotal dan menampilkan di element #total
  function updateTotalHarga() {
    let totalHarga = 0;
    let jumlahItems = document.querySelectorAll('.jumlah-item');
    // Saya ingin for loop setiap item dan mengambil harga dan jumlah, lalu totalHarga += harga * jumlah
    jumlahItems.forEach(item => {
      let harga = item.getAttribute('data-harga').replace(/,/g, "");;
      let jumlah = item.value;
      console.log(harga)
      console.log(jumlah)
      totalHarga += harga * jumlah;
    });
    document.querySelector('#total').innerHTML = totalHarga.toLocaleString();
    const simpanBtn = document.querySelector('#submit');
    if (totalHarga === 0) {
      // jika iya, tombol simpan tidak bisa diklik dan warnanya berubah menjadi abu-abu
      simpanBtn.disabled = true;
      simpanBtn.style.backgroundColor = '#d1e3f8';
      simpanBtn.style.borderColor = '#d1e3f8';
      simpanBtn.style.opacity = 1
    } else {
        // jika tidak, tombol simpan bisa diklik dan warnanya kembali seperti semula
        simpanBtn.disabled = false;
        simpanBtn.style.backgroundColor = '#007bff';
    }
  }

  // Event listener pada input jumlah item
  const jumlahItems = document.querySelectorAll('.jumlah-item');
  jumlahItems.forEach(function(item) {
    item.addEventListener('input', function() {
      const harga = this.dataset.harga;
      const jumlah = this.value;
      const subtotal = harga * jumlah;
      const tdSubtotal = this.parentNode.parentNode.querySelector('td.subtotal');
      tdSubtotal.innerHTML = subtotal;

      updateTotalHarga();
    });
  });

  // Event listener pada tombol increment
  $('.btn-increment').on('click', function() {
    var input = $(this).parent().find('input');
    input.val(parseInt(input.val()) + 1);
    input.trigger('input');
    updateTotalHarga();
  });

  // Event listener pada tombol decrement
  $('.btn-decrement').on('click', function() {
    var input = $(this).parent().find('input');
    var value = parseInt(input.val());
    if (value > 0) {
      input.val(value - 1);
      input.trigger('input');
      updateTotalHarga();
    }
  });

  document.querySelectorAll('.jumlah-item').forEach(function(input) {
    input.addEventListener('change', function() {
      var total = 0;
      document.querySelectorAll('.jumlah-item').forEach(function(input) {
        total += parseInt(input.value) * parseInt(input.dataset.harga);
      });
      document.querySelector('#total').innerHTML = total;
    });
  });
  document.getElementById("submit").addEventListener("click", function(){
    console.log(this.disabled)
    if(!this.disabled){
      document.getElementById("form-kasir").submit();
    }
  });
});
