---
name: skill-clean-code-v5
description: >
  Princípios de arquitetura limpa, pipelines puros e Single Responsibility Principle.
---

# 🧼 Clean Code V5

## 1. SRP: Um arquivo = uma responsabilidade
- `colors.ts` (output), `lib.ts` (detection), `installer.ts` (execution).
- **Regra**: Nunca importe `console.log`. Use wrappers `log()` e `write()`.

## 2. Contratos Fortes (Interfaces)
- Nomeie por **papel**, não tipo: `InstallResult` em vez de `Result`.
- **Proibição**: Nunca use `any` em boundaries de sistema.

## 3. Pipeline Puro: Detect → Collect → Execute
- Side-effects apenas no estágio final (`Execute`).
- Estágios iniciais devem ser testáveis e puros (sem alteração de disco).

## 4. Resiliência de Leitura
- Use `try/catch` para leituras opcionais retornando `null`.
- O caller decide o fallback; o sistema nunca deve dar "crash" em leitura de config.

## 5. Arquitetura Declarativa
- Lógica zero em arquivos de mapeamento (ex: `skills-map.ts`).
- Adicionar features = adicionar objetos, não código.

## 6. Fallback Chain de Execução
- 3 níveis: `dist/compiled` → `native TS` → `spawn --experimental-flags`.