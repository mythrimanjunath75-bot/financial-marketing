# Website Structure - Flask Finance Application

## Complete Page Flow & Navigation

### Public Pages (No Login Required)
```
┌─────────────────────────────────────────────────────────────┐
│                      HOME PAGE (/)                           │
│  - Welcome message                                           │
│  - Feature highlights                                        │
│  - "Start Your Financial Journey" → Register                │
│  - "Login here" link → Login                                │
└─────────────────────────────────────────────────────────────┘
                    ↓                           ↓
        ┌──────────────────┐        ┌──────────────────┐
        │  REGISTER (/register)      │  LOGIN (/login)  │
        │  - Create account  │        │  - Email/Pass    │
        │  - Financial info  │        │  - Auth check    │
        └──────────────────┘        └──────────────────┘
                    ↓                           ↓
                    └───────────┬───────────────┘
                                ↓
                        User Logged In
                                ↓
```

### Authenticated Pages (Login Required)
```
┌──────────────────────────────────────────────────────────────────┐
│                    NAVIGATION BAR (All Pages)                     │
│  [Dashboard] [Portfolio] [Stock Insights] [AI Advisor]           │
│  [Human Advisors] [Logout]                                       │
└──────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   DASHBOARD (/dashboard)                         │
│  - Financial Health Score                                        │
│  - Financial Summary (Income, Savings, Debt)                     │
│  - Quick Actions: → Portfolio, Stock Insights, AI Advisor,       │
│                     Human Advisors                               │
│  - Financial Tips                                                │
└─────────────────────────────────────────────────────────────────┘
         ↓              ↓               ↓                ↓
    ┌────────┐    ┌──────────┐   ┌──────────┐    ┌──────────────┐
    │PORTFOLIO│    │  STOCK   │   │    AI    │    │    HUMAN     │
    │         │    │ INSIGHTS │   │  ADVISOR │    │   ADVISORS   │
    └────────┘    └──────────┘   └──────────┘    └──────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   PORTFOLIO (/portfolio)                         │
│  - Total Investment, Current Value, P/L                          │
│  - Add Stock Form                                                │
│  - Holdings Table (Symbol, Quantity, Prices, P/L)                │
│  - Delete Holdings                                               │
│  - Links: → Stock Insights (for stock data)                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              STOCK INSIGHTS (/stock-insights)                    │
│  - Search Stock Form                                             │
│  - Real-time Stock Price & Change                                │
│  - 30-Day Price Chart (Chart.js)                                 │
│  - Investment Tips & Analysis                                    │
│  - Links: → Portfolio (to add stock)                             │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   CHATBOT (/chatbot)                             │
│  - AI Chat Interface                                             │
│  - Chat History Display                                          │
│  - Quick Question Buttons                                        │
│  - Real-time Chat (AJAX)                                         │
│  - Links: → Human Advisors (for expert help)                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              HUMAN ADVISORS (/human-advisors)                    │
│  - Benefits Section (Free, Certified, Confidential)              │
│  - Consultation Request Form                                     │
│  - Request History Table                                         │
│  - FAQ Section                                                   │
│  - Links: → Dashboard, AI Advisor                                │
└─────────────────────────────────────────────────────────────────┘
```

## Navigation Links Map

### Header Navigation (base.html)
- **Logo** → Home (/)
- **Dashboard** → /dashboard
- **Portfolio** → /portfolio
- **Stock Insights** → /stock-insights
- **AI Advisor** → /chatbot
- **Human Advisors** → /human-advisors
- **Logout** → /logout → Home

### Internal Page Links

#### Home Page
- "Start Your Financial Journey" button → /register
- "Login here" link → /login

#### Dashboard
- "View Portfolio" button → /portfolio
- "Stock Insights" button → /stock-insights
- "Get AI Advice" button → /chatbot
- "Talk to Human Advisors (FREE)" button → /human-advisors

#### Portfolio
- Each stock symbol → Can link to /stock-insights (for analysis)
- "Delete" button → /portfolio/delete/<id>

#### Stock Insights
- Search results → Display on same page
- Can navigate to → /portfolio to add stocks

#### AI Chatbot
- Chat interface → /api/chat (AJAX endpoint)
- Quick questions → Pre-fill chat input

#### Human Advisors
- Form submission → Same page with success message
- Previous requests → Display in table

## URL Routing Structure

| URL Route              | Template File         | Purpose                           |
|------------------------|-----------------------|-----------------------------------|
| `/`                    | home.html             | Landing page                      |
| `/register`            | register.html         | User registration                 |
| `/login`               | login.html            | User login                        |
| `/logout`              | (redirect)            | Logout & return to home           |
| `/dashboard`           | dashboard.html        | Main user dashboard               |
| `/portfolio`           | portfolio.html        | Portfolio management              |
| `/portfolio/delete/<id>`| (redirect)           | Delete stock holding              |
| `/stock-insights`      | stock_insights.html   | Stock data & charts               |
| `/chatbot`             | chatbot.html          | AI financial advisor              |
| `/api/chat`            | (JSON API)            | Chat endpoint                     |
| `/human-advisors`      | advisors.html         | Human advisor consultation        |

## Session Flow

1. **New User**: Home → Register → Login → Dashboard
2. **Returning User**: Home → Login → Dashboard
3. **Logged In**: Access any authenticated page via navigation
4. **Logout**: Any page → Logout → Home

## Database Connections

- **Users** ← Dashboard, Portfolio, Chatbot, Human Advisors
- **Portfolio** ← Portfolio page, Stock Insights
- **Chat History** ← Chatbot
- **Advisor Requests** ← Human Advisors

## All Pages Are Linked Via:

1. **Navigation Menu** (base.html) - Available on all pages
2. **Quick Action Buttons** (dashboard.html) - Main hub
3. **Form Submissions** - POST requests with redirects
4. **Internal Links** - Cross-references between pages
5. **Session Management** - Login/logout flow

## Access Your Complete Website

**URL**: http://localhost:5000

All 9 pages are interconnected and accessible through navigation!
