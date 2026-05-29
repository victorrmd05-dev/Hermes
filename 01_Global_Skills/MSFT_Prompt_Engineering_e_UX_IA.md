---
tags: [prompt-engineering, ux, chat-ui, alucinacao, trust, microsoft, aula-04, aula-05, aula-12]
fonte: https://github.com/microsoft/generative-ai-for-beginners
licoes: [04, 05, 12]
status: profundo
---

# 🎯 Engenharia de Prompt e UX para IA — Conversando com o Frontend (Aulas 4, 5 e 12)

> Nota profunda extraida das Licoes 4, 5 e 12 do curriculo Microsoft GenAI.
> **Impacto no Nexus.AI:** Prompts que evitam alucinacoes + UI de chat que inspira confianca.
> Conectada a: [[Skill_Microsoft_GenAI_Curriculum]] | [[🎨 Skill_Frontend_Design_Elite]] | [[💎 Skill_HighEnd_UI_V5]] | [[🧠 Skill_Karpathy_Coding_V5]] | [[00_Mapa_Mestre]]

---

## AULA 4 — Fundamentos de Engenharia de Prompt

### O Que e Engenharia de Prompt (Microsoft)

> "Prompt Engineering e o processo de **designer e otimizar** entradas de texto (prompts) para entregar respostas consistentes e de qualidade para um objetivo de aplicacao e modelo especificos."

**Prompt = a interface de programacao primaria** para apps de GenAI.

### Por que Precisamos de Prompt Engineering?

3 problemas fundamentais dos LLMs:

1. **Respostas sao estocasticas** — o mesmo prompt pode gerar respostas diferentes a cada execucao
2. **Modelos fabricam respostas** — "alucinacoes" / "fabricacoes" quando nao sabem a resposta
3. **Capacidades variam por modelo** — GPT-4 != Claude != Llama (requer customizacao)

> Microsoft usa o termo **"fabrication"** em vez de "hallucination" — mais preciso tecnicamente e mais inclusivo culturalmente.

### Anatomia de um Prompt Completo

```
[SYSTEM MESSAGE]   → Define personalidade/contexto do assistente
[USER MESSAGE]     → Pergunta/instrucao do usuario
[ASSISTANT MESSAGE]→ Resposta previa (para multi-turn)
[PRIMARY CONTENT]  → Dados/documentos relevantes
[SECONDARY CONTENT]→ Contexto adicional (formato, restricoes)
```

```python
# Exemplo completo Microsoft (API ChatCompletion)
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Voce e um especialista em imoveis de alto padrao."},
        {"role": "user", "content": "Quais os melhores bairros para investir em SP?"},
        {"role": "assistant", "content": "Os bairros mais valorizados sao..."},
        {"role": "user", "content": "E no Rio de Janeiro?"}
    ]
)
```

### Como LLMs Processam Prompts (Base vs Instruction-Tuned)

**Base LLM:** apenas prediz o proximo token. Sem instrucoes, apenas completa texto.

**Instruction-Tuned LLM:** treinado com RLHF para seguir instrucoes e aprender com feedback humano.

```
Base LLM:        "O presidente dos EUA e..." → completa qualquer coisa estatisticamente
Instruction-LLM: Recebe: "Me explique em 1 paragrafo quem e o presidente dos EUA"
                 Entende a TAREFA e responde de forma estruturada
```

### Melhores Praticas Microsoft (tabela completa)

| Pratica | Por que Importa |
|---------|-----------------|
| Avalie modelos mais novos | Cada geracao tem melhorias e novos quirks |
| Separe instrucoes do contexto | Ajuda o modelo a pesar tokens corretamente |
| Seja especifico e claro | Mais detalhes = mais qualidade e consistencia |
| Use exemplos (show & tell) | Modelos respondem melhor ao "zero-shot → few-shot" |
| Use cues para iniciar resposta | Nudge o modelo na direcao certa |
| Repita instrucoes criticas | Order matters — recency bias existe |
| De uma "saida" ao modelo | Fallback response reduz fabricacoes |
| Templates para consistencia | Biblioteca de prompts reutilizavel |

---

## AULA 5 — Tecnicas Avancadas de Prompting

### 7 Tecnicas Avancadas (Microsoft Curriculum)

#### 1. Zero-Shot — Direto ao ponto
```
Prompt: "O que e algebra?"
Sem exemplos, confia apenas no treinamento.
Bom para: perguntas gerais, tarefas simples.
```

#### 2. Few-Shot — Aprenda com exemplos
```
Prompt: "Traduza para espanhol:
'The Sun is Shining' => 'El Sol está brillando'
'It's a Cold Day' =>
"
Modelo infere o padrao sem instrucao explicita.
Bom para: tarefas com formato especifico, classificacao.
```

#### 3. Chain-of-Thought (CoT) — Ensine o raciocinio
```
SEM CoT: "Alice tem 5 macas, joga 3, da 2 para Bob, Bob da 1 de volta. Quantas?"
         LLM responde: 5 (ERRADO)

COM CoT: "Lisa tem 7 macas, joga 1 = 6, da 4 = 2, recebe 1 = 3.
          Alice tem 5 macas, joga 3 = ?, da 2 = ?, recebe 1 = ?"
          LLM responde: 1 (CORRETO)

Tecnica: fornecer um exemplo com o raciocinio passo a passo antes da pergunta real.
```

#### 4. Generated Knowledge — Enriquecer com dados proprios
```python
# Template com dados da empresa
prompt = f"""
Empresa: {company_name}
Produtos: {products_list}
Budget do cliente: {budget}
Restricoes: {restrictions}

Sugira o melhor produto para este cliente.
"""
# Chave: usar 'restrict' e separar 'type:' e 'cost:' melhora precisao
```

#### 5. Least-to-Most — Decomposicao em sub-tarefas
```
Prompt: "Como fazer data science em 5 passos?"
1. Coletar dados
2. Limpar dados
3. Analisar dados
4. Visualizar dados
5. Apresentar dados

Usar cada passo como sub-prompt independente para maior precisao.
```

#### 6. Self-Refine — Critica iterativa
```
Passo 1: Pedir ao LLM para resolver o problema
Passo 2: Pedir ao LLM para sugerir 3 melhorias
Passo 3: Pedir ao LLM para aplicar as melhorias
Repetir ate satisfatorio.

Util para: geracao de codigo, textos tecnicos.
```

#### 7. Maieutic Prompting — Verificacao de consistencia
```
Pedir resposta → Pedir explicacao de cada parte → Verificar consistencia
Descartar partes inconsistentes → Repetir ate ter resposta confiavel.
```

### Temperatura — Controlando Criatividade vs Determinismo

```
Temperatura 0.0 → Muito determinístico (respostas quase identicas a cada run)
Temperatura 0.7 → Balanceado (padrao) — bom para chat geral
Temperatura 1.0 → Muito variado (criativo, imprevisivel)

Para Producao:     temperatura 0.1-0.3 (consistencia)
Para Criatividade: temperatura 0.7-0.9 (diversidade)
Para Codigo:       temperatura 0.0-0.2 (precisao)
```

Outros parametros: `top-k`, `top-p`, `repetition_penalty` (fora do escopo deste curriculo).

---

## AULA 12 — Design de UX para Aplicacoes de IA

### Os 4 Pilares de UX em Apps de IA (Microsoft)

| Pilar | Definicao | Exemplo Pratico |
|-------|-----------|-----------------|
| **Useful** | Funcionalidade alinhada ao proposito | Chatbot que realmente resolve o problema |
| **Reliable** | Consistente e sem erros (ou errors graceful) | Mensagens de erro claras e uteis |
| **Accessible** | Funciona para todos (inclusividade) | Suporte a teclado, screen readers |
| **Pleasant** | Agradavel de usar | Micro-animacoes, feedback visual |

### Trust e Transparencia — O Core da UX de IA

**O risco do extremo errado:**
- **Mistrrust** (desconfianca): usuario rejeita o app antes de tentar
- **Overtrust** (confianca cega): usuario aceita erros sem verificar → consequencias graves

**Como desenhar para o trust certo:**

#### Explainability (Explicabilidade)
- Deixe claro que e IA, nao humano
- Em vez de: `"Converse com seu tutor agora"`
- Use: `"Use nosso tutor de IA que adapta ao seu ritmo de aprendizado"`
- Explique como a IA tomou a decisao
- Simplifique — usuarios nao sao especialistas em IA

#### Control (Controle)
- Permitir que o usuario modifique prompts e resultados
- Opcao de opt-in/opt-out de coleta de dados
- Variar formato, tom e tamanho da resposta (como Bing Chat)
- **Key insight Microsoft:** criar "friccao intencional" entre prompt e resultado para evitar overtrust

### Collaboration e Feedback Loops

**AI nao e perfeita** — o design deve aceitar isso:

```
Loop de Feedback Ideal:
━━━━━━━━━━━━━━━━━━━━━
Usuario → Pergunta → IA gera resposta
                  ↓
           [👍 / 👎] — Feedback simples
                  ↓
           Aprendizado continuo + Trust building
```

**Handling de erros gracefully:**
```
NAO: "Erro 500 — Requisição inválida"

SIM: "Desculpe, nosso produto foi treinado nos seguintes assuntos: 
      Historia, Matematica, Ciencias. 
      Nao consigo responder sobre Geografia. 
      Posso te ajudar com algo dentro dessas areas?"
```

### Aplicacao em Chat UI — Nexus.AI Frontend Design

Conectando com [[🎨 Skill_Frontend_Design_Elite]] e [[💎 Skill_HighEnd_UI_V5]]:

```
Checklist de UX para Chat de IA (Microsoft + Nexus.AI):

[ ] Deixar claro que e IA (tooltip, label, disclaimer)
[ ] Mostrar estado de loading/thinking (animacao)
[ ] Botoes de feedback (thumbs up/down) em cada resposta
[ ] Opcao de regenerar resposta
[ ] Limitar escopo com mensagem educativa quando fora do dominio
[ ] Permitir edicao do prompt pelo usuario
[ ] Navegacao por teclado completa (acessibilidade)
[ ] Mensagens de erro em linguagem humana, nao tecnica
[ ] Historico de conversa visivel e editavel
[ ] Indicador de confianca/fonte quando possivel
```

---

## Templates de Prompt para o Nexus.AI

### Template: Camila Imobiliaria
```python
system_prompt = """
Voce e a Camila, especialista em imoveis de alto padrao em {cidade}.
Use APENAS as informacoes de imoveis fornecidas no contexto RAG.
Se nao souber a resposta, diga: "Deixa eu verificar na nossa base atualizada."
NAO invente caracteristicas, preco ou disponibilidade de imoveis.
Responda sempre em portugues, tom profissional mas acolhedor.
"""
```

### Template: Jarvis_Voz
```python
system_prompt = """
Voce e o Jarvis, assistente executivo pessoal do usuario.
Seu objetivo: executar tarefas com maxima eficiencia usando as ferramentas disponíveis.
Para tarefas de voz: use a tool tts_speak.
Para calendario: use a tool calendar_check.
Para busca de dados: use a tool search_knowledge_base.
Seja conciso. Confirme antes de executar acoes irreversiveis.
"""
```

### Regra Anti-Alucinacao (Nexus.AI Standard)
```python
# Sempre incluir no system prompt de agentes com dados reais:
anti_hallucination = """
REGRA CRITICA: Voce so pode afirmar fatos que estao no contexto fornecido.
Se a informacao nao estiver no contexto, diga: "Nao tenho essa informacao no momento."
NUNCA invente numeros, datas, nomes ou disponibilidades.
"""
```

---

*Aulas 4, 5 e 12 — Microsoft GenAI for Beginners*
*Links: [Aula 04](https://github.com/microsoft/generative-ai-for-beginners/tree/main/04-prompt-engineering-fundamentals) | [Aula 05](https://github.com/microsoft/generative-ai-for-beginners/tree/main/05-advanced-prompts) | [Aula 12](https://github.com/microsoft/generative-ai-for-beginners/tree/main/12-designing-ux-for-ai-applications)*
