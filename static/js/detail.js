$(document).ready(function() {
    $('#exampleModal').on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget) // Button that triggered the modal
      var id = button.data('transaksi-id') // Extract info from data-* attributes
      var modal = $(this)
      modal.find('.modal-footer .btn-primary').attr("href", "/kasir/ubah-status/" + id)
    })
  });