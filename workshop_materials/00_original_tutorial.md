# Tutorial CI/CD dengan GitHub Actions

Panduan ini menjelaskan bagaimana "robot" otomatis (GitHub Actions) bekerja di repo ini untuk memastikan kode kita tidak error.

## 1. Apa itu CI/CD?

Dalam project sederhana ini, kita fokus pada **CI (Continuous Integration)**.
Bayangkan kamu punya asisten rajin yang melakukan ini setiap kali kamu kirim kode:
1. Download kodingan terbaru kamu.
2. Install Python.
3. Coba jalankan script `etl_pipeline.py`.
4. Lapor: "Aman bos!" (Hijau) atau "Error bos!" (Merah).

Itulah yang dilakukan oleh file `.github/workflows/quality_check.yml`.

---

## 2. Bedah Kode `quality_check.yml`

File ini ada di folder `.github/workflows/`. Mari kita bedah bahasanya:

```yaml
name: Data Pipeline CI  # Nama "Robot" nya

on:
  push:                 # Kapan dia jalan?
    branches: [ "main" ] # Setiap ada Push ke branch main
  pull_request:         # DAN setiap ada Pull Request ke main
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest  # Robotnya jalan di server Ubuntu (gratis dari GitHub)

    steps:
    - uses: actions/checkout@v3       # Step 1: Ambil kodingan kita
    
    - name: Set up Python 3.10        # Step 2: Install Python
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
        
    - name: Run ETL Pipeline          # Step 3: Jalankan script kita
      run: |
        python src/etl_pipeline.py
```

---

## 3. Cara Demo Saat Webinar (Live Action)

Ini cara paling seru untuk menunjukkan CI ke peserta:

### Skenario 1: Bikin Error (Si Merah ❌)
1. Buka file `src/etl_pipeline.py`.
2. Hapus satu tanda kurung `)` atau buat typo yang fatal (syntax error).
3. Commit dan Push.
4. Buka tab **Actions** di GitHub.
5. Tunjukkan bahwa prosesnya **Merah (Failed)**.
6. Klik detailnya, lihat log error-nya sama persis dengan di terminal lokal.
   > **Pelajaran:** "Lihat, robotnya mencegah kode error masuk ke produksi/main branch secara diam-diam."

### Skenario 2: Perbaiki Error (Si Hijau ✅)
1. Perbaiki typo tadi.
2. Commit dan Push lagi.
3. Buka tab **Actions**.
4. Tunggu sebentar... **Hijau (Success)**.
   > **Pelajaran:** "Sekarang kode kita terjamin jalan. Kita bisa tidur nyenyak."

---

## 4. Why GitHub Actions?
1. **Gratis** untuk public repo.
2. **Terintegrasi** langsung (tidak perlu daftar web lain).
3. **Standar Industri** (banyak perusahaan pakai ini).

---

## Tips Tambahan
Jika kamu mau menambahkan tes otomatis, cukup update bagian `run` di YAML menjadi:

```yaml
    - name: Run Tests
      run: |
        pip install pytest
        pytest
```

Tapi untuk "Anti-Ribet", menjalankan `python src/etl_pipeline.py` saja sudah cukup membuktikan konsep CI: **Code Must Run.**
