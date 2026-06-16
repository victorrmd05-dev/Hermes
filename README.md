# 🏆 Bem-vindo ao Nexus Core OS

**Este não é apenas um cofre comum de anotações.** O Nexus Core OS é um Sistema Operacional vivo, projetado para integrar a inteligência humana com a alta performance das IAs. Ele é o seu cérebro digital, estruturado para pensar, organizar e executar tarefas no mais alto nível de eficiência.

---

## 🚀 Como Instalar e Abrir no Obsidian

1. **Faça o Download:** Você pode clonar este repositório via terminal usando `git clone https://github.com/victorrmd05-dev/Hermes.git` OU clicar no botão verde **Code > Download ZIP** no canto superior direito desta página e extrair a pasta no seu computador.
2. **Abra no Obsidian:** Baixe e instale o [Obsidian](https://obsidian.md/), abra o aplicativo, clique em **"Open folder as vault"** (Abrir pasta como cofre) e selecione a pasta `Hermes` que você extraiu.
3. **Siga a Ativação:** Leia a seção abaixo com atenção para ativar os superpoderes do cofre!

---

## 🔌 Ativação dos Plugins (Primeiro Acesso)

Seja muito bem-vindo à sua nova base de operações! Para garantir que a experiência seja perfeita desde o primeiro segundo:

> [!IMPORTANT]
> **Confie Neste Cofre (Trust Vault)**
> Assim que você abrir esta pasta no Obsidian pela primeira vez, o software exibirá um popup de segurança perguntando se você confia nos autores deste cofre.
> 
> Você deve clicar em **"Sim / Trust"**. Isso ativará automaticamente todo o nosso design escuro premium e carregará instantaneamente nossos plugins essenciais pré-configurados (como **Dataview**, **Templater** e **Omnisearch**). Sem isso, o cofre roda em modo de segurança.

---

## 📥 O Motor de Ingestão (.raw)

O Nexus possui um motor automatizado e silencioso de processamento de dados. Esqueça a bagunça de arquivos espalhados. Siga o fluxo de ingestão:

1. **Jogue no Buraco Negro:** Arraste qualquer PDF, planilha ou relatório de tráfego para a pasta `.raw/` (Nota: esta pasta fica estrategicamente oculta dentro do Obsidian para manter a interface limpa, mas você pode visualizá-la e interagir com ela pelo Explorador de Arquivos do Windows/Mac).
2. **Ative a IA:** Chame o Claude ou o seu agente de IA preferido no terminal e rode o comando:
   ```bash
   /wiki-ingest nome-do-arquivo.pdf
   ```
3. **Magia Feita:** A IA vai engolir os dados, processá-los de forma inteligente, armazenar tudo perfeitamente estruturado na pasta `wiki/` e limpar o arquivo da entrada automaticamente.

---

## 🚀 O Protocolo de Auto-Evolução (Nexus V5)

Este cofre não é estático; ele **aprende sozinho**. O Nexus foi projetado sob um framework de melhoria contínua:

- **Captura de Inteligência:** Sempre que uma IA (ou você) resolver um problema complexo ou trouxer uma documentação de valor de fora, ela usará o template padrão do sistema.
- **Transformação em Skill:** A IA vai empacotar essa solução gerando uma habilidade (skill) e a salvará na pasta `01_Global_Skills/`.
- **Sincronização:** Em seguida, ela indexará o novo aprendizado no Mapa Mestre e rodará o comando interno `graphify` para atualizar as conexões neurais do sistema. Seu cérebro digital fica mais inteligente a cada interação.

---

## 🤖 Conexão via MCP (Model Context Protocol)

O Nexus Core OS brilha de verdade quando conectado às suas ferramentas de trabalho automatizadas (Claude Desktop, Cursor, Windsurf). Para que as IAs possam ler e editar seu cofre em tempo real, usamos o protocolo MCP.

O plugin **Local REST API** já vem pré-instalado neste cofre para facilitar essa conexão. Em caso de dúvidas sobre o funcionamento do plugin, consulte a [Documentação Oficial do Local REST API](https://coddingtonbear.github.io/obsidian-local-rest-api/). Siga os passos básicos abaixo:

1. **Pegue sua Chave:** No Obsidian, vá em `Configurações` > `Local REST API` (no menu lateral esquerdo). Copie a sua **API Key**.
2. **Ative o HTTP:** Role a página de configurações do plugin até o final e ative a opção **"Enable Non-encrypted (HTTP) Server"** para habilitar a porta de conexão local.
3. **Configure o Servidor:** No seu agente de IA (Cursor, Claude, etc), adicione a seguinte configuração JSON no seu arquivo de MCP (substitua a chave pela sua):

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": [
        "-y",
        "@calclavia/mcp-obsidian"
      ],
      "env": {
        "OBSIDIAN_API_KEY": "COLE_SUA_CHAVE_AQUI",
        "OBSIDIAN_HOST": "http://127.0.0.1:27123"
      }
    }
  }
}
```

> [!TIP]
> **O Caminho Mais Fácil (Prompt Mágico)**
> Se não quiser mexer com configurações JSON manualmente, basta abrir o chat da sua IA e colar este prompt:
> 
> *"Configure o servidor MCP do Obsidian para mim. O plugin Local REST API já está rodando. A URL é http://127.0.0.1:27123 e a minha chave de API é [COLE_SUA_CHAVE_AQUI]. Faça a configuração no meu arquivo de MCP e me avise quando estiver pronto."*

---

## 👁️ Visualização de Memória da IA (AgentMemory)

Seu sistema está preparado para se conectar ao **AgentMemory**, um painel avançado que permite rastrear o raciocínio, as decisões e o histórico dos agentes de IA em tempo real. Como este é o seu primeiro acesso em um ambiente novo, você precisará acionar o pacote para abrir o dashboard.

Para instalar e abrir a interface visual:

1. **Abra o Terminal** dentro da pasta raiz do Nexus Core OS.
2. **Execute o comando:**
   ```bash
   npx @agentmemory/agentmemory demo
   ```
3. **Instalação Automática:** Se o terminal perguntar se deseja instalar o pacote ou componentes do console, responda com "Yes" ou `y`.
4. **Acesse o Dashboard:** Assim que o comando rodar, ele exibirá um link local no terminal (geralmente `http://localhost:3114` ou `3113`). Basta clicar (ou copiar e colar no seu navegador) para ter visão total do cérebro da sua IA trabalhando em tempo real!

---
*Todos os sistemas nominais. O Nexus está online.* 🟢
