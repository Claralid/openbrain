import os
import shutil

# Base Directory: Current working directory (where openbrain is started)
WORKSPACE_DIR = os.environ.get("OPENBRAIN_WORKSPACE", os.getcwd())

# Folders to ignore from the brain UI
IGNORED_FOLDERS = {".git", "venv", "__pycache__", "openbrain", ".openclaw", ".vscode", ".idea"}

def get_memory_tree():
    """ Construye la estructura de carpetas y archivos basándose en el Workspace Actual """
    def build_tree(current_dir, is_root=False):
        tree = []
        try:
            items = sorted(os.listdir(current_dir))
        except FileNotFoundError:
            return tree
        
        folder_name = os.path.basename(current_dir)
        
        for item in items:
            item_path = os.path.join(current_dir, item)
            rel_path = os.path.relpath(item_path, WORKSPACE_DIR)
            
            if os.path.isdir(item_path):
                if item in IGNORED_FOLDERS or item.startswith("."):
                    continue
                    
                sub_index = f"{item}_index.md"
                sub_index_path = os.path.join(item_path, sub_index)
                has_index = os.path.exists(sub_index_path)
                
                # Omit empty folders without index and no .md contents
                children = build_tree(item_path, is_root=False)
                if not children and not has_index:
                     continue
                     
                tree.append({
                    "name": item,
                    "path": rel_path,
                    "type": "folder",
                    "index_path": os.path.relpath(sub_index_path, WORKSPACE_DIR) if has_index else None,
                    "children": children
                })
            elif item.endswith(".md"):
                # Determinamos si el archivo actual es un índice de su carpeta contenedora
                is_index = False
                if is_root and item == "index.md":
                    is_index = True
                elif not is_root and item == f"{folder_name}_index.md":
                    is_index = True
                    
                tree.append({
                    "name": item,
                    "path": rel_path,
                    "type": "index" if is_index else "file"
                })
                
        # Order: Indexes first, Folders second, normal Files third
        def sort_key(x):
            if x["type"] == "index": return 0
            if x["type"] == "folder": return 1
            return 2
            
        tree.sort(key=lambda x: (sort_key(x), x["name"]))
        return tree

    return build_tree(WORKSPACE_DIR, is_root=True)

def resolve_path(rel_path):
    path = os.path.join(WORKSPACE_DIR, rel_path)
    if not os.path.abspath(path).startswith(os.path.abspath(WORKSPACE_DIR)):
         raise ValueError("Path no válido.")
    return path

def read_memory_file(rel_path):
    path = resolve_path(rel_path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {rel_path} no existe.")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_memory_file(rel_path, content):
    path = resolve_path(rel_path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def create_memory_node(parent_dir, name, is_folder):
    """
    Crea una carpeta lógica o un documento.
    parent_dir: e.g. "memory/projects" o "." para root
    """
    parent_dir = parent_dir.strip("/")
    if parent_dir == "." or parent_dir == "":
        parent_path = WORKSPACE_DIR
    else:
        parent_path = os.path.join(WORKSPACE_DIR, parent_dir)
        
    if not os.path.abspath(parent_path).startswith(os.path.abspath(WORKSPACE_DIR)):
         raise ValueError("Path no válido.")
         
    if is_folder:
        dir_path = os.path.join(parent_path, name)
        os.makedirs(dir_path, exist_ok=True)
        index_file = os.path.join(dir_path, f"{name}_index.md")
        if not os.path.exists(index_file):
            with open(index_file, "w", encoding="utf-8") as f:
                f.write(f"# {name.capitalize()}\n\n")
        return os.path.relpath(index_file, WORKSPACE_DIR)
    else:
        file_name = f"{name}.md" if not name.endswith(".md") else name
        file_path = os.path.join(parent_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                name_clean = file_name.replace('.md','')
                f.write(f"# {name_clean.capitalize()}\n\n")
                
        # Aggregate reference in parent's index
        if parent_path == WORKSPACE_DIR:
             parent_index = os.path.join(parent_path, "index.md")
        else:
             parent_folder_name = os.path.basename(parent_path)
             parent_index = os.path.join(parent_path, f"{parent_folder_name}_index.md")
             
        if os.path.exists(parent_index):
            with open(parent_index, "a", encoding="utf-8") as f:
                f.write(f"\n- [{name_clean}](./{file_name})\n")
                
        return os.path.relpath(file_path, WORKSPACE_DIR)

def delete_memory_node(rel_path):
    path = resolve_path(rel_path)
    if not os.path.exists(path):
        raise ValueError("El archivo o sección no existe.")
        
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
        
def rename_memory_node(rel_path, new_name):
    path = resolve_path(rel_path)
    if not os.path.exists(path):
        raise ValueError("El archivo o sección no existe.")
        
    parent_dir = os.path.dirname(path)
    is_folder = os.path.isdir(path)
    old_basename = os.path.basename(path)
    
    if is_folder:
        new_path = os.path.join(parent_dir, new_name)
        if os.path.exists(new_path): raise ValueError("Ya existe una carpeta con ese nombre.")
        os.rename(path, new_path)
        
        # Rename internal index if it exists
        old_index = os.path.join(new_path, f"{old_basename}_index.md")
        if os.path.exists(old_index):
            new_index = os.path.join(new_path, f"{new_name}_index.md")
            os.rename(old_index, new_index)
            
        return os.path.relpath(new_path, WORKSPACE_DIR)
    else:
        new_file_name = f"{new_name}.md" if not new_name.endswith(".md") else new_name
        new_path = os.path.join(parent_dir, new_file_name)
        if os.path.exists(new_path): raise ValueError("Ya existe un archivo con ese nombre.")
        os.rename(path, new_path)
        return os.path.relpath(new_path, WORKSPACE_DIR)
