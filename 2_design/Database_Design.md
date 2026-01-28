# Database Design

## 1. User Table

| Column Name | Data Type | Description |
|------------|----------|-------------|
| id | Integer (PK) | Unique user ID |
| email | String | User email |
| password | String | Encrypted password |
| created_at | Timestamp | Account creation time |

---

## 2. Risk_Record Table

| Column Name | Data Type | Description |
|------------|----------|-------------|
| id | Integer (PK) | Record ID |
| user_id | Integer (FK) | Reference to User |
| income | Float | Annual income |
| debt | Float | Total debt |
| credit_score | Integer | Credit score |
| risk_level | String | Risk category |
| created_at | Timestamp | Record time |

---

## 3. Relationships
- One User → Many Risk Records
