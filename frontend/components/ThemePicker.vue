<template>
  <div class="relative" ref="container">
    <button
      @click="open = !open"
      class="flex items-center gap-2 px-3 py-2 rounded-lg text-sm text-gd-muted hover:text-white hover:bg-gd-card border border-transparent hover:border-gd-border/60 transition-all"
      title="Cambiar tema"
    >
      <span class="w-3 h-3 rounded-full border border-white/20 flex-shrink-0" :style="{ background: currentColor }"></span>
      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01" />
      </svg>
    </button>

    <!-- Dropdown -->
    <div
      v-if="open"
      class="absolute right-0 top-full mt-2 bg-gd-surface border border-gd-border/60 rounded-xl p-3 shadow-xl shadow-black/50 z-50 min-w-[160px]"
    >
      <p class="text-xs text-gd-muted uppercase tracking-widest mb-2.5 px-1">Tema</p>
      <div class="space-y-0.5">
        <button
          v-for="(theme, key) in themes"
          :key="key"
          @click="select(key)"
          class="w-full flex items-center gap-3 px-2.5 py-2 rounded-lg text-sm transition-colors"
          :class="currentTheme === key
            ? 'bg-gd-card text-white'
            : 'text-gd-muted hover:text-white hover:bg-gd-card/60'"
        >
          <span
            class="w-4 h-4 rounded-full flex-shrink-0 border-2"
            :style="{ background: theme.accent, borderColor: currentTheme === key ? 'white' : 'transparent' }"
          ></span>
          {{ theme.label }}
          <svg v-if="currentTheme === key" class="w-3.5 h-3.5 ml-auto text-white/60" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useTheme, THEMES } from '../composables/useTheme.js'

const { currentTheme, themes, setTheme } = useTheme()
const open = ref(false)
const container = ref(null)

const currentColor = computed(() => THEMES[currentTheme.value]?.accent ?? '#7c3aed')

function select(key) {
  setTheme(key)
  open.value = false
}

function onClickOutside(e) {
  if (container.value && !container.value.contains(e.target)) {
    open.value = false
  }
}

onMounted(() => document.addEventListener('click', onClickOutside))
onUnmounted(() => document.removeEventListener('click', onClickOutside))
</script>
