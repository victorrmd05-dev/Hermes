---
name: skill-performance-v5
description: >
  ⚡ Performance V5
---

# ⚡ Performance V5

## 1. Cache de I/O Duplo
- `if (fileCache.has(path)) return cache.get(path);`
- **Cross-popula**: Ao ler conteúdo, já valide a existência no `existsCache`.
- **Ganho**: -90% disk reads em scans profundos.

## 2. Lazy Evaluation & Early Exit
- Só compute I/O pesado (Gems/Vendor) se necessário.
- Use `maxDepth=3` e early exit em recursões de scan.

## 3. Lookups O(1)
- Use `new Set()` para todas as listas consultadas em loops (`SKIP_DIRS`, `EXTENSIONS`).
- **Ganho**: O(1) vs O(n).

## 4. Worker Pool (Concurrency=6)
- Use `Array.from({length: 6}, () => worker())`.
- Use `nextIdx++` para fila atômica sem locks.

## 5. Pre-warm (Zero Blocking)
- Use `setImmediate(initAction)` para resolver I/O durante tempo idle da UI.

## 6. Manifest Preload
- Leia `package.json` ou `Gemfile` uma única vez e passe a referência para os sub-módulos.

## 7. UX Optimization
- Spinner em **80ms** (12.5 FPS). Renderize **apenas** se houver trabalho ativo.