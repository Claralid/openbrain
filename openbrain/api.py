from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import traceback

from .core import (
    get_memory_tree, read_memory_file, 
    save_memory_file, create_memory_node
)
from .templates import HTML_TEMPLATE

app = FastAPI(title="OpenBrain Workspace Memory API")

class SaveRequest(BaseModel):
    path: str
    content: str

class CreateRequest(BaseModel):
    parent: str
    name: str
    is_folder: bool

@app.get("/api/memory")
def api_get_memory():
    try:
        return {"tree": get_memory_tree()}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/memory/file")
def api_read_file(path: str):
    try:
        return {"content": read_memory_file(path)}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/memory/file")
def api_save_file(request: SaveRequest):
    try:
        save_memory_file(request.path, request.content)
        return {"message": "Guardado exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/memory/create")
def api_create_node(req: CreateRequest):
    try:
        created_path = create_memory_node(req.parent, req.name, req.is_folder)
        return {"message": "Creado exitosamente", "path": created_path}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
def root():
    return HTML_TEMPLATE
