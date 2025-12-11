"""
test_baseline.py
Load Qf2.mat, apply baseline, and compare against MATLAB output
"""

import sys
import os

# Add the current directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

from baseline import baseline


def test_baseline_against_matlab():
    """
    Load Qf2.mat, compute baseline in Python, and compare with MATLAB output.
    """
    # Load the data
    data = loadmat('Qf2.mat')
    Qf2 = data['data_variable'].flatten().astype(np.float64)
    
    # Compute baseline in Python
    B = 1000
    python_baseline = baseline(Qf2, B)
    
    # Load MATLAB output
    matlab_data = loadmat('baseline_matlab_output.mat')
    matlab_baseline = matlab_data['baseline_result'].flatten()
    
    # Compare results
    max_diff = np.max(np.abs(python_baseline - matlab_baseline))
    mean_diff = np.mean(np.abs(python_baseline - matlab_baseline))
    
    print(f"Comparison of Python vs MATLAB baseline results:")
    print(f"  Input length: {len(Qf2)}")
    print(f"  Output length: {len(python_baseline)}")
    print(f"  Maximum absolute difference: {max_diff:.2e}")
    print(f"  Mean absolute difference: {mean_diff:.2e}")
    
    # Check if results are close (within numerical tolerance)
    tolerance = 1e-10
    if max_diff < tolerance:
        print(f"\nSUCCESS: Python and MATLAB results match within tolerance ({tolerance})")
        success = True
    else:
        print(f"\nWARNING: Differences exceed tolerance ({tolerance})")
        # Find indices where differences are largest
        diff = np.abs(python_baseline - matlab_baseline)
        worst_indices = np.argsort(diff)[-5:][::-1]
        print("\nLargest differences at indices:")
        for idx in worst_indices:
            print(f"  Index {idx}: Python={python_baseline[idx]:.6f}, "
                  f"MATLAB={matlab_baseline[idx]:.6f}, Diff={diff[idx]:.2e}")
        success = False
    
    # Plot comparison
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    
    # Plot 1: Original signal and both baselines
    ax1 = axes[0]
    ax1.plot(Qf2, label='Original signal', alpha=0.7)
    ax1.plot(python_baseline, label='Python baseline', linewidth=2)
    ax1.plot(matlab_baseline, '--', label='MATLAB baseline', linewidth=2)
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Signal and Baseline Comparison')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Python vs MATLAB baseline overlay
    ax2 = axes[1]
    ax2.plot(python_baseline, label='Python baseline', linewidth=2)
    ax2.plot(matlab_baseline, '--', label='MATLAB baseline', linewidth=2)
    ax2.set_ylabel('Amplitude')
    ax2.set_title('Baseline Comparison (Python vs MATLAB)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Difference between Python and MATLAB
    ax3 = axes[2]
    difference = python_baseline - matlab_baseline
    ax3.plot(difference, label='Python - MATLAB', color='red')
    ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax3.set_xlabel('Sample')
    ax3.set_ylabel('Difference')
    ax3.set_title(f'Difference (max: {max_diff:.2e}, mean: {mean_diff:.2e})')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('baseline_comparison.png', dpi=150)
    print("\nPlot saved to baseline_comparison.png")
    plt.show()
    
    return success


if __name__ == '__main__':
    test_baseline_against_matlab()
