import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

# Create directory for figures
import os
if not os.path.exists('figures'):
    os.makedirs('figures')

# Figure 1: CPU Frequency Impact
def create_cpu_frequency_figure():
    frequencies = np.array([1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 3.6])
    
    # Different scaling for different optimizations
    no_opt = 2.5 * frequencies
    tso_gro = 7 * frequencies**0.8
    jumbo = 7.5 * frequencies**0.9
    all_opt = 12 * frequencies**0.7
    
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies, no_opt, 'o-', label='No Optimizations')
    plt.plot(frequencies, tso_gro, 's-', label='TSO/GRO')
    plt.plot(frequencies, jumbo, '^-', label='Jumbo Frames')
    plt.plot(frequencies, all_opt, 'D-', label='All Optimizations')
    
    plt.xlabel('CPU Frequency (GHz)')
    plt.ylabel('Throughput (Gbps)')
    plt.title('Impact of CPU Frequency on Network Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    plt.savefig('cpu_frequency_impact.png', dpi=300)
    plt.close()

# Figure 2: Interrupt Coalescing
def create_interrupt_coalescing_figure():
    coalescing = np.array([0, 50, 100, 150, 200, 250])
    
    # Throughput increases with coalescing but plateaus
    throughput = 20 * (1 - np.exp(-0.015 * coalescing))
    
    # Latency increases with coalescing
    latency = 0.1 + 0.002 * coalescing
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    color = 'tab:blue'
    ax1.set_xlabel('Interrupt Coalescing (μs)')
    ax1.set_ylabel('Throughput (Gbps)', color=color)
    ax1.plot(coalescing, throughput, 'o-', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Latency (ms)', color=color)
    ax2.plot(coalescing, latency, 's-', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('Throughput and Latency vs. Interrupt Coalescing')
    fig.tight_layout()
    
    plt.savefig('interrupt_coalescing.png', dpi=300)
    plt.close()

# Figure 3: Workload Patterns
def create_workload_patterns_figure():
    patterns = ['Bulk Transfer', 'Request-Response', 'Streaming', 'Bursty']
    
    # Different metrics for different patterns
    throughput = [40, 15, 25, 20]
    latency = [10, 2, 5, 15]
    cpu_util = [80, 40, 60, 70]
    
    x = np.arange(len(patterns))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width, throughput, width, label='Throughput (Gbps)')
    rects2 = ax.bar(x, latency, width, label='Latency (ms)')
    rects3 = ax.bar(x + width, cpu_util, width, label='CPU Utilization (%)')
    
    ax.set_xlabel('Workload Pattern')
    ax.set_ylabel('Value')
    ax.set_title('Performance Characteristics of Different Workload Patterns')
    ax.set_xticks(x)
    ax.set_xticklabels(patterns)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('workload_patterns.png', dpi=300)
    plt.close()

# Figure 4: Congestion Control
def create_congestion_control_figure():
    loss_rates = np.array([0, 0.01, 0.05, 0.1, 0.5, 1.0])
    
    # Different algorithms have different responses to loss
    cubic = 40 * np.exp(-2 * loss_rates)
    bbr = 40 * np.exp(-1 * loss_rates)
    vegas = 30 * np.exp(-3 * loss_rates)
    westwood = 35 * np.exp(-1.5 * loss_rates)
    
    plt.figure(figsize=(10, 6))
    plt.plot(loss_rates, cubic, 'o-', label='Cubic')
    plt.plot(loss_rates, bbr, 's-', label='BBR')
    plt.plot(loss_rates, vegas, '^-', label='Vegas')
    plt.plot(loss_rates, westwood, 'D-', label='Westwood')
    
    plt.xlabel('Packet Loss Rate (%)')
    plt.ylabel('Throughput (Gbps)')
    plt.title('Impact of Packet Loss on Different Congestion Control Algorithms')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    plt.savefig('congestion_control.png', dpi=300)
    plt.close()

# Create all figures
create_cpu_frequency_figure()
create_interrupt_coalescing_figure()
create_workload_patterns_figure()
create_congestion_control_figure()

print("All figures created successfully!")
