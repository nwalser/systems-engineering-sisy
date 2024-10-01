import matplotlib.pyplot as plt
import neurokit2 as nk
import numpy as np
import scipy as sp

ecg_signal = np.genfromtxt('4_data_ekg.csv', delimiter=',', skip_header=False)

f_decimal = '{0:.2f}'

f = 500
t = np.linspace(0, len(ecg_signal) / f, len(ecg_signal))

# calculate features of signal
_, rpeaks = nk.ecg_peaks(ecg_signal, sampling_rate=f)
_, waves_peak = nk.ecg_delineate(ecg_signal, rpeaks, sampling_rate=f, method="peak", show=True, show_type="all")
ax = plt.gca()
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
plt.title("EKG Signal Overlay aligned on RPeaks")
plt.show()

# calculate RPeak intervals
rpeaks_t_s = rpeaks["ECG_R_Peaks"] / f
rpeaks_intervals_s = np.gradient(rpeaks_t_s)
heart_rate_bpm = 60/rpeaks_intervals_s

# calculate beats per minute
beats_per_minute = np.average(heart_rate_bpm)

# calculate breaths per minute
breath_peak_indices = sp.signal.find_peaks(heart_rate_bpm)[0]
breath_peak_t_s = rpeaks_t_s[breath_peak_indices]
breath_peak_intervals_s = np.gradient(breath_peak_t_s)
breath_t_average = np.average(breath_peak_intervals_s)
print(breath_peak_intervals_s)
breaths_per_minute = 60/breath_t_average
print(f"Breaths per Minute: {breaths_per_minute}")


# plot
plt.figure(1)
view_min = 1600
view_max = 2200
nk.events_plot([rpeaks['ECG_R_Peaks'], waves_peak['ECG_T_Peaks'], waves_peak['ECG_P_Peaks'], waves_peak['ECG_Q_Peaks'],
                waves_peak['ECG_S_Peaks']], ecg_signal)
plt.xlim([view_min, view_max])
ax = plt.gca()
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
plt.title("Single Heart Beat with PQRST Annotations")
plt.show()

# plot breaths
plt.figure(1)
plt.plot(rpeaks_t_s, heart_rate_bpm)
plt.plot(rpeaks_t_s[breath_peak_indices], heart_rate_bpm[breath_peak_indices], linestyle="None", marker="x")
plt.ylim([20, 80])
plt.title("Heart Rate vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Heart Rate [bpm]")

plt.hlines([beats_per_minute], np.min(rpeaks_t_s), np.max(rpeaks_t_s), color="k", linestyle="--")
plt.text(x=0, y=22, s=f"T Average: {f_decimal.format(np.average(rpeaks_intervals_s))}s \n"
                     f"T Min: {f_decimal.format(np.min(rpeaks_intervals_s))}s \n"
                     f"T Max: {f_decimal.format(np.max(rpeaks_intervals_s))}s \n\n"
                     f"BPM Average: {f_decimal.format(np.average(heart_rate_bpm))} 1/s\n"
                     f"BPM Min: {f_decimal.format(np.min(heart_rate_bpm))} 1/s\n"
                     f"BPM Max: {f_decimal.format(np.max(heart_rate_bpm))} 1/s\n\n"
                     f"{f_decimal.format(breaths_per_minute)} Breaths per Minute ")

plt.show()