# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from scipy.stats import ks_2samp, norm, gaussian_kde
from scipy.optimize import minimize_scalar, minimize
from scipy.integrate import simps


no_zeros = 1e-10
# Load dataset
data = ascii.read('./ZTF_flares.dat')
print(f"Loaded {len(data)} sources")

# Group offsets by type
offsets = {'SN': [], 'AGN': [], 'Unknown': []}
for entry in data:
    if 'SN' in entry['classification']:
        offsets['SN'].append(entry['offset_median'])
    elif 'AGN' in entry['classification']:
        offsets['AGN'].append(entry['offset_median'])
    else:
        offsets['Unknown'].append(entry['offset_median'])

# Convert to arrays
for key in offsets:
    offsets[key] = np.array(offsets[key])

# Plot distributions
plt.figure(figsize=(10, 5))
for label, color in zip(['SN', 'AGN', 'Unknown'], ['blue', 'orange', 'green']):
    plt.hist(offsets[label], bins=40, alpha=0.5, label=label, color=color)
plt.xlabel("Offset (arcsec)")  
plt.ylabel("Source count")    
plt.title("Offset by Type")  
plt.legend()
plt.grid(True)
plt.savefig("figure1.pdf")
plt.show()

# Run KS tests 
ks_sn = ks_2samp(offsets['Unknown'], offsets['SN'])
ks_agn = ks_2samp(offsets['Unknown'], offsets['AGN'])

print("KS test for Unknown vs AGN")
print(f"D-stat: {(ks_agn.statistic):.4f}")
print(f"p-val : {(ks_agn.pvalue):.4f}")

print("KS test for Unknown vs SN")
print(f"D-stat: {(ks_sn.statistic):.4f}")
print(f"p-val : {(ks_sn.pvalue):.4f}")

# Define P_nuc
def gauss_pdf(r, sigma):
    return norm.pdf(r, loc=0, scale=sigma)

def p_nuc(r, sigma):
    #this is one of the functions we got in the introduction, it appears to be a raileigh distribution.
    return np.sqrt(2 * np.pi) * (r / sigma) * gauss_pdf(r, sigma)

# Simulate P_nuc
np.random.seed(42)
x_fake = np.random.normal(0, 1, 10000)
y_fake = np.random.normal(0, 1, 10000)
r_sim = np.sqrt(x_fake**2 + y_fake**2)

r_values = np.linspace(0, 5, 100)
plt.hist(r_sim, bins=50, density=True, alpha=0.5, label='Simulated')
plt.plot(r_values, p_nuc(r_values, sigma=1), label='Theory $P_{nuc}$ (σ=1)')
plt.xlabel("Offset r")           
plt.ylabel("PDF")                
plt.title("Simulated vs Model")
plt.legend()
plt.grid(True)
plt.savefig("figure2.pdf")

plt.show()

# Estimate σ_xy from AGN with MLE
def neg_loglike_sigma(sigma):
    r_data = offsets['AGN']
    p_values = p_nuc(r_data, sigma)
    p_values = np.clip(p_values, no_zeros, None)
    return -np.sum(np.log(p_values))

bounds = (0.01, 1)
fit = minimize_scalar(neg_loglike_sigma, bounds=bounds, method='bounded')
sigma_xy = fit.x
print(f"Estimated σ_xy: {sigma_xy:.4f} arcsec")

# Compute r_90
r_90 = sigma_xy * np.sqrt(2 * np.log(10)) # read report why this is correct
print(f"Estimated r_90: {r_90:.4f} arcsec")

# KDE for SN
sn_data = offsets['SN']
sn_kde = gaussian_kde(sn_data, bw_method=0.01 / sn_data.std()) # best bandwith, found by trial and error

r_values = np.linspace(0, 0.8, 1000)
sn_pdf = sn_kde(r_values)

plt.figure(figsize=(8, 4))
plt.hist(sn_data, bins=40, density=True, alpha=0.4, label='SN Histogram')
plt.plot(r_values, sn_pdf, color='darkred', label='SN KDE')
plt.xlabel("Offset r")        
plt.ylabel("PDF")             
plt.title("SN KDE PDF")       
plt.legend()
plt.grid(True)
plt.show()

# Fit f_nuc to Unknowns
def pdf_mix(r, f_nuc, sigma_xy, sn_kde):
    #this is one of the functions we got in the introduction for the mixture
    return f_nuc * p_nuc(r, sigma_xy) + (1 - f_nuc) * sn_kde(r)

def neg_loglike_f_nuc(f_nuc):
    if not (0 <= f_nuc <= 1):
        return np.inf
    r_unknown = offsets['Unknown']
    p_values = pdf_mix(r_unknown, f_nuc, sigma_xy, sn_kde)
    p_values = np.clip(p_values, no_zeros, None)
    return -np.sum(np.log(p_values))

f_fit = minimize_scalar(neg_loglike_f_nuc, bounds=(0, 1), method='bounded')
f_nuclear = f_fit.x
f_sn = 1 - f_nuclear

print(f"Estimated f_nuclear: {f_nuclear:.4f}")
print(f"Estimated f_SN: {f_sn:.4f}")

# Plot SN fraction
r_bins = np.linspace(0, 0.8, 100)
p_n = p_nuc(r_bins, sigma_xy)
p_s = sn_kde(r_bins)
p_total = f_nuclear * p_n + (1 - f_nuclear) * p_s
f_sn_r = (1 - f_nuclear) * p_s / p_total
f_sn_r[0] = 0  # avoid first term (is 1)

plt.figure(figsize=(8, 4))
plt.plot(r_bins, f_sn_r, label='SN Fraction')
plt.axvline(r_90, linestyle='--', color='gray', label=f'$r_{{90}}$ = {r_90:.2f}')
plt.xlabel("Offset r")            
plt.ylabel("SN fraction")         
plt.title("SN fraction vs Offset")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("figure3.pdf")
    
# Integrate area within r_90
mask = r_bins < r_90
sn_area = f_sn_r[mask] * p_total[mask]
total_area = p_total[mask]
frac_sn_r90 = simps(sn_area, r_bins[mask]) / simps(total_area, r_bins[mask])
print(f"SN fraction within r_90: {frac_sn_r90:.4f}")

# Joint Fit; bonus
def neg_loglike_joint(params):
    f_nuc, sigma_xy = params
    if not (0 <= f_nuc <= 1) or sigma_xy <= 0:
        return np.inf
    r_unknown = offsets['Unknown']
    p_values = pdf_mix(r_unknown, f_nuc, sigma_xy, sn_kde)
    p_values = np.clip(p_values, no_zeros, None)
    return -np.sum(np.log(p_values))

joint_init_guess = [f_nuclear, sigma_xy]
joint_bounds = [(0, 1), (0.01, 1)]
joint_fit = minimize(neg_loglike_joint, joint_init_guess, bounds=joint_bounds, method='L-BFGS-B')
f_joint, sigma_joint = joint_fit.x
f_sn_joint = 1 - f_joint

print(f"Joint Fit f_nuclear: {f_joint:.4f}")
print(f"Joint Fit σ_xy: {sigma_joint:.4f}")
print(f"Joint Fit f_SN: {f_sn_joint:.4f}")

# Plot joint fit
p_n_joint = p_nuc(r_bins, sigma_joint)
p_mix_joint = f_joint * p_n_joint + (1 - f_joint) * p_s
f_sn_frac = (1 - f_joint) * p_s / p_mix_joint
f_sn_frac[0] = 0  # avoid first term (is 1)

plt.figure(figsize=(8, 4))
plt.plot(r_bins, f_sn_frac, label='SN fraction (Joint)', color='purple')
plt.axvline(r_90, linestyle='--', color='gray', label=f'$r_{{90}}$ = {r_90:.2f}')
plt.xlabel("Offset r")                 
plt.ylabel("SN fraction")               
plt.title("SN fraction (Joint Fit)")    
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("figure4.pdf")

# Integrate area within r_90 joint fit
mask = r_bins < r_90
contrib_area = f_sn_frac[mask] * p_mix_joint[mask]
total_area = p_mix_joint[mask]
frac_sn_joint_r90 = simps(contrib_area, r_bins[mask]) / simps(total_area, r_bins[mask])
print(f"SN fraction within r_90 (Joint): {frac_sn_joint_r90:.4f}")

# Bootstrap confidence intervals (error calculation)
# Here we will resample the AGN and Unknown offsets an n number of times, re-fit, and store the results to get an error.

n_boot = 1000  # number of bootstrap samples
sigma_samples = []
f_nuc_samples = []
f_sn_samples = []
joint_f_samples = []
joint_sigma_samples = []
joint_f_sn_samples = []

np.random.seed(42)
for _ in range(n_boot):
    # Resample AGN and Unknown with replacement
    resample_agn = np.random.choice(offsets['AGN'], size=len(offsets['AGN']), replace=True)
    resample_unknown = np.random.choice(offsets['Unknown'], size=len(offsets['Unknown']), replace=True)

    # Re-fit sigma
    def bootstrap_neg_loglike_sigma(sigma):
        p_vals = p_nuc(resample_agn, sigma)
        p_vals = np.clip(p_vals, no_zeros, None)
        return -np.sum(np.log(p_vals))

    bootstrap_sigma = minimize_scalar(bootstrap_neg_loglike_sigma, bounds=(0.01, 1), method='bounded').x
    sigma_samples.append(bootstrap_sigma)

    # Re-fit f_nuc
    def bootstrap_neg_loglike_f_nuc(f_nuc):
        if not (0 <= f_nuc <= 1):
            return np.inf
        p_vals = pdf_mix(resample_unknown, f_nuc, bootstrap_sigma, sn_kde)
        p_vals = np.clip(p_vals, no_zeros, None)
        return -np.sum(np.log(p_vals))

    bootstrap_f_nuc = minimize_scalar(bootstrap_neg_loglike_f_nuc, bounds=(0, 1), method='bounded').x
    bootstrap_f_sn = 1 - bootstrap_f_nuc
    f_nuc_samples.append(bootstrap_f_nuc)
    f_sn_samples.append(bootstrap_f_sn)

    # Re-fit joint fit
    def bootstrap_joint_neg_loglike(params):
        f, sigma = params
        if not (0 <= f <= 1) or sigma <= 0:
            return np.inf
        p_vals = pdf_mix(resample_unknown, f, sigma, sn_kde)
        p_vals = np.clip(p_vals, no_zeros, None)
        return -np.sum(np.log(p_vals))

    joint_result = minimize(bootstrap_joint_neg_loglike, [bootstrap_f_nuc, bootstrap_sigma], bounds=joint_bounds, method='L-BFGS-B')
    joint_f, joint_sigma = joint_result.x
    joint_f_samples.append(joint_f)
    joint_sigma_samples.append(joint_sigma)
    joint_f_sn_samples.append(1 - joint_f)

# Function to get 95% confidence intervals
conf_int = lambda arr: (np.percentile(arr, 2.5), np.percentile(arr, 97.5))

print("\ n95% Confidence Intervals (Bootstrap, n=1000)")
print(f"σ_xy: {sigma_xy:.4f} arcsec (95% CI: {conf_int(sigma_samples)[0]:.4f} – {conf_int(sigma_samples)[1]:.4f})")
print(f"f_nuclear: {f_nuclear:.4f} (95% CI: {conf_int(f_nuc_samples)[0]:.4f} – {conf_int(f_nuc_samples)[1]:.4f})")
print(f"f_SN: {f_sn:.4f} (95% CI: {conf_int(f_sn_samples)[0]:.4f} – {conf_int(f_sn_samples)[1]:.4f})")
print(f"Joint f_nuclear: {f_joint:.4f} (95% CI: {conf_int(joint_f_samples)[0]:.4f} – {conf_int(joint_f_samples)[1]:.4f})")
print(f"Joint σ_xy: {sigma_joint:.4f} (95% CI: {conf_int(joint_sigma_samples)[0]:.4f} – {conf_int(joint_sigma_samples)[1]:.4f})")
print(f"Joint f_SN: {f_sn_joint:.4f} (95% CI: {conf_int(joint_f_sn_samples)[0]:.4f} – {conf_int(joint_f_sn_samples)[1]:.4f})")
