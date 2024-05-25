import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def volume_pressure_plot(bladder_volume,bladder_pressure,feedback_times,save_fig=None,show_fig=None):
    """Plot bladder volume and bladder pressure
    bladder_volume: np array
    bladder_pressure: np array
    feedback_times: np array
    save_fig: string
    show_fig: Bool
    
    """
    fig1, ax1_1 = plt.subplots(figsize = (10,6))

    feedback_times = [tx/1000 for tx in feedback_times]
    bladder_volume = [bx*1000 for bx in bladder_volume]

    color = 'tab:red'
    ax1_1.set_xlabel('Time (t) [s]')
    ax1_1.set_ylabel('Bladder Volume (V) [ul]', color=color)
    ax1_1.plot(feedback_times, bladder_volume, color=color,lw=0.5)
    ax1_1.tick_params(axis='y', labelcolor=color)

    ax2_1 = ax1_1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2_1.set_ylabel('Bladder Pressure (P) [cm H2O]', color=color)  # we already handled the x-label with ax1
    # ax2_1.set_ylim(bottom=5,top=40)
    ax2_1.plot(feedback_times, bladder_pressure, color=color,lw=0.5)
    ax2_1.tick_params(axis='y', labelcolor=color)

    fig1.tight_layout()  # otherwise the right y-label is slightly clipped

    if show_fig:
        plt.show()
    if save_fig:
        plt.savefig(save_fig)

def plot_spiking_rate(df, node_set, included_groups, time_window_ms=100):
    # Filter the DataFrame to include only the specified groups
    df_filtered = df[df['group'].isin(included_groups)].copy()
    
    # Create time bins
    time_bins = np.arange(0, df_filtered['timestamps'].max() + time_window_ms, time_window_ms)

    # Bin the timestamps
    df_filtered.loc[:, 'time_bin'] = pd.cut(df_filtered['timestamps'], bins=time_bins, labels=time_bins[:-1])
    
    # Group by time bin and group, then count spikes
    spike_counts = df_filtered.groupby(['time_bin', 'group']).size().unstack(fill_value=0)
    
    # Convert to firing rate (spikes per second)
    time_window_sec = time_window_ms / 1000
    firing_rate = spike_counts / time_window_sec

    
    # Plot the firing rate for each group
    plt.figure(figsize=(15, 8))
    for group in firing_rate.columns:
        color = next(item['color'] for item in node_set if item['name'] == group)
        # Calculate group sizes
        group_sizes = {group['name']: group['end'] - group['start'] + 1 for group in node_set}
        plt.plot(firing_rate.index.astype(float), firing_rate[group]/group_sizes[group], marker='o', linestyle='-', color=color, label=group)
    
    plt.xlabel('Time (s)')
    plt.ylabel('Firing Rate (spikes/s)')
    plt.title('Neuron Spiking Rate Over Time by Group')
    plt.legend()
    plt.grid(True)
    plt.show()

def raster(spikes_df, node_set, start=0,end=80000):
    spikes_df = spikes_df[spikes_df['timestamps'] > start]
    spikes_df = spikes_df[spikes_df['timestamps'] < end]
    for node in node_set:
        cells = range(node['start'], node['end'] + 1)  # +1 to be inclusive of last cell
        cell_spikes = spikes_df[spikes_df['node_ids'].isin(cells)]

        plt.scatter(cell_spikes['timestamps'], cell_spikes['node_ids'],
                   c=node['color'], s=2, label=node['name'])

    plt.gca().legend(loc='lower right')
    plt.grid(False)




