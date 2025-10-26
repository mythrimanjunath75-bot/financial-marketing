"""
Fix Database Issues
- Remove invalid stock entries
- Clean up duplicate data
"""

import sqlite3

DATABASE = 'finance.db'

def fix_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    print("\n" + "="*80)
    print("DATABASE CLEANUP")
    print("="*80 + "\n")
    
    # Check current portfolio
    cursor.execute('SELECT * FROM portfolio')
    portfolio = cursor.fetchall()
    print(f"Current portfolio entries: {len(portfolio)}")
    
    # Remove invalid stock entries (symbol = "STOCKS")
    cursor.execute("DELETE FROM portfolio WHERE symbol = 'STOCKS'")
    deleted = cursor.rowcount
    print(f"Deleted {deleted} invalid stock entries (symbol='STOCKS')")
    
    # Show remaining portfolio
    cursor.execute('SELECT * FROM portfolio')
    remaining = cursor.fetchall()
    print(f"Remaining portfolio entries: {len(remaining)}")
    
    if remaining:
        print("\nRemaining stocks:")
        for stock in remaining:
            print(f"  - {stock[2]} (Quantity: {stock[3]}, Price: ${stock[4]})")
    else:
        print("\n✅ Portfolio is now empty and ready for new entries!")
    
    conn.commit()
    conn.close()
    
    print("\n" + "="*80)
    print("DATABASE FIXED!")
    print("="*80 + "\n")
    print("Now you can add valid stock symbols like:")
    print("  - AAPL (Apple)")
    print("  - GOOGL (Google)")
    print("  - MSFT (Microsoft)")
    print("  - TSLA (Tesla)")
    print()

if __name__ == '__main__':
    fix_database()
