import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Benchmark data (modified as per OUTPUT_NODMESG.txt)
data = [
    {"buffer_size": 256, "iterations": 10, "total_time": 26181, "avg_latency": 2618.10},
    {"buffer_size": 256, "iterations": 50, "total_time": 58314, "avg_latency": 1166.28},
    {"buffer_size": 256, "iterations": 100, "total_time": 241097, "avg_latency": 2410.97},
    {"buffer_size": 256, "iterations": 500, "total_time": 576266, "avg_latency": 1152.53},
    {"buffer_size": 256, "iterations": 1000, "total_time": 1140540, "avg_latency": 1140.54},
    {"buffer_size": 256, "iterations": 5000, "total_time": 5663330, "avg_latency": 1132.67},
    {"buffer_size": 256, "iterations": 10000, "total_time": 10744844, "avg_latency": 1074.48},
    {"buffer_size": 512, "iterations": 10, "total_time": 11587, "avg_latency": 1158.70},
    {"buffer_size": 512, "iterations": 50, "total_time": 53148, "avg_latency": 1062.96},
    {"buffer_size": 512, "iterations": 100, "total_time": 104730, "avg_latency": 1047.30},
    {"buffer_size": 512, "iterations": 500, "total_time": 519217, "avg_latency": 1038.43},
    {"buffer_size": 512, "iterations": 1000, "total_time": 1050159, "avg_latency": 1050.16},
    {"buffer_size": 512, "iterations": 5000, "total_time": 5221508, "avg_latency": 1044.30},
    {"buffer_size": 512, "iterations": 10000, "total_time": 10369536, "avg_latency": 1036.95},
    {"buffer_size": 1024, "iterations": 10, "total_time": 11609, "avg_latency": 1160.90},
    {"buffer_size": 1024, "iterations": 50, "total_time": 53748, "avg_latency": 1074.96},
    {"buffer_size": 1024, "iterations": 100, "total_time": 106103, "avg_latency": 1061.03},
    {"buffer_size": 1024, "iterations": 500, "total_time": 527180, "avg_latency": 1054.36},
    {"buffer_size": 1024, "iterations": 1000, "total_time": 1061757, "avg_latency": 1061.76},
    {"buffer_size": 1024, "iterations": 5000, "total_time": 5265286, "avg_latency": 1053.06},
    {"buffer_size": 1024, "iterations": 10000, "total_time": 12157886, "avg_latency": 1215.79},
    {"buffer_size": 2048, "iterations": 10, "total_time": 11882, "avg_latency": 1188.20},
    {"buffer_size": 2048, "iterations": 50, "total_time": 53756, "avg_latency": 1075.12},
    {"buffer_size": 2048, "iterations": 100, "total_time": 106468, "avg_latency": 1064.68},
    {"buffer_size": 2048, "iterations": 500, "total_time": 528434, "avg_latency": 1056.87},
    {"buffer_size": 2048, "iterations": 1000, "total_time": 1053971, "avg_latency": 1053.97},
    {"buffer_size": 2048, "iterations": 5000, "total_time": 5268239, "avg_latency": 1053.65},
    {"buffer_size": 2048, "iterations": 10000, "total_time": 10550813, "avg_latency": 1055.08},
    {"buffer_size": 4096, "iterations": 10, "total_time": 13403, "avg_latency": 1340.30},
    {"buffer_size": 4096, "iterations": 50, "total_time": 60443, "avg_latency": 1208.86},
    {"buffer_size": 4096, "iterations": 100, "total_time": 119489, "avg_latency": 1194.89},
    {"buffer_size": 4096, "iterations": 500, "total_time": 592199, "avg_latency": 1184.40},
    {"buffer_size": 4096, "iterations": 1000, "total_time": 1202368, "avg_latency": 1202.37},
    {"buffer_size": 4096, "iterations": 5000, "total_time": 5940212, "avg_latency": 1188.04},
    {"buffer_size": 4096, "iterations": 10000, "total_time": 11864954, "avg_latency": 1186.50},
    {"buffer_size": 8192, "iterations": 10, "total_time": 16673, "avg_latency": 1667.30},
    {"buffer_size": 8192, "iterations": 50, "total_time": 73945, "avg_latency": 1478.90},
    {"buffer_size": 8192, "iterations": 100, "total_time": 146370, "avg_latency": 1463.70},
    {"buffer_size": 8192, "iterations": 500, "total_time": 725402, "avg_latency": 1450.80},
    {"buffer_size": 8192, "iterations": 1000, "total_time": 1450186, "avg_latency": 1450.19},
    {"buffer_size": 8192, "iterations": 5000, "total_time": 7287022, "avg_latency": 1457.40},
    {"buffer_size": 8192, "iterations": 10000, "total_time": 14495673, "avg_latency": 1449.57},
    {"buffer_size": 16384, "iterations": 10, "total_time": 32227, "avg_latency": 3222.70},
    {"buffer_size": 16384, "iterations": 50, "total_time": 133612, "avg_latency": 2672.24},
    {"buffer_size": 16384, "iterations": 100, "total_time": 244214, "avg_latency": 2442.14},
    {"buffer_size": 16384, "iterations": 500, "total_time": 1203000, "avg_latency": 2406.00},
    {"buffer_size": 16384, "iterations": 1000, "total_time": 2404327, "avg_latency": 2404.33},
    {"buffer_size": 16384, "iterations": 5000, "total_time": 11892815, "avg_latency": 2378.56},
    {"buffer_size": 16384, "iterations": 10000, "total_time": 24940175, "avg_latency": 2494.02},
    {"buffer_size": 2097152, "iterations": 10, "total_time": 6471968, "avg_latency": 647196.80},
    {"buffer_size": 2097152, "iterations": 50, "total_time": 32361627, "avg_latency": 647232.54},
    {"buffer_size": 2097152, "iterations": 100, "total_time": 65496447, "avg_latency": 654964.47},
    {"buffer_size": 2097152, "iterations": 500, "total_time": 292565775, "avg_latency": 585131.55},
    {"buffer_size": 2097152, "iterations": 1000, "total_time": 510974904, "avg_latency": 510974.90},
    {"buffer_size": 2097152, "iterations": 5000, "total_time": 2534647040, "avg_latency": 506929.41},
    {"buffer_size": 2097152, "iterations": 10000, "total_time": 5223332715, "avg_latency": 522333.27},
]

# Extract unique buffer sizes and iterations
buffer_sizes = sorted(list(set(d["buffer_size"] for d in data)))
iterations = sorted(list(set(d["iterations"] for d in data)))

# Create an index array for constant spacing
x_positions = np.arange(len(buffer_sizes))

# Organize data for plotting
total_time_data = {it: [] for it in iterations}
avg_latency_data = {it: [] for it in iterations}

for d in data:
    # Convert nanoseconds -> milliseconds for total_time
    total_time_data[d["iterations"]].append(d["total_time"] / 1e6)
    # Convert nanoseconds -> microseconds for avg_latency
    avg_latency_data[d["iterations"]].append(d["avg_latency"] / 1e3)

# --- PLOT 1: Total Time vs. Buffer Size ---
plt.figure(figsize=(12, 6))
for it in iterations:
    plt.plot(x_positions, total_time_data[it], marker='o', label=f"Iterations={it}")

plt.title("Total Time vs. Buffer Size for Different Iterations")
plt.xlabel("Buffer Size (bytes)")
plt.ylabel("Total Time (ms)")
plt.xticks(x_positions, buffer_sizes)
ax1 = plt.gca()

# Set y-axis to log scale for better visibility across large ranges
ax1.set_yscale('log')

# Optional: add more frequent grid lines
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.legend()
plt.show()

# --- PLOT 2: Average Latency per Call vs. Buffer Size ---
plt.figure(figsize=(12, 6))
for it in iterations:
    plt.plot(x_positions, avg_latency_data[it], marker='o', label=f"Iterations={it}")

plt.title("Average Latency per Call vs. Buffer Size for Different Iterations")
plt.xlabel("Buffer Size (bytes)")
plt.ylabel("Average Latency (µs)")
plt.xticks(x_positions, buffer_sizes)
ax2 = plt.gca()

# Again, use a log scale for the y-axis
ax2.set_yscale('log')
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.legend()
plt.show()
