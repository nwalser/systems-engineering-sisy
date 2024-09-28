import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import scipy as sp

ecg_signal = np.genfromtxt('4_data_ekg.csv', delimiter=',', skip_header=False)

f = 500
t = np.linspace(0, len(ecg_signal) / f, len(ecg_signal))

# calculate features of signal
_, rpeaks = nk.ecg_peaks(ecg_signal, sampling_rate=f)
_, waves_peak = nk.ecg_delineate(ecg_signal, rpeaks, sampling_rate=f, method="peak", show=True, show_type="all")
plt.show()

# calculate RPeak intervals
rpeaks_t_s = rpeaks["ECG_R_Peaks"] / f
rpeaks_intervals_s = np.gradient(rpeaks_t_s)

# calculate beats per minute
t_average = np.average(rpeaks_intervals_s)
beats_per_minute = 60 / t_average
print(f"Beats per Minute: {beats_per_minute}")

# calculate breaths per minute
breath_peak_indices = sp.signal.find_peaks(rpeaks_intervals_s)[0]
breath_peak_t_s = rpeaks_t_s[breath_peak_indices]
breath_peak_intervals_s = np.gradient(breath_peak_t_s)
breath_t_average = np.average(breath_peak_intervals_s)
print(breath_peak_intervals_s)
breaths_per_minute = 60 / breath_t_average
print(f"Breaths per Minute: {breaths_per_minute}")


# plot figure 1
plt.figure(1, figsize=(12, 8))
view_min = 1600
view_max = 2200
nk.events_plot([rpeaks['ECG_R_Peaks'], waves_peak['ECG_T_Peaks'], waves_peak['ECG_P_Peaks'], waves_peak['ECG_Q_Peaks'],
                waves_peak['ECG_S_Peaks']], ecg_signal)
plt.xlim([view_min, view_max])
ax = plt.gca()
ax.get_yaxis().set_visible(False)
plt.show()

# plot figure 2
plt.figure(1, figsize=(12, 8))
plt.plot(rpeaks_t_s, rpeaks_intervals_s)
plt.title("RPeak Intervals")
plt.xlabel("Time [s]")
plt.show()

# plot breaths
plt.figure(1, figsize=(12, 8))
plt.plot(rpeaks_t_s, rpeaks_intervals_s)
plt.plot(rpeaks_t_s[breath_peak_indices], rpeaks_intervals_s[breath_peak_indices], linestyle="None", marker="x")
plt.title("RPeak Intervals")
plt.xlabel("Time [s]")
plt.show()