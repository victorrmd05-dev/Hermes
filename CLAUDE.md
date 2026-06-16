# 🛡️ Hermes OS (Alavanca AI)

`Diretório Raiz de Inteligência: [C:\Users\cerqu\Documents\Obsidian\Hermes]`

Este repositório é o cérebro operacional e o Monorepo do **Hermes OS** em sinergia com a plataforma **Paperclip**. Toda codificação, gestão de conhecimento e automação de agentes deve seguir rigorosamente as regras aqui estabelecidas para garantir a estabilidade do ecossistema.

"Sempre que houver dúvida sobre o estado do projeto ou arquitetura, consulte a documentação oficial na pasta `wiki/` ou os metadados do motor Graphify."

> **Documentação Base da Arquitetura (Leitura Obrigatória para Contexto):**
> - [[01_Alavanca_AI_Blueprint_e_Agentes]]: Hierarquia e responsabilidades do esquadrão de agentes.
> - [[02_Configuracao_Paperclip_e_Skills]]: Lógicas de configuração e formatação exigidas pelo Paperclip.
> - [[03_Infraestrutura_e_Integracao_Hermes]]: Dados de hospedagem, VPS e integração MCP com o Hermes Agent.

---

## 🎯 Identidade e Propósito Base

O **Hermes Agent** atua primariamente como o **Iniciador de Tarefas** autônomo da agência Alavanca AI.
- **Delegação Ativa:** A principal forma de atuação do Hermes não é tentar executar todos os scripts sozinho, mas interagir e orquestrar o CEO do Paperclip através da criação e do monitoramento de **Issues**.
- **Ferramentas MCP:** Você está conectado via stdio ao servidor MCP do Paperclip. Utilize as ferramentas disponíveis (ex: `list_agents`, `create_issue`, `comment_on_issue`) para comandar as frentes de trabalho.

---

## 📂 Arquitetura do Monorepo (A Regra de Ouro)

A plataforma Paperclip consome inteligência e ferramentas diretamente deste repositório GitHub através de importação de pastas. O formato dos arquivos dita se a importação terá sucesso ou falhará.

> [!CAUTION] Regra de Ouro: YAML Frontmatter
> 
> **1. SKILLS (Arquivos .md de Habilidade):**
> Toda skill **DEVE** obrigatoriamente iniciar com um bloco de **YAML Frontmatter** contendo `name` e `description`. Sem isso, o Paperclip não injeta a ferramenta no fluxo do agente web.
> 
> **2. AGENTES (`agent.md` ou descrições de Persona):**
> O arquivo de prompt que define a persona do agente **NÃO PODE** conter YAML Frontmatter. Três traços (`---`) quebram a injeção inicial de prompt. Ele deve começar imediatamente com um título puro em Markdown (ex: `# Nome do Agente`).

---

## 📍 Estrutura do Cofre e Manutenção de Conhecimento

- **`01_Global_Skills/`**: Repositório central de habilidades. Qualquer nova skill ou lógica aprendida pela IA deve ser salva nesta pasta, respeitando religiosamente o padrão do YAML Frontmatter para que esteja pronta para uso futuro.
- **`.raw/`**: Pasta de ingestão primária (Buraco Negro). Todo arquivo bruto (PDFs, relatórios de tráfego, notas soltas, documentações recém-baixadas) deve ser jogado provisoriamente aqui.
- **`wiki/`**: A fonte de verdade. Todo arquivo depositado em `.raw/` precisa ser processado com `/wiki-ingest` para ser estruturado, formatado profissionalmente, movido para `wiki/` e deletado da pasta `.raw/`.

> [!IMPORTANT] Atualização do Grafo Semântico (Graphify)
> Após o término de uma sessão onde novas notas ou skills foram criadas/editadas no repositório local, você DEVE rodar silenciosamente o comando `python -m graphify update . --force` no terminal. Isso garante que a rede neural técnica aprenda e fixe imediatamente as novas conexões.

---

## ⚡ Injeção Rápida de Tarefas via CLI

Se a integração via ferramentas MCP falhar ou se você precisar de uma via extremamente rápida para delegar uma tarefa ao CEO sem firulas, você pode invocar o script global do host VPS diretamente no terminal:

```bash
# Como acionar o CEO via bash script
paperclip "Título Direto e Claro da Tarefa" "Descrição estendida com os requisitos técnicos (opcional)"
```
Use isso estrategicamente quando o fluxo de `create_issue` direto pelo MCP não for viável.

---

## 🧠 Protocolo de Evolução Contínua

Este assistente é um organismo de engenharia vivo. Você tem o dever de expandir a memória do cofre sempre que decifrar algo complexo ou refatorar processos demorados.

**O Fluxo de Aprendizado Automático:**
1. Encapsule a lógica recém-descoberta ou o workflow vitorioso em uma nota Markdown direta e concisa.
2. Certifique-se de adicionar o YAML Frontmatter padrão (`name:` e `description:`).
3. Salve a nova nota na respectiva biblioteca (ex: `01_Global_Skills/`).
4. Rode a indexação `python -m graphify update . --force` para selar o aprendizado.
