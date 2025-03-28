🚀 Mini Query Engine (FastAPI Backend)
This is a lightweight backend service that simulates an AI-powered data query system. It translates natural language queries into pseudo-SQL and returns mock responses.

🛠️ Features
- Natural Language Query Processing (/query)
- Query Explanation (/explain)
- Query Validation (/validate)
- Mock Database Connection (SQLite/In-Memory)
- Basic Error Handling & Authentication

📌 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Saijasi/mini-query-engine.git
cd mini-query-engine

2️⃣ Create & Activate a Virtual Environment
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the FastAPI Server
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000

📌 API Endpoints
🔹 1. Query Processing
Endpoint: POST /query
-Request Body:
{
  "query": "Show total sales for January"
}
-Response:
{
  "sql": "SELECT SUM(sales) FROM orders WHERE month='January'",
  "result": 150000
}

🔹 2. Query Explanation
Endpoint: POST /explain
-Response:
{
  "query": "Show total sales for January",
  "translated_sql": "SELECT SUM(sales) FROM orders WHERE month='January'",
  "breakdown": "Fetching total sales from the orders table for January"
}

🔹 3. Query Validation
Endpoint: POST /validate
-Response:
{
  "query": "Show total sales for January",
  "valid": true,
  "message": "Query can be executed."
}

📌 Deployment (Render)
-Push your code to GitHub
-Go to Render → New Web Service
-Connect GitHub Repository
-Set up the environment:
-Build Command:
pip install -r requirements.txt
-Start Command:
uvicorn main:app --host 0.0.0.0 --port 10000
-Deploy & Get Public API URL 🎉


