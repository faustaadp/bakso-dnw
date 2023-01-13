$(document).ready(function() {
  // Menjumlahkan semua subtotal dan menampilkan di element #total
  function updateTotalHarga() {
    let totalHarga = 0;
    let jumlahItems = document.querySelectorAll('.jumlah-item');
    // Saya ingin for loop setiap item dan mengambil harga dan jumlah, lalu totalHarga += harga * jumlah
    jumlahItems.forEach(item => {
      let harga = item.getAttribute('data-harga');
      let jumlah = item.value;
      totalHarga += harga * jumlah;
    });
    document.querySelector('#total').innerHTML = totalHarga;
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
});
