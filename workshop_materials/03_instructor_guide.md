# Instructor Guide: GitHub Workflow (Branching Edition)

**Focus**: Mengajarkan "Safe Workflow" menggunakan Branch & PR.

## 1. Preparation
(Sama seperti sebelumnya)

## 2. Minute-by-Minute Run Sheet

### Opening (00:00 - 00:15)
*   **Narrative**: "Di tim besar, kita DILARANG commit langsung ke Main. Kenapa? Karena Main = Production. Kalau error, user marah."
*   **Solution**: "Kita pakai Branch (Cabang) dan Pull Request (Proposal)."

### Phase 1: The Secure Feature (Green Flow)
*   **Step**:
    1.  Minta peserta ketik `git checkout -b feature/etl-logic`.
    2.  Jelaskan: "Kita sekarang di timeline dimensi lain. Apapun yang rusak di sini, tidak ngefek ke Main."
    3.  Implementasi Code -> Commit -> Push.
    4.  **GitHub Demo**: Tunjukkan cara Buka PR.
    5.  **Talking Point**: "Lihat centang hijau itu? Itu robot bilang 'Code ini aman untuk digabung'."
    6.  Merge.

### Phase 2: The Blocked Bug (Red-to-Green Flow)
*   **Step**:
    1.  Update Main dulu: `git checkout main` -> `git pull`. (PENTING! Banyak yang lupa ini).
    2.  Buat branch baru: `git checkout -b fix/rules`.
    3.  Buat Error (Typo) -> Commit -> Push.
    4.  **GitHub Demo**: Buka PR -> Lihat Merah.
    5.  **Talking Point**: "Bayangkan kalau tadi langsung push ke Main? Server meledak. Tapi karena di PR, tombol Merge jadi seram (atau bisa kita lock)."
    6.  Fix code -> Push lagi -> Lihat Hijau -> Merge.

### Phase 3 (Bonus): The Automated Test (Optional)
*   **Target Audience**: Peserta yang selesai duluan (The "Fast Runners").
*   **Activity**:
    1.  Minta mereka buat branch `chore/add-tests`.
    2.  Tambah step `pytest` di YAML.
    3.  Kalau berhasil, mereka akan dapat badge "CI Expert" (Virtual appreciation).
*   **Why**: Ini jembatan ke materi advanced CI/CD.

## 3. FAQ Tambahan (Branching)

**Q: Saya lupa `checkout -b`, terlanjur coding di main.**
A: Tenang. Selama belum commit, tinggal ketik `git checkout -b nama-branch` sekarang. Kodingan akan ikut pindah.

**Q: Saat `git pull` ada conflict?**
A: (Untuk pemula) Hapus folder, clone ulang. (Untuk advance) Resolve conflict di VS Code. *Di workshop ini kita hindari conflict dengan kerja di file berbeda/sequential.*

**Q: Kenapa `push -u origin ...`?**
A: Supaya Git tahu "Track" branch lokal ini ke server. Next time cukup `git push` saja.
