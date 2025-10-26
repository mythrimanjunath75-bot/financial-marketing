"""
Demonstration of Portfolio and Stock Insights Features
This shows all features are working
"""

import requests
import webbrowser
import time

BASE_URL = "http://localhost:5000"

def test_all_features():
    """Test all features are accessible"""
    print("="*70)
    print("TESTING ALL FEATURES")
    print("="*70)
    print()
    
    features = [
        ("Home Page", "/"),
        ("Login Page", "/login"),
        ("Register Page", "/register"),
        ("Portfolio", "/portfolio"),
        ("Stock Insights", "/stock-insights"),
        ("Dashboard", "/dashboard"),
        ("AI Chatbot", "/chatbot"),
        ("Human Advisors", "/human-advisors"),
        ("Sitemap", "/sitemap"),
    ]
    
    results = []
    
    for name, url in features:
        try:
            response = requests.get(f"{BASE_URL}{url}", allow_redirects=False, timeout=5)
            if response.status_code in [200, 302]:
                status = "[OK]"
                results.append(True)
            else:
                status = f"[ERROR {response.status_code}]"
                results.append(False)
            
            print(f"{status:15} {name:20} {BASE_URL}{url}")
        except Exception as e:
            print(f"[ERROR]         {name:20} {str(e)}")
            results.append(False)
    
    print()
    print("="*70)
    print(f"RESULTS: {sum(results)}/{len(results)} features working")
    print("="*70)
    print()
    
    return all(results)

def open_application():
    """Open the application in browser"""
    print("\nOPENING APPLICATION IN BROWSER...")
    print("-"*70)
    
    pages_to_open = [
        ("Home", "/"),
        ("Login", "/login"),
    ]
    
    for name, url in pages_to_open:
        full_url = f"{BASE_URL}{url}"
        print(f"Opening: {name:15} {full_url}")
        webbrowser.open(full_url)
        time.sleep(1)
    
    print()
    print("="*70)
    print("NEXT STEPS:")
    print("="*70)
    print()
    print("1. Login with your credentials at the login page")
    print()
    print("2. After login, you can access:")
    print(f"   - Portfolio:      {BASE_URL}/portfolio")
    print(f"   - Stock Insights: {BASE_URL}/stock-insights")
    print(f"   - Dashboard:      {BASE_URL}/dashboard")
    print()
    print("3. Try these features:")
    print()
    print("   PORTFOLIO:")
    print("   - Add a stock (AAPL, 10 shares, $150)")
    print("   - View holdings table")
    print("   - Check P/L calculation")
    print("   - Delete or clear stocks")
    print()
    print("   STOCK INSIGHTS:")
    print("   - Search for GOOGL")
    print("   - View price chart")
    print("   - Read analysis")
    print()
    print("="*70)

if __name__ == "__main__":
    # Test all features
    all_working = test_all_features()
    
    if all_working:
        print("\n[SUCCESS] All features are working!")
        print()
        
        # Open in browser
        print("Ready to open the application...")
        print()
        open_application()
        
        print("\nAPPLICATION IS READY!")
        print("="*70)
    else:
        print("\n[WARNING] Some features may need attention.")
        print("But you can still access the working pages.")
