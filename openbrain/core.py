import os
import json
import shutil
from datetime import datetime

# ==========================================
# CONFIGURACIÓN Y SETUP DE RUTAS
# ==========================================
OPENCLAW_DIR = os.environ.get("OPENCLAW_DIR", os.path.expanduser("~/.openclaw"))
CONFIG_FILE = os.path.join(OPENCLAW_DIR, "openclaw.json")
BACKUPS_DIR = os.path.join(OPENCLAW_DIR, "backups")
SKILLS_DIR = os.path.join(OPENCLAW_DIR, "skills")

def ensure_structure():
    """Inicializa la estructura de directorios y datos de prueba locales si no existen"""
    os.makedirs(OPENCLAW_DIR, exist_ok=True)
    os.makedirs(BACKUPS_DIR, exist_ok=True)
    os.makedirs(SKILLS_DIR, exist_ok=True)
    
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "version": "1.0.0",
            "active_model": "gpt-4-turbo",
            "available_models": ["gpt-4-turbo", "gpt-3.5-turbo", "claude-3-opus", "llama-3-70b"],
            "settings": {
                "temperature": 0.7,
                "max_tokens": 2048
            }
        }
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
            
    # Crear skills de prueba como carpetas
    dummy_skills = ["web_search", "image_gen", "code_executor"]
    for skill in dummy_skills:
        skill_path = os.path.join(SKILLS_DIR, skill)
        os.makedirs(skill_path, exist_ok=True)
        if skill == "image_gen" and not os.path.exists(os.path.join(skill_path, ".disabled")):
            open(os.path.join(skill_path, ".disabled"), "w").close()

def get_config():
    """Obtiene el archivo de configuracion openclaw.json"""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(data: dict):
    """Guarda la configuración con copia de seguridad obligatoria primero y valida que sea JSON válido (dict)."""
    if not isinstance(data, dict):
        raise ValueError("El cuerpo no es un objeto JSON válido (diccionario).")
        
    # Validar que sea un JSON que se puede codificar sin errores
    json.dumps(data)
    
    # Crear backup automático previniendo pérdida de datos
    if os.path.exists(CONFIG_FILE):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"openclaw.json.bak_{timestamp}"
        shutil.copy2(CONFIG_FILE, os.path.join(BACKUPS_DIR, backup_name))

    # Sobrescribir de forma segura
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_skills():
    """Lee y devuelve los skills configurados"""
    skills = []
    if os.path.exists(SKILLS_DIR):
        for item in os.listdir(SKILLS_DIR):
            if os.path.isdir(os.path.join(SKILLS_DIR, item)):
                is_disabled = os.path.exists(os.path.join(SKILLS_DIR, item, ".disabled"))
                skills.append({"name": item, "active": not is_disabled})
    return skills

def toggle_skill(skill_name: str) -> bool:
    """Alterna el estado de un skill devolviendo el nuevo estado activo"""
    skill_path = os.path.join(SKILLS_DIR, skill_name)
    
    if not os.path.exists(skill_path):
        raise ValueError("Skill no encontrado")
        
    disabled_marker = os.path.join(skill_path, ".disabled")
    if os.path.exists(disabled_marker):
        os.remove(disabled_marker) # Activar
        return True
    else:
        open(disabled_marker, "w").close() # Desactivar
        return False

def get_backups():
    """Obtiene un arreglo con todos los backups ZIP"""
    backups = []
    if os.path.exists(BACKUPS_DIR):
        for f in sorted(os.listdir(BACKUPS_DIR), reverse=True):
            if f.endswith(".zip"):
                path = os.path.join(BACKUPS_DIR, f)
                size_mb = round(os.path.getsize(path) / (1024 * 1024), 2)
                backups.append({"name": f, "size": f"{size_mb} MB"})
    return backups

def create_manual_backup():
    """Genera un archivo ZIP con todos los datos locales dentro del directorio backup"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = os.path.join(BACKUPS_DIR, backup_name)
    
    # Comprimir la carpeta de OpenClaw
    shutil.make_archive(backup_path, 'zip', OPENCLAW_DIR)
    return backup_name + ".zip"

def delete_backup(filename: str):
    """Borra un archivo de backup por nombre"""
    filepath = os.path.join(BACKUPS_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False

def get_metrics():
    """Obtains basic statistics for the home dashboard"""
    config = get_config()
    skills = get_skills()
    backups = get_backups()
    
    # Datos simulados de tokens para demostración (en un caso real vendrían de logs/DB)
    token_usage = {
        "gpt-4-turbo": {"total": 125000, "cost": 1.25, "history": [4000, 8000, 15000, 12000, 18000, 25000, 15000]},
        "gpt-3.5-turbo": {"total": 450000, "cost": 0.45, "history": [20000, 35000, 45000, 30000, 55000, 70000, 45000]},
        "claude-3-opus": {"total": 85000, "cost": 1.70, "history": [5000, 7000, 12000, 10000, 15000, 20000, 10000]},
        "llama-3-70b": {"total": 300000, "cost": 0.00, "history": [10000, 25000, 40000, 35000, 50000, 65000, 30000]}
    }
    
    return {
        "active_model": config.get("active_model", "N/A"),
        "total_skills": len(skills),
        "active_skills": len([s for s in skills if s["active"]]),
        "total_backups": len(backups),
        "last_backup": backups[0]["name"] if backups else "None",
        "version": config.get("version", "1.0.0"),
        "token_usage": token_usage
    }
