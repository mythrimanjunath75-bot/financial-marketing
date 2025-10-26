# 📊 How to Use Portfolio & Stock Insights

## 🎯 Quick Start Guide

### **STEP 1: Register & Login**

#### If you're a NEW USER:
1. Open: http://localhost:5000
2. Click **"Don't have an account? Register here"**
3. Fill the registration form:
   - Name: Your name
   - Email: your.email@example.com
   - Password: (minimum 6 characters)
   - Monthly Income: e.g., 5000
   - Total Savings: e.g., 10000
   - Total Debt: e.g., 2000 (or 0 if no debt)
4. Click **"Register"**
5. You'll be redirected to Login page
6. Enter your email and password
7. Click **"Login"**

#### If you ALREADY HAVE an account:
1. Open: http://localhost:5000/login
2. Enter your email and password
3. Click **"Login"**

---

## 💼 HOW TO USE PORTFOLIO

**Direct Link:** http://localhost:5000/portfolio

### **What You Can Do:**

#### ✅ **1. Add Stocks to Your Portfolio**

**Step-by-Step:**
1. After login, click **"Portfolio"** in the top menu
2. Find the "Add Stock to Portfolio" form
3. Fill in the details:
   - **Stock Symbol**: Enter ticker (e.g., AAPL, GOOGL, MSFT, TSLA)
   - **Quantity**: How many shares (e.g., 10)
   - **Purchase Price**: Price per share (e.g., 150.50)
   - **Purchase Date**: When you bought it (e.g., 2024-01-15)
4. Click **"Add"** button

**Valid Stock Symbols to Try:**
```
AAPL  - Apple Inc.
GOOGL - Alphabet (Google)
MSFT  - Microsoft
TSLA  - Tesla
AMZN  - Amazon
META  - Meta (Facebook)
NVDA  - NVIDIA
JPM   - JPMorgan Chase
```

#### ✅ **2. View Your Holdings Table**

Once you add stocks, you'll see a table showing:
- **Symbol**: Stock ticker
- **Quantity**: Number of shares you own
- **Purchase Price**: What you paid per share
- **Current Price**: Today's price (real-time or sample)
- **Investment**: Total amount invested
- **Current Value**: Current worth of your shares
- **Profit/Loss**: How much you've gained or lost
- **P/L %**: Profit/loss percentage
- **Actions**: Delete button for each stock

#### ✅ **3. View Total Summary**

At the top of the page, you'll see cards showing:
- **Total Investment**: How much money you've put in
- **Current Value**: What your portfolio is worth now
- **Total Profit/Loss**: Overall gain or loss
  - Green = Profit
  - Red = Loss

#### ✅ **4. Delete Stocks**

**Delete Individual Stock:**
- Click the **trash icon** (🗑️) next to any stock
- Stock is removed immediately

**Clear All Stocks:**
- Click the **"Clear All"** button (red button at top right)
- Confirms before deleting
- Removes ALL stocks from your portfolio

---

## 📈 HOW TO USE STOCK INSIGHTS

**Direct Link:** http://localhost:5000/stock-insights

### **What You Can Do:**

#### ✅ **1. Search for Any Stock**

**Step-by-Step:**
1. After login, click **"Stock Insights"** in the top menu
2. Find the search box
3. Enter a stock symbol (e.g., AAPL)
4. Click **"Search"** button
5. Results appear below!

**What You'll See:**
- Company Name
- Current Stock Price
- Price Change (up or down)
- 30-day Price Chart

#### ✅ **2. View Real-Time Data**

The stock card shows:
- **Symbol & Company Name**
- **Current Price**: Latest price
- **Today's Change**: 
  - Green (↑) = Stock went up
  - Red (↓) = Stock went down

#### ✅ **3. Analyze Price Charts**

**Interactive Chart Features:**
- Hover over chart to see exact prices
- View 30-day price trend
- Identify price patterns
- Compare historical performance

#### ✅ **4. Get Investment Tips**

Below the chart, you'll find:
- **Investment Analysis**: AI-generated insights
- **Tips & Recommendations**: What to consider
- **Risk Assessment**: Investment considerations

---

## 🎯 EXAMPLE WORKFLOWS

### **Workflow 1: Build Your First Portfolio**

```
1. Login to your account
   ↓
2. Go to Portfolio page
   ↓
3. Add first stock:
   - Symbol: AAPL
   - Quantity: 10
   - Purchase Price: 150
   - Date: Today
   ↓
4. Add second stock:
   - Symbol: GOOGL
   - Quantity: 5
   - Purchase Price: 120
   - Date: Today
   ↓
5. View your total investment and P/L
   ↓
6. Done! Your portfolio is created
```

### **Workflow 2: Research Before Buying**

```
1. Login to your account
   ↓
2. Go to Stock Insights
   ↓
3. Search for TSLA
   ↓
4. Review the price chart
   ↓
5. Read the analysis and tips
   ↓
6. Decide if you want to buy
   ↓
7. If yes, go to Portfolio and add it!
```

### **Workflow 3: Track Your Investments**

```
1. Login daily/weekly
   ↓
2. Check Portfolio page
   ↓
3. See updated prices
   ↓
4. Check if you're in profit or loss
   ↓
5. Research any stock in Stock Insights
   ↓
6. Decide to hold, sell, or buy more
```

---

## 📋 QUICK REFERENCE

### **Portfolio Features:**

| Feature | How to Use | Location |
|---------|-----------|----------|
| **Add Stock** | Fill form at top | Portfolio page |
| **View Holdings** | Scroll down | Portfolio page |
| **See P/L** | Check colored numbers | Portfolio page |
| **Delete Stock** | Click trash icon | Next to each stock |
| **Clear All** | Click red button | Top right of form |

### **Stock Insights Features:**

| Feature | How to Use | Location |
|---------|-----------|----------|
| **Search Stock** | Enter symbol, click search | Top of page |
| **View Price** | After searching | Stock card |
| **See Chart** | Scroll down | Below stock card |
| **Get Tips** | Read text below chart | Bottom of page |

---

## 💡 PRO TIPS

### **For Portfolio:**
- ✅ **Start small**: Add 2-3 stocks first
- ✅ **Use real symbols**: Check Yahoo Finance for correct tickers
- ✅ **Track regularly**: Check weekly to see performance
- ✅ **Diversify**: Don't put all money in one stock
- ✅ **Keep records**: Note why you bought each stock

### **For Stock Insights:**
- ✅ **Research first**: Always check insights before buying
- ✅ **Compare stocks**: Search multiple stocks to compare
- ✅ **Watch trends**: Look for upward or downward patterns
- ✅ **Read tips**: Pay attention to the analysis provided
- ✅ **Use chart**: Hover on chart for detailed price info

---

## 🚨 IMPORTANT NOTES

### **About Stock Prices:**
- Prices are fetched from Yahoo Finance
- If API is down, sample prices shown
- Check the info alert at top of page
- Sample data is for demonstration only

### **About Data Accuracy:**
- Real-time data when API works
- Sample data shown with warning icon
- Calculations are always accurate
- Use for learning and tracking only

### **Not Financial Advice:**
- This is a demonstration app
- For educational purposes only
- Consult real financial advisor for investments
- Don't make real investment decisions based solely on this app

---

## 🔗 QUICK LINKS

| Page | URL | Purpose |
|------|-----|---------|
| **Home** | http://localhost:5000 | Start here |
| **Login** | http://localhost:5000/login | Sign in |
| **Register** | http://localhost:5000/register | Create account |
| **Portfolio** | http://localhost:5000/portfolio | Manage investments |
| **Stock Insights** | http://localhost:5000/stock-insights | Research stocks |
| **Dashboard** | http://localhost:5000/dashboard | Financial overview |

---

## ❓ TROUBLESHOOTING

### **"I can't access Portfolio/Stock Insights"**
- **Solution**: You must be logged in. Go to login page first.

### **"No stocks showing in Portfolio"**
- **Solution**: Add stocks using the form at top of Portfolio page.

### **"Stock search returns no results"**
- **Solution**: 
  - Check symbol spelling (e.g., AAPL not Apple)
  - Use uppercase letters
  - Try common stocks: AAPL, GOOGL, MSFT

### **"Prices don't look right"**
- **Solution**: 
  - Check for warning icon (sample data)
  - API might be temporarily down
  - Sample data is shown for demonstration

### **"Can't delete a stock"**
- **Solution**: 
  - Make sure you're logged in
  - Click the trash icon, not the row
  - Refresh page if needed

---

## 📞 NEED HELP?

### **How to Get Started:**
1. Open: http://localhost:5000
2. Register/Login
3. Click "Portfolio" or "Stock Insights"
4. Follow the on-screen instructions

### **Example Test Data:**
```
Test User Registration:
- Name: John Doe
- Email: test@example.com
- Password: test123
- Income: 5000
- Savings: 10000
- Debt: 2000

Test Stock to Add:
- Symbol: AAPL
- Quantity: 10
- Price: 150
- Date: 2024-01-01
```

---

## ✅ SUCCESS CHECKLIST

- [ ] I registered an account
- [ ] I logged in successfully
- [ ] I can see the Portfolio page
- [ ] I added at least one stock
- [ ] I can see my stock in the holdings table
- [ ] I can see the P/L calculation
- [ ] I searched for a stock in Stock Insights
- [ ] I can see the price chart
- [ ] I understand how to delete stocks
- [ ] I know how to add more stocks

---

**Your Portfolio and Stock Insights are fully functional! Start using them now!** 🚀

**Direct Link to Login:** http://localhost:5000/login
