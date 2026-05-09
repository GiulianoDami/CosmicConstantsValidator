def validate_universe_constants(constants):
    """
    Validates if the given universe constants fall within the sweet spot for liquid-based life.
    
    Args:
        constants (dict): Dictionary containing physical constants with their values
        
    Returns:
        dict: Validation results including whether constants are within acceptable ranges
    """
    # Define acceptable ranges for key physical constants
    acceptable_ranges = {
        'plancks_constant': (6.5e-34, 6.9e-34),  # J⋅s
        'gravitational_constant': (6.5e-11, 7.0e-11),  # m³⋅kg⁻¹⋅s⁻²
        'fine_structure_constant': (0.007, 0.008),  # dimensionless
        'boltzmann_constant': (1.37e-23, 1.40e-23),  # J⋅K⁻¹
        'electron_charge': (1.5e-19, 1.7e-19),  # C
        'proton_mass': (1.65e-27, 1.70e-27),  # kg
        'neutron_mass': (1.66e-27, 1.71e-27),  # kg
        'speed_of_light': (2.99e8, 3.01e8),  # m/s
    }
    
    results = {}
    
    for const_name, (min_val, max_val) in acceptable_ranges.items():
        if const_name in constants:
            value = constants[const_name]
            is_valid = min_val <= value <= max_val
            results[const_name] = {
                'value': value,
                'valid': is_valid,
                'acceptable_range': (min_val, max_val)
            }
        else:
            results[const_name] = {
                'value': None,
                'valid': False,
                'error': 'Constant not provided'
            }
    
    # Overall validation result
    valid_count = sum(1 for result in results.values() if isinstance(result.get('valid'), bool) and result['valid'])
    total_count = len([k for k in results.keys() if 'error' not in results[k]])
    
    results['overall_validation'] = {
        'passed': valid_count == total_count,
        'valid_count': valid_count,
        'total_count': total_count,
        'percentage': (valid_count / total_count * 100) if total_count > 0 else 0
    }
    
    return results