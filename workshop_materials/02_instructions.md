# Workshop Instructions: Data Engineering Lite (Branching Edition)

**Cheat Sheet** untuk pengerjaan tugas menggunakan teknik **Branching** dan **Pull Request**.

## Task 1: New Feature (Green Flow)

**Objective**: Bekerja isolasi di branch baru, lalu Merge jika CI Hijau.

1.  **Create Branch**:
    ```bash
    git checkout -b feature/etl-logic
    ```

2.  **Coding**:
    Buka `src/etl_pipeline.py` dan implementasikan logika ETL (copy-paste kode yang sudah disiapkan).

3.  **Commit & Push**:
    ```bash
    git add src/etl_pipeline.py
    git commit -m "feat: implement csv aggregation logic"
    git push -u origin feature/etl-logic
    ```

4.  **GitHub Action**:
    *   Buka Repository di GitHub.
    *   Klik **Compare & pull request** (Tombol hijau yang muncul).
    *   Pastikan base: `main` <- compare: `feature/etl-logic`.
    *   Klik **Create pull request**.
    *   Tunggu **Checks** selesai (Harus Hijau).
    *   Klik **Merge pull request** -> **Confirm merge**.

---

## Task 2: Bug Fix (Red-to-Green Flow)

**Objective**: Menghadapi error di branch terpisah, perbaiki, lalu Merge.

1.  **Preparation**:
    Pindah ke main dan update (biar sinkron), lalu buat branch baru.
    ```bash
    git checkout main
    git pull origin main
    git checkout -b fix/currency-validation
    ```

2.  **Simulate Bug**:
    Ubah kode di `src/etl_pipeline.py` agar error (misal: Typo `row['amounts']`).

3.  **Commit "Dirty" Code**:
    ```bash
    git add src/etl_pipeline.py
    git commit -m "chore: update validation rules"
    git push -u origin fix/currency-validation
    ```

4.  **Observe Failure**:
    *   Buat Pull Request di GitHub.
    *   Lihat **Checks** (CI) berubah **MERAH (Failed)**.
    *   *Jangan di-merge dulu!*

5.  **Fix It**:
    Kembali ke VS Code, perbaiki typo menjadi `row['amount']`.

6.  **Push Fix**:
    ```bash
    git add src/etl_pipeline.py
    git commit -m "fix: resolve typo in currency field"
    git push
    ```

7.  **Success**:
    *   Cek kembali PR tadi.
    *   Tunggu **Checks** berubah **HIJAU (Passed)**.
    *   Klik **Merge pull request**.

## Task 3: Automated Testing (Optional / Bonus)

**Objective**: Memodifikasi "Robot" CI/CD agar menjalankan Unit Tests.

1.  **Branch**:
    ```bash
    git checkout main
    git pull
    git checkout -b chore/add-tests
    ```

2.  **Create Test File**:
    Buat file baru `tests/test_pipeline.py`:
    ```python
    import pytest
    
    def test_basic_math():
        assert 1 + 1 == 2
        
    def test_pipeline_import():
        from src.etl_pipeline import run_pipeline
        assert callable(run_pipeline)
    ```

3.  **Update CI Workflow**:
    Edit `.github/workflows/quality_check.yml`. Tambahkan di bagian `steps`:
    
    ```yaml
    # ... (setelah step Run ETL Pipeline)
    
    - name: Install Testing Tools
      run: pip install pytest
      
    - name: Run Unit Tests
      run: pytest
    ```

4.  **Push & Verify**:
    ```bash
    git add .
    git commit -m "chore: add pytest and update workflow"
    git push -u origin chore/add-tests
    ```
    *   Buka Pull Request.
    *   Lihat di tab **Checks**, sekarang ada step "Run Unit Tests".

---

## Git Command Cheat Sheet

| Action | Command |
| :--- | :--- |
| **New Branch** | `git checkout -b <branch-name>` |
| **Check Status** | `git status` |
| **Stage Files** | `git add <file>` |
| **Commit** | `git commit -m "type: message"` |
| **First Push** | `git push -u origin <branch-name>` |
| **Next Push** | `git push` |
| **Switch Branch**| `git checkout <branch-name>` |
| **Update Main** | `git checkout main` -> `git pull` |
