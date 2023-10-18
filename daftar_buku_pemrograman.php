<?php
// panggil koneksi
require_once "connection.php";


// query memanggil seluruh data
$query = "SELECT * FROM tb_buku WHERE kategori='Pemrograman'";



// jalankan query
$data = mysqli_query($conn, $query);

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="Style.css?v=<?php echo time(); ?>">
    <title>Perpustakaan Online</title>
</head>

<body>

    <div id="container">
        <div class="header">
            <h1>Perpustakaan Universitas Bumigora</h1>
        </div>
        <h4>Selamat Datang</h4>

        <div class="main">
            <div class="left">
                <h3 align="center">MENU</h3>
                <ul>
                    <li><a href="index.php">Logout</a></li>
                    <li><a href="home.php">Home</a></li>
                </ul>

                <br>

                <h3 align="center">BUKU TERPOPULER</h3>
                <ul>
                    <li><a href="daftar_buku_web_design.php">Web Design</a></li>
                    <li><a href="daftar_buku_pemrograman.php">Pemrograman</a></li>
                    <li><a href="daftar_buku_database.php">Database</a></li>
                </ul>
            </div>
        </div>

        <div class="middle2">
            <h2 align="center">DAFTAR BUKU PEMROGRAMAN</h2><br>
            <div align="center">
            </div>

            <?php
            while ($hasil = mysqli_fetch_array($data)) {
                ?>
                <div class="buku" style="margin-bottom: 10px;">
                    <div class="foto">
                        <img src="gambar_upload/<?= $hasil['gambar']; ?>">
                        <div class="judul">
                            <?= $hasil['judul']; ?>
                        </div>
                        <div class="penulis">Penulis:
                            <?= $hasil['penulis']; ?>
                        </div>
                    </div>
                </div>
            <?php } ?>
        </div>
    </div>
    <div class="footer">
        <p align="center">Copyright © 2023 - Kelompok Prikitiew</a></p>
    </div>
</body>

</html>