<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-4xl font-bold text-white font-display">Catálogo de Juegos</h1>
      <p class="text-gd-muted mt-1.5">{{ filteredGames.length }} juego{{ filteredGames.length !== 1 ? 's' : '' }} encontrado{{ filteredGames.length !== 1 ? 's' : '' }}</p>
    </div>

    <div class="flex gap-6">
      <!-- Sidebar Filters -->
      <aside class="w-64 flex-shrink-0">
        <div class="bg-gd-surface border border-gd-border/60 rounded-xl p-4 sticky top-20 space-y-5">
          <h2 class="text-white font-semibold text-xs uppercase tracking-widest">Filtros</h2>

          <!-- Search -->
          <div>
            <label class="text-gd-muted text-xs uppercase tracking-wider mb-2 block">Buscar</label>
            <div class="relative">
              <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gd-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <input
                v-model="localFilters.search"
                type="text"
                placeholder="Nombre del juego…"
                class="w-full bg-gd-card border border-gd-border/60 rounded-lg pl-9 pr-3 py-2 text-sm text-white placeholder-gd-muted focus:outline-none focus:border-gd-accent/60 focus:ring-1 focus:ring-gd-accent/20 transition-colors"
              />
            </div>
          </div>

          <!-- Genre -->
          <div>
            <label class="text-gd-muted text-xs uppercase tracking-wider mb-2 block">Género</label>
            <select
              v-model="localFilters.genre"
              class="w-full bg-gd-card border border-gd-border/60 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-gd-accent/60 transition-colors"
            >
              <option value="">Todos los géneros</option>
              <option v-for="g in genres" :key="g.id" :value="g.id">{{ g.name }}</option>
            </select>
          </div>

          <!-- Console -->
          <div>
            <label class="text-gd-muted text-xs uppercase tracking-wider mb-2 block">Consola</label>
            <select
              v-model="localFilters.console"
              class="w-full bg-gd-card border border-gd-border/60 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-gd-accent/60 transition-colors"
            >
              <option value="">Todas las consolas</option>
              <option v-for="c in consoles" :key="c.id" :value="c.id">{{ c.name }}</option>
            </select>
          </div>

          <!-- Year -->
          <div>
            <label class="text-gd-muted text-xs uppercase tracking-wider mb-2 block">Año</label>
            <select
              v-model="localFilters.year"
              class="w-full bg-gd-card border border-gd-border/60 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-gd-accent/60 transition-colors"
            >
              <option value="">Todos los años</option>
              <option v-for="y in years" :key="y" :value="String(y)">{{ y }}</option>
            </select>
          </div>

          <!-- Reset -->
          <button
            v-if="hasActiveFilters"
            @click="resetFilters"
            class="w-full py-2 text-sm text-gd-accent hover:text-white border border-gd-accent/40 hover:bg-gd-accent rounded-lg transition-colors"
          >
            Limpiar filtros
          </button>
        </div>
      </aside>

      <!-- Games Grid -->
      <div class="flex-1">
        <div v-if="filteredGames.length === 0" class="flex flex-col items-center justify-center py-20 text-gd-muted">
          <svg class="w-16 h-16 mb-4 opacity-30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-lg font-medium">No se encontraron juegos</p>
          <p class="text-sm mt-1">Prueba con otros filtros</p>
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          <Link
            v-for="game in filteredGames"
            :key="game.id"
            :href="`/collection/${game.slug}/`"
            class="group bg-gd-card border border-gd-border/60 rounded-2xl overflow-hidden hover:border-gd-accent/40 hover:shadow-xl hover:shadow-gd-accent/20 hover:scale-[1.02] transition-all duration-200 cursor-pointer"
          >
            <!-- Cover with overlay -->
            <div class="h-48 relative overflow-hidden bg-gradient-to-br" :class="coverGradient(game)">
              <img
                v-if="game.cover_url"
                :src="game.cover_url"
                :alt="game.name"
                class="absolute inset-0 w-full h-full object-cover"
                loading="lazy"
                @error="e => e.target.style.display = 'none'"
              />
              <!-- Bottom overlay with game info -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent" />
              <div class="absolute bottom-0 left-0 right-0 p-3">
                <h3 class="text-white font-semibold text-sm leading-snug line-clamp-2 drop-shadow">
                  {{ game.name }}
                </h3>
                <div class="mt-1.5 flex items-center gap-1.5 flex-wrap">
                  <span v-if="game.genre" class="text-xs bg-gd-accent/30 text-gd-accent rounded-full px-2 py-0.5 backdrop-blur-sm">
                    {{ game.genre.name }}
                  </span>
                  <span class="text-xs font-bold bg-black/40 text-white/70 rounded px-1.5 py-0.5 backdrop-blur-sm ml-auto">
                    {{ game.release_year || '—' }}
                  </span>
                </div>
              </div>
            </div>
          </Link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Link } from '@inertiajs/vue3'

const props = defineProps({
  games: Array,
  genres: Array,
  consoles: Array,
  years: Array,
  filters: Object,
})

const localFilters = ref({
  search: props.filters?.search || '',
  genre: props.filters?.genre || '',
  console: props.filters?.console || '',
  year: props.filters?.year || '',
})

const hasActiveFilters = computed(() =>
  Object.values(localFilters.value).some(v => v !== '')
)

const filteredGames = computed(() => {
  return props.games.filter(game => {
    const { search, genre, console: consoleId, year } = localFilters.value
    if (search && !game.name.toLowerCase().includes(search.toLowerCase())) return false
    if (genre && game.genre?.id !== genre) return false
    if (consoleId && !game.consoles.some(c => c.id === consoleId)) return false
    if (year && String(game.release_year) !== year) return false
    return true
  })
})

function resetFilters() {
  localFilters.value = { search: '', genre: '', console: '', year: '' }
}

const gradients = [
  'from-purple-900 to-blue-900',
  'from-red-900 to-orange-900',
  'from-green-900 to-teal-900',
  'from-blue-900 to-indigo-900',
  'from-pink-900 to-purple-900',
  'from-yellow-900 to-orange-900',
]

function coverGradient(game) {
  const idx = game.name.charCodeAt(0) % gradients.length
  return gradients[idx]
}
</script>
