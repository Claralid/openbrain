import argparse
import uvicorn
import os
import sys
from .core import WORKSPACE_DIR

def start_server(port=8000):
    print(f"Iniciando panel de control OpenBrain Workspace Memory Editor...")
    print(f"Directorio de memoria: {WORKSPACE_DIR}")
    uvicorn.run("openbrain.api:app", host="0.0.0.0", port=port, reload=False)

def show_status():
    print("=== Estado de OpenBrain ===")
    print(f"Directorio de memoria: {WORKSPACE_DIR}")
    print("Para iniciar el servidor, ejecuta: openbrain start")

def app():
    parser = argparse.ArgumentParser(description="Editor de Memoria para Workspace OpenBrain")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")
    
    parser_start = subparsers.add_parser("start", help="Inicia el servidor web local")
    parser_start.add_argument("--port", type=int, default=8000, help="Puerto del servidor")
    
    parser_status = subparsers.add_parser("status", help="Muestra el estado actual")
    
    args = parser.parse_args()
    
    if args.command == "start":
        start_server(args.port)
    elif args.command == "status":
        show_status()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    app()
