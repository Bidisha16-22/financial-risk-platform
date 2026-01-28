# Software Requirements Specification (SRS)

## 1. Introduction
The Financial Risk Assessment System is a cloud-ready, full-stack web application developed using the Flask framework. The system helps assess the financial risk of users based on their financial inputs such as income, debt, and credit score.

The application follows the complete Software Development Life Cycle (SDLC), including requirement analysis, system design, development, testing, deployment, monitoring, and maintenance.

---

## 2. Purpose
The purpose of this system is to:
- Provide an automated financial risk evaluation
- Support rule-based and ML-based risk prediction
- Store user and risk data securely
- Provide dashboards and reports for analysis

---

## 3. Scope
The system includes:
- User registration and login
- Financial data input
- Risk score calculation
- Visualization using charts
- SQL-based data storage
- Monitoring and logging support

The system is designed to be beginner-friendly and cloud-deployable without dependency on advanced cloud services.

---

## 4. Definitions and Acronyms
- SDLC: Software Development Life Cycle  
- API: Application Programming Interface  
- ML: Machine Learning  
- DB: Database  

---

## 5. Stakeholders
- End Users
- System Administrator
- Project Evaluators
- Developers

---

## 6. Overall Description
The system is a Flask-based web application using server-side rendering with HTML templates and static assets. The backend processes user requests, performs risk calculations, and stores data in a SQL database.

---

## 7. Assumptions
- Users have internet access
- System is deployed in a controlled environment
- Data provided by users is assumed to be valid

---

## 8. Constraints
- Flask framework must be used
- SQL database must be used
- Beginner-friendly cloud deployment
