#!/usr/bin/env python3
import os

def create_directories():
    dirs = ["data", "data/invoices", "logs", "tests", "docs", "configs", "scripts"]
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"Created/verified: {directory}")

if __name__ == "__main__":
    print("\n=== Med Store Setup ===")
    create_directories()
    print("\nSetup complete!\n")
