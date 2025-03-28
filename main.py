from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Create FastAPI instance
app = FastAPI()

# In-memory SQLite database for demo
conn = sqlite3.connect(":memory:", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35)
])
conn.commit()

class QueryRequest(BaseModel):
    natural_query: str

def translate_to_sql(natural_query: str) -> str:
    """Simple rule-based conversion of natural language queries to SQL."""
    if "list all users" in natural_query.lower():
        return "SELECT * FROM users;"
    elif "find user named" in natural_query.lower():
        name = natural_query.split("named")[-1].strip()
        return f"SELECT * FROM users WHERE name = '{name}';"
    else:
        return ""

@app.post("/query")
async def query(request: QueryRequest):
    sql_query = translate_to_sql(request.natural_query)
    if not sql_query:
        raise HTTPException(status_code=400, detail="Query could not be translated.")
    
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return {"query": sql_query, "result": result}

@app.post("/explain")
async def explain(request: QueryRequest):
    sql_query = translate_to_sql(request.natural_query)
    if not sql_query:
        raise HTTPException(status_code=400, detail="Cannot explain query.")
    
    return {"natural_query": request.natural_query, "translated_sql": sql_query}

@app.post("/validate")
async def validate(request: QueryRequest):
    sql_query = translate_to_sql(request.natural_query)
    if sql_query:
        return {"valid": True, "message": "Query is feasible"}
    return {"valid": False, "message": "Query is not feasible"}
