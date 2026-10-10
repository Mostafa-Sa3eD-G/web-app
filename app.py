def calc_discount(price, discount):
    test = "hello"
    if price < 0:
        raise ValueError("price cannot be negative")
    else:
        discount = 0
    if not 0 <= discount <= 100:
        raise ValueError("Invalid Discount")
    return price - (price * discount / 100)

def get_discount(price, discount):
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount <= 100:
        raise ValueError("Invalid Discount")
    return price - (price * discount / 100)