"""
View Database Contents
This script displays all data in the finance.db database
"""

import sqlite3
from datetime import datetime

DATABASE = 'finance.db'

def view_database():
    """Display all database contents in a readable format"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    print("=" * 80)
    print("FINANCE DATABASE VIEWER")
    print("=" * 80)
    print()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table['name']
        print(f"\n{'=' * 80}")
        print(f"TABLE: {table_name.upper()}")
        print("=" * 80)
        
        # Get table structure
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        column_names = [col['name'] for col in columns]
        
        print(f"\nColumns: {', '.join(column_names)}")
        
        # Get row count
        cursor.execute(f"SELECT COUNT(*) as count FROM {table_name}")
        count = cursor.fetchone()['count']
        print(f"Total Records: {count}")
        
        # Get all data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        if rows:
            print(f"\nData:")
            print("-" * 80)
            for i, row in enumerate(rows, 1):
                print(f"\nRecord #{i}:")
                for col in column_names:
                    value = row[col]
                    # Format long text
                    if isinstance(value, str) and len(value) > 100:
                        value = value[:100] + "..."
                    print(f"  {col}: {value}")
        else:
            print("\n(No records found)")
    
    conn.close()
    print("\n" + "=" * 80)
    print("END OF DATABASE")
    print("=" * 80)

def view_table_summary():
    """Show quick summary of all tables"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    print("\n" + "=" * 80)
    print("DATABASE SUMMARY")
    print("=" * 80)
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table['name']
        cursor.execute(f"SELECT COUNT(*) as count FROM {table_name}")
        count = cursor.fetchone()['count']
        print(f"  {table_name}: {count} records")
    
    conn.close()
    print("=" * 80 + "\n")

if __name__ == '__main__':
    print("\n")
    print("FINANCE DATABASE CONTENTS")
    print()
    
    # Show summary first
    view_table_summary()
    
    # Ask if user wants full details
    choice = input("Do you want to see full database details? (y/n): ").lower()
    
    if choice == 'y':
        view_database()
    else:
        print("\nShowing summary only. Run again and choose 'y' for full details.")
