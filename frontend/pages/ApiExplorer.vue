<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <div class="flex items-center gap-3 mb-2">
        <div class="w-10 h-10 bg-gd-accent/20 border border-gd-accent/30 rounded-xl flex items-center justify-center">
          <svg class="w-5 h-5 text-gd-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
          </svg>
        </div>
        <div>
          <h1 class="text-3xl font-bold text-white">API Explorer</h1>
          <p class="text-gd-muted text-sm">GameDex REST API — v1</p>
        </div>
      </div>
      <div class="flex items-center gap-3 mt-4">
        <span class="text-xs bg-green-900/50 text-green-400 border border-green-700/50 rounded-full px-3 py-1 font-medium">● Live</span>
        <span class="text-xs text-gd-muted font-mono">Base URL: <span class="text-white">{{ baseUrl }}</span></span>
      </div>
    </div>

    <div class="flex gap-6">
      <!-- Sidebar -->
      <aside class="w-52 flex-shrink-0">
        <nav class="sticky top-24 space-y-1">
          <button
            v-for="group in endpoints"
            :key="group.group"
            @click="activeGroup = group.group"
            class="w-full text-left flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm transition-colors"
            :class="activeGroup === group.group
              ? 'bg-gd-accent/20 text-gd-accent font-medium'
              : 'text-gd-muted hover:text-white hover:bg-gd-card'"
          >
            <span class="w-2 h-2 rounded-full flex-shrink-0" :class="`bg-${group.color}-400`"></span>
            {{ group.group }}
            <span class="ml-auto text-xs opacity-60">{{ group.endpoints.length }}</span>
          </button>
        </nav>
      </aside>

      <!-- Endpoints -->
      <div class="flex-1 space-y-4">
        <template v-for="group in endpoints" :key="group.group">
          <div v-if="activeGroup === group.group || activeGroup === 'all'" :id="group.group.toLowerCase()">
            <!-- Group header -->
            <div class="flex items-center gap-3 mb-4">
              <span class="w-3 h-3 rounded-full" :class="`bg-${group.color}-400`"></span>
              <h2 class="text-xl font-bold text-white">{{ group.group }}</h2>
              <div class="flex-1 h-px bg-gd-border"></div>
            </div>

            <!-- Endpoint cards -->
            <div v-for="ep in group.endpoints" :key="ep.path" class="mb-3">
              <div
                class="bg-gd-surface border border-gd-border rounded-xl overflow-hidden cursor-pointer hover:border-gd-accent/50 transition-colors"
                @click="toggleEndpoint(ep.path)"
              >
                <!-- Header row -->
                <div class="flex items-center gap-3 px-4 py-3">
                  <span class="text-xs font-bold bg-green-600/30 text-green-400 border border-green-600/40 rounded px-2 py-0.5 font-mono w-10 text-center flex-shrink-0">
                    GET
                  </span>
                  <code class="text-white text-sm font-mono flex-1">{{ ep.path }}</code>
                  <span class="text-gd-muted text-xs hidden sm:block">{{ ep.description }}</span>
                  <svg
                    class="w-4 h-4 text-gd-muted flex-shrink-0 transition-transform"
                    :class="expanded.has(ep.path) ? 'rotate-180' : ''"
                    fill="none" stroke="currentColor" viewBox="0 0 24 24"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </div>

                <!-- Expanded content -->
                <div v-if="expanded.has(ep.path)" class="border-t border-gd-border" @click.stop>
                  <div class="p-4 space-y-4">
                    <p class="text-gd-muted text-sm">{{ ep.description }}</p>

                    <!-- Parameters -->
                    <div v-if="ep.params.length">
                      <h4 class="text-xs font-semibold text-gd-muted uppercase tracking-wider mb-2">Parámetros</h4>
                      <div class="space-y-1.5">
                        <div
                          v-for="param in ep.params"
                          :key="param.name"
                          class="flex items-start gap-3 bg-gd-card rounded-lg px-3 py-2"
                        >
                          <div class="flex items-center gap-2 min-w-0">
                            <code class="text-gd-accent text-xs font-mono">{{ param.name }}</code>
                            <span class="text-xs text-gd-muted font-mono bg-gd-border rounded px-1.5 py-0.5">{{ param.type }}</span>
                            <span v-if="param.required" class="text-xs text-red-400">requerido</span>
                            <span v-else class="text-xs text-gd-muted/60">opcional</span>
                          </div>
                          <span class="text-gd-muted text-xs flex-1 text-right">{{ param.description }}</span>
                        </div>
                      </div>
                    </div>
                    <div v-else class="text-xs text-gd-muted">Sin parámetros</div>

                    <!-- Try it -->
                    <div>
                      <div class="flex items-center gap-2 mb-2">
                        <h4 class="text-xs font-semibold text-gd-muted uppercase tracking-wider">Try it out</h4>
                        <div class="flex-1 h-px bg-gd-border"></div>
                      </div>
                      <div class="flex gap-2">
                        <div class="flex-1 flex items-center gap-2 bg-gd-card border border-gd-border rounded-lg px-3 py-2">
                          <span class="text-green-400 text-xs font-mono font-bold">GET</span>
                          <input
                            v-model="tryUrls[ep.path]"
                            class="flex-1 bg-transparent text-sm text-white font-mono focus:outline-none min-w-0"
                            :placeholder="baseUrl + ep.path"
                          />
                        </div>
                        <button
                          @click="executeRequest(ep)"
                          :disabled="loading[ep.path]"
                          class="px-4 py-2 bg-gd-accent hover:bg-gd-accent/80 text-white text-sm font-medium rounded-lg disabled:opacity-50 transition-colors flex items-center gap-2 flex-shrink-0"
                        >
                          <svg v-if="loading[ep.path]" class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                          </svg>
                          {{ loading[ep.path] ? 'Ejecutando…' : 'Ejecutar' }}
                        </button>
                      </div>
                    </div>

                    <!-- Response -->
                    <div v-if="responses[ep.path] !== undefined">
                      <div class="flex items-center justify-between mb-2">
                        <h4 class="text-xs font-semibold text-gd-muted uppercase tracking-wider">Respuesta</h4>
                        <span
                          class="text-xs font-bold rounded px-2 py-0.5"
                          :class="responses[ep.path].status < 400
                            ? 'bg-green-900/50 text-green-400'
                            : 'bg-red-900/50 text-red-400'"
                        >
                          {{ responses[ep.path].status }}
                        </span>
                      </div>
                      <pre class="bg-gd-bg border border-gd-border rounded-lg p-3 text-xs text-green-300 font-mono overflow-auto max-h-64 leading-relaxed">{{ responses[ep.path].body }}</pre>
                    </div>

                    <!-- Example response -->
                    <div v-else>
                      <h4 class="text-xs font-semibold text-gd-muted uppercase tracking-wider mb-2">Ejemplo de respuesta</h4>
                      <pre class="bg-gd-bg border border-gd-border rounded-lg p-3 text-xs text-gd-muted font-mono overflow-auto max-h-48 leading-relaxed">{{ prettyJson(ep.example_response) }}</pre>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

const props = defineProps({
  endpoints: Array,
})

const activeGroup = ref(props.endpoints[0]?.group || 'all')
const expanded = ref(new Set())
const loading = reactive({})
const responses = reactive({})
const tryUrls = reactive({})

const baseUrl = computed(() => window.location.origin)

function toggleEndpoint(path) {
  if (expanded.value.has(path)) {
    expanded.value.delete(path)
  } else {
    expanded.value.add(path)
  }
}

async function executeRequest(ep) {
  const url = tryUrls[ep.path] || (window.location.origin + ep.path.replace(/{.*?}/g, ''))
  loading[ep.path] = true
  responses[ep.path] = undefined
  try {
    const res = await fetch(url, {
      headers: { 'Accept': 'application/json' },
    })
    const text = await res.text()
    let body
    try {
      body = JSON.stringify(JSON.parse(text), null, 2)
    } catch {
      body = text
    }
    responses[ep.path] = { status: res.status, body }
  } catch (err) {
    responses[ep.path] = { status: 0, body: `Error: ${err.message}` }
  } finally {
    loading[ep.path] = false
  }
}

function prettyJson(str) {
  try {
    return JSON.stringify(JSON.parse(str), null, 2)
  } catch {
    return str
  }
}
</script>
