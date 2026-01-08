# Git Troubleshooting Cheat Sheet (Workshop Edition)

Dokumen ini berisi **16 Masalah Paling Sering Terjadi** di workshop, diurutkan dari yang paling dasar hingga masalah Git Flow.

---

## Masalah Dasar (Setup & Error Awal)

### 1. Error: `src refspec main does not match any`
**Gejala**: Saat `git push origin main`, muncul error ini.
**Penyebab**: Belum pernah **Commit** sama sekali. Git tidak bisa mengirim "angin kosong".
**Solusi**:
```bash
git add .
git commit -m "first commit"
git push origin main
```

### 2. Error: `Updates were rejected...`
**Gejala**: Push ditolak server.
**Penyebab**: Repo di GitHub sudah ada isinya (misal: README/License), tapi lokal belum punya.
**Solusi Aman Workshop**:
```bash
git pull origin main
git push origin main
```

### 3. Salah Folder / `not a git repository`
**Gejala**: `fatal: not a git repository...`
**Penyebab**: Terminal tidak berada di folder project yang sudah di-init git.
**Solusi**:
```bash
ls
cd NAMA_FOLDER_REPO
git status
```

### 4. Lupa Save File
**Gejala**: `git status` bilang "working tree clean" padahal yakin sudah edit file.
**Penyebab**: File di VS Code belum di-save (masih ada dot bulat di tab).
**Solusi**:
Tekan `Ctrl+S`, lalu cek lagi:
```bash
git status
```

---

## Masalah Saat Coding & Commit

### 5. Lupa `git add`
**Gejala**: Output commit: `nothing to commit, untracked files present`.
**Penyebab**: File baru/editan belum masuk Staging Area.
**Solusi**:
```bash
git add .
git commit -m "feat: pesan fitur"
```

### 6. Terjebak di "Vim" (Editor Layar Hitam)
**Gejala**: Layar hitam, ada tulisan `Please enter a commit message...`, tidak bisa keluar.
**Penyebab**: Lupa ketik `-m` saat commit atau sedang merge otomatis.
**Solusi**:
1. Ketik `:q!` lalu `Enter` (Keluar paksa).
2. Ulangi commit dengan benar: `git commit -m "pesan"`

### 7. "LF will be replaced by CRLF"
**Gejala**: Warning banyak baris saat `git add`.
**Penyebab**: Beda format baris baru Windows vs Linux/Mac.
**Solusi**: **Abaikan saja**. Ini normal di Windows dan tidak merusak kode.

### 8. `nothing added to commit` tapi sudah `git add .`
**Gejala**: File tetap tidak mau masuk staging.
**Penyebab**: File tersebut mungkin terdaftar di `.gitignore`.
**Solusi**: Cek isi file `.gitignore`.

---

## Masalah Push & Pull Request

### 9. Permission Denied (403)
**Gejala**: `remote: Permission to ... denied` atau error 403.
**Penyebab**: Repo bukan milikmu atau salah akun GitHub yang login di laptop.
**Solusi**:
*   Cek remote URL: `git remote -v`
*   Login ulang via browser/Credential Manager bila diminta.

### 10. Salah Branch (Push ke Main padahal harus Feature)
**Gejala**: PR tidak muncul, atau codingan masuk ke tempat yang salah.
**Penyebab**: Lupa `checkout -b`.
**Solusi**:
```bash
git branch
git checkout -b feature/nama-task-benar
git push -u origin feature/nama-task-benar
```

### 11. PR Tidak Muncul Tombol
**Gejala**: Sudah push, tapi tidak ada prompt "Compare & pull request" di GitHub.
**Penyebab**: Push ke branch yang salah atau belum push sama sekali.
**Solusi**:
Cek branch saat ini dan push eksplisit:
```bash
git branch
git push -u origin NAMA_BRANCH_AKTIF
```
Atau buat PR manual via Menu **Pull requests** > **New pull request**.

### 12. Salah Branch (`Detached HEAD`)
**Gejala**: `git status` bilang `HEAD detached at...`.
**Solusi**:
```bash
git checkout main
```

### 13. Merge Conflict
**Gejala**: `CONFLICT (content)` saat pull/merge.
**Solusi Singkat**:
1. Buka file yang merah/conflict di VS Code.
2. Pilih "Accept Current Change" atau "Accept Incoming".
3. Simpan.
4. `git add .` -> `git commit -m "fix: resolve conflict"`.

---

## Masalah Account & Config (Advanced)

### 14. Error: Support for password authentication was removed
**Gejala**: Saat git push, diminta password, tapi setelah diisi password GitHub yang benar tetap gagal/error 403.
**Penyebab**: GitHub sudah tidak menerima password akun. Harus pakai Personal Access Token (PAT).
**Solusi**:
1. Generate token di GitHub (Settings > Developer Settings > Personal Access Tokens).
2. Saat diminta password di terminal, masukkan Token tersebut, bukan password akun.

### 15. Masalah "Email Privacy" (Push Rejected)
**Gejala**: `remote: error: GH007: Your push would publish a private email address.`
**Penyebab**: Peserta mencentang "Keep my email addresses private" di settings GitHub, tapi git di laptop pakai email asli.
**Solusi**:
Ketik ini di terminal (pakai email dummy dari GitHub settings):
```bash
git config user.email "ID+username@users.noreply.github.com"
git commit --amend --reset-author --no-edit
git push
```

### 16. Salah Folder (Repo di dalam Repo)
**Gejala**: Folder project di GitHub muncul sebagai ikon folder warna abu-abu dan tidak bisa diklik (Submodule yang tidak sengaja).
**Penyebab**: Peserta melakukan `git init` di dalam folder yang sudah ada folder `.git`-nya (nested repository).
**Solusi**:
1. Hapus folder `.git` yang salah (paling dalam).
2. `git rm --cached folder_nama -f`
3. `git add .` lalu commit ulang.

---

## The 4 Command Penyelamat

Kalau panik dan bingung "Saya ada dimana?" atau "Codingan saya hancur!":

1.  `git status` (Lihat kondisi file)
2.  `git branch` (Lihat lagi di jalan/branch mana)
3.  `git log --oneline -5` (Lihat history terakhir)
4.  `git restore .` (**The Last Resort**: Undo all changes that are not committed)
