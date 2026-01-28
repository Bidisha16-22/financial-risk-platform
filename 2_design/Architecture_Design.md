# System Architecture Design

## Request Flow

1. User accesses the login page.
2. Frontend sends login data to Flask backend.
3. Backend authenticates user via database.
4. User submits financial data.
5. Backend processes data using risk engine.
6. ML service predicts risk category.
7. Results are stored in the database.
8. Dashboard displays risk score and charts.

---

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Database: SQL (SQLite/PostgreSQL)
- ML: Scikit-learn
- Deployment: Docker (Beginner Cloud)
