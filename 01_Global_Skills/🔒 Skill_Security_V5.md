---
name: skill-security-v5
description: >
  🔒 Security V5 (Supply Chain)
---

# 🔒 Security V5 (Supply Chain)

## 1. Hardened .npmrc (fendo pattern)
- `ignore-scripts=true`: Bloqueia scripts post/preinstall maliciosos.
- `save-exact=true`: Pins de versão exata (sem ^ ou ~) para builds determinísticos.
- `engine-strict=true`: Falha imediata se a versão do Node.js for incompatível.

## 2. Zero Runtime Deps
- **Regra**: Priorize stdlib do Node.js sobre pacotes externos.
- **Ganho**: Elimina vulnerabilidades de terceiros e overhead de instalação.

## 3. Cross-Platform Spawn Safety
- **Windows**: Use `shell: true` e comando `npx.cmd`.
- **Unix**: Use `shell: false` e comando `npx`.

## 4. Entrypoint Gatekeeping
- Valide `process.versions.node` logo no `index.js`.
- Bloqueie a execução se o ambiente for inseguro ou desatualizado.