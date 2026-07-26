

DISCOUNT_RATE = 0.05        # this is the decimal value for 5% discount
MIN_STRIPS_FOR_DISCOUNT = 2 # need at least 2 strips to get discount


def calculate_tablet_sale(quantity, rate_per_tablet, rate_per_strip, tablets_per_strip):
    
    strips    = quantity // tablets_per_strip
    remaining = quantity %  tablets_per_strip

    if strips >= 1:
        strip_cost    = strips * rate_per_strip
        tablet_cost   = remaining * rate_per_tablet
        subtotal      = strip_cost + tablet_cost

        if strips >= MIN_STRIPS_FOR_DISCOUNT:
            discount_amount = round(subtotal * DISCOUNT_RATE, 2)
        else:
            discount_amount = 0.0

        total = round(subtotal - discount_amount, 2)

        return {
            "strips":           strips,
            "remaining_tablets": remaining,
            "strip_cost":       round(strip_cost, 2),
            "tablet_cost":      round(tablet_cost, 2),
            "subtotal":         round(subtotal, 2),
            "discount_applied": discount_amount > 0,
            "discount_amount":  discount_amount,
            "total":            total,
        }

    else:
        subtotal = quantity * rate_per_tablet
        return {
            "strips":            0,
            "remaining_tablets": quantity,
            "strip_cost":        0.0,
            "tablet_cost":       round(subtotal, 2),
            "subtotal":          round(subtotal, 2),
            "discount_applied":  False,
            "discount_amount":   0.0,
            "total":             round(subtotal, 2),
        }

#this function helps to calculate the total cost of a sale and the discount if needed.
def calculate_strip_sale(quantity_strips, rate_per_strip, tablets_per_strip):
    
    subtotal = quantity_strips * rate_per_strip

    if quantity_strips >= MIN_STRIPS_FOR_DISCOUNT:
        discount_amount = round(subtotal * DISCOUNT_RATE, 2)
    else:
        discount_amount = 0.0

    total = round(subtotal - discount_amount, 2)

    return {
        "strips":             quantity_strips,
        "tablets_equivalent": quantity_strips * tablets_per_strip,
        "subtotal":           round(subtotal, 2),
        "discount_applied":   discount_amount > 0,
        "discount_amount":    discount_amount,
        "total":              round(total, 2),
    }
