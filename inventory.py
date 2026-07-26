

INVENTORY_FILE = "medicines.txt"


def load_inventory():
    
    medicines = []
    try:
        with open(INVENTORY_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 6:
                    continue 
                medicine = {
                    "name":              parts[0],
                    "brand":             parts[1],
                    "stock":             int(parts[2]),   
                    "rate_per_tablet":   float(parts[3]),
                    "rate_per_strip":    float(parts[4]),
                    "tablets_per_strip": int(parts[5]),
                }
                medicines.append(medicine)
    except FileNotFoundError:
        print(f"[ERROR] '{INVENTORY_FILE}' not found. Starting with empty inventory.")
    return medicines


def save_inventory(medicines):
    try:
        with open(INVENTORY_FILE, "w") as f:
            for m in medicines:
                line = (
                    f"{m['name']}, {m['brand']}, {m['stock']}, "
                    f"{int(m['rate_per_tablet'])}, {int(m['rate_per_strip'])}, "
                    f"{m['tablets_per_strip']}\n"
                )
                f.write(line)
    except IOError as e:
        print(f"[ERROR] Could not save inventory: {e}")

#this function display the medicine that is stored in a tabular format.
def display_inventory(medicines):
    
    if not medicines:
        print("\n  No medicines available in stock.\n")
        return

    print("\n" + "=" * 150)
    print(f"  {'#':<4} {'Medicine':<25} {'Brand':<18} {'Stock':>6} {'Tab/Rs':>7} {'Strip/Rs':>9} {'Tab/Strip':>10}")
    print("=" * 150)
    for i, m in enumerate(medicines, 1):
        print(
            f"  {i:<4} {m['name']:<25} {m['brand']:<18} "
            f"{m['stock']:>6} {m['rate_per_tablet']:>7.0f} "
            f"{m['rate_per_strip']:>9.0f} {m['tablets_per_strip']:>10}"
        )
    print("=" * 150 + "\n")
