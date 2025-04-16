import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

# Figure 3: Single Flow Performance
def create_single_flow_figure():
    # Create a figure with 2x2 subplots
    fig = plt.figure(figsize=(12, 10))
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])
    
    # Figure 3(a): Throughput per Core
    ax1 = plt.subplot(gs[0, 0])
    configs = ['No Opt', 'TSO/GRO', 'Jumbo', 'TSO/GRO\n+Jumbo', 'TSO/GRO\n+aRFS', 'Jumbo\n+aRFS', 'All Opt']
    throughput_per_core = [4.8, 15.0, 25.9, 32.5, 28.7, 35.4, 41.2]
    
    ax1.bar(configs, throughput_per_core, color='skyblue')
    ax1.set_ylabel('Throughput per Core (Gbps)')
    ax1.set_title('(a) Throughput per Core')
    ax1.tick_params(axis='x', rotation=45)
    
    # Figure 3(b): Throughput and CPU Utilization
    ax2 = plt.subplot(gs[0, 1])
    throughput = [9.0, 26.6, 33.8, 38.5, 35.2, 39.7, 42.2]
    sender_cpu = [101.5, 95.2, 70.3, 64.2, 66.5, 62.8, 59.8]
    receiver_cpu = [185.8, 176.5, 130.2, 118.5, 123.4, 112.1, 100.0]
    
    x = np.arange(len(configs))
    width = 0.25
    
    ax2.bar(x - width, throughput, width, label='Throughput (Gbps)', color='skyblue')
    ax2.bar(x, sender_cpu, width, label='Sender CPU (%)', color='lightcoral')
    ax2.bar(x + width, receiver_cpu, width, label='Receiver CPU (%)', color='lightgreen')
    
    ax2.set_ylabel('Value')
    ax2.set_title('(b) Throughput and CPU Utilization')
    ax2.set_xticks(x)
    ax2.set_xticklabels(configs, rotation=45)
    ax2.legend()
    
    # Figure 3(c): Sender CPU Utilization Breakdown
    ax3 = plt.subplot(gs[1, 0])
    categories = ['data_copy', 'etc', 'lock', 'mm', 'netdev', 'sched', 'skb', 'tcp/ip']
    
    # Data for different configurations
    no_opt = [15.2, 8.3, 5.5, 7.2, 10.8, 4.5, 7.0, 41.5]
    tso_gro = [28.6, 10.2, 6.8, 8.5, 15.3, 5.2, 8.7, 16.7]
    all_opt = [48.0, 12.5, 7.2, 9.3, 5.5, 3.8, 1.0, 12.7]
    
    x = np.arange(len(categories))
    width = 0.25
    
    ax3.bar(x - width, no_opt, width, label='No Opt', color='skyblue')
    ax3.bar(x, tso_gro, width, label='TSO/GRO', color='lightcoral')
    ax3.bar(x + width, all_opt, width, label='All Opt', color='lightgreen')
    
    ax3.set_ylabel('CPU Utilization (%)')
    ax3.set_title('(c) Sender CPU Utilization Breakdown')
    ax3.set_xticks(x)
    ax3.set_xticklabels(categories, rotation=45)
    ax3.legend()
    
    # Figure 3(d): Receiver CPU Utilization Breakdown
    ax4 = plt.subplot(gs[1, 1])
    
    # Data for different configurations
    no_opt_r = [12.5, 7.8, 4.2, 6.5, 8.7, 3.2, 2.3, 54.8]
    tso_gro_r = [22.3, 9.5, 5.7, 7.8, 33.8, 4.5, 7.2, 9.2]
    all_opt_r = [54.3, 11.2, 6.5, 8.7, 12.5, 3.2, 1.6, 2.0]
    
    ax4.bar(x - width, no_opt_r, width, label='No Opt', color='skyblue')
    ax4.bar(x, tso_gro_r, width, label='TSO/GRO', color='lightcoral')
    ax4.bar(x + width, all_opt_r, width, label='All Opt', color='lightgreen')
    
    ax4.set_ylabel('CPU Utilization (%)')
    ax4.set_title('(d) Receiver CPU Utilization Breakdown')
    ax4.set_xticks(x)
    ax4.set_xticklabels(categories, rotation=45)
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig('fig3_single_flow.png', dpi=300)
    plt.close()

# Figure 4: One-to-One Performance
def create_one_to_one_figure():
    # Create a figure with 1x3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Figure 4(a): Throughput vs. Number of Flows
    cores = [1, 2, 4, 6]
    no_opt = [9.0, 17.5, 32.8, 45.2]
    tso_gro = [26.6, 52.3, 78.5, 85.7]
    all_opt = [42.2, 68.5, 88.3, 95.2]
    
    ax1.plot(cores, no_opt, 'o-', label='No Opt', color='skyblue')
    ax1.plot(cores, tso_gro, 's-', label='TSO/GRO', color='lightcoral')
    ax1.plot(cores, all_opt, '^-', label='All Opt', color='lightgreen')
    
    ax1.set_xlabel('Number of Cores/Flows')
    ax1.set_ylabel('Aggregate Throughput (Gbps)')
    ax1.set_title('(a) Throughput vs. Number of Flows')
    ax1.legend()
    ax1.grid(True)
    
    # Figure 4(b): CPU Utilization vs. Number of Flows
    cpu_no_opt = [185.8, 370.2, 720.5, 1050.3]
    cpu_tso_gro = [176.5, 345.8, 680.2, 950.7]
    cpu_all_opt = [100.0, 195.3, 380.5, 560.2]
    
    ax2.plot(cores, cpu_no_opt, 'o-', label='No Opt', color='skyblue')
    ax2.plot(cores, cpu_tso_gro, 's-', label='TSO/GRO', color='lightcoral')
    ax2.plot(cores, cpu_all_opt, '^-', label='All Opt', color='lightgreen')
    
    ax2.set_xlabel('Number of Cores/Flows')
    ax2.set_ylabel('CPU Utilization (%)')
    ax2.set_title('(b) CPU Utilization vs. Number of Flows')
    ax2.legend()
    ax2.grid(True)
    
    # Figure 4(c): Local vs. Remote NUMA
    local_numa = [42.2, 68.5, 88.3, 95.2]
    remote_numa = [38.5, 55.2, 62.8, 60.3]
    
    ax3.plot(cores, local_numa, 'o-', label='Local NUMA', color='skyblue')
    ax3.plot(cores, remote_numa, 's-', label='Remote NUMA', color='lightcoral')
    
    ax3.set_xlabel('Number of Cores/Flows')
    ax3.set_ylabel('Aggregate Throughput (Gbps)')
    ax3.set_title('(c) Local vs. Remote NUMA')
    ax3.legend()
    ax3.grid(True)
    
    plt.tight_layout()
    plt.savefig('fig4_one_to_one.png', dpi=300)
    plt.close()

# Figure 5: Incast Performance
def create_incast_figure():
    senders = [1, 2, 4, 8, 16, 32]
    no_opt = [9.0, 17.2, 28.5, 35.2, 38.5, 36.8]
    tso_gro = [26.6, 45.3, 65.8, 78.5, 82.3, 80.5]
    all_opt = [42.2, 62.5, 82.8, 92.5, 95.8, 94.2]
    
    plt.figure(figsize=(10, 6))
    plt.plot(senders, no_opt, 'o-', label='No Opt', color='skyblue')
    plt.plot(senders, tso_gro, 's-', label='TSO/GRO', color='lightcoral')
    plt.plot(senders, all_opt, '^-', label='All Opt', color='lightgreen')
    
    plt.xlabel('Number of Senders')
    plt.ylabel('Aggregate Throughput (Gbps)')
    plt.title('Incast Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    plt.savefig('fig5_incast.png', dpi=300)
    plt.close()

# Figure 7: Packet Loss Impact
def create_packet_loss_figure():
    loss_rates = [0, 0.01, 0.05, 0.1, 0.5, 1.0]
    cubic = [42.2, 25.3, 12.5, 8.2, 3.5, 2.1]
    reno = [42.2, 22.5, 10.2, 6.8, 2.8, 1.5]
    bbr = [42.2, 35.8, 28.5, 22.3, 15.2, 10.5]
    
    plt.figure(figsize=(10, 6))
    plt.plot(loss_rates, cubic, 'o-', label='Cubic', color='skyblue')
    plt.plot(loss_rates, reno, 's-', label='Reno', color='lightcoral')
    plt.plot(loss_rates, bbr, '^-', label='BBR', color='lightgreen')
    
    plt.xlabel('Packet Loss Rate (%)')
    plt.ylabel('Throughput (Gbps)')
    plt.title('Impact of Packet Loss on TCP Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    plt.savefig('fig7_packet_loss.png', dpi=300)
    plt.close()

# Figure 8: Short Flow Performance
def create_short_flow_figure():
    # Create a figure with 1x3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Figure 8(a): Short Flow Completion Time
    flows = [1, 2, 4, 8, 16, 32]
    small = [0.5, 0.8, 1.2, 2.5, 5.2, 12.5]
    medium = [1.2, 1.8, 2.5, 4.8, 9.5, 22.3]
    large = [2.5, 3.5, 5.2, 8.5, 15.8, 35.2]
    
    ax1.plot(flows, small, 'o-', label='Small (4KB)', color='skyblue')
    ax1.plot(flows, medium, 's-', label='Medium (16KB)', color='lightcoral')
    ax1.plot(flows, large, '^-', label='Large (64KB)', color='lightgreen')
    
    ax1.set_xlabel('Number of Concurrent Flows')
    ax1.set_ylabel('Completion Time (ms)')
    ax1.set_title('(a) Short Flow Completion Time')
    ax1.legend()
    ax1.grid(True)
    
    # Figure 8(b): Short Flow CPU Utilization
    cpu_small = [15.2, 28.5, 52.3, 85.2, 150.5, 280.3]
    cpu_medium = [22.5, 42.3, 78.5, 125.8, 220.5, 380.2]
    cpu_large = [35.8, 65.2, 120.5, 210.3, 350.2, 520.5]
    
    ax2.plot(flows, cpu_small, 'o-', label='Small (4KB)', color='skyblue')
    ax2.plot(flows, cpu_medium, 's-', label='Medium (16KB)', color='lightcoral')
    ax2.plot(flows, cpu_large, '^-', label='Large (64KB)', color='lightgreen')
    
    ax2.set_xlabel('Number of Concurrent Flows')
    ax2.set_ylabel('CPU Utilization (%)')
    ax2.set_title('(b) Short Flow CPU Utilization')
    ax2.legend()
    ax2.grid(True)
    
    # Figure 8(c): Short Flow NUMA Effects
    local_small = [0.5, 0.8, 1.2, 2.5, 5.2, 12.5]
    remote_small = [0.8, 1.3, 2.0, 4.2, 8.5, 20.3]
    local_large = [2.5, 3.5, 5.2, 8.5, 15.8, 35.2]
    remote_large = [4.2, 5.8, 8.5, 14.2, 25.3, 55.8]
    
    ax3.plot(flows, local_small, 'o-', label='Local NUMA (4KB)', color='skyblue')
    ax3.plot(flows, remote_small, 's-', label='Remote NUMA (4KB)', color='lightcoral')
    ax3.plot(flows, local_large, '^-', label='Local NUMA (64KB)', color='lightgreen')
    ax3.plot(flows, remote_large, 'D-', label='Remote NUMA (64KB)', color='orange')
    
    ax3.set_xlabel('Number of Concurrent Flows')
    ax3.set_ylabel('Completion Time (ms)')
    ax3.set_title('(c) Short Flow NUMA Effects')
    ax3.legend()
    ax3.grid(True)
    
    plt.tight_layout()
    plt.savefig('fig8_short_flow.png', dpi=300)
    plt.close()

# Create all figures
create_single_flow_figure()
create_one_to_one_figure()
create_incast_figure()
create_packet_loss_figure()
create_short_flow_figure()

print("All original paper figures created successfully!")
