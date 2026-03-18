<template>
  <div class="min-h-screen bg-gd-bg flex flex-col">
    <!-- Top glow -->
    <div class="fixed top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-gd-accent/60 to-transparent z-50 pointer-events-none" />

    <!-- Navbar -->
    <nav class="bg-gd-bg/95 backdrop-blur-md border-b border-gd-border/50 sticky top-0 z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-14">
          <!-- Logo -->
          <Link href="/" class="flex items-center gap-2.5 group">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" class="w-8 h-8 flex-shrink-0">
              <defs>
                <linearGradient id="logo-bg" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#7c3aed"/>
                  <stop offset="100%" stop-color="#4f46e5"/>
                </linearGradient>
              </defs>
              <circle cx="32" cy="32" r="32" fill="url(#logo-bg)"/>
              <rect x="12" y="22" width="40" height="22" rx="11" ry="11" fill="white" opacity="0.95"/>
              <rect x="12" y="30" width="10" height="18" rx="5" ry="5" fill="white" opacity="0.95"/>
              <rect x="42" y="30" width="10" height="18" rx="5" ry="5" fill="white" opacity="0.95"/>
              <rect x="18" y="31" width="10" height="3.5" rx="1.5" fill="#4f46e5"/>
              <rect x="21.25" y="28" width="3.5" height="10" rx="1.5" fill="#4f46e5"/>
              <circle cx="40" cy="30" r="2" fill="#7c3aed"/>
              <circle cx="44" cy="33.5" r="2" fill="#06b6d4"/>
              <circle cx="36" cy="33.5" r="2" fill="#f59e0b"/>
              <circle cx="40" cy="37" r="2" fill="#4f46e5"/>
              <rect x="29" y="31.5" width="3" height="2.5" rx="1.25" fill="#4f46e5" opacity="0.7"/>
              <rect x="32.5" y="31.5" width="3" height="2.5" rx="1.25" fill="#4f46e5" opacity="0.7"/>
            </svg>
            <span class="text-white font-bold text-xl tracking-tight font-display">
              Game<span class="text-gd-accent">Dex</span>
            </span>
          </Link>

          <!-- Nav links -->
          <div class="flex items-center gap-1">
            <ThemePicker />
            <NavLink href="/" :active="$page.url === '/' || $page.url.startsWith('/?')">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
              </svg>
              Catálogo
            </NavLink>
            <NavLink href="/collection/" :active="$page.url.startsWith('/collection')">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
              </svg>
              Colección
            </NavLink>
            <NavLink href="/api-explorer/" :active="$page.url.startsWith('/api-explorer')">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
              </svg>
              API
            </NavLink>
          </div>
        </div>
      </div>
    </nav>

    <!-- Page content -->
    <main class="flex-1">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="border-t border-gd-border/50 py-5 text-center text-gd-muted text-xs">
      <span class="opacity-50">GameDex &mdash; {{ new Date().getFullYear() }}</span>
    </footer>
  </div>
</template>

<script setup>
import { Link } from '@inertiajs/vue3'
import NavLink from './NavLink.vue'
import ThemePicker from './ThemePicker.vue'
</script>
