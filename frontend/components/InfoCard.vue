<template>
  <div class="bg-gd-surface border border-gd-border rounded-xl p-4">
    <p class="text-xs font-semibold text-gd-muted uppercase tracking-wider mb-2">{{ title }}</p>
    <slot />
  </div>
</template>

<script setup>
defineProps({ title: String })
</script>
