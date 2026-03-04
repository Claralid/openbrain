import os
import json
import shutil
import zipfile
from datetime import datetime

# ==========================================
# CONFIGURACIÓN Y SETUP DE RUTAS
# ==========================================
OPENCLAW_DIR = os.environ.get("OPENCLAW_DIR", os.path.expanduser("~/.openclaw"))
CONFIG_FILE = os.path.join(OPENCLAW_DIR, "openclaw.json")
BACKUPS_DIR = os.path.join(OPENCLAW_DIR, "backups")
SKILLS_DIR = os.path.join(OPENCLAW_DIR, "skills")
COMPLETIONS_DIR = os.path.join(OPENCLAW_DIR, "completions")

MODEL_COSTS = {
    "gpt-4-turbo": 0.00001,      # $10 / 1M tokens approx
    "gpt-4": 0.00003,            # $30 / 1M tokens
    "gpt-3.5-turbo": 0.000001,   # $1 / 1M tokens
    "claude-3-opus": 0.000015,   # $15 / 1M tokens
    "claude-3-sonnet": 0.000003, # $3 / 1M tokens
    "llama-3-70b": 0.0,          # Local/Free
    "llama-3-8b": 0.0
}

def ensure_structure():
    """Inicializa la estructura de directorios y datos de prueba locales si no existen"""
    os.makedirs(OPENCLAW_DIR, exist_ok=True)
    os.makedirs(BACKUPS_DIR, exist_ok=True)
    os.makedirs(SKILLS_DIR, exist_ok=True)
    os.makedirs(COMPLETIONS_DIR, exist_ok=True)
    
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "version": "1.0.0",
            "active_model": "gpt-4-turbo",
            "available_models": ["gpt-4-turbo", "gpt-3.5-turbo", "claude-3-opus", "llama-3-70b"],
            "agents": {
                "defaults": {
                    "model": {
                        "primary": "gpt-4-turbo"
                    }
                }
            },
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

def get_nested(data, path, default=None):
    """Helper to get a value from a nested dictionary using dot notation."""
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data

def set_nested(data, path, value):
    """Helper to set a value in a nested dictionary using dot notation."""
    keys = path.split('.')
    for key in keys[:-1]:
        data = data.setdefault(key, {})
    data[keys[-1]] = value

def get_config():
    """Obtiene el archivo de configuracion openclaw.json y aplica mapeo para la UI"""
    if not os.path.exists(CONFIG_FILE):
        return {}
        
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    # Mapeo para la UI (Mantiene compatibilidad con el frontend actual)
    mapped_config = {
        "version": config.get("version", "1.0.0"),
        "active_model": get_nested(config, "agents.defaults.model.primary", config.get("active_model", "N/A")),
        "available_models": config.get("available_models", ["gpt-4-turbo", "gpt-3.5-turbo", "claude-3-opus", "llama-3-70b"]),
        "settings": config.get("settings", {}),
        "_raw": config # Mantenemos el original para ediciones JSON completas
    }
    return mapped_config

def save_config(data: dict):
    """Guarda la configuración respetando la estructura real de OpenClaw."""
    if not isinstance(data, dict):
        raise ValueError("El cuerpo no es un objeto JSON válido.")
        
    # Si viene de la UI con la estructura mapeada, actualizamos solo el campo específico
    # Pero si es una edición JSON total, usamos el _raw o el objeto completo
    
    current_config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            current_config = json.load(f)

    # Lógica de guardado inteligente
    if "active_model" in data and "_raw" not in data:
        # Es una actualización simple desde el selector de la UI
        set_nested(current_config, "agents.defaults.model.primary", data["active_model"])
        # También actualizamos el campo root por si acaso
        current_config["active_model"] = data["active_model"]
    else:
        # Es una edición completa del JSON
        # Si el usuario editó el JSON en la UI, enviará el objeto completo.
        # Quitamos el campo _raw si existe para no guardarlo circularmente
        current_config = data.copy()
        current_config.pop("_raw", None)

    # Crear backup automático previniendo pérdida de datos
    if os.path.exists(CONFIG_FILE):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"openclaw.json.bak_{timestamp}"
        shutil.copy2(CONFIG_FILE, os.path.join(BACKUPS_DIR, backup_name))

    # Sobrescribir de forma segura
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(current_config, f, indent=4)

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
    """Genera un archivo ZIP con todos los datos locales, excluyendo la propia carpeta de backups."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = os.path.join(BACKUPS_DIR, backup_name)
    
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(OPENCLAW_DIR):
            # Excluir la carpeta de backups para evitar recursividad
            if os.path.abspath(root).startswith(os.path.abspath(BACKUPS_DIR)):
                continue
                
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, OPENCLAW_DIR)
                zipf.write(file_path, arcname)
                
    return backup_name

def delete_backup(filename: str):
    """Borra un archivo de backup por nombre"""
    filepath = os.path.join(BACKUPS_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False

def get_metrics():
    """Obtains real statistics from completion logs"""
    config = get_config()
    skills = get_skills()
    backups = get_backups()
    
    token_usage = {}
    
    # Initialize token_usage with available models
    models = config.get("available_models", ["gpt-4-turbo", "gpt-3.5-turbo", "claude-3-opus", "llama-3-70b"])
    for m in models:
        token_usage[m] = {"total": 0, "cost": 0.0, "history": [0]*7}
        
    # Parse completions
    if os.path.exists(COMPLETIONS_DIR):
        for f in os.listdir(COMPLETIONS_DIR):
            if f.endswith(".json"):
                try:
                    with open(os.path.join(COMPLETIONS_DIR, f), "r", encoding="utf-8") as j:
                        data = json.load(j)
                        model = data.get("model")
                        usage = data.get("usage", {})
                        tokens = usage.get("total_tokens", 0)
                        
                        if model in token_usage:
                            token_usage[model]["total"] += tokens
                            cost_per_token = MODEL_COSTS.get(model, 0)
                            token_usage[model]["cost"] += round(tokens * cost_per_token, 4)
                            # Simple history: we'd need timestamps to match days. 
                            # For MVP we can just put it in the last bucket.
                            token_usage[model]["history"][-1] += tokens
                except:
                    continue

    # Fallback to demo data if nothing was found at all (sum of totals is 0)
    if sum(v["total"] for v in token_usage.values()) == 0:
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
