---
name: elite-claw-skills
description: >
  Orquestrador local, sincronização de estados e comandos distribuídos do Claw-Code.
---

# 🦅 Elite Claw Skills

> **Status:** Destilado e Otimizado | **Origem:** Repositório do Motor Claw-Code | **Peso:** ~3KB (Redução de 85% de bloat)

---

## 🌿 Visão Geral do Motor Claw

O motor `Claw` é o orquestrador local e de CLI usado para sincronização de estados, comandos distribuídos e execução assistida. Esta nota documenta os padrões estruturais de alto padrão extraídos de sua implementação técnica.

### 📌 Mapeamento do Repositório
- **Core CLI:** `rust/crates/claw-cli` e `src/commands.py`
- **Ambientes Remotos/Sandbox:** `rust/crates/runtime/src/sandbox.rs`
- **Extensões & Hooks:** `rust/crates/plugins/src/hooks.rs`

---

## 🧠 Skills & Padrões Extraídos (Padrões de Ouro)

Estes padrões foram extraídos diretamente do arquivo `src/commands.py` do motor de execução e servem como referência de engenharia de elite para qualquer codificação de assistentes e microserviços.

### 🧩 Snapshot-Based Command Registry
- **Conceito:** JSON snapshot lido uma única vez do disco e cacheado para lookup.
- **Implementação:** `@lru_cache(maxsize=1)` para a função de carregamento que retorna uma tupla imutável. Zero overhead de I/O após primeira carga e total segurança em concorrência (thread-safe).
- **Estrutura:** 
  ```python
  SNAPSHOT_PATH = Path(__file__).resolve().parent / 'reference_data' / 'commands_snapshot.json'

  @lru_cache(maxsize=1)
  def load_command_snapshot() -> tuple[PortingModule, ...]:
      raw_entries = json.loads(SNAPSHOT_PATH.read_text())
      return tuple(PortingModule(**entry) for entry in raw_entries)
  ```

### 🧩 Case-Insensitive Lookup com Busca Parcial
- **Conceito:** Sanitização e uniformização de termos de busca antes da correspondência.
- **Implementação:** A query é convertida para minúsculas (`needle = query.lower()`) e testada contra campos de texto secundários (como descrições ou fontes).
- **Estrutura:**
  ```python
  def find_commands(query: str, limit: int = 20) -> list[PortingModule]:
      needle = query.lower()
      return [m for m in PORTED_COMMANDS if needle in m.name.lower() or needle in m.source_hint.lower()][:limit]
  ```

### 🧩 Filtro Composicional de Comandos
- **Conceito:** Encapsulamento de regras booleanas encadeadas sobre uma lista imutável.
- **Implementação:** Criação de cópias locais sem efeitos colaterais na lista global original.
- **Estrutura:**
  ```python
  def get_commands(include_plugins: bool = True, include_skills: bool = True) -> tuple[PortingModule, ...]:
      commands = list(PORTED_COMMANDS)
      if not include_plugins:
          commands = [m for m in commands if 'plugin' not in m.source_hint.lower()]
      if not include_skills:
          commands = [m for m in commands if 'skills' not in m.source_hint.lower()]
      return tuple(commands)
  ```

### 🧩 Execução com Feedback Estruturado (None-Guard)
- **Conceito:** Retorno consistente usando tipos de dados ricos e imutáveis, evitando tratamento de erros complexos.
- **Implementação:** `@dataclass(frozen=True)` retornando o status de tratamento (`handled: bool`) e mensagem explicativa clara.
- **Estrutura:**
  ```python
  @dataclass(frozen=True)
  class CommandExecution:
      name: str
      source_hint: str
      prompt: str
      handled: bool
      message: str

  def execute_command(name: str, prompt: str = '') -> CommandExecution:
      module = get_command(name)
      if module is None:
          return CommandExecution(name=name, source_hint='', prompt=prompt, handled=False, message='Unknown command')
      return CommandExecution(name=module.name, source_hint=module.source_hint, prompt=prompt, handled=True, message='Executed successfully')
  ```

---

> 💡 **Nota de Design:** O ecossistema Nexus.AI utiliza estas exatas heurísticas estruturais para manter a latência de busca semântica baixa e garantir robustez na comunicação de rede.
