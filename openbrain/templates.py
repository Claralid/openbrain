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
    <aside class="w-72 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 flex flex-col shrink-0 transition-colors duration-300 h-screen overflow-hidden">
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

        <!-- Scrollable Navigation Area -->
        <div class="flex-1 overflow-y-auto w-full pb-20">


            <!-- Top Menu (Notion Style) -->
            <div class="px-3 pt-4 space-y-0.5">
                <div class="flex items-center gap-2.5 px-3 py-2 text-sm font-bold text-gray-700 dark:text-gray-200 bg-gray-100 dark:bg-gray-800/50 rounded-lg cursor-pointer" onclick="showHome()">
                    <svg class="w-4 h-4 shrink-0 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                    Home
                </div>
                <!-- Search Button -->
                <div class="flex items-center gap-2.5 px-3 py-1.5 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50 rounded-lg transition-colors cursor-pointer" onclick="openSearchModal()">
                    <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                    Search
                </div>
                
                <!-- Outputs -->
                <a href="#" class="flex items-center gap-2.5 px-3 py-1.5 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50 rounded-lg transition-colors opacity-60 cursor-not-allowed" title="Próximamente">
                    <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
                    Outputs
                </a>
                
                <!-- Future Modules -->
                <a href="#" class="flex items-center gap-2.5 px-3 py-1.5 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50 rounded-lg transition-colors opacity-60 cursor-not-allowed">
                    <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
                    Tasks
                </a>
                <a href="#" class="flex items-center gap-2.5 px-3 py-1.5 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50 rounded-lg transition-colors opacity-60 cursor-not-allowed">
                    <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Reminders
                </a>
                <a href="#" class="flex items-center gap-2.5 px-3 py-1.5 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50 rounded-lg transition-colors opacity-60 cursor-not-allowed">
                    <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                    Routines
                </a>
            </div>

            <!-- Workspace Data (Restored original style) -->
            <div class="px-3 pt-6">
                <button class="w-full flex items-center justify-between px-3 py-2 text-xs font-bold text-gray-400 dark:text-gray-500 uppercase tracking-widest group">
                    <span>Workspace</span>
                </button>
                <div class="mt-1 space-y-0.5 px-2">
                    
                    <!-- Projects -->
                    <div class="flex flex-col">
                        <div class="flex items-center justify-between px-3 py-2 text-sm font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50/50 dark:bg-emerald-900/10 rounded-lg group">
                            <div class="flex items-center gap-2.5">
                                <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>
                                Projects
                            </div>
                            <button onclick="promptCreateNode(false)" class="p-1 rounded bg-white dark:bg-emerald-900/40 text-emerald-600 dark:text-emerald-400 opacity-60 hover:opacity-100 hover:shadow-sm transition-all" title="Crear Nuevo Documento">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                            </button>
                        </div>
                        <div class="pl-2 pr-1 pb-1 pt-1 ml-3 border-l-2 border-emerald-100 dark:border-emerald-900/40" id="tree-container">
                            <div class="text-[11px] text-gray-400 italic px-3 py-2">Loading projects...</div>
                        </div>
                    </div>

                    <!-- Chats -->
                    <div class="flex flex-col">
                        <div class="flex flex-col gap-2 px-3 py-2 rounded-lg transition-colors mt-2">
                            <div class="flex items-center gap-2.5 text-sm font-bold text-gray-700 dark:text-gray-300 hover:text-emerald-600 dark:hover:text-emerald-400 cursor-pointer" onclick="toggleChat(true)">
                                <svg class="w-4 h-4 shrink-0 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                                Chats
                            </div>
                        </div>
                        <div class="pl-2 pr-1 pb-1 pt-1 ml-3 border-l-2 border-gray-100 dark:border-gray-800">
                            <!-- Placeholder File -->
                            <div class="flex items-center group cursor-pointer" data-chat-path="data/workspace/Chats/Ideas_para_Proyecto_React.md" onclick="openFile('data/workspace/Chats/Ideas_para_Proyecto_React.md')">
                                <div class="w-4 h-px bg-gray-200 dark:bg-gray-700"></div>
                                <div class="flex-1 flex items-center justify-between gap-2 px-2 py-1.5 text-xs text-gray-600 dark:text-gray-300 hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-900/10 rounded-r-md transition-colors overflow-hidden">
                                    <div class="flex items-center gap-2 truncate">
                                        <svg class="w-3.5 h-3.5 opacity-50 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
                                        <span class="truncate font-medium">Ideas para React</span>
                                    </div>
                                    <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                                         <button onclick="event.stopPropagation(); promptRename('data/workspace/Chats/Ideas_para_Proyecto_React.md', 'Ideas_para_Proyecto_React.md')" class="p-1 hover:bg-emerald-200/50 dark:hover:bg-emerald-800/50 rounded text-gray-400 hover:text-emerald-600" title="Renombrar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg></button>
                                         <button onclick="event.stopPropagation(); promptDelete('data/workspace/Chats/Ideas_para_Proyecto_React.md', 'Ideas_para_Proyecto_React.md')" class="p-1 hover:bg-red-100 dark:hover:bg-red-900/40 rounded text-gray-400 hover:text-red-500" title="Eliminar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Skills -->
                    <div class="flex flex-col">
                        <div class="flex items-center justify-between px-3 py-2 text-sm font-bold text-gray-700 dark:text-gray-300 hover:text-emerald-600 dark:hover:text-emerald-400 rounded-lg group mt-2 transition-colors cursor-pointer" onclick="toggleSection('skills-tree', 'icon-skills-tree', 'icon-skills-active')">
                            <div class="flex items-center gap-2.5">
                                <svg class="w-4 h-4 shrink-0 transition-transform rotate-90" id="icon-skills-tree" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                <svg class="w-4 h-4 shrink-0 -ml-1 text-emerald-500 hidden" id="icon-skills-active" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                Skills
                            </div>
                            <button class="p-0.5 rounded hover:bg-gray-200 dark:hover:bg-gray-700 text-gray-400 opacity-0 group-hover:opacity-100 transition-all" title="Add Skill" onclick="event.stopPropagation(); alert('Adición de Skills próximamente')">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                            </button>
                        </div>
                        <div class="pl-2 pr-1 pb-1 pt-1 ml-3 border-l-2 border-gray-100 dark:border-gray-800" id="skills-tree">
                            
                            <!-- Dummy Skill 1 -->
                            <div class="flex items-center group cursor-pointer" onclick="alert('This will open the skill view')">
                                <div class="w-4 h-px bg-gray-200 dark:bg-gray-700"></div>
                                <div class="flex-1 flex items-center justify-between gap-2 px-2 py-1.5 text-xs text-gray-600 dark:text-gray-300 hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-900/10 rounded-r-md transition-colors overflow-hidden">
                                    <div class="flex items-center gap-2 truncate">
                                        <svg class="w-3.5 h-3.5 opacity-50 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                        <span class="truncate font-medium text-emerald-600 dark:text-emerald-400">Python Expert</span>
                                    </div>
                                    <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                                         <button onclick="event.stopPropagation();" class="p-1 hover:bg-red-100 dark:hover:bg-red-900/40 rounded text-gray-400 hover:text-red-500" title="Eliminar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                                    </div>
                                </div>
                            </div>

                            <!-- Dummy Skill 2 -->
                            <div class="flex items-center group cursor-pointer" onclick="alert('This will open the skill view')">
                                <div class="w-4 h-px bg-gray-200 dark:bg-gray-700"></div>
                                <div class="flex-1 flex items-center justify-between gap-2 px-2 py-1.5 text-xs text-gray-600 dark:text-gray-300 hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-900/10 rounded-r-md transition-colors overflow-hidden">
                                    <div class="flex items-center gap-2 truncate">
                                        <svg class="w-3.5 h-3.5 opacity-50 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                        <span class="truncate font-medium">UX/UI Design Pattern</span>
                                    </div>
                                    <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                                         <button onclick="event.stopPropagation();" class="p-1 hover:bg-red-100 dark:hover:bg-red-900/40 rounded text-gray-400 hover:text-red-500" title="Eliminar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Dummy Skill 3 -->
                            <div class="flex items-center group cursor-pointer" onclick="alert('This will open the skill view')">
                                <div class="w-4 h-px bg-gray-200 dark:bg-gray-700"></div>
                                <div class="flex-1 flex items-center justify-between gap-2 px-2 py-1.5 text-xs text-gray-600 dark:text-gray-300 hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-900/10 rounded-r-md transition-colors overflow-hidden">
                                    <div class="flex items-center gap-2 truncate">
                                        <svg class="w-3.5 h-3.5 opacity-50 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                        <span class="truncate font-medium">Blogging Formatting</span>
                                    </div>
                                    <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                                         <button onclick="event.stopPropagation();" class="p-1 hover:bg-red-100 dark:hover:bg-red-900/40 rounded text-gray-400 hover:text-red-500" title="Eliminar"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Bottom Actions (Settings) -->
        <div class="px-3 pb-4 pt-2 border-t border-gray-100 dark:border-gray-800 shrink-0 bg-white dark:bg-gray-900">
            <a href="#" class="flex items-center gap-2.5 px-3 py-2 text-sm font-medium text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800/80 rounded-lg transition-colors">
                <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                Settings
            </a>
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
                <div class="h-6 w-px bg-gray-200 dark:bg-gray-800"></div>
                <button id="btn-save" onclick="saveCurrentFile()" class="bg-gray-900 dark:bg-emerald-500 text-white dark:text-gray-900 px-5 py-2 rounded-xl text-sm font-bold opacity-50 cursor-not-allowed transition-all shadow-md">Guardar</button>
            </div>
        </header>

        <!-- Workspace App Area -->
        <div class="flex-1 relative overflow-hidden flex bg-white dark:bg-[#191919] transition-colors duration-300">
            
            <!-- Home Dashboard View (New) -->
            <div id="home-container" class="absolute inset-0 z-10 p-10 overflow-y-auto bg-white dark:bg-[#191919] transition-opacity duration-300">
                <div class="max-w-5xl mx-auto w-full">
                    <!-- Dynamic Greeting -->
                    <h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-2 ml-2 mt-4" id="home-greeting">Good evening</h1>
                    
                    <!-- Projects / Recently visited -->
                    <div class="mt-12">
                        <div class="flex items-center gap-2 text-gray-500 mb-4 ml-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            <span class="text-sm font-medium">Projects Summary</span>
                        </div>
                        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4" id="home-projects-grid">
                            <!-- Popular project cards overview -->
                            <div class="bg-gray-50 hover:bg-gray-100 dark:bg-[#202020] dark:hover:bg-[#282828] rounded-2xl p-4 cursor-pointer transition-colors border border-transparent hover:border-gray-200 dark:hover:border-gray-700 h-36 flex flex-col justify-between group">
                                <svg class="w-6 h-6 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                                <div>
                                    <h3 class="text-sm font-bold text-gray-900 dark:text-gray-100 mb-1 truncate">Workspace Root</h3>
                                    <p class="text-xs text-gray-500">Root folder</p>
                                </div>
                            </div>
                            
                            <div class="text-[13px] text-gray-400 italic col-span-full ml-2 mt-2">More projects will appear here...</div>
                        </div>
                    </div>

                    <!-- Skills / Learn -->
                    <div class="mt-12">
                        <div class="flex items-center gap-2 text-gray-500 mb-4 ml-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                            <span class="text-sm font-medium">Skills & Knowledge</span>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="home-skills-grid">
                            <!-- Skill Card Placeholder -->
                            <div class="bg-gray-50 hover:bg-gray-100 dark:bg-[#202020] dark:hover:bg-[#282828] rounded-2xl p-5 cursor-pointer transition-colors border border-gray-100 dark:border-gray-800 h-48 flex flex-col items-center justify-center text-center group" onclick="alert('Feature in development')">
                                <div class="w-12 h-12 rounded-full bg-gray-200 dark:bg-gray-800 flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
                                    <svg class="w-6 h-6 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
                                </div>
                                <h3 class="text-sm font-bold text-gray-900 dark:text-gray-100">Add new skill</h3>
                                <p class="text-[13px] text-gray-500 mt-1 max-w-[200px]">Create an AI skill to give the system new abilities.</p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Editor Area (Main View) -->
            <div id="editor-container" class="absolute inset-0 z-0 p-8 overflow-y-auto bg-white dark:bg-[#191919] hidden">
                <textarea id="markdown-editor" class="w-full max-w-4xl mx-auto block h-min min-h-full bg-transparent text-gray-800 dark:text-gray-200 font-mono text-sm leading-relaxed focus:outline-none resize-none" spellcheck="false" placeholder="El archivo está vacío..." disabled></textarea>
            </div>

            <!-- Global Search Modal Overlay (ChatGPT Style) -->
            <div id="search-modal" class="absolute inset-0 z-50 bg-black/20 dark:bg-black/50 backdrop-blur-sm hidden items-start justify-center pt-[10vh]">
                <div class="w-full max-w-[650px] bg-white dark:bg-[#212121] rounded-2xl shadow-2xl border border-gray-100 dark:border-white/10 overflow-hidden transform transition-all scale-95 opacity-0 flex flex-col max-h-[75vh]" id="search-modal-content">
                    
                    <!-- Search Input Area -->
                    <div class="flex items-center p-3 px-5 border-b border-gray-100 dark:border-white/10 relative shrink-0">
                        <input type="text" id="global-search-input" placeholder="Search chats..." class="w-full py-2 bg-transparent border-none focus:ring-0 text-[15px] font-medium text-gray-900 dark:text-white placeholder-gray-400 placeholder:font-normal" autocomplete="off">
                        <button onclick="closeSearchModal()" class="text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors p-1" title="Close">
                           <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>

                    <!-- Results Area (ChatGPT Layout) -->
                    <div class="flex-1 overflow-y-auto p-3" id="search-results-container">
                        
                        <!-- New Chat Action -->
                        <div class="flex items-center gap-3 px-3 py-3 mb-2 bg-gray-100 hover:bg-gray-200 dark:bg-[#2f2f2f] dark:hover:bg-[#383838] rounded-xl cursor-pointer transition-colors text-gray-800 dark:text-gray-200" onclick="alert('Creating new chat...')">
                            <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                            <span class="text-sm font-medium">New chat</span>
                        </div>

                        <!-- Timeframe Group: Yesterday -->
                        <div class="mt-4 mb-1 px-3">
                            <span class="text-xs font-semibold text-gray-400 dark:text-gray-500">Yesterday</span>
                        </div>
                        <div class="flex flex-col gap-0.5">
                            <div class="flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-gray-50 dark:hover:bg-[#2f2f2f] cursor-pointer transition-colors group">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                                <span class="text-[14px] text-gray-700 dark:text-gray-300 font-medium truncate group-hover:text-gray-900 dark:group-hover:text-white">Organizando el siguiente paso</span>
                            </div>
                            <div class="flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-gray-50 dark:hover:bg-[#2f2f2f] cursor-pointer transition-colors group">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                                <span class="text-[14px] text-gray-700 dark:text-gray-300 font-medium truncate group-hover:text-gray-900 dark:group-hover:text-white">Resumen de manejo de software</span>
                            </div>
                            <div class="flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-gray-50 dark:hover:bg-[#2f2f2f] cursor-pointer transition-colors group">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                                <span class="text-[14px] text-gray-700 dark:text-gray-300 font-medium truncate group-hover:text-gray-900 dark:group-hover:text-white">Frases célebres motivadoras</span>
                            </div>
                        </div>

                        <!-- Timeframe Group: Previous 7 Days -->
                        <div class="mt-4 mb-1 px-3">
                            <span class="text-xs font-semibold text-gray-400 dark:text-gray-500">Previous 7 Days</span>
                        </div>
                        <div class="flex flex-col gap-0.5">
                            <div class="flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-gray-50 dark:hover:bg-[#2f2f2f] cursor-pointer transition-colors group">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                                <span class="text-[14px] text-gray-700 dark:text-gray-300 font-medium truncate group-hover:text-gray-900 dark:group-hover:text-white">Avanzando proyectos juntos</span>
                            </div>
                            <div class="flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-gray-50 dark:hover:bg-[#2f2f2f] cursor-pointer transition-colors group">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                                <span class="text-[14px] text-gray-700 dark:text-gray-300 font-medium truncate group-hover:text-gray-900 dark:group-hover:text-white">BlackCloud y el IDE</span>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            <!-- Chat Interface (Floating Widget) -->
            <div id="chat-container" class="absolute top-4 right-4 bottom-4 w-[400px] z-50 flex flex-col bg-white dark:bg-[#191919] rounded-[24px] shadow-[0_12px_40px_-10px_rgba(0,0,0,0.15)] dark:shadow-[0_12px_40px_-10px_rgba(0,0,0,0.6)] border border-gray-200 dark:border-gray-800 transition-all duration-300 ease-in-out transform origin-top-right">
                <div class="w-full flex flex-col h-full pt-6 pb-5 px-5">
                    
                    <!-- Chat Header -->
                    <div class="flex items-center justify-between mb-8 w-full">
                        <div class="flex items-center gap-1.5 cursor-pointer text-gray-500 hover:text-gray-900 dark:hover:text-gray-100 transition-colors">
                            <span class="text-[13px] font-semibold">New AI chat</span>
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                        <div class="flex items-center gap-1 text-gray-400">
                            <button class="p-1 hover:bg-gray-100 dark:hover:bg-[#2c2c2c] rounded-md transition-colors" title="New Chat" onclick="toggleChat()">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                            </button>
                            <button class="p-1 hover:bg-gray-100 dark:hover:bg-[#2c2c2c] rounded-md transition-colors" title="Resize/Popout" onclick="document.getElementById('chat-container').classList.toggle('w-[400px]'); document.getElementById('chat-container').classList.toggle('w-[600px]')">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
                            </button>
                            <button class="p-1 hover:bg-gray-100 dark:hover:bg-[#2c2c2c] rounded-md transition-colors" title="Close AI" onclick="toggleChat()">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 6L6 18M6 6l12 12"></path></svg>
                            </button>
                        </div>
                    </div>
                    
                    <!-- Chat Body & Suggestions -->
                    <div class="flex-1 flex flex-col justify-start w-full">
                        <!-- Avatar -->
                        <div class="mb-5 flex items-center">
                            <div class="w-[52px] h-[52px] rounded-full bg-[#f1f1f0] dark:bg-[#efefed] flex items-center justify-center relative shadow-sm border border-gray-200 dark:border-transparent">
                                <!-- Minimal avatar drawing similar to Notion's -->
                                <svg class="w-6 h-6 text-gray-900" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>
                                <!-- Flower badge -->
                                <div class="absolute -top-1 -right-1 text-pink-400">
                                    <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2.2c-.4 0-.8.3-1 .6-.6-1.5-2.7-1.9-3.9-.6-.9.9-1.1 2.3-.5 3.4-1.4-.4-2.8 0-3.5 1.3-.7 1.2-.4 2.8.7 3.6-1.3.6-1.8 2.3-1.1 3.5.7 1.2 2.3 1.4 3.5.6-.6 1.4-.1 2.9 1 3.7 1.2.9 2.9.8 3.8-.4 1.2 1.3 3.3.9 4-.6.6 1.4 2.7 1.9 3.9.6.9-.9 1.1-2.3.5-3.4 1.4.4 2.8 0 3.5-1.3.7-1.2.4-2.8-.7-3.6 1.3-.6 1.8-2.3 1.1-3.5-.7-1.2-2.3-1.4-3.5-.6.6-1.4.1-2.9-1-3.7-1.2-.9-2.9-.8-3.8.4z"></path></svg>
                                </div>
                            </div>
                        </div>
                        
                        <h2 class="text-[22px] font-bold text-gray-900 dark:text-gray-100 mb-8 tracking-tight">What can I brighten up for you today?</h2>
                    </div>

                    <!-- Chat Input Container -->
                    <div class="w-full mt-auto relative">
                        <!-- Blue active ring wrapper -->
                        <div class="border-[1.5px] border-emerald-500 rounded-[18px] p-3 shadow-lg bg-white dark:bg-[#202020] transition-all">
                            
                            <!-- Textarea -->
                            <textarea class="w-full bg-transparent border-0 focus:ring-0 resize-none text-[15px] text-gray-800 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 p-0 mb-3" rows="1" placeholder="Habla con tu cerebro..."></textarea>
                            
                            <!-- Bottom Action Bar -->
                            <div class="flex items-center justify-between">
                                <!-- Left Actions (Settings/Personality only) -->
                                <div class="flex items-center gap-2 text-gray-400">
                                    <button class="p-1.5 hover:text-emerald-500 hover:bg-emerald-50 dark:hover:bg-emerald-900/20 rounded-md transition-colors" title="Settings / Personality">
                                        <!-- Sliders icon for settings/personality -->
                                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
                                    </button>
                                </div>
                                
                                <!-- Right Actions (Send) -->
                                <div class="flex items-center">
                                    <button class="w-8 h-8 rounded-full bg-gray-100 dark:bg-[#333] flex items-center justify-center text-gray-400 hover:text-white hover:bg-emerald-500 dark:hover:bg-emerald-500 transition-colors shadow-sm cursor-pointer" title="Enviar">
                                        <svg class="w-4 h-4 translate-y-[-1px]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Floating Chat Toggle Button (Visible when chat is closed) -->
        <button onclick="toggleChat(true)" id="chat-toggle-btn" class="fixed bottom-6 right-6 w-14 h-14 bg-emerald-600 hover:bg-emerald-700 text-white rounded-full flex items-center justify-center shadow-lg hover:shadow-xl transition-all hover:scale-105 z-40 hidden" title="Abrir Chat Assistant">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
        </button>
    </main>

    <!-- Modal Viewer (Placeholder) -->
    <div id="viewer-modal" class="fixed inset-0 bg-black/80 backdrop-blur-md z-[60] hidden flex items-center justify-center p-4">
        <div class="bg-gray-50 dark:bg-gray-950 rounded-2xl w-full h-[90vh] shadow-2xl border border-gray-200 dark:border-gray-800 transform transition-all flex flex-col overflow-hidden relative">
            
            <!-- Viewer Topbar -->
            <div class="h-14 border-b border-gray-200 dark:border-gray-800 flex items-center justify-between px-4 bg-white/50 dark:bg-gray-900/50">
                <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-lg bg-indigo-50 dark:bg-indigo-900/20 text-indigo-500 flex items-center justify-center shrink-0 border border-indigo-100 dark:border-indigo-900/50">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                    </div>
                    <div>
                        <span class="block text-sm font-bold text-gray-900 dark:text-white leading-tight">Document Viewer</span>
                        <span class="block text-xs text-gray-500">Preview Mode</span>
                    </div>
                </div>
                <div class="flex items-center gap-2">
                    <button class="px-3 py-1.5 text-xs font-bold bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-md text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 transition" disabled>Download</button>
                    <button onclick="closeViewer()" class="p-1.5 text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors rounded-lg hover:bg-gray-200 dark:hover:bg-gray-700">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                    </button>
                </div>
            </div>

            <!-- Viewer Canvas -->
            <div class="flex-1 overflow-auto p-8 flex items-center justify-center bg-gray-100/50 dark:bg-black/20" id="viewer-canvas">
                <div class="text-center w-full max-w-sm">
                    <div class="w-20 h-20 bg-gray-200 dark:bg-gray-800 rounded-2xl mx-auto flex items-center justify-center mb-6 border border-gray-300 dark:border-gray-700 shadow-inner">
                        <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                    </div>
                    <h4 class="text-lg font-bold text-gray-900 dark:text-gray-100 mb-2">Editor de Recursos</h4>
                    <p class="text-sm text-gray-500 dark:text-gray-400">Este es el espacio destinado al Viewer de imágenes y documentos nativo de OpenBrain. Integración lógica próxima.</p>
                </div>
            </div>
        </div>
    </div>

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

    <!-- Modal Agent Settings -->
    <div id="agent-settings-modal" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-gray-50 dark:bg-gray-950 rounded-2xl w-full max-w-2xl shadow-2xl border border-gray-200 dark:border-gray-800 transform transition-all flex flex-col md:flex-row overflow-hidden max-h-[85vh]">
            <!-- Sidebar / Nav Modules -->
            <div class="w-full md:w-1/3 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 p-6 flex flex-col gap-2 shrink-0">
                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-4">Agent Settings</h3>
                <nav class="space-y-1">
                    <button class="w-full text-left px-4 py-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-900/20 text-emerald-700 dark:text-emerald-400 font-bold transition-colors flex items-center gap-3">
                        <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>
                        Voice Settings
                    </button>
                    <!-- Próximamente -->
                    <button disabled class="w-full text-left px-4 py-2.5 rounded-xl text-gray-400 dark:text-gray-600 font-medium flex items-center gap-3 cursor-not-allowed" title="Próximamente para el usuario">
                        <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Personality
                    </button>
                    <button disabled class="w-full text-left px-4 py-2.5 rounded-xl text-gray-400 dark:text-gray-600 font-medium flex items-center gap-3 cursor-not-allowed" title="Próximamente para el usuario">
                        <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                        Behavior
                    </button>
                </nav>
            </div>
            
            <!-- Main Config Area -->
            <div class="flex-1 flex flex-col relative bg-transparent overflow-y-auto">
                <div class="absolute top-4 right-4 relative z-10 flex justify-end p-4 pb-0">
                    <button onclick="closeAgentSettings()" class="p-1 text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors rounded-lg bg-gray-100 dark:bg-gray-800/80">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                    </button>
                </div>
                <div class="flex-1 p-6 lg:p-10 pt-4" id="agent-settings-content">
                    <div class="text-center text-sm text-gray-500 py-10">Conectando módulos de IA...</div>
                </div>
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
            const exists = document.querySelector(`.file-node[data-path="${currentFile}"]`);
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
                
                showEditor(); // Ensure editor is visible when opening a file

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
                    
                    // Update dummy chats if affected
                    const chatItem = document.querySelector(`[data-chat-path="${path}"]`);
                    if (chatItem) {
                         chatItem.setAttribute('data-chat-path', data.path);
                         chatItem.setAttribute('onclick', `openFile('${data.path}')`);
                         const btns = chatItem.querySelectorAll('button');
                         if(btns.length >= 2) {
                             btns[0].setAttribute('onclick', `event.stopPropagation(); promptRename('${data.path}', '${safeName}')`);
                             btns[1].setAttribute('onclick', `event.stopPropagation(); promptDelete('${data.path}', '${safeName}')`);
                         }
                         const textSpan = chatItem.querySelector('.truncate.font-medium');
                         if(textSpan) textSpan.textContent = safeName;
                    }
                    
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

        function toggleChat(forceOpen = false) {
            const chatContainer = document.getElementById('chat-container');
            const toggleBtn = document.getElementById('chat-toggle-btn');
            
            if (chatContainer) {
                if (forceOpen) {
                    chatContainer.classList.remove('hidden');
                    if (toggleBtn) toggleBtn.classList.add('hidden');
                } else {
                    const isHidden = chatContainer.classList.contains('hidden');
                    if (isHidden) {
                        chatContainer.classList.remove('hidden');
                        if (toggleBtn) toggleBtn.classList.add('hidden');
                    } else {
                        chatContainer.classList.add('hidden');
                        if (toggleBtn) toggleBtn.classList.remove('hidden');
                    }
                }
            }
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
                        resetToChat();
                    }
                    
                    // Remove dummy chat if affected
                    const chatItem = document.querySelector(`[data-chat-path="${path}"]`);
                    if (chatItem) chatItem.remove();
                    
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

        // Viewer logic (Placeholder UI)
        function openViewer() {
            document.getElementById('viewer-modal').classList.remove('hidden');
        }

        function closeViewer() {
            document.getElementById('viewer-modal').classList.add('hidden');
        }

        async function openAgentSettings() {
            document.getElementById('agent-settings-modal').classList.remove('hidden');
            const content = document.getElementById('agent-settings-content');
            
            try {
                const res = await fetch('/api/agent/settings');
                const data = await res.json();
                
                content.innerHTML = `
                    <div class="mb-6">
                        <h4 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">Canal Vocal Actual</h4>
                        <p class="text-sm text-gray-500 dark:text-gray-400">Verifica el estado de los puentes de audio operacionales de OpenBrain hacia el chat.</p>
                    </div>
                    
                    <div class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm overflow-hidden mb-8">
                        <div class="p-5 border-b border-gray-100 dark:border-gray-800 flex items-center justify-between">
                            <div class="flex items-center gap-4">
                                <div class="w-10 h-10 rounded-lg bg-blue-50 dark:bg-blue-900/20 text-blue-500 flex items-center justify-center shrink-0 border border-blue-100 dark:border-blue-900/50">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path></svg>
                                </div>
                                <div>
                                    <span class="block text-sm font-bold text-gray-900 dark:text-white leading-tight">Speech-to-Text (Escucha)</span>
                                    <span class="block text-xs text-gray-500">Transforma tus notas de voz en texto</span>
                                </div>
                            </div>
                            <span class="px-2.5 py-1 bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-md text-xs font-bold text-gray-600 dark:text-gray-300 shadow-inner">${data.voice.stt_provider}</span>
                        </div>
                        
                        <div class="p-5 flex items-center justify-between">
                            <div class="flex items-center gap-4">
                                <div class="w-10 h-10 rounded-lg bg-emerald-50 dark:bg-emerald-900/20 text-emerald-500 flex items-center justify-center shrink-0 border border-emerald-100 dark:border-emerald-900/50">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path></svg>
                                </div>
                                <div>
                                    <span class="block text-sm font-bold text-gray-900 dark:text-white leading-tight">Text-to-Speech (Habla)</span>
                                    <span class="block text-xs text-gray-500">El motor principal con el que interactúa</u></span>
                                </div>
                            </div>
                            <span class="px-2.5 py-1 bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-md text-xs font-bold text-gray-600 dark:text-gray-300 shadow-inner">${data.voice.tts_provider}</span>
                        </div>
                    </div>
                    
                    <div>
                        <span class="block text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Health / Delivery</span>
                        <div class="bg-gray-900 dark:bg-black rounded-xl p-4 border border-gray-800 relative z-0 flex items-center justify-between shadow-lg">
                            <div>
                                <span class="text-emerald-400 font-bold text-sm bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/20 flex items-center gap-2 inline-flex mb-1">
                                     <div class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></div> ${data.voice.status}
                                </span>
                                <span class="block text-[11px] text-gray-400 mt-1">${data.voice.description}</span>
                            </div>
                        </div>
                    </div>
                `;
            } catch (err) {
                content.innerHTML = `<span class="text-sm text-red-500">Error cargando módulos del agente.</span>`;
            }
        }

        function closeAgentSettings() {
            document.getElementById('agent-settings-modal').classList.add('hidden');
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

        function showHome() {
            document.getElementById('editor-container').classList.add('hidden');
            document.getElementById('home-container').classList.remove('hidden');
            setGreeting();
        }

        function showEditor() {
            document.getElementById('home-container').classList.add('hidden');
            document.getElementById('editor-container').classList.remove('hidden');
        }

        function setGreeting() {
            const hour = new Date().getHours();
            let greeting = 'Good morning';
            if (hour >= 12 && hour < 17) greeting = 'Good afternoon';
            else if (hour >= 17) greeting = 'Good evening';
            document.getElementById('home-greeting').innerText = greeting;
        }

        // Toggle generic sections 
        function toggleSection(sectionId, iconId, activeIconId) {
            const el = document.getElementById(sectionId);
            const icon = document.getElementById(iconId);
            if(el.classList.contains('hidden')) {
                el.classList.remove('hidden');
                if(icon) icon.classList.add('rotate-90');
            } else {
                el.classList.add('hidden');
                if(icon) icon.classList.remove('rotate-90');
            }
        }

        /* --- Global Search Modal Logic --- */
        function openSearchModal() {
            const modal = document.getElementById('search-modal');
            const content = document.getElementById('search-modal-content');
            const input = document.getElementById('global-search-input');
            
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            
            // Animate in
            setTimeout(() => {
                content.classList.remove('scale-95', 'opacity-0');
                content.classList.add('scale-100', 'opacity-100');
                input.focus();
            }, 10);
        }

        function closeSearchModal() {
            const modal = document.getElementById('search-modal');
            const content = document.getElementById('search-modal-content');
            
            // Animate out
            content.classList.remove('scale-100', 'opacity-100');
            content.classList.add('scale-95', 'opacity-0');
            
            setTimeout(() => {
                modal.classList.remove('flex');
                modal.classList.add('hidden');
                document.getElementById('global-search-input').value = ''; // clear on close
            }, 200);
        }

        // Close search modal on Escape or clicking outside
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeSearchModal();
            }
        });

        document.getElementById('search-modal').addEventListener('click', (e) => {
            if (e.target.id === 'search-modal') {
                closeSearchModal();
            }
        });

        document.addEventListener('DOMContentLoaded', () => {
             setGreeting();
             loadMemoryTree();
             setInterval(() => loadMemoryTree(true), 3000);
        });
    </script>
</body>
</html>
"""
