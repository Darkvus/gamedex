import { ref } from 'vue'

export const THEMES = {
  violet: { label: 'Violet', accent: '#7c3aed', rgb: '124 58 237' },
  blue:   { label: 'Blue',   accent: '#2563eb', rgb: '37 99 235'  },
  cyan:   { label: 'Cyan',   accent: '#06b6d4', rgb: '6 182 212'  },
  green:  { label: 'Green',  accent: '#10b981', rgb: '16 185 129' },
  orange: { label: 'Orange', accent: '#f97316', rgb: '249 115 22' },
  pink:   { label: 'Pink',   accent: '#ec4899', rgb: '236 72 153' },
  red:    { label: 'Red',    accent: '#ef4444', rgb: '239 68 68'  },
}

const STORAGE_KEY = 'gamedex-theme'

function getInitialTheme() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (saved && THEMES[saved]) return saved
  } catch {}
  return 'violet'
}

const currentTheme = ref(getInitialTheme())

function applyTheme(name) {
  const theme = THEMES[name] || THEMES.violet
  document.documentElement.style.setProperty('--gd-accent-rgb', theme.rgb)
}

export function useTheme() {
  function setTheme(name) {
    currentTheme.value = name
    applyTheme(name)
    try { localStorage.setItem(STORAGE_KEY, name) } catch {}
  }

  return { currentTheme, themes: THEMES, setTheme }
}
