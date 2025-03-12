import numpy as np
import time
import matplotlib.pyplot as plt
import mplcursors

plt.rcParams['figure.figsize'] = (12, 4)
N = 2**10
lwL = 2
lwr = 1
axRxlims = [0, N]
axRylim = [200, 600]
_t = np.linspace(0, N, N)
_y = (1 + np.sin(5 / N * 2 * np.pi * _t))
dframe = np.full(N + 1, fill_value=np.nan, dtype=float)

t = np.tile(_t, (N, 1))
y = np.tile(_y, (N, 1))

for i in range(N):
    t[i, i + 1:] = np.nan
    y[i, i + 1:] = np.nan

fig, (axL, axR) = plt.subplots(ncols=2, tight_layout=True)
fig.suptitle("Complete")

for frame in range(N):
    axL.clear(), axR.clear()
    dframe[frame] = time.perf_counter()
    y2 = 1000 * np.diff(dframe)
    y2_avg = np.nanmean(y2)

    axL.set(xlabel="distance(m)", ylabel="amplitude")
    axL.set_title(f"n={frame}")
    axL.grid()
    axL.plot(t[frame], y[frame], lw=lwr)

    # Add mplcursors for interactive hovering on the left plot
    mplcursors.cursor(axL, hover=True)

    axR.set(xlabel="frame Number", ylabel="Frame time (ms)")
    axR.set_title(f"Avg = {y2_avg:.1f} ms ({1000/y2_avg:.1f} fps)")
    axR.set_xlim(axRxlims)
    axR.set_ylim(axRylim)
    axR.grid()
    axR.plot(t[frame], y2, lw=lwr)

    # Add mplcursors for interactive hovering on the right plot
    mplcursors.cursor(axR, hover=True)

    fig.canvas.draw()

    plt.pause(0.000001)

plt.show()
