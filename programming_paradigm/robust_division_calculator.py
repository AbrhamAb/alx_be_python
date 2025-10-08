def safe_divide(numerator, denominator):
    """
    Safely performs division while handling potential errors.
    
    Args:
        numerator: The number to be divided (can be numeric or string)
        denominator: The number to divide by (can be numeric or string)
    
    Returns:
        float or str: The result of division if successful, or error message if failed
    """
    try:
        # Convert inputs to floats, handling non-numeric values
        num = float(numerator)
        den = float(denominator)
        
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        # Perform division, handling division by zero
        result = num / den
        return result
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."