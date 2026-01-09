# Mini PHP Compiler

Mini PHP Compiler adalah compiler/interpreter PHP sederhana yang dibuat untuk tujuan pembelajaran. Proyek ini mensimulasikan proses dasar **lexing, parsing, dan eksekusi** dengan cakupan fitur yang terbatas.

## Fitur yang Didukung
Mini compiler ini mampu menjalankan subset bahasa PHP berikut:

- Deklarasi dan penggunaan **variabel**
- Operasi **aritmatika** (`+`, `-`, `*`, `/`, `%`)
- Operasi **penggabungan string** (`.`)
- **Assignment** dan compound assignment (`=`, `+=`, `-=`, dll)
- **Perbandingan nilai** (`!=`, `>=`, `<=`)
- Struktur kontrol:
  - `if – else`
  - `while`
  - `for`
- Output ke layar menggunakan:
  - `echo`
  - `print`
- Penanganan **string, integer, dan float**
- Dukungan **komentar** dalam kode
- Blok kode menggunakan `{}` dan statement dengan `;`

## Contoh Kode
```php
<?php
$a = 10;
$b = 5;

if ($x >= $y) {
    echo "a lebih besar";
}
?>
