# 🚀 User Flow - AI Personal Finance Application

## 📊 Complete Navigation Flow

```
┌─────────────────────────────────────────────────────────────┐
│                        HOME PAGE                             │
│                    (Landing Page)                            │
│                  http://localhost:5000/                      │
│                                                              │
│  Features Display:                                           │
│  - Financial Health Score                                    │
│  - Smart Portfolio                                           │
│  - AI Financial Advisor                                      │
│                                                              │
│  Primary Action:                                             │
│  🔵 [Login to Your Account] Button                          │
│                                                              │
│  Secondary Link:                                             │
│  "Don't have an account? Register here" → Register          │
└─────────────────────────────────────────────────────────────┘
                          ↓
                    Click "Login"
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                      LOGIN PAGE                              │
│               http://localhost:5000/login                    │
│                                                              │
│  Form Fields:                                                │
│  - Email Address                                             │
│  - Password                                                  │
│                                                              │
│  🔵 [Login] Button                                          │
│                                                              │
│  Link at bottom:                                             │
│  "Don't have an account? Register here" → Register          │
└─────────────────────────────────────────────────────────────┘
                          ↓
              If no account, click "Register"
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    REGISTER PAGE                             │
│              http://localhost:5000/register                  │
│                                                              │
│  Form Fields:                                                │
│  - Full Name                                                 │
│  - Email Address                                             │
│  - Password                                                  │
│  - Age (optional)                                            │
│  - Risk Level                                                │
│  - Monthly Income                                            │
│  - Total Savings                                             │
│  - Total Debt                                                │
│                                                              │
│  🔵 [Register] Button                                       │
│                                                              │
│  Link at bottom:                                             │
│  "Already have an account? Login here" → Login              │
└─────────────────────────────────────────────────────────────┘
                          ↓
              Registration successful → Redirects to Login
                          ↓
              User logs in with credentials
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                      DASHBOARD                               │
│             http://localhost:5000/dashboard                  │
│                    (Main User Hub)                           │
│                                                              │
│  Displays:                                                   │
│  - Financial Health Score (with status)                      │
│  - Financial Summary (Income, Savings, Debt)                 │
│  - Quick Action Buttons                                      │
│  - Financial Tips                                            │
│                                                              │
│  Navigation Menu (Available on ALL pages):                   │
│  [Dashboard] [Portfolio] [Stock Insights] [AI Advisor]       │
│  [Human Advisors] [Logout]                                   │
└─────────────────────────────────────────────────────────────┘
         ↓              ↓              ↓              ↓
    ┌────────┐    ┌──────────┐   ┌──────────┐   ┌───────────┐
    │        │    │          │   │          │   │           │
    ↓        ↓    ↓          ↓   ↓          ↓   ↓           ↓

┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  PORTFOLIO   │ │STOCK INSIGHTS│ │   CHATBOT    │ │    HUMAN     │
│              │ │              │ │  (AI Advisor)│ │   ADVISORS   │
│ /portfolio   │ │/stock-insights│ │  /chatbot   │ │/human-advisors│
│              │ │              │ │              │ │              │
│ Features:    │ │ Features:    │ │ Features:    │ │ Features:    │
│ - Add stocks │ │ - Search     │ │ - Chat       │ │ - Request    │
│ - View P/L   │ │ - Real-time  │ │ - AI tips    │ │   consultation│
│ - Delete     │ │ - Charts     │ │ - History    │ │ - View       │
│ - Clear all  │ │ - Analysis   │ │ - Quick Qs   │ │   requests   │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
       ↑                ↑                ↑                ↑
       └────────────────┴────────────────┴────────────────┘
              All accessible from Navigation Menu
```

## 🎯 Detailed User Journey

### **1. First-Time User**

```
Step 1: Home Page
  ↓ Click "Login to Your Account"
  
Step 2: Login Page
  ↓ Click "Don't have an account? Register here"
  
Step 3: Register Page
  ↓ Fill form and submit
  ↓ Auto-redirect to Login
  
Step 4: Login Page
  ↓ Enter email & password
  ↓ Click "Login"
  
Step 5: Dashboard (Logged In)
  ↓ Now access all features via navigation menu
```

### **2. Returning User**

```
Step 1: Home Page
  ↓ Click "Login to Your Account"
  
Step 2: Login Page
  ↓ Enter email & password
  ↓ Click "Login"
  
Step 3: Dashboard (Logged In)
  ↓ Access all features
```

---

## 📋 Feature Access Flow

Once logged in, users can access features in this order:

### **From Dashboard → Features**

```
DASHBOARD
    ├─→ PORTFOLIO (Track investments)
    │   └─→ Add/View/Delete stocks
    │   └─→ Real-time prices & P/L
    │
    ├─→ STOCK INSIGHTS (Market research)
    │   └─→ Search stocks
    │   └─→ View charts & analysis
    │
    ├─→ CHATBOT (AI Advisor)
    │   └─→ Ask financial questions
    │   └─→ Get AI recommendations
    │
    └─→ HUMAN ADVISORS (Expert consultation)
        └─→ Request free consultation
        └─→ View request history
```

---

## 🔄 Complete Page Flow Map

| Step | Page | URL | Next Action |
|------|------|-----|-------------|
| 1 | **Home** | `/` | Click "Login" button |
| 2 | **Login** | `/login` | Enter credentials OR click "Register" |
| 3 | **Register** | `/register` | Fill form, submit → redirects to Login |
| 4 | **Login** | `/login` | Login with new account |
| 5 | **Dashboard** | `/dashboard` | Choose feature from nav or quick actions |
| 6a | **Portfolio** | `/portfolio` | Add/manage stocks |
| 6b | **Stock Insights** | `/stock-insights` | Research stocks |
| 6c | **Chatbot** | `/chatbot` | Ask AI questions |
| 6d | **Human Advisors** | `/human-advisors` | Request consultation |

---

## 🌐 Navigation Structure

### **Top Navigation Menu** (Available after login)
```
┌──────────────────────────────────────────────────────────────┐
│ [Logo] Dashboard | Portfolio | Stock Insights | AI Advisor   │
│        Human Advisors | Logout                               │
└──────────────────────────────────────────────────────────────┘
```

### **Dashboard Quick Actions**
```
┌──────────────────────────────────────────────────────────────┐
│                    Quick Actions                              │
│                                                               │
│  [View Portfolio] [Stock Insights] [Get AI Advice]           │
│  [Talk to Human Advisors (FREE)]                             │
└──────────────────────────────────────────────────────────────┘
```

---

## 🎯 Key User Paths

### **Path 1: New Investor**
```
Home → Login → Register → Login → Dashboard → Portfolio → Add Stocks
```

### **Path 2: Research Mode**
```
Home → Login → Dashboard → Stock Insights → Search Stock → View Charts
```

### **Path 3: Get Advice**
```
Home → Login → Dashboard → AI Chatbot → Ask Question → Get Response
```

### **Path 4: Expert Help**
```
Home → Login → Dashboard → Human Advisors → Fill Form → Submit Request
```

---

## 📱 All Available URLs

| Page | URL |
|------|-----|
| Home | http://localhost:5000 |
| Login | http://localhost:5000/login |
| Register | http://localhost:5000/register |
| Dashboard | http://localhost:5000/dashboard |
| Portfolio | http://localhost:5000/portfolio |
| Stock Insights | http://localhost:5000/stock-insights |
| AI Chatbot | http://localhost:5000/chatbot |
| Human Advisors | http://localhost:5000/human-advisors |
| Sitemap | http://localhost:5000/sitemap |
| Logout | http://localhost:5000/logout |

---

## ✅ Summary

**Primary Flow:**
1. **Home** → Login button
2. **Login** → "Don't have account?" link
3. **Register** → Submit form
4. **Login** → With credentials
5. **Dashboard** → Access all features
6. **Portfolio** → Manage investments
7. **Stock Insights** → Research stocks
8. **Chatbot** → Get AI advice
9. **Human Advisors** → Expert consultation

**All features accessible from navigation menu once logged in!**
