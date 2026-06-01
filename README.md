# PacCommerce: Customer Membership System

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

PacCommerce adalah sistem manajemen dan prediksi tingkatan (*tier*) membership pelanggan berbasis e-commerce. Sistem ini menggunakan pendekatan **Machine Learning sederhana (K-Nearest Neighbors konsep dasar)** dengan menghitung **Euclidean Distance** untuk mengkategorikan pelanggan ke dalam tiga tingkatan: *Silver*, *Gold*, atau *Platinum* berdasarkan profil keuangan bulanan mereka.

## 🚀 Fitur Utama
- **Otomatisasi Data**: Pengelolaan basis data berbasis file JSON secara dinamis tanpa intervensi manual.
- **Prediksi Akurat**: Menggunakan rumus kalkulasi jarak matematis terdekat (*Euclidean*) untuk menentukan kriteria tier pelanggan.
- **Kalkulator Diskon**: Perhitungan otomatis potongan harga belanjaan yang disesuaikan dengan keuntungan (*benefit*) masing-masing tingkatan member.
- **Arsitektur Modular**: Pemisahan komponen kode yang bersih antara data (*Persistence Layer*), logika bisnis (*Business Logic*), dan eksekusi utama (*Entry Point*).

---

## 📁 Struktur Project
```text
paccommerce/
│
├── data/
│   └── users.json         # Basis data tiruan (Mock Database) berbasis JSON
│
├── src/
│   ├── database.py       # Pengelola fungsi CRUD (Read/Write JSON)
│   └── membership.py     # Logika bisnis utama & kalkulasi Euclidean Distance
│
├── .gitignore            # Proteksi berkas lokal/sampah agar tidak terunggah ke Git
├── main.py               # File eksekusi utama (Automated Demo Runner)
└── requirements.txt      # Daftar dependencies library pihak ketiga