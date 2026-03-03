from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from .core import (
    ensure_structure, get_config, save_config, get_skills,
    toggle_skill, get_backups, create_manual_backup, delete_backup,
    get_metrics
)
from .templates import HTML_TEMPLATE

# Aseguramos la estructura en el inicio
ensure_structure()

app = FastAPI(title="OpenBrain API")

@app.get("/api/config")
def api_get_config():
    try:
        return get_config()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/metrics")
def api_get_metrics():
    try:
        return get_metrics()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/config")
async def api_save_config(request: Request):
    try:
        data = await request.json()
        save_config(data)
        return {"message": "Configuración guardada exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/skills")
def api_get_skills():
    return {"skills": get_skills()}

@app.post("/api/skills/toggle")
async def api_toggle_skill(request: Request):
    data = await request.json()
    skill_name = data.get("name")
    try:
        status = toggle_skill(skill_name)
        return {"message": f"Skill {'activado' if status else 'desactivado'}", "active": status}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/backups")
def api_get_backups():
    return {"backups": get_backups()}

@app.post("/api/backups")
def api_create_backup():
    try:
        create_manual_backup()
        return {"message": "Backup creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/backups/{filename}")
def api_delete_backup(filename: str):
    try:
        if delete_backup(filename):
            return {"message": "Backup eliminado"}
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
def root():
    return HTML_TEMPLATE
