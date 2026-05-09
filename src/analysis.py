def calculate_deviation_score(constants, reference_values):
    """
    Calculate deviation score for given constants compared to reference values.
    
    Args:
        constants (dict): Dictionary of current constant values
        reference_values (dict): Dictionary of reference constant values
        
    Returns:
        float: Normalized deviation score (0-100)
    """
    if not constants or not reference_values:
        return 0.0
    
    total_deviation = 0
    count = 0
    
    for key, value in reference_values.items():
        if key in constants:
            # Calculate relative deviation percentage
            if value != 0:
                deviation = abs((constants[key] - value) / value) * 100
                total_deviation += deviation
                count += 1
    
    if count == 0:
        return 0.0
    
    # Normalize to 0-100 scale
    average_deviation = total_deviation / count
    score = max(0, min(100, 100 - average_deviation))
    
    return round(score, 2)


def analyze_life_sustainability(constants):
    """
    Analyze if constants support life sustainability based on known thresholds.
    
    Args:
        constants (dict): Dictionary of current constant values
        
    Returns:
        dict: Analysis results including sustainability status and risk factors
    """
    # Define critical thresholds for life-sustaining conditions
    thresholds = {
        'fine_structure_constant': {'min': 0.007, 'max': 0.008},
        'gravitational_constant': {'min': 6.67e-11, 'max': 6.69e-11},
        'plancks_constant': {'min': 6.5e-34, 'max': 6.7e-34}
    }
    
    results = {
        'sustainable': True,
        'risk_factors': [],
        'deviation_scores': {}
    }
    
    for const_name, thresholds_dict in thresholds.items():
        if const_name in constants:
            value = constants[const_name]
            min_val = thresholds_dict['min']
            max_val = thresholds_dict['max']
            
            # Check if value is within acceptable range
            if not (min_val <= value <= max_val):
                results['sustainable'] = False
                results['risk_factors'].append(const_name)
                
            # Calculate deviation score for this constant
            reference_value = (min_val + max_val) / 2
            deviation = abs((value - reference_value) / reference_value) * 100
            results['deviation_scores'][const_name] = round(deviation, 2)
    
    return results