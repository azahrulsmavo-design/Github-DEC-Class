# Rancangan Project: Listener Workshop (Branching Edition)

Ini adalah versi workshop dengan standar **Professional Workflow**. Kita tidak lagi commit langsung ke `main`, melainkan menggunakan teknik **Branching** & **Pull Request (PR)**.

## 1. Persiapan (Template Provided)
*   Sama seperti sebelumnya (Template start).
*   **Tamabahan**: Branch protection rule (optional, untuk mencegah push to main langsung) - *Instructor Note*.

## 2. Alur Pengerjaan (Scenario)

### Scenario 1: The New Feature (Green Flow)
**Story**: Anda diminta membuat fitur ETL baru, tapi tidak boleh mengganggu code yang ada di `main`.
1.  **Branch**: `feature/etl-logic`
2.  **Action**: Implementasi kode Python yang valid.
3.  **Commit**: `feat: implement aggregation logic`
4.  **Flow**: Push -> **Create Pull Request** -> CI Checks (Green) -> **Merge**.

### Scenario 2: The Bug & The Fix (Red-to-Green Flow)
**Story**: Ada kebutuhan update modul (misal: validasi currency). Anda membuat branch baru, tapi tidak sengaja membuat typo.
1.  **Branch**: `fix/currency-validation`
2.  **Action (Bug)**: Sengaja buat typo (`row['amounts']`).
3.  **Commit**: `chore: update validation rules` (Ternyata error).
4.  **Flow**: Push -> **Create Pull Request** -> CI Checks (**RED/Failed**).
    *   *System prevents dirty code entering main!*
5.  **Action (Fix)**: Perbaiki typo (`row['amount']`).
6.  **Commit**: `fix: resolve typo in currency field`.
7.  **Flow**: Push lagi -> CI Checks (**GREEN**) -> **Merge**.

### Scenario 3: The CI Expert (Optional / Bonus)
**Story**: Pipeline saat ini hanya menjalankan script. Kita ingin memastikan kualitas kode dengan **Automated Tests**.
1.  **Branch**: `chore/add-tests`
2.  **Action**: 
    - Buat unit test sederhana.
    - Edit file YAML `.github/workflows/quality_check.yml` untuk menjalankan `pytest`.
3.  **Flow**: Push -> PR -> Lihat "Run Tests" di Actions log -> Merge.

## 3. Komponen Template

Kita perlu menyiapkan repository "Starter" dengan isi sebagai berikut:

**A. `.github/workflows/quality_check.yml`**
(Sudah ada, siap pakai)

**B. `src/etl_pipeline.py` (Starter Code)**
Berisi kode minimal agar tidak error saat pertama kali dijalankan.
```python
import pandas as pd

def run_pipeline():
    print("Pipeline started...")
    # TODO: Implement ETL logic here
    print("Pipeline finished.")

if __name__ == "__main__":
    run_pipeline()
```

**C. `requirements.txt`**
```text
pandas
pytest
```

## 4. Kelebihan Pendekatan Ini
1.  **Low Barrier**: Peserta tidak pusing setup `.gitignore` atau YAML indentation.
2.  **Quick Win**: Dalam 10 menit pertama peserta sudah melihat "Action Hijau" di GitHub mereka.
3.  **Focus**: 100% fokus di Python logic dan Git Flow (Commit/Push), bukan konfigurasi tools.
4.  **Tidy History**: Commit log peserta bersih, hanya berisi hal yang bermakna (`feat` fun, `fix` fun).
