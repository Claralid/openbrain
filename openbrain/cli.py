import argparse
import uvicorn
import os
import sys
from .core import OPENCLAW_DIR, create_manual_backup, ensure_structure

def start_server():
    ensure_structure()
    print(f"Iniciando panel de control OpenBrain...")
    print(f"Directorio de configuración activo: {OPENCLAW_DIR}")
    # Ejecutamos uvicorn usando la app definida en api.py
    # Usamos host 0.0.0.0 para evitar problemas de conexión en Windows/Firewall
    uvicorn.run("openbrain.api:app", host="0.0.0.0", port=5050, reload=False)

def show_status():
    ensure_structure()
    print("=== Estado de OpenBrain ===")
    print(f"Directorio de configuración: {OPENCLAW_DIR}")
    config_path = os.path.join(OPENCLAW_DIR, "openclaw.json")
    if os.path.exists(config_path):
        print(f"Archivo de configuración encontrado.")
    else:
        print(f"No se ha inicializado el entorno en esta locación.")
    print("Para iniciar el servidor, ejecuta: openbrain start")

def run_backup():
    ensure_structure()
    print("Iniciando creación de punto de restauración...")
    filename = create_manual_backup()
    print(f"Backup creado exitosamente: {filename}")
    print(f"Guardado en: {os.path.join(OPENCLAW_DIR, 'backups', filename)}")

def app():
    parser = argparse.ArgumentParser(description="Gestor local para OpenClaw")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
    
    # Subcomando: start
    parser_start = subparsers.add_parser("start", help="Inicia el servidor web local")
    
    # Subcomando: status
    parser_status = subparsers.add_parser("status", help="Muestra el estado actual de la configuración")
    
    # Subcomando: backup
    parser_backup = subparsers.add_parser("backup", help="Crea un backup manual de la configuración")
    
    args = parser.parse_args()
    
    if args.command == "start":
        start_server()
    elif args.command == "status":
        show_status()
    elif args.command == "backup":
        run_backup()
    else:
        # Imprimir ayuda por defecto
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    app()
