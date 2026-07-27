"""
Invoice generation module.
"""

import os
from datetime import datetime

INVOICES_DIR = "data/invoices"


def _ensure_invoices_dir():
    if not os.path.exists(INVOICES_DIR):
        os.makedirs(INVOICES_DIR)


def _unique_filename(prefix):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(INVOICES_DIR, f"{prefix}_{timestamp}.txt")


def _separator(char="=", width=55):
    return char * width


def generate_sale_invoice(customer_name, items, grand_total):
    _ensure_invoices_dir()
    filename = _unique_filename("SALE")
    now = datetime.now()

    lines = []
    lines.append(_separator())
    lines.append("        MEDSTORE PVT. LTD.")
    lines.append("     Wholesale Medicine Distributor")
    lines.append(_separator())
    lines.append(f"  Invoice Type : SALE INVOICE")
    lines.append(f"  Date         : {now.strftime('%Y-%m-%d')}")
    lines.append(f"  Time         : {now.strftime('%H:%M:%S')}")
    lines.append(f"  Customer     : {customer_name}")
    lines.append(_separator("-"))
    lines.append(f"  {'Medicine':<22} {'Qty':<14} {'Sub(Rs)':>8} {'Disc(Rs)':>9} {'Total(Rs)':>10}")
    lines.append(_separator("-"))

    for item in items:
        unit_type = item["unit_type"]
        if unit_type == "tablet":
            if item["strips"] >= 1:
                if item["remaining_tablets"] > 0:
                    qty_str = f"{item['strips']}strip+{item['remaining_tablets']}tab"
                else:
                    qty_str = f"{item['strips']} strip(s)"
            else:
                qty_str = f"{item['remaining_tablets']} tablet(s)"
        else:
            qty_str = f"{item['strips']} strip(s)"

        disc_str = f"{item['discount_amount']:.2f}" if item["discount_applied"] else "-"

        lines.append(
            f"  {item['name']:<22} {qty_str:<14} "
            f"{item['subtotal']:>8.2f} {disc_str:>9} {item['total']:>10.2f}"
        )
        lines.append(f"    Brand: {item['brand']}")

    lines.append(_separator("-"))
    lines.append(f"  {'GRAND TOTAL':>44}   Rs {grand_total:.2f}")
    lines.append(_separator())
    lines.append("  Thank you for your purchase!")
    lines.append(_separator())

    try:
        with open(filename, "w") as f:
            f.write("\n".join(lines) + "\n")
    except IOError as e:
        print(f"[ERROR] Could not save sale invoice: {e}")
        return None

    return filename


def generate_restock_invoice(supplier_name, items, grand_total):
    _ensure_invoices_dir()
    filename = _unique_filename("RESTOCK")
    now = datetime.now()

    lines = []
    lines.append(_separator())
    lines.append("        MEDSTORE PVT. LTD.")
    lines.append("     Wholesale Medicine Distributor")
    lines.append(_separator())
    lines.append(f"  Invoice Type : RESTOCK NOTE")
    lines.append(f"  Date         : {now.strftime('%Y-%m-%d')}")
    lines.append(f"  Time         : {now.strftime('%H:%M:%S')}")
    lines.append(f"  Supplier     : {supplier_name}")
    lines.append(_separator("-"))
    lines.append(f"  {'Medicine':<22} {'Brand':<16} {'Qty':<12} {'Rate':>6} {'Total(Rs)':>10}")
    lines.append(_separator("-"))

    for item in items:
        qty_str = f"{item['quantity']} {item['unit_type']}(s)"
        lines.append(
            f"  {item['name']:<22} {item['brand']:<16} "
            f"{qty_str:<12} {item['rate']:>6.2f} {item['total']:>10.2f}"
        )

    lines.append(_separator("-"))
    lines.append(f"  {'GRAND TOTAL':>54}   Rs {grand_total:.2f}")
    lines.append(_separator())
    lines.append("  Restock recorded successfully.")
    lines.append(_separator())

    try:
        with open(filename, "w") as f:
            f.write("\n".join(lines) + "\n")
    except IOError as e:
        print(f"[ERROR] Could not save restock invoice: {e}")
        return None

    return filename
