# Financial Risk Assessment Platform

A full-stack web application built using Flask to assess financial risk based on user inputs.  
The project follows the complete **Software Development Life Cycle (SDLC)** and demonstrates real-world industry practices including authentication, data persistence, analytics, testing, cloud deployment, monitoring, and maintenance.

---

## 🚀 Key Features

- User registration, login, logout, and password reset
- Secure session-based authentication
- Financial risk calculation based on income, debt, and credit score
- Interactive dashboard for risk assessment
- Risk history stored and retrieved from database
- REST API for risk calculation
- Manual and automated testing
- Cloud deployment with monitoring and maintenance support

---

## 🛠️ Technology Stack

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Gunicorn

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Database
- SQLite

### Testing
- Manual Testing
- Automated Testing using PyTest

### Deployment & Monitoring
- Render Cloud Platform
- Gunicorn production server
- Application logging
- Health check endpoint

---

## 📂 Project Structure

financial-risk-platform/
│
├── 1_requirements/ # Requirement analysis documents
├── 2_design/ # System design (HLD & LLD)
├── 3_development/ # Application source code
│ └── backend/
│ ├── app/
│ ├── instance/
│ ├── run.py
│ ├── config.py
│ └── requirements.txt
├── 4_testing/ # Manual & automated testing
├── venv/ # Virtual environment (local)
└── README.md


---

## ⚙️ Application Workflow

1. User registers or logs in
2. User accesses dashboard
3. User enters financial details
4. System calculates financial risk
5. Risk result is displayed
6. Risk history is saved and shown in dashboard

---

## 🧪 Testing

### Manual Testing
- Test cases documented
- Test plan and test report created

### Automated Testing
- Authentication tests
- Dashboard access tests
- Risk calculation tests

All automated tests pass successfully.

---

## ☁️ Cloud Deployment

- Application is deployed on **Render**
- Automatic build and redeploy on GitHub commits
- Production server managed by Gunicorn
- Public URL provided by Render

---

## 📊 Monitoring & Maintenance

### Monitoring
- Real-time application logs via Render dashboard
- Request and error tracking
- Health check endpoint (`/health`)
- Automatic service restart (self-healing)

### Maintenance
- Bug fixes through Git commits
- Dependency updates via `requirements.txt`
- Continuous redeployment on code changes
- UI and performance improvements

---

## 🔐 Security Considerations

- Session-based authentication
- Secure password handling
- Environment-based configuration support
- Access control using login-required routes

---

## 🎓 SDLC Coverage

✔ Requirement Analysis  
✔ System Design (HLD & LLD)  
✔ Development  
✔ Testing  
✔ Deployment  
✔ Monitoring  
✔ Maintenance  

---

## 👩‍💻 Author

**Bidisha Bhattacharjee**  
Final Year Project — Financial Risk Assessment Platform  

---

## 📌 Note

This project is developed for academic and learning purposes and demonstrates real-life industry-level full-stack development practices.
