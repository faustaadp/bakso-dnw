const cards = document.querySelectorAll('.card');

cards.forEach(card => {
    card.addEventListener('click', (event) => {
        // Mendapatkan id transaksi dari data attribute
        const transaksiId = card.getAttribute('data-transaksi-id');
        // Redirect ke halaman detail transaksi dengan id transaksi yang didapat
        window.location.href = `/kasir/detail/${transaksiId}`;
    });
});