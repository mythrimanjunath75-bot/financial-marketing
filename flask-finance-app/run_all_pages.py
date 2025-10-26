"""
Test All HTML Pages in Flask Application
Opens all linked pages and verifies they work
"""

import requests
import webbrowser
import time

BASE_URL = "http://localhost:5000"

# All pages in the application
PAGES = [
    {"name": "Home", "url": "/", "description": "Landing page with login/register"},
    {"name": "Login", "url": "/login", "description": "User login page"},
    {"name": "Register", "url": "/register", "description": "New user registration"},
    {"name": "Sitemap", "url": "/sitemap", "description": "Site navigation map"},
]

# Protected pages (require login)
PROTECTED_PAGES = [
    {"name": "Dashboard", "url": "/dashboard", "description": "Main user dashboard"},
    {"name": "Portfolio", "url": "/portfolio", "description": "Stock portfolio management"},
    {"name": "Stock Insights", "url": "/stock-insights", "description": "Real-time stock data"},
    {"name": "AI Chatbot", "url": "/chatbot", "description": "AI financial advisor"},
    {"name": "Human Advisors", "url": "/human-advisors", "description": "Free consultation requests"},
]

def test_all_pages():
    """Test all pages and show results"""
    print("="*70)
    print("TESTING ALL HTML PAGES IN FLASK APPLICATION")
    print("="*70)
    print()
    
    results = []
    
    # Test public pages
    print("PUBLIC PAGES (No login required):")
    print("-"*70)
    for page in PAGES:
        try:
            response = requests.get(f"{BASE_URL}{page['url']}")
            status = "[OK]" if response.status_code == 200 else f"[ERROR {response.status_code}]"
            results.append({**page, "status": status, "code": response.status_code})
            print(f"{status:12} {page['name']:20} {BASE_URL}{page['url']}")
            print(f"{'':12} {page['description']}")
            print()
        except Exception as e:
            results.append({**page, "status": "[ERROR]", "code": 0})
            print(f"[ERROR]      {page['name']:20} {str(e)}")
            print()
    
    # Test protected pages (will redirect to login)
    print("\nPROTECTED PAGES (Require login - will redirect):")
    print("-"*70)
    for page in PROTECTED_PAGES:
        try:
            response = requests.get(f"{BASE_URL}{page['url']}", allow_redirects=False)
            # Protected pages should redirect (302) or be accessible (200)
            if response.status_code in [200, 302]:
                status = "[OK]"
            else:
                status = f"[ERROR {response.status_code}]"
            results.append({**page, "status": status, "code": response.status_code})
            print(f"{status:12} {page['name']:20} {BASE_URL}{page['url']}")
            print(f"{'':12} {page['description']}")
            print()
        except Exception as e:
            results.append({**page, "status": "[ERROR]", "code": 0})
            print(f"[ERROR]      {page['name']:20} {str(e)}")
            print()
    
    # Summary
    print("="*70)
    print("SUMMARY")
    print("="*70)
    total_ok = sum(1 for r in results if r['status'] == '[OK]')
    total_pages = len(results)
    print(f"Total Pages: {total_pages}")
    print(f"Working:     {total_ok}")
    print(f"Success Rate: {(total_ok/total_pages)*100:.1f}%")
    print("="*70)
    
    return results

def open_all_public_pages():
    """Open all public pages in browser"""
    print("\n\nOPENING PUBLIC PAGES IN BROWSER...")
    print("-"*70)
    
    for page in PAGES:
        url = f"{BASE_URL}{page['url']}"
        print(f"Opening: {page['name']:20} {url}")
        webbrowser.open(url)
        time.sleep(0.5)  # Small delay between opens
    
    print("\nAll public pages opened in your default browser!")
    print("To access protected pages, please login first at:")
    print(f"{BASE_URL}/login")

if __name__ == "__main__":
    # Test all pages
    results = test_all_pages()
    
    # Ask to open pages
    print("\n\nWould you like to open all public pages in your browser?")
    print("Press Enter to open, or Ctrl+C to skip...")
    try:
        input()
        open_all_public_pages()
    except KeyboardInterrupt:
        print("\n\nSkipped opening pages.")
    
    print("\n\nDirect Links to All Pages:")
    print("="*70)
    print("\nPUBLIC PAGES:")
    for page in PAGES:
        print(f"  {page['name']:20} {BASE_URL}{page['url']}")
    
    print("\nPROTECTED PAGES (Login required):")
    for page in PROTECTED_PAGES:
        print(f"  {page['name']:20} {BASE_URL}{page['url']}")
    
    print("\n" + "="*70)
    print("Your Flask application is running at: " + BASE_URL)
    print("="*70)
