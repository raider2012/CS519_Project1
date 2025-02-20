import matplotlib.pyplot as plt
import numpy as np

# Benchmark data (same as before)
data = [
    {"buffer_size": 256, "iterations": 10, "total_time": 52983, "avg_latency": 5298.30},
    {"buffer_size": 256, "iterations": 50, "total_time": 110798, "avg_latency": 2215.96},
    {"buffer_size": 256, "iterations": 100, "total_time": 212270, "avg_latency": 2122.70},
    {"buffer_size": 256, "iterations": 500, "total_time": 1040877, "avg_latency": 2081.75},
    {"buffer_size": 256, "iterations": 1000, "total_time": 2169747, "avg_latency": 2169.75},
    {"buffer_size": 512, "iterations": 10, "total_time": 25477, "avg_latency": 2547.70},
    {"buffer_size": 512, "iterations": 50, "total_time": 121947, "avg_latency": 2438.94},
    {"buffer_size": 512, "iterations": 100, "total_time": 226997, "avg_latency": 2269.97},
    {"buffer_size": 512, "iterations": 500, "total_time": 1034733, "avg_latency": 2069.47},
    {"buffer_size": 512, "iterations": 1000, "total_time": 2120861, "avg_latency": 2120.86},
    {"buffer_size": 1024, "iterations": 10, "total_time": 25614, "avg_latency": 2561.40},
    {"buffer_size": 1024, "iterations": 50, "total_time": 114529, "avg_latency": 2290.58},
    {"buffer_size": 1024, "iterations": 100, "total_time": 213834, "avg_latency": 2138.34},
    {"buffer_size": 1024, "iterations": 500, "total_time": 1118462, "avg_latency": 2236.92},
    {"buffer_size": 1024, "iterations": 1000, "total_time": 2208484, "avg_latency": 2208.48},
    {"buffer_size": 2048, "iterations": 10, "total_time": 26079, "avg_latency": 2607.90},
    {"buffer_size": 2048, "iterations": 50, "total_time": 112288, "avg_latency": 2245.76},
    {"buffer_size": 2048, "iterations": 100, "total_time": 226756, "avg_latency": 2267.56},
    {"buffer_size": 2048, "iterations": 500, "total_time": 1174539, "avg_latency": 2349.08},
    {"buffer_size": 2048, "iterations": 1000, "total_time": 2563208, "avg_latency": 2563.21},
    {"buffer_size": 4096, "iterations": 10, "total_time": 30453, "avg_latency": 3045.30},
    {"buffer_size": 4096, "iterations": 50, "total_time": 127318, "avg_latency": 2546.36},
    {"buffer_size": 4096, "iterations": 100, "total_time": 250048, "avg_latency": 2500.48},
    {"buffer_size": 4096, "iterations": 500, "total_time": 1247536, "avg_latency": 2495.07},
    {"buffer_size": 4096, "iterations": 1000, "total_time": 2571484, "avg_latency": 2571.48},
    {"buffer_size": 8192, "iterations": 10, "total_time": 33127, "avg_latency": 3312.70},
    {"buffer_size": 8192, "iterations": 50, "total_time": 146639, "avg_latency": 2932.78},
    {"buffer_size": 8192, "iterations": 100, "total_time": 269981, "avg_latency": 2699.81},
    {"buffer_size": 8192, "iterations": 500, "total_time": 1383910, "avg_latency": 2767.82},
    {"buffer_size": 8192, "iterations": 1000, "total_time": 2771766, "avg_latency": 2771.77},
    {"buffer_size": 16384, "iterations": 10, "total_time": 51221, "avg_latency": 5122.10},
    {"buffer_size": 16384, "iterations": 50, "total_time": 189922, "avg_latency": 3798.44},
    {"buffer_size": 16384, "iterations": 100, "total_time": 381787, "avg_latency": 3817.87},
    {"buffer_size": 16384, "iterations": 500, "total_time": 1864823, "avg_latency": 3729.65},
    {"buffer_size": 16384, "iterations": 1000, "total_time": 3929463, "avg_latency": 3929.46},
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
    total_time_data[d["iterations"]].append(d["total_time"] / 1e6)  # Convert to milliseconds
    avg_latency_data[d["iterations"]].append(d["avg_latency"] / 1e3)  # Convert to microseconds

# Plot 1: Total Time vs. Buffer Size for Different Iterations
plt.figure(figsize=(12, 6))
for it in iterations:
    plt.plot(x_positions, total_time_data[it], marker='o', label=f"Iterations={it}")

plt.title("Total Time vs. Buffer Size for Different Iterations")
plt.xlabel("Buffer Size (bytes)")
plt.ylabel("Total Time (ms)")
plt.xticks(x_positions, buffer_sizes)  # Replace x-axis ticks with buffer sizes
plt.grid(True)
plt.legend()
plt.show()

# Plot 2: Average Latency per Call vs. Buffer Size for Different Iterations
plt.figure(figsize=(12, 6))
for it in iterations:
    plt.plot(x_positions, avg_latency_data[it], marker='o', label=f"Iterations={it}")

plt.title("Average Latency per Call vs. Buffer Size for Different Iterations")
plt.xlabel("Buffer Size (bytes)")
plt.ylabel("Average Latency (µs)")
plt.xticks(x_positions, buffer_sizes)  # Replace x-axis ticks with buffer sizes
plt.grid(True)
plt.legend()
plt.show()
