"""Quick Database Viewer"""
import sqlite3

DATABASE = 'finance.db'
conn = sqlite3.connect(DATABASE)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

print("\n" + "="*80)
print("DATABASE SUMMARY")
print("="*80 + "\n")

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

for table in tables:
    table_name = table['name']
    cursor.execute(f"SELECT COUNT(*) as count FROM {table_name}")
    count = cursor.fetchone()['count']
    print(f"Table: {table_name}")
    print(f"  Records: {count}")
    
    # Show first 3 records
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
    rows = cursor.fetchall()
    
    if rows:
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col['name'] for col in cursor.fetchall()]
        print(f"  Columns: {', '.join(columns)}")
        
        for i, row in enumerate(rows, 1):
            print(f"\n  Record {i}:")
            for col in columns:
                value = row[col]
                if isinstance(value, str) and len(value) > 50:
                    value = value[:50] + "..."
                print(f"    {col}: {value}")
    print("\n" + "-"*80 + "\n")

conn.close()
print("="*80)
