# Protocolo de Ajuste de Layout JSON Canvas

## 🎯 Objetivo
Padronizar a correção de fluxos visuais no Obsidian Canvas, garantindo que a arquitetura descrita na documentação (JARVIS V4.0) esteja refletida visualmente com conexões bidirecionais e alinhamento de grid.

## 🛠️ Pré-requisitos
- Acesso ao arquivo `.canvas` via MCP Obsidian.
- Skill `json-canvas` carregada para referência de tipos e coordenadas.
- Documentação do projeto (ex: `Jarvis_Voz.md`) para validar a topologia.

## 📝 Workflow (Passo a Passo)
1. **Identificação de Componentes:** Comparar os nós do Canvas com a Stack mencionada na documentação. (Ex: ElevenLabs estava ausente no fluxo visual).
2. **Correção de Topologia:** Adicionar nós faltantes e configurar conexões bidirecionais entre o Motor de Voz (ElevenLabs) e a Camada de Ação (Rube MCP) usando as propriedades `fromEnd: arrow` e `toEnd: arrow`.
3. **Alinhamento de Coordenadas:** Reposicionar os nós em um eixo horizontal limpo (ex: Frontend -> ElevenLabs -> Rube MCP) para evitar o "layout bagunçado" (scattering).
4. **Referência Documental:** Posicionar a nota de documentação do projeto (`.md`) acima do fluxo central para servir de contexto.
5. **Validação:** Garantir que o JSON resultante é válido e segue a especificação JSON Canvas 1.0.

## ⚠️ Regras e Restrições
- NUNCA deixar conexões unidirecionais onde o fluxo de dados exige feedback (ex: Tool Invocation).
- EVITAR coordenadas aleatórias ou saltos verticais desnecessários (manter alinhamento no grid de 10/20px).
- SEMPRE usar cores Nexus para diferenciar as camadas (Ex: Roxo para Engine, Verde para MCP, Ciano para Frontend).

## 🔗 Links Relacionados
- [[Workflow_Nexus_Brain.canvas]]
- [[00_Mapa_Mestre]]
