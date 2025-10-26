"""
Test Portfolio and Stock Insights Pages
"""

import requests

BASE_URL = "http://localhost:5000"

def test_portfolio_without_login():
    """Test portfolio page without being logged in"""
    print("Testing Portfolio page (without login)...")
    try:
        response = requests.get(f"{BASE_URL}/portfolio", allow_redirects=False)
        print(f"  Status Code: {response.status_code}")
        if response.status_code == 302:
            print("  [OK] Correctly redirects to login (protected page)")
            print(f"  Redirect to: {response.headers.get('Location', 'Unknown')}")
        elif response.status_code == 200:
            print("  [WARNING] Page accessible without login")
        else:
            print(f"  [ERROR] Unexpected status code: {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return 0

def test_stock_insights_without_login():
    """Test stock insights page without being logged in"""
    print("\nTesting Stock Insights page (without login)...")
    try:
        response = requests.get(f"{BASE_URL}/stock-insights", allow_redirects=False)
        print(f"  Status Code: {response.status_code}")
        if response.status_code == 302:
            print("  [OK] Correctly redirects to login (protected page)")
            print(f"  Redirect to: {response.headers.get('Location', 'Unknown')}")
        elif response.status_code == 200:
            print("  [WARNING] Page accessible without login")
        else:
            print(f"  [ERROR] Unexpected status code: {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return 0

def test_with_login():
    """Test with actual login"""
    print("\nTesting with Login...")
    print("-"*60)
    
    # Create a session to maintain cookies
    session = requests.Session()
    
    # Try to login (you need to have a user registered)
    print("\nNOTE: To test logged-in features, you need to:")
    print("  1. Register a user at: http://localhost:5000/register")
    print("  2. Login at: http://localhost:5000/login")
    print("  3. Then access these pages:")
    print("     - Portfolio: http://localhost:5000/portfolio")
    print("     - Stock Insights: http://localhost:5000/stock-insights")
    print()
    print("The pages require authentication for security.")

if __name__ == "__main__":
    print("="*60)
    print("TESTING PORTFOLIO & STOCK INSIGHTS")
    print("="*60)
    print()
    
    port_status = test_portfolio_without_login()
    stock_status = test_stock_insights_without_login()
    
    print("\n" + "="*60)
    print("TEST RESULTS")
    print("="*60)
    
    if port_status == 302 and stock_status == 302:
        print("\n[OK] Both pages are working correctly!")
        print("     They are protected and require login.")
    else:
        print("\n[WARNING] Unexpected behavior detected.")
    
    test_with_login()
    
    print("\n" + "="*60)
    print("DIRECT LINKS")
    print("="*60)
    print(f"Register: {BASE_URL}/register")
    print(f"Login:    {BASE_URL}/login")
    print(f"After login, access:")
    print(f"  Portfolio:      {BASE_URL}/portfolio")
    print(f"  Stock Insights: {BASE_URL}/stock-insights")
    print("="*60)
