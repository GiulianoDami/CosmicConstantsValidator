import matplotlib.pyplot as plt
import numpy as np

def plot_constant_comparison(measured_constants, expected_constants):
    """
    Create a visualization comparing measured constants with expected values.
    
    Args:
        measured_constants (dict): Dictionary of measured constant values
        expected_constants (dict): Dictionary of expected constant values
    """
    # Extract constant names and values
    constants = list(measured_constants.keys())
    measured_values = [measured_constants[const] for const in constants]
    expected_values = [expected_constants[const] for const in constants]
    
    # Create the plot
    x = np.arange(len(constants))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width/2, measured_values, width, label='Measured', alpha=0.8)
    bars2 = ax.bar(x + width/2, expected_values, width, label='Expected', alpha=0.8)
    
    # Customize the plot
    ax.set_xlabel('Physical Constants')
    ax.set_ylabel('Values')
    ax.set_title('Comparison of Measured vs Expected Physical Constants')
    ax.set_xticks(x)
    ax.set_xticklabels(constants, rotation=45, ha='right')
    ax.legend()
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.2e}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.2e}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()