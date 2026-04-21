def shipping_cost(weight: float, has_label: bool, international: bool) -> float: 
    """Cost of shipping a package based on weight, label, and international status.""" 
    if not has_label:
        return 0.0
    if weight <= 1.0:
        if international:
            return 15.0
        else:
            return 5.0
    elif  1.0 < weight <= 5.0:
        if international:
            return 20.0
        else:
            return 10.0
    else:
        if international:
            return 30.0
        else:
            return 20.0
            
print(shipping_cost(0.5, True, False))  # Output: 5.0
print(shipping_cost(3.0, True, True))   # Output: 20.0
