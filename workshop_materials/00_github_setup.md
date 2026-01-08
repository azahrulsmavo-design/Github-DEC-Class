# Panduan Setup GitHub & Push End-to-End

Panduan ini akan menuntun kamu dari folder project lokal sampai kode live di GitHub dengan CI/CD yang berjalan.

## 1. Buat Repository Kosong di GitHub
1. Buka [github.com/new](https://github.com/new).
2. **Repository name**: `github-workflow-etl-lite` (atau nama lain yang kamu suka).
3. **Visibility**: Public (agar Actions gratis quota-nya lebih lega).
4. **Initialize this repository with**: ⚠️ **JANGAN CENTANG APAPUN**.
   - Biarkan kosong (jangan add README, .gitignore, atau License).
   - Kita ingin repo yang benar-benar bersih karena kita sudah punya file-file tersebut di lokal.
5. Klik **Create repository**.
6. Simpan URL repo kamu, misal: `https://github.com/USERNAME/github-workflow-etl-lite.git`

---

## 2. Setup Git di Lokal (Terminal VS Code)
Buka terminal di VS Code (`Ctrl + J`), pastikan kamu berada di folder `my-data-project` (atau nama folder project kamu).

Jalankan perintah berikut satu per satu:

### A. Inisialisasi Git
```bash
git init
```
*Output: Initialized empty Git repository in ...*

### B. Rename Branch Utama
GitHub sekarang menggunakan `main` sebagai default, bukan `master`.
```bash
git branch -M main
```

### C. Masukkan Semua File ke Staging
```bash
git add .
```

### D. Commit Pertama
```bash
git commit -m "feat: initial project structure (anti-ribet)"
```
*Output: [main (root-commit)] feat: initial project structure...*

---

## 3. Sambungkan ke GitHub (Remote)
Ganti `URL_REPO_KAMU` dengan link yang kamu dapat di Langkah 1.

```bash
git remote add origin https://github.com/USERNAME/github-workflow-etl-lite.git
```
*(Contoh: `git remote add origin https://github.com/azahr/github-workflow-etl-lite.git`)*

---

## 4. Push Kode ke GitHub
Sekarang kirim kode lokal ke server GitHub.

```bash
git push -u origin main
```

---

## 5. Verifikasi Otomatis Check (CI)
Setelah push berhasil:
1. Buka halaman repo kamu di GitHub.
2. Kamu akan melihat file-file kamu sudah muncul.
3. Klik tab **Actions** di bagian atas.
4. Kamu akan melihat workflow **Data Pipeline CI** sedang berjalan (kuning) atau sudah sukses (hijau).
   - Ini karena kita punya file `.github/workflows/quality_check.yml`.
   - GitHub otomatis menjalankannya setiap kali ada push ke main.

---

## Selesai! 🎉
Repo kamu sudah siap digunakan untuk webinar/demo.

### Cheat Sheet untuk Peserta Webinar Nanti
Saat webinar, alur yang dilakukan peserta adalah:
1. `git checkout -b feature/ubah-filter` (Bikin branch baru)
2. Edit file `src/etl_pipeline.py`.
3. `git add .`
4. `git commit -m "feat: update filter limit"`
5. `git push origin feature/ubah-filter`
6. Buka GitHub -> Klik **Compare & pull request**.
