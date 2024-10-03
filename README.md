# Monitoring Komputasi Paralel

Proyek ini melakukan monitoring penggunaan CPU, memori, dan GPU pada sistem selama periode waktu yang ditentukan. Data monitoring disimpan dalam file CSV dan divisualisasikan dalam bentuk grafik untuk menganalisis performa sistem secara real-time.

## Fitur Utama
- Monitoring penggunaan CPU, memori, dan GPU (jika tersedia) pada sistem.
- Penyimpanan data monitoring dalam file CSV.
- Visualisasi data dalam bentuk grafik untuk melihat penggunaan resource dalam jangka waktu tertentu (1 hingga 10 menit).
  
## Prasyarat
Pastikan Anda memiliki **Python** yang telah terinstall di sistem. Untuk memeriksa versi Python:

```bash
python --version
pip install psutil pandas matplotlib gputil
python -m ensurepip --upgrade
python -m pip install --upgrade pip setuptools
pip install wheel
python Monitoring.py

