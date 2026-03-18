<template>
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Back -->
    <Link href="/collection/" class="inline-flex items-center gap-2 text-gd-muted hover:text-white text-sm mb-6 transition-colors group">
      <svg class="w-4 h-4 group-hover:-translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
      </svg>
      Volver a la colección
    </Link>

    <!-- Hero -->
    <div class="bg-gd-surface border border-gd-border/60 rounded-2xl overflow-hidden mb-6">
      <div class="h-72 bg-gradient-to-br flex items-end p-6 relative overflow-hidden" :class="coverGradient">
        <img
          v-if="game.cover_url"
          :src="game.cover_url"
          :alt="game.name"
          class="absolute inset-0 w-full h-full object-cover"
          @error="e => e.target.style.display = 'none'"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-gd-bg via-gd-bg/60 to-transparent" />
        <div class="relative z-10">
          <div class="flex flex-wrap gap-2 mb-3">
            <span v-if="game.genre" class="text-xs font-semibold bg-gd-accent/25 text-gd-accent border border-gd-accent/30 rounded-full px-3 py-1 backdrop-blur-sm">
              {{ game.genre.name }}
            </span>
            <span v-if="game.release_year" class="text-xs font-semibold bg-gd-hot/20 text-gd-hot border border-gd-hot/30 rounded-full px-3 py-1 backdrop-blur-sm">
              {{ game.release_year }}
            </span>
          </div>
          <h1 class="text-4xl font-bold text-white leading-tight font-display">{{ game.name }}</h1>
        </div>
      </div>

      <div class="p-6">
        <p v-if="game.description" class="text-gd-muted leading-relaxed">{{ game.description }}</p>
        <p v-else class="text-gd-muted italic">Sin descripción disponible.</p>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Info cards -->
      <div class="lg:col-span-1 space-y-4">
        <!-- Developer -->
        <InfoCard title="Desarrollador">
          <span class="text-white font-medium">{{ game.developer?.name || '—' }}</span>
        </InfoCard>

        <!-- Publisher -->
        <InfoCard title="Publisher">
          <span class="text-white font-medium">{{ game.publisher?.name || '—' }}</span>
        </InfoCard>

        <!-- Consoles -->
        <InfoCard title="Plataformas">
          <div v-if="game.consoles.length" class="flex flex-wrap gap-1.5">
            <span
              v-for="c in game.consoles"
              :key="c.id"
              class="text-xs bg-gd-card border border-gd-border/60 text-gd-muted rounded-lg px-2.5 py-1 hover:text-white hover:border-gd-accent/30 transition-colors"
            >
              {{ c.name }}
            </span>
          </div>
          <span v-else class="text-gd-muted text-sm">Sin plataformas registradas</span>
        </InfoCard>
      </div>

      <!-- Releases table -->
      <div class="lg:col-span-2">
        <div class="bg-gd-surface border border-gd-border/60 rounded-xl overflow-hidden">
          <div class="px-5 py-4 border-b border-gd-border/60 bg-gd-card/50">
            <h2 class="text-white font-semibold font-display">
              Lanzamientos
              <span class="ml-2 text-xs bg-gd-accent/20 text-gd-accent rounded-full px-2 py-0.5">
                {{ game.releases?.length || 0 }}
              </span>
            </h2>
          </div>

          <div v-if="!game.releases?.length" class="text-center py-10 text-gd-muted text-sm">
            No hay información de lanzamientos
          </div>

          <table v-else class="w-full">
            <thead>
              <tr class="bg-gd-card border-b border-gd-border/60">
                <th class="text-left px-5 py-3 text-xs font-semibold text-gd-muted uppercase tracking-wider">Región</th>
                <th class="text-left px-5 py-3 text-xs font-semibold text-gd-muted uppercase tracking-wider">Consola</th>
                <th class="text-left px-5 py-3 text-xs font-semibold text-gd-muted uppercase tracking-wider">Fecha</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="release in game.releases"
                :key="release.id"
                class="border-b border-gd-border/30 last:border-0 hover:bg-gd-accent/5 transition-colors"
              >
                <td class="px-5 py-3.5">
                  <div class="flex items-center gap-2.5">
                    <span class="text-xs font-bold bg-gd-accent/15 text-gd-accent border border-gd-accent/20 rounded px-1.5 py-0.5 font-mono">
                      {{ release.region.code }}
                    </span>
                    <span class="text-white text-sm">{{ release.region.name }}</span>
                  </div>
                </td>
                <td class="px-5 py-3.5">
                  <span class="text-gd-muted text-sm">{{ release.console?.name || 'PC / Digital' }}</span>
                </td>
                <td class="px-5 py-3.5">
                  <span class="text-gd-muted text-sm tabular-nums">{{ formatDate(release.release_date) }}</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Link } from '@inertiajs/vue3'
import InfoCard from '../components/InfoCard.vue'

const props = defineProps({
  game: Object,
})

const gradients = [
  'from-purple-900 via-purple-800 to-blue-900',
  'from-red-900 via-red-800 to-orange-900',
  'from-green-900 via-green-800 to-teal-900',
  'from-blue-900 via-blue-800 to-indigo-900',
  'from-pink-900 via-pink-800 to-purple-900',
  'from-yellow-900 via-yellow-800 to-orange-900',
]

const coverGradient = computed(() => {
  const idx = props.game.name.charCodeAt(0) % gradients.length
  return gradients[idx]
})

function formatDate(date) {
  if (!date) return '—'
  return new Date(date + 'T00:00:00').toLocaleDateString('es-ES', {
    day: '2-digit', month: 'short', year: 'numeric',
  })
}
</script>
