import csv
import os

# Definisi path file (supaya aman dijalankan dari root folder manapun)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'raw', 'transactions.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'processed', 'clean_sales.csv')

def run_pipeline():
    print("Memulai ETL Pipeline sederhana...")
    
    processed_data = []
    
    # 1. EXTRACT
    try:
        with open(INPUT_FILE, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            print(f"Membaca data dari: {INPUT_FILE}")
            
            # 2. TRANSFORM
            for row in reader:
                # Membersihkan nama produk menjadi HURUF BESAR
                clean_product = row['product'].strip().upper()
                
                # Mengubah amount menjadi integer
                amount = int(row['amount'])
                
                # Filter: Hanya ambil transaksi di atas 20 USD
                if amount > 20:
                    processed_data.append({
                        'id': row['id'],
                        'product': clean_product,
                        'amount': amount,
                        'currency': row['currency']
                    })
                    
    except FileNotFoundError:
        print("Error: File input tidak ditemukan!")
        return

    # 3. LOAD
    try:
        # Pastikan folder output ada
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        
        with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['id', 'product', 'amount', 'currency']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(processed_data)
            
        print(f"Sukses! Data tersimpan di: {OUTPUT_FILE}")
        print(f"Total baris data tersimpan: {len(processed_data)}")
        
    except Exception as e:
        print(f"Error saat menyimpan data: {e}")

if __name__ == "__main__":
    run_pipeline()
