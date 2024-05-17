import matplotlib.pyplot as plt
import pandas as pd

def plot_figure(bladder_volume,bladder_pressure,feedback_times,save_fig=None,show_fig=None):
    #Plot bladder volume and bladder pressure
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
        plt.savefig("results.png")

bladder_volume = pd.read_csv('output/bladder_volume.csv')
bladder_pressure = pd.read_csv('output/bladder_pressure.csv')
feedback_times = pd.read_csv('output/feedback_times.csv')

plot_figure(bladder_volume.to_numpy(),bladder_pressure.to_numpy(),feedback_times.to_numpy(),show_fig=False,save_fig=True)