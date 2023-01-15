$(document).ready(function() {
    document.getElementById("submit").addEventListener("click", function(){
        var currentUrl = window.location.href; // mendapatkan url saat ini
        var splitUrl = currentUrl.split("/"); // memisahkan url berdasarkan "/"
        var id = splitUrl[splitUrl.length - 1]; // ambil elemen terakhir dari array yang dihasilkan dari splitUrl, yang merupakan id
        window.location.href = `/kasir/ubah-status/` + id;
    });
});