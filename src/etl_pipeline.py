import os

# Definisi path file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'raw', 'transactions.csv')

def run_pipeline():
    print("Pipeline Started...")
    
    # TODO: Peserta akan mengisi logika di sini nanti (Feat 1)
    
    if os.path.exists(INPUT_FILE):
        print("File ditemukan, siap diproses.")
    else:
        print("File tidak ditemukan.")
    
    print("Pipeline Finished.")

if __name__ == "__main__":
    run_pipeline()
