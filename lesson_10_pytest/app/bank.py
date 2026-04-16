

def calculate_discount(price, category):
    """Нараховує знижку: 'VIP' - 20%, 'Student' - 10%, іншим - 0%."""
    if price < 0:
        raise ValueError("Price can not less than 0")

    if category == "VIP":
        return price * 0.8
    elif category == "Student":
        return price * 0.9
    else:
        return price
