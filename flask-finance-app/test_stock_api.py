"""
Test Stock Data API (Yahoo Finance)
"""

import yfinance as yf

def test_stock_api():
    """Test if Yahoo Finance API is working"""
    print("="*60)
    print("TESTING STOCK DATA API (Yahoo Finance)")
    print("="*60)
    print()
    
    test_symbols = ['AAPL', 'GOOGL', 'MSFT']
    
    for symbol in test_symbols:
        print(f"Testing {symbol}...")
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period='1d')
            
            if not data.empty:
                current_price = data['Close'].iloc[-1]
                open_price = data['Open'].iloc[-1]
                change = current_price - open_price
                
                print(f"  [OK] {symbol}")
                print(f"       Current Price: ${current_price:.2f}")
                print(f"       Open Price: ${open_price:.2f}")
                print(f"       Change: ${change:.2f}")
                
                # Try to get company name
                try:
                    info = stock.info
                    company_name = info.get('longName', symbol)
                    print(f"       Company: {company_name}")
                except:
                    print(f"       Company: {symbol} (name unavailable)")
            else:
                print(f"  [WARNING] No data returned for {symbol}")
        except Exception as e:
            print(f"  [ERROR] {symbol}: {str(e)}")
        print()
    
    print("="*60)
    print("API TEST COMPLETE")
    print("="*60)
    print()
    print("If all stocks show [OK], the API is working!")
    print("If errors occur, it might be:")
    print("  - Internet connection issue")
    print("  - Yahoo Finance API temporarily unavailable")
    print("  - Invalid stock symbol")
    print()
    print("Try these valid symbols:")
    print("  AAPL, GOOGL, MSFT, TSLA, AMZN, META, NVDA")

if __name__ == "__main__":
    test_stock_api()
