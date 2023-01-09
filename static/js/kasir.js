$(document).ready(function () {
  const jumlahItems = document.querySelectorAll('.jumlah-item');
  jumlahItems.forEach(function(item) {
    item.addEventListener('input', function() {
      const harga = this.dataset.harga;
      const jumlah = this.value;
      const subtotal = harga * jumlah;
      const tdSubtotal = this.parentNode.parentNode.querySelector('td.subtotal');
      tdSubtotal.innerHTML = subtotal;

      // Menjumlahkan semua subtotal
      let totalHarga = 0;
      const subtotals = document.querySelectorAll('.subtotal');
      subtotals.forEach(function(subtotal) {
        totalHarga += parseInt(subtotal.innerHTML);
      });

      console.log(totalHarga)

      // Menampilkan total harga di element #total
      document.querySelector('#total').innerHTML = totalHarga;
    });
  });
});
