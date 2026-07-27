# Med Store

Comprehensive pharmacy and medical inventory management application.

## Overview

Med Store is designed to streamline pharmacy operations, track drug inventory, and manage customer sales seamlessly.

## Features

- **Inventory Management**: Track medicine stock with tablet and strip units
- **Sales Processing**: Process customer sales with automatic 5% bulk discounts
- **Restocking**: Manage supplier purchases and inventory updates
- **Invoice Generation**: Automatic invoice creation for transactions
- **Flexible Pricing**: Support for both tablet and strip pricing
- **Data Persistence**: Automatic inventory saving

## Project Structure

```
Med_Store/
├── src/
│   ├── core/              # Business logic
│   │   ├── inventory.py   # Inventory management
│   │   ├── calculator.py  # Price calculations
│   │   └── invoices.py    # Invoice generation
│   ├── ui/                # User interface
│   │   ├── main_ui.py     # Main menu
│   │   ├── sales_ui.py    # Sales transactions
│   │   └── restock_ui.py  # Restock transactions
│   └── __init__.py
├── data/                  # Data files
│   ├── medicines.txt      # Inventory database
│   └── invoices/          # Generated invoices
├── tests/                 # Unit tests
├── docs/                  # Documentation
├── configs/               # Configuration files
├── scripts/               # Utility scripts
├── main.py               # Entry point
├── requirements.txt      # Dependencies
├── setup.py              # Package setup
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── CONTRIBUTING.md      # Contribution guidelines
└── LICENSE              # MIT License
```

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup

```bash
git clone https://github.com/Nikesh-Acharya-10/Med_Store.git
cd Med_Store
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Usage

### Main Menu

1. **View Inventory** - Display all medicines in stock
2. **Sell Medicines** - Process customer sales
3. **Restock Medicines** - Add inventory from suppliers
4. **Exit** - Close the application

### Selling Medicines

1. Enter customer name
2. Select medicine by number
3. Choose unit type (Tablet or Strip)
4. Enter quantity
5. Review pricing (5% discount for 2+ strips)
6. Confirm sale
7. Invoice auto-generated

### Restocking Medicines

1. Enter supplier name
2. Select medicine
3. Choose unit type
4. Enter quantity and cost per unit
5. Confirm restock
6. Restock note auto-generated

## Data Format

### medicines.txt

```
Medicine Name, Brand, Stock, Price/Tablet, Price/Strip, Tablets/Strip
Paracetamol 500mg, Lomus, 1252, 5, 45, 10
Cetirizine 10mg, Quest, 503, 4, 35, 12
```

### Invoices

Generated in `data/invoices/`:
- `SALE_YYYYMMDD_HHMMSS.txt` - Customer sales
- `RESTOCK_YYYYMMDD_HHMMSS.txt` - Supplier purchases

## Testing

```bash
python -m pytest tests/ -v
python -m unittest discover -s tests -v
```

## Configuration

Edit `configs/.env.example`:

```env
DISCOUNT_RATE=0.05
MIN_STRIPS_FOR_DISCOUNT=2
INVENTORY_FILE=data/medicines.txt
INVOICES_DIR=data/invoices
```

## Development

### Code Structure

- `src/core/` - Pure business logic
- `src/ui/` - User interaction
- `tests/` - Unit tests

## Future Enhancements

- Database integration (PostgreSQL)
- Web interface (Flask/Django)
- Advanced reporting
- Multi-location support
- Barcode scanning
- Expiry tracking

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) file.

## Support

- GitHub Issues: [Report bugs](https://github.com/Nikesh-Acharya-10/Med_Store/issues)
- GitHub Discussions: [Ask questions](https://github.com/Nikesh-Acharya-10/Med_Store/discussions)

## Author

**Nikesh Acharya**
- GitHub: [@Nikesh-Acharya-10](https://github.com/Nikesh-Acharya-10)

---

**Version**: 1.0.0  
**Last Updated**: July 27, 2026
