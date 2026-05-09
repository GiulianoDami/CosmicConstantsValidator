# src/constants.py

DEFAULT_CONSTANTS = {
    'plancks_constant': 6.62607015e-34,      # J⋅s
    'gravitational_constant': 6.67430e-11,   # m³⋅kg⁻¹⋅s⁻²
    'speed_of_light': 299792458,             # m/s
    'boltzmann_constant': 1.380649e-23,      # J/K
    'avogadro_number': 6.02214076e23,       # mol⁻¹
    'fine_structure_constant': 7.2973525693e-3,  # dimensionless
    'electron_mass': 9.10938356e-31,        # kg
    'proton_mass': 1.6726219e-27,           # kg
    'elementary_charge': 1.602176634e-19,   # C
}

LIFE_SUSTAINING_THRESHOLDS = {
    'plancks_constant': {'min': 6.626e-34, 'max': 6.627e-34},
    'gravitational_constant': {'min': 6.67e-11, 'max': 6.68e-11},
    'speed_of_light': {'min': 299792000, 'max': 299793000},
    'boltzmann_constant': {'min': 1.380e-23, 'max': 1.381e-23},
    'fine_structure_constant': {'min': 7.29e-3, 'max': 7.30e-3},
    'electron_mass': {'min': 9.109e-31, 'max': 9.110e-31},
    'proton_mass': {'min': 1.672e-27, 'max': 1.673e-27},
}