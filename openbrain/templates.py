HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenBrain - Intelligent Management</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
        html { scroll-behavior: smooth; }
        body { transition: background-color 0.3s ease, color 0.3s ease; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        .dark ::-webkit-scrollbar-thumb { background: #334155; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .page { animation: fadeIn 0.3s ease-out; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body class="bg-gray-50 text-gray-900 dark:bg-gray-950 dark:text-gray-100 font-sans flex h-screen overflow-hidden">

    <!-- Sidebar -->
    <aside class="w-64 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 flex flex-col transition-colors duration-300 z-20 shrink-0">
        <!-- Logo -->
        <div class="h-20 flex items-center px-6 border-b border-gray-100 dark:border-gray-800">
            <div class="flex items-center gap-3 text-emerald-600 dark:text-emerald-500">
                <svg class="w-10 h-10" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M50 15c-15 0-25 10-25 25 0 8 4 15 10 20-5 10-2 15 5 20h20c7-5 10-10 5-20 6-5 10-12 10-20 0-15-10-25-25-25z" />
                    <line x1="50" y1="15" x2="50" y2="80" />
                    <circle cx="35" cy="30" r="3" fill="currentColor" />
                    <path d="M35 30h10" />
                    <circle cx="30" cy="45" r="3" fill="currentColor" />
                    <path d="M30 45h15" />
                    <circle cx="35" cy="60" r="3" fill="currentColor" />
                    <path d="M35 60h10" />
                    <circle cx="65" cy="35" r="3" fill="currentColor" />
                    <path d="M65 35H55" />
                    <circle cx="70" cy="50" r="3" fill="currentColor" />
                    <path d="M70 50H55" />
                    <circle cx="65" cy="65" r="3" fill="currentColor" />
                    <path d="M65 65H55" />
                </svg>
                <span class="text-xl font-bold tracking-tight text-gray-900 dark:text-white">OpenBrain</span>
            </div>
        </div>

        <!-- Navigation -->
        <nav class="flex-1 overflow-y-auto no-scrollbar py-6 px-4 space-y-1">
            <p class="px-2 text-xs font-semibold text-gray-400 uppercase tracking-wider mb-4 font-mono">Main Menu</p>
            <a href="#home" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors group">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                Dashboard
            </a>
            <a href="#skills" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors group">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                Skills
            </a>
            <a href="#config" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors group">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                Settings
            </a>
            <a href="#backups" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors group">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"></path></svg>
                Backups
            </a>
        </nav>

        <div class="p-6 border-t border-gray-100 dark:border-gray-800 bg-gray-50/50 dark:bg-gray-950/50">
            <div class="flex items-center justify-between mb-4">
                <span class="text-[10px] text-gray-400 font-bold uppercase tracking-widest">System</span>
                <span id="app-version" class="text-[10px] bg-emerald-100 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-400 px-2 py-0.5 rounded-full font-bold">...</span>
            </div>
            <div class="flex items-center gap-3">
                <div id="status-indicator" class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></div>
                <span id="status-text" class="text-xs font-semibold text-gray-500">Connecting...</span>
            </div>
        </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen overflow-hidden relative">
        <!-- Topbar -->
        <header class="h-20 bg-white/80 dark:bg-gray-900/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-800 flex items-center justify-between px-8 sticky top-0 z-10 transition-colors duration-300">
            <div class="flex items-center gap-6">
                <!-- Active Model Indicator -->
                <div class="hidden md:flex items-center gap-3 bg-emerald-50 dark:bg-emerald-900/20 px-4 py-2 rounded-xl border border-emerald-100 dark:border-emerald-800/50">
                    <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
                    <span class="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-widest">Active Model</span>
                    <span id="header-active-model" class="text-sm font-bold text-gray-900 dark:text-white">...</span>
                </div>

                <div class="hidden md:block h-6 w-px bg-gray-200 dark:bg-gray-800"></div>

                <h2 id="page-title" class="text-xl font-bold text-gray-900 dark:text-white">...</h2>
            </div>
            <div class="flex items-center gap-6">
                <!-- Theme Toggle -->
                <button onclick="toggleTheme()" class="p-2.5 rounded-xl bg-gray-100 dark:bg-gray-800 text-gray-500 hover:text-emerald-500 transition-all focus:outline-none border border-gray-200 dark:border-gray-700 hover:border-emerald-500">
                    <svg id="theme-icon-sun" class="w-5 h-5 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                    <svg id="theme-icon-moon" class="w-5 h-5 block dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                </button>
            </div>
        </header>

        <!-- Breadcrumb Bar -->
        <div class="px-8 py-2 bg-gray-100/30 dark:bg-gray-900/10 border-b border-gray-200/50 dark:border-gray-800/50 flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-gray-400 transition-colors duration-300">
            <span class="opacity-50">OpenBrain</span>
            <span class="opacity-30">/</span>
            <span id="breadcrumb-active" class="text-emerald-500">...</span>
        </div>

        <!-- Pages Container -->
        <div class="flex-1 overflow-y-auto" id="pages-container">
            
            <!-- PAGE: HOME -->
            <div id="page-home" class="page p-8 max-w-6xl mx-auto space-y-10">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                    <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm transition-all hover:shadow-md">
                        <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Total Tokens</p>
                        <h3 id="stat-tokens-total" class="text-2xl font-black text-gray-900 dark:text-white">0</h3>
                    </div>
                    <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm transition-all hover:shadow-md">
                        <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Est. Cost ($)</p>
                        <h3 id="stat-tokens-cost" class="text-2xl font-black text-emerald-500">$0.00</h3>
                    </div>
                    <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm transition-all hover:shadow-md">
                        <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Active Skills</p>
                        <h3 id="stat-skills-active" class="text-2xl font-black text-gray-900 dark:text-white">0</h3>
                    </div>
                    <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-sm transition-all hover:shadow-md">
                        <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Backup Points</p>
                        <h3 id="stat-backups-total" class="text-2xl font-black text-gray-900 dark:text-white">0</h3>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <div class="lg:col-span-2 bg-white dark:bg-gray-900 p-8 rounded-3xl border border-gray-200 dark:border-gray-800 shadow-sm">
                        <div class="flex items-center justify-between mb-8">
                            <h3 class="text-lg font-bold text-gray-900 dark:text-white">Token Activity</h3>
                            <span class="text-xs font-bold text-gray-400 flex items-center gap-1">
                                <span class="w-3 h-3 bg-emerald-500 rounded-full"></span>
                                Last 7 Days
                            </span>
                        </div>
                        <div class="h-64">
                            <canvas id="tokenChart"></canvas>
                        </div>
                    </div>
                    <div class="bg-white dark:bg-gray-900 p-8 rounded-3xl border border-gray-200 dark:border-gray-800 shadow-sm">
                        <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-8">Usage by Model</h3>
                        <div id="model-usage-list" class="space-y-6">
                            <!-- List item -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE: SKILLS -->
            <div id="page-skills" class="page p-8 max-w-5xl mx-auto">
                <div class="bg-white dark:bg-gray-900 rounded-3xl border border-gray-200 dark:border-gray-800 overflow-hidden shadow-sm">
                    <div class="p-8 border-b border-gray-100 dark:border-gray-800 flex justify-between items-center">
                        <h3 class="text-xl font-bold text-gray-900 dark:text-white">Skill Management</h3>
                        <span id="skill-count-badge" class="text-[10px] font-black bg-gray-100 dark:bg-gray-800 text-gray-500 dark:text-gray-400 px-3 py-1 rounded-full uppercase tabular-nums">0 SKILLS</span>
                    </div>
                    <div id="skills-grid" class="p-4 grid grid-cols-1 md:grid-cols-2 gap-4">
                        <!-- Dynamic Skills -->
                    </div>
                </div>
            </div>

            <!-- PAGE: CONFIG -->
            <div id="page-config" class="page p-8 max-w-5xl mx-auto h-full flex flex-col">
                <div class="bg-white dark:bg-gray-900 rounded-3xl border border-gray-200 dark:border-gray-800 flex-1 flex flex-col overflow-hidden shadow-sm shadow-emerald-500/5">
                    <div class="p-6 border-b border-gray-100 dark:border-gray-800 flex justify-between items-center bg-gray-50/10 dark:bg-gray-950/10">
                        <div class="flex items-center gap-4">
                            <h3 class="text-xl font-bold text-gray-900 dark:text-white">System Configuration</h3>
                        </div>
                        <div class="flex items-center gap-4">
                            <!-- Model Selector inside Config -->
                            <div class="flex items-center gap-3 bg-gray-100 dark:bg-gray-800 px-4 py-2 rounded-xl border border-gray-200 dark:border-gray-700">
                                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-widest text-gray-400">Primary Model</span>
                                <select id="model-selector" class="bg-transparent text-sm font-bold text-gray-900 dark:text-white focus:outline-none cursor-pointer">
                                    <option>Loading...</option>
                                </select>
                            </div>
                            <button onclick="saveConfig()" class="bg-gray-900 dark:bg-white text-white dark:text-gray-900 px-6 py-2.5 rounded-xl text-sm font-bold shadow-xl shadow-black/10 dark:shadow-white/5 hover:scale-105 active:scale-95 transition-all">
                                Save JSON
                            </button>
                        </div>
                    </div>
                    <div class="flex-1 p-2 bg-gray-50/50 dark:bg-gray-950/50">
                        <textarea id="config-editor" class="w-full h-full bg-transparent text-gray-800 dark:text-emerald-400 p-6 font-mono text-sm focus:outline-none resize-none" spellcheck="false"></textarea>
                    </div>
                </div>
            </div>

            <!-- PAGE: BACKUPS -->
            <div id="page-backups" class="page p-8 max-w-5xl mx-auto">
                <div class="bg-white dark:bg-gray-900 rounded-3xl border border-gray-200 dark:border-gray-800 overflow-hidden shadow-sm">
                    <div class="p-8 border-b border-gray-100 dark:border-gray-800 flex justify-between items-center bg-gray-50/30 dark:bg-gray-950/30">
                        <div>
                            <h3 class="text-xl font-bold text-gray-900 dark:text-white">Restore Points</h3>
                            <p class="text-xs text-gray-400 font-medium mt-1">Full backup of your local OpenClaw environment.</p>
                        </div>
                        <button onclick="createBackup()" class="flex items-center gap-2 bg-emerald-500 hover:bg-emerald-600 text-white px-6 py-3 rounded-2xl text-sm font-bold shadow-lg shadow-emerald-500/20 transition-all active:scale-95">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                            Create Backup
                        </button>
                    </div>
                    <div class="divide-y divide-gray-100 dark:divide-gray-800" id="backups-list">
                        <!-- Dynamic Backups -->
                    </div>
                </div>
            </div>

        </div>
    </main>

    <!-- Notification -->
    <div id="toast" class="fixed top-24 right-8 transform translate-x-72 opacity-0 transition-all duration-500 z-50">
        <div class="bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-2xl shadow-2xl p-5 flex items-start gap-4 pr-12 min-w-[320px]">
            <div id="toast-icon-bg" class="p-2 rounded-xl">
                <div id="toast-icon" class="w-5 h-5"></div>
            </div>
            <div>
                <p id="toast-title" class="text-xs font-black uppercase tracking-widest text-gray-400">Notification</p>
                <p id="toast-message" class="text-sm font-semibold text-gray-700 dark:text-gray-200 mt-1"></p>
            </div>
            <button onclick="hideToast()" class="absolute top-4 right-4 text-gray-300 hover:text-gray-500">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
        </div>
    </div>

    <script>
        // ==========================================
        // SPA ROUTER
        // ==========================================
        const SPA = {
            currentHash: '',
            pages: ['home', 'skills', 'config', 'backups'],
            titles: {
                'home': 'System Overview',
                'skills': 'Skills Management',
                'config': 'System Configuration',
                'backups': 'Backups & Recovery'
            },
            init() {
                window.addEventListener('hashchange', () => this.handleRoute());
                const initialHash = window.location.hash.replace('#', '') || 'home';
                window.location.hash = initialHash;
                this.handleRoute();
            },
            handleRoute() {
                const hash = window.location.hash.replace('#', '') || 'home';
                if (!this.pages.includes(hash)) return;
                
                this.currentHash = hash;
                
                // Toggle Pages
                document.querySelectorAll('.page').forEach(p => p.classList.add('hidden'));
                document.getElementById(`page-${hash}`).classList.remove('hidden');
                
                // Update Nav Links
                document.querySelectorAll('.nav-link').forEach(link => {
                    const isSelected = link.getAttribute('href') === `#${hash}`;
                    link.className = `nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-bold transition-all group ${
                        isSelected 
                        ? 'bg-emerald-50 dark:bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 shadow-sm shadow-emerald-500/10' 
                        : 'text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-800/50'
                    }`;
                });
                
                // Update Topbar
                document.getElementById('page-title').textContent = this.titles[hash];
                document.getElementById('breadcrumb-active').textContent = hash.charAt(0).toUpperCase() + hash.slice(1);
                
                // Trigger page-specific loads
                if (hash === 'home') this.renderCharts();
                if (hash === 'skills') loadSkills();
                if (hash === 'backups') loadBackups();
                if (hash === 'config') loadConfig();
            },
            renderCharts() {
                if (!window.metrics) return;
                const ctx = document.getElementById('tokenChart');
                if (!ctx) return;
                
                if (window.myChart) window.myChart.destroy();
                
                const labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
                const datasets = Object.entries(window.metrics.token_usage).map(([model, data], i) => {
                    const colors = ['#10b981', '#3b82f6', '#f59e0b', '#8b5cf6'];
                    return {
                        label: model,
                        data: data.history,
                        borderColor: colors[i % colors.length],
                        backgroundColor: colors[i % colors.length] + '10',
                        borderWidth: 3,
                        tension: 0.4,
                        fill: true,
                        pointRadius: 0
                    };
                });

                window.myChart = new Chart(ctx, {
                    type: 'line',
                    data: { labels, datasets },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { legend: { display: false } },
                        scales: {
                            y: { display: false },
                            x: { grid: { display: false }, ticks: { font: { weight: 'bold', size: 10 }, color: '#94a3b8' } }
                        }
                    }
                });
                
                const list = document.getElementById('model-usage-list');
                list.innerHTML = Object.entries(window.metrics.token_usage).map(([model, data]) => `
                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-widest">${model}</span>
                            <span class="text-xs font-black text-gray-900 dark:text-white">${data.total.toLocaleString()}</span>
                        </div>
                        <div class="w-full h-1.5 bg-gray-100 dark:bg-gray-800 rounded-full overflow-hidden">
                            <div class="h-full bg-emerald-500 rounded-full" style="width: ${Math.min(100, (data.total / 500000) * 100)}%"></div>
                        </div>
                    </div>
                `).join('');
            }
        };

        const API = '/api';
        
        async function loadAll() {
            try {
                const [configRes, metricsRes] = await Promise.all([
                    fetch(`${API}/config`),
                    fetch(`${API}/metrics`)
                ]);
                
                if(!configRes.ok || !metricsRes.ok) throw new Error('API Error');
                
                window.config = await configRes.json();
                window.metrics = await metricsRes.json();
                
                document.getElementById('app-version').textContent = `v${window.config.version}`;
                const indicator = document.getElementById('status-indicator');
                indicator.className = 'w-2 h-2 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.5)]';
                document.getElementById('status-text').textContent = 'Connected';
                
                const totalTokens = Object.values(window.metrics.token_usage).reduce((acc, curr) => acc + curr.total, 0);
                const totalCost = Object.values(window.metrics.token_usage).reduce((acc, curr) => acc + curr.cost, 0);
                
                document.getElementById('stat-tokens-total').textContent = totalTokens.toLocaleString();
                document.getElementById('stat-tokens-cost').textContent = `$${totalCost.toFixed(2)}`;
                document.getElementById('stat-skills-active').textContent = window.metrics.active_skills;
                document.getElementById('stat-backups-total').textContent = window.metrics.total_backups;

                document.getElementById('header-active-model').textContent = window.config.active_model;

                const select = document.getElementById('model-selector');
                if (select) {
                    select.innerHTML = window.config.available_models.map(m => `
                        <option value="${m}" ${m === window.config.active_model ? 'selected' : ''}>${m}</option>
                    `).join('');
                    
                    select.onchange = async (e) => {
                        const oldModel = window.config.active_model;
                        window.config.active_model = e.target.value;
                        document.getElementById('header-active-model').textContent = e.target.value;
                        const editor = document.getElementById('config-editor');
                        if (editor) editor.value = JSON.stringify(window.config, null, 4);
                        
                        try {
                            const res = await fetch(`${API}/config`, {
                                method: 'POST',
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify(window.config)
                            });
                            if (res.ok) showToast('Primary Model Updated', 'success');
                            else throw new Error();
                        } catch {
                            window.config.active_model = oldModel;
                            e.target.value = oldModel;
                            document.getElementById('header-active-model').textContent = oldModel;
                            if (editor) editor.value = JSON.stringify(window.config, null, 4);
                            showToast('Error changing model', 'error');
                        }
                    };
                }

                SPA.init();
            } catch (err) {
                console.error(err);
                document.getElementById('status-text').textContent = 'Offline';
            }
        }

        async function loadSkills() {
            const res = await fetch(`${API}/skills`);
            const data = await res.json();
            const grid = document.getElementById('skills-grid');
            document.getElementById('skill-count-badge').textContent = `${data.skills.length} SKILLS`;
            
            grid.innerHTML = data.skills.map(skill => `
                <div class="flex items-center justify-between p-5 bg-gray-50/50 dark:bg-gray-800/30 border border-gray-100 dark:border-gray-800 rounded-2xl transition-all hover:border-emerald-500/50 group">
                    <div class="flex items-center gap-4">
                        <div class="p-3 bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 text-gray-400 group-hover:text-emerald-500 transition-colors">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"></path></svg>
                        </div>
                        <div>
                            <p class="text-sm font-black text-gray-900 dark:text-white uppercase tracking-tight">${skill.name}</p>
                            <span class="text-[10px] font-bold ${skill.active ? 'text-emerald-500' : 'text-gray-400'} uppercase">${skill.active ? 'Active' : 'Disabled'}</span>
                        </div>
                    </div>
                    <button onclick="toggleSkill('${skill.name}')" 
                            class="relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none ${skill.active ? 'bg-emerald-500' : 'bg-gray-200 dark:bg-gray-700'}">
                        <span class="pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow-xl transition duration-200 ease-in-out ${skill.active ? 'translate-x-5' : 'translate-x-0'}"></span>
                    </button>
                </div>
            `).join('');
        }

        async function toggleSkill(name) {
            const res = await fetch(`${API}/skills/toggle`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name})
            });
            if (res.ok) {
                const r = await res.json();
                showToast(`Skill ${name} ${r.active ? 'enabled' : 'disabled'}`, 'success');
                loadSkills();
            }
        }

        async function loadBackups() {
            const res = await fetch(`${API}/backups`);
            const data = await res.json();
            const list = document.getElementById('backups-list');
            
            if (data.backups.length === 0) {
                list.innerHTML = '<div class="p-12 text-center text-gray-400 font-bold uppercase tracking-widest text-[10px]">No backups created yet</div>';
                return;
            }
            
            list.innerHTML = data.backups.map(b => {
                // Parse date from filename: backup_YYYYMMDD_HHMMSS.zip
                let dateStr = "Unknown Date";
                const match = b.name.match(/backup_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})/);
                if (match) {
                    const [_, year, month, day, hour, min, sec] = match;
                    dateStr = `${day}/${month}/${year} ${hour}:${min}`;
                }

                return `
                <div class="p-6 flex items-center justify-between hover:bg-gray-50/50 dark:hover:bg-gray-800/30 transition-all group">
                    <div class="flex items-center gap-4">
                        <div class="w-10 h-10 bg-gray-100 dark:bg-gray-800 rounded-xl flex items-center justify-center text-gray-400 group-hover:text-emerald-500 transition-colors">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                        </div>
                        <div>
                            <p class="text-sm font-bold text-gray-800 dark:text-gray-200">${dateStr}</p>
                            <p class="text-[10px] font-black text-gray-400 dark:text-gray-600 uppercase tracking-widest">${b.name} • ${b.size}</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="deleteBackup('${b.name}')" class="p-2 text-gray-300 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition-all opacity-0 group-hover:opacity-100">
                             <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                        </button>
                    </div>
                </div>`;
            }).join('');

            // Add Restore Guide at the end of the list if it doesn't exist
            if (!document.getElementById('restore-guide')) {
                const guide = document.createElement('div');
                guide.id = 'restore-guide';
                guide.className = 'p-8 bg-emerald-50/50 dark:bg-emerald-900/10 border-t border-gray-100 dark:border-gray-800';
                guide.innerHTML = `
                    <h4 class="text-xs font-black uppercase tracking-widest text-emerald-600 dark:text-emerald-400 mb-4">Restore Guide</h4>
                    <div class="space-y-3">
                        <p class="text-xs text-gray-600 dark:text-gray-400 flex items-start gap-2">
                            <span class="font-bold text-emerald-500">1.</span>
                            <span>Unzip the backup file into a temporary directory.</span>
                        </p>
                        <p class="text-xs text-gray-600 dark:text-gray-400 flex items-start gap-2">
                            <span class="font-bold text-emerald-500">2.</span>
                            <span>Copy the contents (openclaw.json, skills/, etc.) to your <b>~/.openclaw</b> directory.</span>
                        </p>
                        <p class="text-xs text-gray-600 dark:text-gray-400 flex items-start gap-2">
                            <span class="font-bold text-emerald-500">3.</span>
                            <span>Restart OpenBrain to see the changes applied.</span>
                        </p>
                    </div>
                `;
                list.parentElement.appendChild(guide);
            }
        }

        async function createBackup() {
            showToast('Creating compressed backup...', 'success');
            const res = await fetch(`${API}/backups`, {method: 'POST'});
            if (res.ok) {
                showToast('Restore point created', 'success');
                loadBackups();
            }
        }

        async function deleteBackup(name) {
            if (!confirm(`Permanently delete backup?`)) return;
            const res = await fetch(`${API}/backups/${name}`, {method: 'DELETE'});
            if (res.ok) {
                showToast('File deleted', 'success');
                loadBackups();
            }
        }

        async function loadConfig() {
            const res = await fetch(`${API}/config`);
            const data = await res.json();
            document.getElementById('config-editor').value = JSON.stringify(data, null, 4);
        }

        async function saveConfig() {
            try {
                const raw = document.getElementById('config-editor').value;
                const parsed = JSON.parse(raw);
                const res = await fetch(`${API}/config`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(parsed)
                });
                if (res.ok) {
                    showToast('Configuration saved and validated', 'success');
                    window.config = parsed;
                } else throw new Error();
            } catch {
                showToast('Error: Invalid JSON or Network failure', 'error');
            }
        }

        function toggleTheme() {
            const html = document.documentElement;
            html.classList.toggle('dark');
            localStorage.theme = html.classList.contains('dark') ? 'dark' : 'light';
        }
        
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        }

        function showToast(message, type = 'success') {
            const toast = document.getElementById('toast');
            document.getElementById('toast-message').textContent = message;
            const bg = document.getElementById('toast-icon-bg');
            const icon = document.getElementById('toast-icon');
            
            if (type === 'success') {
                bg.className = 'p-2 rounded-xl bg-emerald-50 dark:bg-emerald-900/20 text-emerald-500';
                icon.innerHTML = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>';
            } else {
                bg.className = 'p-2 rounded-xl bg-red-50 dark:bg-red-900/20 text-red-500';
                icon.innerHTML = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>';
            }
            
            toast.classList.remove('translate-x-72', 'opacity-0');
            setTimeout(hideToast, 4000);
        }

        function hideToast() {
            document.getElementById('toast').classList.add('translate-x-72', 'opacity-0');
        }

        document.addEventListener('DOMContentLoaded', loadAll);
    </script>
</body>
</html>
"""
