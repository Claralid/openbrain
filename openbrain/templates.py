HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenBrain</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        emerald: {
                            50: '#ecfdf5', 100: '#d1fae5', 200: '#a7f3d0', 300: '#6ee7b7',
                            400: '#34d399', 500: '#10b981', 600: '#059669', 700: '#047857',
                            800: '#065f46', 900: '#064e3b', 950: '#022c22',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        .dark ::-webkit-scrollbar-thumb { background: #334155; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="bg-gray-50 text-gray-900 dark:bg-gray-950 dark:text-gray-100 font-sans flex h-screen overflow-hidden">
    
    <!-- Sidebar -->
    <aside class="w-72 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 flex flex-col shrink-0 transition-colors duration-300">
        <!-- Logo -->
        <div class="h-16 flex items-center px-6 border-b border-gray-100 dark:border-gray-800 shrink-0">
            <svg class="w-6 h-6 text-emerald-500 mr-2" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/>
                <path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/>
                <path d="M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4"/>
                <path d="M17.599 6.5A3 3 0 0 0 14 6"/>
                <path d="M6.4 6.5A3 3 0 0 1 10 6"/>
            </svg>
            <span class="text-lg font-bold tracking-tight text-gray-900 dark:text-white">OpenBrain</span>
        </div>

        <!-- Tree container -->
        <div class="flex-1 overflow-y-auto p-4 space-y-1" id="tree-container">
            <div class="text-sm text-gray-500 text-center mt-10">Cargando memoria...</div>
        </div>
        
        <!-- Bottom Actions -->
        <div class="p-4 border-t border-gray-100 dark:border-gray-800 flex flex-col gap-2 shrink-0 bg-gray-50/50 dark:bg-gray-950/50">
             <button onclick="promptCreateNode(true)" class="w-full bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 py-2 rounded-lg text-sm font-semibold transition-colors flex items-center justify-center gap-2 border border-gray-200 dark:border-gray-700">
                 <svg class="w-4 h-4 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"></path></svg>
                 Nueva Sección
             </button>
             <button onclick="promptCreateNode(false)" class="w-full bg-emerald-500 hover:bg-emerald-600 text-white py-2 rounded-lg text-sm font-semibold shadow-lg shadow-emerald-500/20 transition-all flex items-center justify-center gap-2">
                 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                 Nuevo Documento
             </button>
        </div>
    </aside>

    <!-- Main Editor -->
    <main class="flex-1 flex flex-col h-screen overflow-hidden bg-white dark:bg-gray-950 transition-colors duration-300">
        <!-- Topbar -->
        <header class="h-16 border-b border-gray-200 dark:border-gray-800 flex items-center justify-between px-6 shrink-0 bg-white/50 dark:bg-gray-950/50 backdrop-blur-sm">
            <div class="flex items-center gap-4">
                <span id="editor-title" class="text-sm font-semibold text-gray-500 dark:text-gray-400">Selecciona un archivo</span>
                <span id="save-status" class="text-xs bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400 px-2 py-0.5 rounded-full font-bold hidden opacity-0 transition-opacity duration-300">Guardado</span>
            </div>
            <div class="flex items-center gap-4">
                <button onclick="toggleTheme()" class="p-2 text-gray-400 hover:text-emerald-500 transition-colors rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800" title="Cambiar Tema">
                    <svg class="w-5 h-5 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                    <svg class="w-5 h-5 block dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                </button>
                <button onclick="openSettings()" class="p-2 text-gray-400 hover:text-emerald-500 transition-colors rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800" title="Configuración y Mantenimiento">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                </button>
                <div class="h-6 w-px bg-gray-200 dark:bg-gray-800"></div>
                <button id="btn-save" onclick="saveCurrentFile()" class="bg-gray-900 dark:bg-emerald-500 text-white dark:text-gray-900 px-5 py-2 rounded-xl text-sm font-bold opacity-50 cursor-not-allowed transition-all shadow-md">Guardar</button>
            </div>
        </header>

        <!-- Editor Area -->
        <div class="flex-1 p-8 overflow-hidden bg-gray-50/30 dark:bg-gray-900/10">
            <textarea id="markdown-editor" class="w-full max-w-4xl mx-auto block h-full bg-transparent text-gray-800 dark:text-gray-200 font-mono text-sm leading-relaxed focus:outline-none resize-none" spellcheck="false" placeholder="El archivo está vacío..." disabled></textarea>
        </div>
    </main>

    <!-- Modal Nuevo Nodo -->
    <div id="create-modal" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-gray-900 rounded-2xl w-full max-w-sm p-6 shadow-2xl border border-gray-200 dark:border-gray-800 transform transition-all">
            <h3 id="create-modal-title" class="text-xl font-bold mb-6 text-gray-900 dark:text-white">Crear</h3>
            <div class="mb-5">
                <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-2">Ubicación (Carpeta padre)</label>
                <select id="create-parent" class="w-full bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-3 text-sm font-medium text-gray-700 dark:text-gray-200 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-colors"></select>
            </div>
            <div class="mb-6">
                <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-2">Nombre</label>
                <input type="text" id="create-name" class="w-full bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-3 text-sm font-medium text-gray-700 dark:text-gray-200 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-colors" placeholder="Ej: proyectos">
            </div>
            <div class="flex justify-end gap-3 mt-8">
                <button onclick="closeModal()" class="px-5 py-2.5 text-sm font-bold text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">Cancelar</button>
                <button onclick="submitCreate()" class="px-5 py-2.5 bg-emerald-500 text-white text-sm font-bold rounded-xl hover:bg-emerald-600 shadow-lg shadow-emerald-500/20 transition-all active:scale-95">Crear</button>
            </div>
        </div>
    </div>

    <!-- Modal Renombrar -->
    <div id="rename-modal" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-gray-900 rounded-2xl w-full max-w-sm p-6 shadow-2xl border border-gray-200 dark:border-gray-800 transform transition-all">
            <h3 class="text-xl font-bold mb-6 text-gray-900 dark:text-white">Renombrar</h3>
            <input type="hidden" id="rename-path">
            <div class="mb-6">
                <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-2">Nuevo Nombre</label>
                <input type="text" id="rename-name" class="w-full bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-3 text-sm font-medium text-gray-700 dark:text-gray-200 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-colors">
            </div>
            <div class="flex justify-end gap-3 mt-8">
                <button onclick="closeRenameModal()" class="px-5 py-2.5 text-sm font-bold text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">Cancelar</button>
                <button onclick="submitRename()" class="px-5 py-2.5 bg-emerald-500 text-white text-sm font-bold rounded-xl hover:bg-emerald-600 shadow-lg shadow-emerald-500/20 transition-all active:scale-95">Renombrar</button>
            </div>
        </div>
    </div>

    <!-- Modal Eliminar -->
    <div id="delete-modal" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-gray-900 rounded-2xl w-full max-w-sm p-6 shadow-2xl border border-gray-200 dark:border-gray-800 transform transition-all">
            <h3 class="text-xl font-bold mb-4 text-red-600 dark:text-red-500 flex items-center gap-2">
                 <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                 Eliminar
            </h3>
            <input type="hidden" id="delete-path">
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-6">¿Estás seguro de que quieres eliminar <b id="delete-target-name" class="text-gray-900 dark:text-white"></b>? Esta acción no se puede deshacer.</p>
            <div class="flex justify-end gap-3">
                <button onclick="closeDeleteModal()" class="px-5 py-2.5 text-sm font-bold text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">Cancelar</button>
                <button onclick="submitDelete()" class="px-5 py-2.5 bg-red-500 text-white text-sm font-bold rounded-xl hover:bg-red-600 shadow-lg shadow-red-500/20 transition-all active:scale-95">Eliminar</button>
            </div>
        </div>
    </div>

    <!-- Modal Configuración / Mantenimiento -->
    <div id="settings-modal" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white dark:bg-gray-900 rounded-2xl w-full max-w-lg p-6 shadow-2xl border border-gray-200 dark:border-gray-800 transform transition-all flex flex-col max-h-[90vh]">
            <div class="flex justify-between items-center mb-6">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white">Mantenimiento de OpenBrain</h3>
                <button onclick="closeSettings()" class="text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
            
            <div id="settings-content" class="flex-1 overflow-y-auto space-y-4 pr-1">
                <div class="text-center text-sm text-gray-500 py-4">Cargando estado del sistema...</div>
            </div>

            <div class="flex justify-end gap-3 mt-6 pt-4 border-t border-gray-100 dark:border-gray-800 shrink-0">
                <button onclick="closeSettings()" class="px-5 py-2.5 text-sm font-bold text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">Cerrar</button>
                <button id="btn-update-safely" onclick="updateSafely()" class="px-5 py-2.5 bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900 text-sm font-bold rounded-xl hover:bg-gray-800 dark:hover:bg-white shadow-lg transition-all active:scale-95 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                    Actualizar OpenBrain
                </button>
            </div>
        </div>
    </div>

    <!-- Toast -->
    <div id="toast" class="fixed bottom-6 right-6 transform translate-y-20 opacity-0 transition-all duration-300 z-50">
        <div class="bg-gray-900 dark:bg-white text-white dark:text-gray-900 px-5 py-3.5 rounded-xl shadow-2xl shadow-black/20 flex items-center gap-3 min-w-[250px] border border-gray-800 dark:border-gray-200">
            <svg id="toast-icon" class="w-5 h-5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            <span id="toast-message" class="text-sm font-bold">Notificación</span>
        </div>
    </div>

    <script>
        let currentFile = null;
        let memoryTree = [];
        let directories = []; 
        let isCreatingFolder = false;
        let memoryTreeHash = '';
        let openFoldersData = new Set();

        async function loadMemoryTree(isPolling = false) {
            try {
                const res = await fetch('/api/memory');
                const data = await res.json();
                
                const newHash = JSON.stringify(data.tree);
                if (isPolling && newHash === memoryTreeHash) {
                    return; // No changes detected
                }
                
                if (isPolling) {
                    document.querySelectorAll('.folder-el').forEach(el => {
                        const path = el.getAttribute('data-folder-path');
                        const children = el.querySelector('.children-container');
                        if (path && children && !children.classList.contains('hidden')) {
                            openFoldersData.add(path);
                        } else if (path) {
                            openFoldersData.delete(path);
                        }
                    });
                }
                
                memoryTreeHash = newHash;
                memoryTree = data.tree;
                directories = extractDirectories(memoryTree);
                renderTree();
                
                if (isPolling && currentFile) {
                    verifyCurrentFileExists();
                }
            } catch (err) {
                if (!isPolling) {
                    console.error("Error al cargar memoria:", err);
                    document.getElementById('tree-container').innerHTML = '<div class="text-sm text-red-500 p-4">Error al cargar la memoria</div>';
                }
            }
        }

        function verifyCurrentFileExists() {
            const exists = document.querySelector(`.file-node[data-path="${CSS.escape(currentFile)}"]`);
            if (!exists) {
                const btnSave = document.getElementById('btn-save');
                btnSave.textContent = "Eliminado";
                btnSave.classList.add('opacity-50', 'cursor-not-allowed', 'bg-red-500');
                btnSave.classList.remove('bg-gray-900', 'dark:bg-emerald-500');
                document.getElementById('editor-title').textContent = currentFile + " (Eliminado/Movido)";
                showToast("El archivo abierto ya no existe en disco", "error");
            }
        }

        function extractDirectories(nodes, pathPrefix = "") {
            let dirs = [{ path: ".", name: "Root (Workspace)" }];
            for (const node of nodes) {
                if (node.type === 'folder') {
                    dirs.push({ path: node.path, name: node.name });
                    if (node.children) {
                        dirs = dirs.concat(extractDirectories(node.children).filter(d => d.path !== "."));
                    }
                }
            }
            return dirs;
        }

        function createTreeNode(node, padding = 0) {
            const el = document.createElement('div');
            
            if (node.type === 'folder') {
                el.className = 'folder-el';
                el.setAttribute('data-folder-path', node.path);
                
                const folderHeader = document.createElement('div');
                folderHeader.className = `flex items-center justify-between py-2 px-3 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-xl cursor-pointer text-gray-700 dark:text-gray-300 transition-colors group`;
                folderHeader.style.paddingLeft = `${padding + 12}px`;
                
                // Si la carpeta tiene un index_path, el click la abre en el editor y expande
                folderHeader.onclick = () => {
                    const childrenContainer = el.querySelector('.children-container');
                    const chevron = el.querySelector('.chevron');
                    if (childrenContainer) {
                        childrenContainer.classList.toggle('hidden');
                        if(chevron) chevron.classList.toggle('rotate-90');
                    }
                    if (node.index_path) openFile(node.index_path);
                };

                const isPreviouslyOpen = openFoldersData.has(node.path);

                folderHeader.innerHTML = `
                    <div class="flex items-center gap-2.5">
                        <svg class="w-4 h-4 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>
                        <span class="text-sm font-semibold truncate select-none">${node.name}</span>
                    </div>
                    <div class="flex items-center gap-1">
                        <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                             <button onclick="event.stopPropagation(); promptRename('${node.path}', '${node.name}')" class="p-1 hover:bg-gray-200 dark:hover:bg-gray-700 rounded text-gray-500 hover:text-emerald-500" title="Renombrar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg></button>
                             <button onclick="event.stopPropagation(); promptDelete('${node.path}', '${node.name}')" class="p-1 hover:bg-gray-200 dark:hover:bg-gray-700 rounded text-gray-500 hover:text-red-500" title="Eliminar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                        </div>
                        <svg class="chevron w-3.5 h-3.5 opacity-40 transition-transform duration-200 ${isPreviouslyOpen ? 'rotate-90' : ''}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                    </div>
                `;
                el.appendChild(folderHeader);

                const childrenContainer = document.createElement('div');
                childrenContainer.className = `children-container flex flex-col mt-0.5 ${isPreviouslyOpen ? '' : 'hidden'}`;
                
                // Remove folder's index from children list for visual cleanup, since we opened it on folder click
                const visibleChildren = node.children ? node.children.filter(c => c.type !== 'index') : [];
                
                visibleChildren.forEach(child => {
                    childrenContainer.appendChild(createTreeNode(child, padding + 16));
                });
                
                el.appendChild(childrenContainer);

            } else if (node.type === 'file') {
                const fileEl = document.createElement('div');
                fileEl.className = `file-node group flex items-center justify-between py-1.5 px-3 mt-0.5 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg cursor-pointer text-gray-500 dark:text-gray-400 transition-colors`;
                fileEl.style.paddingLeft = `${padding + 12}px`;
                fileEl.setAttribute('data-path', node.path);
                fileEl.onclick = () => openFile(node.path);

                fileEl.innerHTML = `
                    <div class="flex items-center gap-2.5 overflow-hidden">
                        <svg class="w-4 h-4 shrink-0 transition-colors opacity-40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                        <span class="text-sm truncate select-none font-medium">${node.name.replace('.md', '')}</span>
                    </div>
                    <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                         <button onclick="event.stopPropagation(); promptRename('${node.path}', '${node.name}')" class="p-1 hover:bg-gray-200 dark:hover:bg-gray-700 rounded text-gray-500 hover:text-emerald-500" title="Renombrar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg></button>
                         <button onclick="event.stopPropagation(); promptDelete('${node.path}', '${node.name}')" class="p-1 hover:bg-gray-200 dark:hover:bg-gray-700 rounded text-gray-500 hover:text-red-500" title="Eliminar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                    </div>
                `;
                el.appendChild(fileEl);
            } else if (node.type === 'index' && node.name === 'index.md' && padding === 0) {
                 // Root Workspace index.md
                 const fileEl = document.createElement('div');
                 fileEl.className = `file-node flex items-center justify-between py-2 px-3 mb-2 hover:bg-emerald-50 dark:hover:bg-emerald-900/10 rounded-xl cursor-pointer text-emerald-600 dark:text-emerald-400 transition-colors`;
                 fileEl.setAttribute('data-path', node.path);
                 fileEl.onclick = () => openFile(node.path);
                 fileEl.innerHTML = `
                     <div class="flex items-center gap-2.5">
                         <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                         <span class="text-sm truncate select-none font-bold uppercase tracking-wide">Workspace Root</span>
                     </div>
                 `;
                 el.appendChild(fileEl);
            }

            return el;
        }

        function renderTree() {
            const container = document.getElementById('tree-container');
            container.innerHTML = '';
            memoryTree.forEach(node => {
                const el = createTreeNode(node, 0);
                if(el.innerHTML !== '') container.appendChild(el);
            });
            highlightCurrentFile();
        }

        function highlightCurrentFile() {
            document.querySelectorAll('.file-node').forEach(el => {
                const pathAttr = el.getAttribute('data-path');
                if (pathAttr === currentFile) {
                    el.classList.add('bg-emerald-50', 'dark:bg-emerald-900/20', 'text-emerald-600', 'dark:text-emerald-400');
                    el.classList.remove('text-gray-500', 'dark:text-gray-400', 'hover:bg-gray-100', 'dark:hover:bg-gray-800');
                    const svg = el.querySelector('svg');
                    if(svg) svg.classList.remove('opacity-40');
                } else {
                    el.classList.remove('bg-emerald-50', 'dark:bg-emerald-900/20', 'text-emerald-600', 'dark:text-emerald-400');
                    if (!el.textContent.includes('Workspace Root')) { 
                        el.classList.add('text-gray-500', 'dark:text-gray-400', 'hover:bg-gray-100', 'dark:hover:bg-gray-800');
                        const svg = el.querySelector('svg');
                        if(svg) svg.classList.add('opacity-40');
                    }
                }
            });
        }

        function generateBreadcrumb(path) {
            if (!path) return "Selecciona un archivo";
            const parts = path.replace('.md', '').split('/');
            return `<div class="flex items-center gap-2 overflow-hidden max-w-lg text-sm">` + 
                   parts.map((p, i) => {
                       const text = p.charAt(0).toUpperCase() + p.slice(1);
                       const isLast = i === parts.length - 1;
                       return `<span class="truncate ${isLast ? 'text-gray-900 dark:text-gray-100 font-bold' : 'text-gray-500 dark:text-gray-400 font-medium'}">${text}</span>`;
                   }).join('<span class="text-gray-300 dark:text-gray-600 font-normal">/</span>') +
                   `</div>`;
        }

        async function openFile(path) {
            try {
                const res = await fetch(`/api/memory/file?path=${encodeURIComponent(path)}`);
                if (!res.ok) throw new Error("Error fetching file");
                const data = await res.json();
                
                currentFile = path;
                document.getElementById('editor-title').innerHTML = generateBreadcrumb(path);
                
                const editor = document.getElementById('markdown-editor');
                editor.value = data.content;
                editor.disabled = false;
                
                const btnSave = document.getElementById('btn-save');
                btnSave.classList.remove('opacity-50', 'cursor-not-allowed');
                
                highlightCurrentFile();
            } catch (err) {
                showToast("Error abriendo: " + path, "error");
            }
        }

        async function saveCurrentFile() {
            if (!currentFile) return;
            const content = document.getElementById('markdown-editor').value;
            const btnSave = document.getElementById('btn-save');
            btnSave.textContent = "Guardando...";
            btnSave.classList.add('opacity-50', 'cursor-not-allowed');

            try {
                const res = await fetch('/api/memory/file', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ path: currentFile, content: content })
                });
                
                if (res.ok) {
                    const status = document.getElementById('save-status');
                    status.classList.remove('hidden');
                    setTimeout(() => status.classList.remove('opacity-0'), 10);
                    setTimeout(() => {
                        status.classList.add('opacity-0');
                        setTimeout(() => status.classList.add('hidden'), 300);
                    }, 2000);
                } else {
                    throw new Error("Failed");
                }
            } catch (err) {
                showToast("Error al guardar", "error");
            } finally {
                btnSave.textContent = "Guardar";
                btnSave.classList.remove('opacity-50', 'cursor-not-allowed');
            }
        }

        document.getElementById('markdown-editor').addEventListener('input', () => {
             const btnSave = document.getElementById('btn-save');
             if (btnSave.classList.contains('opacity-50')) {
                  btnSave.classList.remove('opacity-50', 'cursor-not-allowed');
             }
        });

        document.addEventListener('keydown', e => {
            if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault();
                saveCurrentFile();
            }
        });

        function promptCreateNode(isFolder) {
            isCreatingFolder = isFolder;
            document.getElementById('create-modal-title').textContent = isFolder ? "Nueva Carpeta Lógica" : "Nuevo Documento";
            document.getElementById('create-modal').classList.remove('hidden');
            setTimeout(() => {
                document.getElementById('create-name').value = '';
                document.getElementById('create-name').focus();
            }, 50);
            
            const parentSelect = document.getElementById('create-parent');
            parentSelect.innerHTML = directories.map(d => `<option value="${d.path}">${d.name}</option>`).join('');
            
            if (currentFile) {
                const parts = currentFile.split('/');
                if (parts.length > 1) {
                    const dirPath = parts.slice(0, -1).join('/');
                    parentSelect.value = dirPath;
                }
            }
        }

        function closeModal() {
            document.getElementById('create-modal').classList.add('hidden');
        }

        async function submitCreate() {
            const parent = document.getElementById('create-parent').value;
            const name = document.getElementById('create-name').value.trim();
            
            if (!name) {
                showToast("El nombre no puede estar vacío", "error");
                return;
            }

            const safeName = name.replace(/\s+/g, '_').toLowerCase();

            try {
                const res = await fetch('/api/memory/create', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ parent, name: safeName, is_folder: isCreatingFolder })
                });

                if (res.ok) {
                    const data = await res.json();
                    closeModal();
                    await loadMemoryTree();
                    openFile(data.path);
                    showToast("Creado exitosamente", "success");
                } else {
                    const d = await res.json();
                    showToast("Error: " + (d.detail || "No se pudo crear"), "error");
                }
            } catch (err) {
                showToast("Error de conexión", "error");
            }
        }

        // Rename logic
        function promptRename(path, name) {
            document.getElementById('rename-modal').classList.remove('hidden');
            document.getElementById('rename-path').value = path;
            const cleanName = name.replace('.md', '');
            document.getElementById('rename-name').value = cleanName;
            setTimeout(() => {
                document.getElementById('rename-name').select();
            }, 50);
        }

        function closeRenameModal() {
            document.getElementById('rename-modal').classList.add('hidden');
        }

        async function submitRename() {
            const path = document.getElementById('rename-path').value;
            const newName = document.getElementById('rename-name').value.trim();
            if(!newName) return showToast("El nombre no puede estar vacío", "error");

            const safeName = newName.replace(/\s+/g, '_').toLowerCase();
            try {
                const res = await fetch('/api/memory/rename', {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ path, new_name: safeName })
                });

                if (res.ok) {
                    const data = await res.json();
                    closeRenameModal();
                    await loadMemoryTree();
                    if (currentFile === path) openFile(data.path);
                    showToast("Renombrado exitosamente", "success");
                } else {
                    const d = await res.json();
                    showToast("Error: " + (d.detail || "No se pudo renombrar"), "error");
                }
            } catch (err) {
                showToast("Error de conexión", "error");
            }
        }

        // Delete logic
        function promptDelete(path, name) {
            document.getElementById('delete-modal').classList.remove('hidden');
            document.getElementById('delete-path').value = path;
            document.getElementById('delete-target-name').textContent = name.replace('.md', '');
        }

        function closeDeleteModal() {
            document.getElementById('delete-modal').classList.add('hidden');
        }

        async function submitDelete() {
            const path = document.getElementById('delete-path').value;
            try {
                const res = await fetch('/api/memory/delete', {
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ path })
                });

                if (res.ok) {
                    closeDeleteModal();
                    await loadMemoryTree(true);
                    if (currentFile === path) {
                        currentFile = null;
                        document.getElementById('markdown-editor').value = '';
                        document.getElementById('markdown-editor').disabled = true;
                        document.getElementById('editor-title').innerHTML = '<span class="text-sm font-semibold text-gray-500 dark:text-gray-400">Selecciona un archivo</span>';
                        document.getElementById('btn-save').classList.add('opacity-50', 'cursor-not-allowed');
                    }
                    showToast("Eliminado exitosamente", "success");
                } else {
                    const d = await res.json();
                    showToast("Error: " + (d.detail || "No se pudo eliminar"), "error");
                }
            } catch (err) {
                showToast("Error de conexión", "error");
            }
        }

        function showToast(msg, type = "success") {
            const el = document.getElementById('toast');
            document.getElementById('toast-message').textContent = msg;
            
            const icon = document.getElementById('toast-icon');
            if(type === 'success') {
                 icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>';
                 icon.className = "w-5 h-5 text-emerald-500";
            } else {
                 icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>';
                 icon.className = "w-5 h-5 text-red-500";
            }
            
            el.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => el.classList.add('translate-y-20', 'opacity-0'), 3000);
        }

        function toggleTheme() {
            document.documentElement.classList.toggle('dark');
            localStorage.theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
        }
        
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }

        async function openSettings() {
            document.getElementById('settings-modal').classList.remove('hidden');
            const content = document.getElementById('settings-content');
            const btnUpdate = document.getElementById('btn-update-safely');
            content.innerHTML = '<div class="text-center text-sm text-gray-500 py-4">Cargando estado del repositorio...</div>';
            btnUpdate.disabled = true;
            btnUpdate.classList.add('opacity-50', 'cursor-not-allowed');

            try {
                const res = await fetch('/api/system/status');
                const data = await res.json();
                
                if (data.error) {
                    content.innerHTML = `<div class="p-4 bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 rounded-xl text-sm font-mono whitespace-pre-wrap">${data.error}</div>`;
                    return;
                }

                // Render info
                let statusHtml = `
                    <div class="bg-gray-50 dark:bg-gray-800/50 p-4 rounded-xl border border-gray-100 dark:border-gray-800">
                        <div class="flex items-center justify-between mb-2">
                            <span class="block text-[10px] font-bold text-gray-400 uppercase tracking-widest">Versión del Sistema</span>
                            <span class="text-xs px-2 py-0.5 bg-gray-200 dark:bg-gray-700 text-gray-600 dark:text-gray-300 rounded font-mono">${data.commit}</span>
                        </div>
                        <p class="text-sm text-gray-700 dark:text-gray-300 truncate" title="${data.last_commit}">${data.last_commit}</p>
                    </div>
                `;

                if (data.has_update) {
                    statusHtml += `
                        <div class="bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 p-4 rounded-xl mt-4">
                            <div class="flex gap-2 items-center text-blue-700 dark:text-blue-500 font-bold text-sm mb-2">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                Actualización Disponible
                            </div>
                            <p class="text-xs text-blue-600 dark:text-blue-400">Hay una nueva versión de OpenBrain lista para descargarse. Actualiza para recibir las últimas mejoras.</p>
                        </div>
                    `;
                    btnUpdate.disabled = false;
                    btnUpdate.classList.remove('opacity-50', 'cursor-not-allowed');
                } else {
                    statusHtml += `
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 p-4 flex items-center gap-3 rounded-xl mt-4">
                            <svg class="w-5 h-5 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            <span class="text-sm text-emerald-700 dark:text-emerald-400 font-bold">OpenBrain está actualizado.</span>
                        </div>
                    `;
                    // Botón desactivado porque ya está en la última versión
                    btnUpdate.disabled = true;
                    btnUpdate.classList.add('opacity-50', 'cursor-not-allowed');
                }

                content.innerHTML = statusHtml;

            } catch (err) {
                content.innerHTML = `<span class="text-sm text-red-500">Hubo un problema de conexión al comprobar el estado del sistema.</span>`;
            }
        }

        function closeSettings() {
            document.getElementById('settings-modal').classList.add('hidden');
        }

        async function updateSafely() {
            const btnUpdate = document.getElementById('btn-update-safely');
            btnUpdate.innerHTML = `<svg class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg> Actualizando...`;
            btnUpdate.disabled = true;
            btnUpdate.classList.add('opacity-50', 'cursor-not-allowed');
            
            try {
                const res = await fetch('/api/system/update', { method: 'POST' });
                const data = await res.json();
                
                if (res.ok) {
                    showToast("¡Actualización exitosa!", "success");
                    document.getElementById('settings-content').innerHTML = `
                        <div class="p-6 bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 rounded-xl flex flex-col items-center text-center">
                            <svg class="w-12 h-12 text-emerald-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            <h4 class="text-emerald-700 dark:text-emerald-400 font-bold text-lg mb-2">¡Sistema Actualizado!</h4>
                            <p class="text-sm text-emerald-600 dark:text-emerald-500 mb-4">Se han descargado las últimas mejoras de OpenBrain de manera exitosa.</p>
                            <span class="text-xs bg-gray-100 dark:bg-gray-800 text-gray-500 px-3 py-1 rounded inline-block">Si ocurre algún error inesperado, intenta recargar esta página web o reiniciar la terminal local.</span>
                        </div>
                    `;
                } else {
                    showToast(data.detail || "Error en la actualización", "error");
                    openSettings(); // refrescar
                }
            } catch (error) {
                showToast("Falla de red", "error");
                openSettings();
            } finally {
                btnUpdate.innerHTML = `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg> Actualizar OpenBrain`;
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
             loadMemoryTree();
             setInterval(() => loadMemoryTree(true), 3000);
        });
    </script>
</body>
</html>
"""
