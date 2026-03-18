<template>
  <Link
    :href="href"
    class="flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-colors"
    :class="active
      ? 'bg-gd-accent/15 text-gd-accent border border-gd-accent/30'
      : 'text-gd-muted hover:text-white hover:bg-gd-card border border-transparent'"
  >
    <slot />
  </Link>
</template>

<script setup>
import { Link } from '@inertiajs/vue3'

defineProps({
  href: String,
  active: Boolean,
})
</script>
