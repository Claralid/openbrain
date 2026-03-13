from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import traceback
import subprocess
import os

from .core import (
    get_memory_tree, read_memory_file, 
    save_memory_file, create_memory_node,
    delete_memory_node, rename_memory_node
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

class RenameRequest(BaseModel):
    path: str
    new_name: str

class DeleteRequest(BaseModel):
    path: str

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

@app.put("/api/memory/rename")
def api_rename_node(req: RenameRequest):
    try:
        new_path = rename_memory_node(req.path, req.new_name)
        return {"message": "Renombrado exitosamente", "path": new_path}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/memory/delete")
def api_delete_node(req: DeleteRequest):
    try:
        delete_memory_node(req.path)
        return {"message": "Eliminado exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

def get_repo_dir():
    # Asumimos que OpenBrain corre desde la raíz de su repositorio
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.get("/api/system/status")
def api_system_status():
    repo_dir = get_repo_dir()
    try:
        # Fetch latest changes from remote without merging
        subprocess.check_output(['git', '-C', repo_dir, 'fetch'], text=True)
        
        commit_hash = subprocess.check_output(['git', '-C', repo_dir, 'rev-parse', '--short', 'HEAD'], text=True).strip()
        last_commit = subprocess.check_output(['git', '-C', repo_dir, 'log', '-1', '--pretty=format:%s (%cr)'], text=True).strip()
        
        # Check if local is behind remote (updates available)
        status_behind = subprocess.check_output(['git', '-C', repo_dir, 'rev-list', 'HEAD..origin/main', '--count'], text=True).strip()
        has_update = int(status_behind) > 0
        
        return {
            "commit": commit_hash,
            "last_commit": last_commit,
            "has_update": has_update
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/system/update")
def api_system_update():
    repo_dir = get_repo_dir()
    try:
        # Perform git pull directly
        pull_output = subprocess.check_output(['git', '-C', repo_dir, 'pull'], text=True).strip()
        return {"message": "Actualización exitosa", "details": pull_output}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar: {e.output}")
    except Exception as e:
         if isinstance(e, HTTPException):
             raise e
         raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agent/settings")
def api_agent_settings():
    return {
        "voice": {
            "stt_provider": "Whisper",
            "tts_provider": "KittenTTS",
            "status": "Online",
            "description": "Texto → KittenTTS → Auto-Delivery al chat de Telegram"
        }
    }

@app.get("/", response_class=HTMLResponse)
def root():
    return HTML_TEMPLATE
