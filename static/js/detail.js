$(document).ready(function() {
    // get element tombol bayar
    const bayarBtn = document.querySelector('#submit');

    if(bayarBtn != null)
    {
        // tambahkan event listener pada tombol bayar
        bayarBtn.addEventListener('click', function() {
            document.querySelector('#myModal').style.display = 'block';
        });
    }

    const closeBtn = document.querySelector('.close'); // atau tombol batal

    closeBtn.addEventListener('click', function() {
        document.getElementById('myModal').style.display = "none";
    });

    const closeBtn2 = document.querySelector('#batal'); // atau tombol batal

    closeBtn2.addEventListener('click', function() {
        document.getElementById('myModal').style.display = "none";
    });

    const bayarBtn2 = document.querySelector('#bayar-btn'); // atau tombol batal

    bayarBtn2.addEventListener('click', function() {
        var currentUrl = window.location.href; // mendapatkan url saat ini
        var splitUrl = currentUrl.split("/"); // memisahkan url berdasarkan "/"
        var id = splitUrl[splitUrl.length - 1]; // ambil elemen terakhir dari array yang dihasilkan dari splitUrl, yang merupakan id
        window.location.href = `/kasir/ubah-status/` + id;
    });

    const closeBtn3 = document.querySelector('#batal2'); // atau tombol batal

    closeBtn3.addEventListener('click', function() {
        document.getElementById('myModal2').style.display = "none";
    });

    const closeBtn4 = document.querySelector('#batal3'); // atau tombol batal

    closeBtn4.addEventListener('click', function() {
        document.getElementById('myModal2').style.display = "none";
    });

    const hapusBtn = document.querySelector('#hps-btn');
    hapusBtn.addEventListener('click', function() {
        document.querySelector('#myModal2').style.display = 'block';
    });

    const hapusBtn2 = document.querySelector('#hapus-btn');
    hapusBtn2.addEventListener('click', function() {
        var currentUrl = window.location.href; // mendapatkan url saat ini
        var splitUrl = currentUrl.split("/"); // memisahkan url berdasarkan "/"
        var id = splitUrl[splitUrl.length - 1]; // ambil elemen terakhir dari array yang dihasilkan dari splitUrl, yang merupakan id
        window.location.href = `/kasir/hapus/` + id;
    });
});