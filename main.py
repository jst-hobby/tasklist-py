from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import uvicorn
from typing import Optional, Dict, Any

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Task List Application")

# Supabase setup
supabase_url: str = os.environ.get("SUPABASE_URL", "")
supabase_key: str = os.environ.get("SUPABASE_KEY", "")
supabase: Client = create_client(supabase_url, supabase_key)

# Templates setup
templates = Jinja2Templates(directory="templates")

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_tasks(request: Request):
    try:
        response = supabase.table("tasks").select("*").execute()
        tasks = response.data
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "tasks": tasks}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks")
async def create_task(title: str = Form(...)):
    try:
        task_data: Dict[str, Any] = {
            "title": title,
            "completed": False
        }
        supabase.table("tasks").insert(task_data).execute()
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks/{task_id}/toggle")
async def toggle_task(task_id: str):
    try:
        # First, get the current state of the task
        task = supabase.table("tasks").select("completed").eq("id", task_id).single().execute()
        current_state = task.data.get("completed", False)
        
        # Then update with the opposite state
        supabase.table("tasks").update({"completed": not current_state}).eq("id", task_id).execute()
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks/{task_id}/delete")
async def delete_task(task_id: str):
    try:
        supabase.table("tasks").delete().eq("id", task_id).execute()
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 