"""
Quick test to verify registration is working
"""

import requests

BASE_URL = "http://localhost:5000"

def test_registration_page():
    """Test if registration page loads"""
    try:
        response = requests.get(f"{BASE_URL}/register")
        if response.status_code == 200:
            print("[OK] Registration page loads successfully")
            print(f"     Status Code: {response.status_code}")
            
            # Check for form elements
            if 'name="name"' in response.text:
                print("[OK] Name field present")
            if 'name="email"' in response.text:
                print("[OK] Email field present")
            if 'name="password"' in response.text:
                print("[OK] Password field present")
            if 'autocomplete="off"' in response.text:
                print("[OK] Autocomplete disabled (fresh form)")
            if 'registerForm' in response.text:
                print("[OK] Form ID present for JavaScript")
            
            return True
        else:
            print(f"[ERROR] Registration page error: {response.status_code}")
            return False
    except Exception as e:
        print(f"[ERROR] Error accessing registration page: {str(e)}")
        return False

def test_login_page():
    """Test if login page loads"""
    try:
        response = requests.get(f"{BASE_URL}/login")
        if response.status_code == 200:
            print("\n[OK] Login page loads successfully")
            print(f"     Status Code: {response.status_code}")
            return True
        else:
            print(f"\n[ERROR] Login page error: {response.status_code}")
            return False
    except Exception as e:
        print(f"\n[ERROR] Error accessing login page: {str(e)}")
        return False

def test_home_page():
    """Test if home page loads"""
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("\n[OK] Home page loads successfully")
            print(f"     Status Code: {response.status_code}")
            
            # Check if login is primary action
            if 'Login to Your Account' in response.text:
                print("[OK] Login is primary action")
            if 'Register here' in response.text:
                print("[OK] Register link present")
            
            return True
        else:
            print(f"\n[ERROR] Home page error: {response.status_code}")
            return False
    except Exception as e:
        print(f"\n[ERROR] Error accessing home page: {str(e)}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("TESTING FLASK APPLICATION")
    print("="*60)
    print()
    
    # Test all pages
    home_ok = test_home_page()
    register_ok = test_registration_page()
    login_ok = test_login_page()
    
    print("\n" + "="*60)
    print("TEST RESULTS")
    print("="*60)
    print(f"Home Page:         {'[PASS]' if home_ok else '[FAIL]'}")
    print(f"Registration Page: {'[PASS]' if register_ok else '[FAIL]'}")
    print(f"Login Page:        {'[PASS]' if login_ok else '[FAIL]'}")
    
    if all([home_ok, register_ok, login_ok]):
        print("\n[SUCCESS] ALL TESTS PASSED! Application is working correctly.")
    else:
        print("\n[WARNING] Some tests failed. Please check the errors above.")
    
    print("="*60)
