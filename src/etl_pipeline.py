import csv
import os

# Definisi path file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'raw', 'transactions.csv')

def run_pipeline():
    print("Pipeline Started...")
    
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
 
    if os.path.exists(INPUT_FILE):
        print("File ditemukan, siap diproses.")
    else:
        print("File tidak ditemukan.")
    
    print("Pipeline Finished.")

if __name__ == "__main__":
    run_pipeline()
