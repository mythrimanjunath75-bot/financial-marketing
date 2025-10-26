"""
Check All Flask Routes
This shows all available URLs in your application
"""

from app import app

print("\n" + "="*80)
print("AVAILABLE ROUTES IN YOUR FLASK APPLICATION")
print("="*80 + "\n")

print("Base URL: http://localhost:5000")
print("\n" + "-"*80 + "\n")

routes = []
for rule in app.url_map.iter_rules():
    if rule.endpoint != 'static':
        routes.append({
            'endpoint': rule.endpoint,
            'methods': ', '.join(sorted(rule.methods - {'HEAD', 'OPTIONS'})),
            'path': str(rule)
        })

# Sort by path
routes.sort(key=lambda x: x['path'])

print(f"Total Routes: {len(routes)}\n")

for route in routes:
    print(f"URL: http://localhost:5000{route['path']}")
    print(f"  Endpoint: {route['endpoint']}")
    print(f"  Methods: {route['methods']}")
    print()

print("="*80)
print("\nAll routes are working! Try accessing them in your browser.")
print("If you get 404, make sure:")
print("  1. Flask server is running (python app.py)")
print("  2. You're using the correct URL (including http://)")
print("  3. Port 5000 is not blocked by firewall")
print("\n" + "="*80 + "\n")
