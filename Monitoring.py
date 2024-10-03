import psutil
import time
import pandas as pd
import matplotlib.pyplot as plt
import GPUtil

# Fungsi untuk mendapatkan penggunaan CPU, memori, dan GPU
def get_system_usage():
    cpu_usage = psutil.cpu_percent(interval=1)  # Persentase penggunaan CPU
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent  # Persentase penggunaan memori

    # Dapatkan informasi GPU jika tersedia
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu_usage = gpus[0].load * 100  # Ambil GPU pertama dan konversi ke persentase
    else:
        gpu_usage = None  # Jika tidak ada GPU

    return cpu_usage, memory_usage, gpu_usage

# List untuk menyimpan data
data = []

# Monitoring sistem selama beberapa menit (misalnya 10 menit)
monitor_duration = 1 * 30  # durasi dalam detik (10 menit)
interval = 2  # interval pengambilan data dalam detik

print("Memulai monitoring...")
start_time = time.time()

# Loop untuk monitoring
while (time.time() - start_time) < monitor_duration:
    cpu, memory, gpu = get_system_usage()
    runtime = (time.time() - start_time) / 60  # Menghitung runtime dalam menit
    data.append([runtime, cpu, memory, gpu])
    if gpu is not None:
        print(f"Runtime: {runtime:.2f} menit, CPU: {cpu}%, Memory: {memory}%, GPU: {gpu}%")
    else:
        print(f"Runtime: {runtime:.2f} menit, CPU: {cpu}%, Memory: {memory}%, GPU: Not Available")
    time.sleep(interval)

# Simpan data ke file CSV
df = pd.DataFrame(data, columns=["Runtime (minutes)", "CPU Usage (%)", "Memory Usage (%)", "GPU Usage (%)"])
csv_file = "system_usage_with_gpu_runtime.csv"
df.to_csv(csv_file, index=False)

print(f"Data monitoring disimpan ke {csv_file}")

# Membaca data dari CSV dan membuat grafik
df = pd.read_csv(csv_file)

# Membuat plot CPU, Memory, dan GPU Usage
plt.figure(figsize=(10, 6))

plt.plot(df['Runtime (minutes)'], df['CPU Usage (%)'], label='CPU Usage (%)', color='b', marker='o')
plt.plot(df['Runtime (minutes)'], df['Memory Usage (%)'], label='Memory Usage (%)', color='g', marker='x')

if 'GPU Usage (%)' in df and df['GPU Usage (%)'].notnull().any():
    plt.plot(df['Runtime (minutes)'], df['GPU Usage (%)'], label='GPU Usage (%)', color='r', marker='s')

plt.xlabel('Runtime (minutes)')
plt.ylabel('Usage (%)')
plt.title('CPU, Memory, and GPU Usage Over Time')
plt.xticks(rotation=45, ha='right')
plt.legend()

plt.tight_layout()
plt.show()
