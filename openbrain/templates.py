HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenBrain Memory</title>
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
            <span class="text-lg font-bold tracking-tight text-gray-900 dark:text-white">OpenBrain Memory</span>
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
                <button onclick="toggleTheme()" class="p-2 text-gray-400 hover:text-emerald-500 transition-colors rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800">
                    <svg class="w-5 h-5 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                    <svg class="w-5 h-5 block dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
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

        async function loadMemoryTree() {
            try {
                const res = await fetch('/api/memory');
                const data = await res.json();
                memoryTree = data.tree;
                directories = extractDirectories(memoryTree);
                renderTree();
            } catch (err) {
                console.error("Error al cargar memoria:", err);
                document.getElementById('tree-container').innerHTML = '<div class="text-sm text-red-500 p-4">Error al cargar la memoria</div>';
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

                folderHeader.innerHTML = `
                    <div class="flex items-center gap-2.5">
                        <svg class="w-4 h-4 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>
                        <span class="text-sm font-semibold truncate select-none">${node.name}</span>
                    </div>
                    <svg class="chevron w-3.5 h-3.5 opacity-40 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                `;
                el.appendChild(folderHeader);

                const childrenContainer = document.createElement('div');
                childrenContainer.className = 'children-container flex flex-col mt-0.5 hidden';
                
                // Remove folder's index from children list for visual cleanup, since we opened it on folder click
                const visibleChildren = node.children ? node.children.filter(c => c.type !== 'index') : [];
                
                visibleChildren.forEach(child => {
                    childrenContainer.appendChild(createTreeNode(child, padding + 16));
                });
                
                el.appendChild(childrenContainer);

            } else if (node.type === 'file') {
                const fileEl = document.createElement('div');
                fileEl.className = `file-node flex items-center gap-2.5 py-1.5 px-3 mt-0.5 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg cursor-pointer text-gray-500 dark:text-gray-400 transition-colors`;
                fileEl.style.paddingLeft = `${padding + 12}px`;
                fileEl.setAttribute('data-path', node.path);
                fileEl.onclick = () => openFile(node.path);

                fileEl.innerHTML = `
                    <svg class="w-4 h-4 shrink-0 transition-colors opacity-40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    <span class="text-sm truncate select-none font-medium">${node.name.replace('.md', '')}</span>
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

        async function openFile(path) {
            try {
                const res = await fetch(`/api/memory/file?path=${encodeURIComponent(path)}`);
                if (!res.ok) throw new Error("Error fetching file");
                const data = await res.json();
                
                currentFile = path;
                document.getElementById('editor-title').textContent = path;
                
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

        document.addEventListener('DOMContentLoaded', loadMemoryTree);
    </script>
</body>
</html>
"""
