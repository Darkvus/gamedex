<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-4xl font-bold text-white font-display">Colección</h1>
        <p class="text-gd-muted mt-1.5">{{ filtered.length }} de {{ games.length }} juegos</p>
      </div>
    </div>

    <!-- Search + Sort -->
    <div class="flex flex-col sm:flex-row gap-3 mb-6">
      <div class="relative flex-1">
        <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gd-muted" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
        <input
          v-model="search"
          type="text"
          placeholder="Buscar juego…"
          class="w-full bg-gd-surface border border-gd-border/60 rounded-lg pl-9 pr-4 py-2.5 text-sm text-white placeholder-gd-muted focus:outline-none focus:border-gd-accent/60 focus:ring-1 focus:ring-gd-accent/20 transition-colors"
        />
      </div>
      <select
        v-model="sortBy"
        class="bg-gd-surface border border-gd-border/60 rounded-lg px-3 py-2.5 text-sm text-white focus:outline-none focus:border-gd-accent/60 transition-colors"
      >
        <option value="name">Nombre A-Z</option>
        <option value="name_desc">Nombre Z-A</option>
        <option value="year_desc">Más reciente</option>
        <option value="year_asc">Más antiguo</option>
      </select>
    </div>

    <!-- Table -->
    <div class="bg-gd-surface border border-gd-border/60 rounded-xl overflow-hidden">
      <table class="w-full">
        <thead>
          <tr class="bg-gd-card border-b border-gd-border">
            <th class="text-left px-4 py-3.5 text-xs font-semibold text-gd-muted uppercase tracking-wider">Juego</th>
            <th class="text-left px-4 py-3.5 text-xs font-semibold text-gd-muted uppercase tracking-wider hidden md:table-cell">Género</th>
            <th class="text-left px-4 py-3.5 text-xs font-semibold text-gd-muted uppercase tracking-wider hidden lg:table-cell">Desarrollador</th>
            <th class="text-left px-4 py-3.5 text-xs font-semibold text-gd-muted uppercase tracking-wider hidden sm:table-cell">Año</th>
            <th class="text-left px-4 py-3.5 text-xs font-semibold text-gd-muted uppercase tracking-wider hidden xl:table-cell">Consolas</th>
            <th class="px-4 py-3.5"></th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(game, i) in paginated"
            :key="game.id"
            class="border-b border-gd-border/40 hover:bg-gd-accent/5 hover:border-l-2 hover:border-l-gd-accent transition-all cursor-pointer"
            :class="i % 2 === 0 ? '' : 'bg-white/[0.015]'"
            @click="navigate(game.slug)"
          >
            <td class="px-4 py-3.5">
              <div class="flex items-center gap-3">
                <div class="w-9 h-12 rounded-md overflow-hidden flex-shrink-0 bg-gd-card border border-gd-border/60">
                  <img
                    v-if="game.cover_url"
                    :src="game.cover_url"
                    :alt="game.name"
                    class="w-full h-full object-cover"
                    loading="lazy"
                    @error="e => e.target.style.display = 'none'"
                  />
                </div>
                <div class="font-medium text-white text-sm">{{ game.name }}</div>
              </div>
            </td>
            <td class="px-4 py-3.5 hidden md:table-cell">
              <span v-if="game.genre" class="text-xs bg-gd-accent/20 text-gd-accent rounded-full px-2 py-0.5">
                {{ game.genre.name }}
              </span>
              <span v-else class="text-gd-muted text-xs">—</span>
            </td>
            <td class="px-4 py-3.5 hidden lg:table-cell">
              <span class="text-gd-muted text-sm">{{ game.developer?.name || '—' }}</span>
            </td>
            <td class="px-4 py-3.5 hidden sm:table-cell">
              <span class="text-gd-muted text-sm tabular-nums">{{ game.release_year || '—' }}</span>
            </td>
            <td class="px-4 py-3.5 hidden xl:table-cell">
              <div class="flex gap-1 flex-wrap max-w-xs">
                <span
                  v-for="c in game.consoles.slice(0, 2)"
                  :key="c.id"
                  class="text-xs bg-gd-border text-gd-muted rounded px-1.5 py-0.5"
                >{{ c.name }}</span>
                <span v-if="game.consoles.length > 2" class="text-xs text-gd-muted">
                  +{{ game.consoles.length - 2 }}
                </span>
              </div>
            </td>
            <td class="px-4 py-3.5 text-right">
              <Link :href="`/collection/${game.slug}/`" class="text-gd-accent hover:text-white text-xs font-medium transition-colors" @click.stop>
                Ver →
              </Link>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Empty state -->
      <div v-if="filtered.length === 0" class="text-center py-16 text-gd-muted">
        <p class="text-lg">No se encontraron juegos</p>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="totalPages > 1" class="flex items-center justify-between mt-6">
      <p class="text-gd-muted text-sm">
        Página {{ currentPage }} de {{ totalPages }}
      </p>
      <div class="flex gap-2">
        <button
          :disabled="currentPage === 1"
          @click="currentPage--"
          class="px-4 py-2 text-sm rounded-full border border-gd-border text-gd-muted hover:text-white hover:border-gd-accent hover:bg-gd-accent/10 disabled:opacity-30 disabled:cursor-not-allowed transition-all"
        >← Anterior</button>
        <button
          :disabled="currentPage === totalPages"
          @click="currentPage++"
          class="px-4 py-2 text-sm rounded-full border border-gd-border text-gd-muted hover:text-white hover:border-gd-accent hover:bg-gd-accent/10 disabled:opacity-30 disabled:cursor-not-allowed transition-all"
        >Siguiente →</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { Link, router } from '@inertiajs/vue3'

const props = defineProps({
  games: Array,
})

const search = ref('')
const sortBy = ref('name')
const currentPage = ref(1)
const perPage = 25

watch(search, () => { currentPage.value = 1 })

const filtered = computed(() => {
  let list = [...props.games]
  if (search.value) {
    const q = search.value.toLowerCase()
    list = list.filter(g => g.name.toLowerCase().includes(q))
  }
  switch (sortBy.value) {
    case 'name':      list.sort((a, b) => a.name.localeCompare(b.name)); break
    case 'name_desc': list.sort((a, b) => b.name.localeCompare(a.name)); break
    case 'year_desc': list.sort((a, b) => (b.release_year || 0) - (a.release_year || 0)); break
    case 'year_asc':  list.sort((a, b) => (a.release_year || 9999) - (b.release_year || 9999)); break
  }
  return list
})

const totalPages = computed(() => Math.ceil(filtered.value.length / perPage))
const paginated = computed(() => {
  const start = (currentPage.value - 1) * perPage
  return filtered.value.slice(start, start + perPage)
})

function navigate(slug) {
  router.visit(`/collection/${slug}/`)
}
</script>
