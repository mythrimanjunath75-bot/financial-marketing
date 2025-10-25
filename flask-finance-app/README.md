# AI Personal Finance - Flask Application

A full-stack Flask application for personal finance management with AI-powered insights, portfolio tracking, and financial advice.

## Features

- 📊 **Financial Health Score** - Calculate your financial health based on income, savings, and debt
- 💼 **Portfolio Management** - Track your stock investments with real-time data
- 📈 **Stock Insights** - Get live stock data and 30-day price charts
- 🤖 **AI Financial Advisor** - Chat with an AI bot for personalized financial advice
- 👤 **User Authentication** - Secure registration and login system

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Database**: SQLite3
- **APIs**: Yahoo Finance (yfinance)
- **Charts**: Chart.js

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project directory:**
   ```bash
   cd flask-finance-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   ```bash
   python database.py
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:5000`

## Usage

1. **Register** a new account with your financial information
2. **Login** to access your dashboard
3. **View Dashboard** to see your financial health score
4. **Add Stocks** to your portfolio and track performance
5. **Get Stock Insights** with real-time data and charts
6. **Chat with AI Advisor** for financial guidance

## Project Structure

```
flask-finance-app/
├── app.py                 # Main Flask application
├── database.py            # Database initialization and management
├── requirements.txt       # Python dependencies
├── finance.db            # SQLite database (created on first run)
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── portfolio.html
│   ├── stock_insights.html
│   └── chatbot.html
└── README.md
```

## Database Schema

### Users Table
- id, name, email, password, age, income, savings, debt, risk_level, created_at

### Portfolio Table
- id, user_id, symbol, quantity, purchase_price, purchase_date

### Chat History Table
- id, user_id, message, reply, timestamp

## API Endpoints

- `GET /` - Home page
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout
- `GET /dashboard` - User dashboard with financial health score
- `GET/POST /portfolio` - Portfolio management
- `GET /portfolio/delete/<id>` - Delete portfolio holding
- `GET/POST /stock-insights` - Stock data and insights
- `GET/POST /chatbot` - AI chatbot interface
- `POST /api/chat` - Chat API endpoint

## Financial Health Score Calculation

```python
score = ((savings - debt) / income) * 100
```

- **Excellent**: 70-100
- **Good**: 40-69
- **Needs Improvement**: 0-39

## Notes

- Stock data is fetched in real-time using Yahoo Finance API
- The chatbot uses rule-based responses (can be upgraded to OpenAI/Gemini)
- All data is stored locally in SQLite database
- This is a prototype - not actual financial advice

## Future Enhancements

- [ ] Integrate OpenAI/Gemini for advanced AI responses
- [ ] Add expense tracking
- [ ] Create budget planning features
- [ ] Add data visualization for spending trends
- [ ] Implement email notifications
- [ ] Add export functionality (PDF reports)
- [ ] Multi-currency support

## License

MIT License - Free to use for educational purposes

## Disclaimer

This application is for educational purposes only. It does not provide actual financial advice. Always consult with a certified financial advisor for real financial decisions.
