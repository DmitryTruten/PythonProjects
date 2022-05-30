def get_formatted_name(first, last, middle=''):
    """Generate formatted full name"""
    if middle:
        full = f"{first} {middle} {last}"
    else:
        full = f"{first} {last}"
    return full.title()
