import os
import re
from pathlib import Path

SKILLS_DIR = Path(r"c:\Users\cerqu\Documents\Obsidian\Hermes\01_Global_Skills")

DESCRIPTIONS = {
    "Nexus_Protocol_Layout_Canvas.md": "Protocolo para ajuste de topologia e conexões visuais no Obsidian Canvas JSON.",
    "Skill_DragonScale_Context.md": "Lógicas de persistência, linting de sanidade e prevenção de duplicação do DragonScale.",
    "Skill_Logic_Google_SEO_Integration.md": "Integração SEO e automação no Search Console e Indexing API para SPAs.",
    "Skill_Synabun_Knowledge_v1.md": "Motor de chunking de sessão baseado no Synabun para extração estruturada de contexto.",
    "⚡Elite_Claw_Skills.md": "Orquestrador local, sincronização de estados e comandos distribuídos do Claw-Code.",
    "⚡Elite_Claw_V3_Turbo.md": "Analista pós-veredicto para extração de insights de testes A/B entre LLMs.",
    "✅ Skill_SEO_OnPage_V5.md": "Agente e pipeline completo para geração e auditoria avançada de SEO on-page.",
    "🎨 Skill_Frontend_Design_Elite.md": "Diretrizes técnicas e design systems para SaaS, Dashboards e apps AI-Native.",
    "💎 Skill_HighEnd_UI_V5.md": "Linguagem de design de luxo inspirada em grandes marcas (Apple, Tesla, Airbnb, etc).",
    "📉 Monitoramento_de_Custos_Claude.md": "Rastreamento e limitação de custos da API do Claude durante o desenvolvimento.",
    "🔒 Skill_Security_V5.md": "Monitoramento de consumo, segurança e limitação de custos via API da Anthropic.",
    "🖋️ Skill_Luxury_Copywriting_V5.md": "Técnicas de copywriting autoritário e exclusividade narrativa para alto luxo.",
    "🛍️ Skill_Liquid_Mastery_V5.md": "Arquitetura e desenvolvimento focado em temas da Shopify (Liquid).",
    "🛍️ Skill_Performance_V5.md": "Otimização de performance extrema com Cache Duplo, Lazy Evaluation e Worker Pools.",
    "🛍️ Skill_Shopify_Functions_V5.md": "Customizações WebAssembly serverless para Shopify Checkout, descontos e fretes.",
    "🛍️ Skill_Shopify_GraphQL_V5.md": "Integração e consultas avançadas para Shopify Admin API via GraphQL e Remix.",
    "🥷GSD_Core_Protocol.md": "Protocolos do sistema GSD para gestão autônoma de projetos e workflow ágil.",
    "🧠 Skill_Anthropic_Global_Suite_V5.md": "Suíte global de ferramentas Anthropic para testes, APIs, design e artefatos web.",
    "🧠 Skill_Claude_Design_Elite_V5.md": "Padrões de ritmo visual e hierarquia extraídos diretamente do Claude Design System.",
    "🧠 Skill_GStack_Executive_Suite.md": "Mindset de desenvolvimento GStack focado em zero falhas silenciosas e decisões executivas.",
    "🧠 Skill_Karpathy_Coding_V5.md": "Mentalidade Karpathy para engenharia de software cirúrgica e prevenção contra alucinações.",
    "🧼 Skill_Clean_Code_V5.md": "Princípios de arquitetura limpa, pipelines puros e Single Responsibility Principle.",
    "🪨 Skill Caveman Token Optimizer.md": "Modos de compressão gramatical agressiva para otimização radical de tokens em prompts."
}

def process_file(filepath):
    desc = DESCRIPTIONS.get(filepath.name)
    if not desc:
        return
        
    content = filepath.read_text(encoding='utf-8')
    # Regex to find description and replace it
    pattern = r"description:\s*>.*?---"
    replacement = f"description: >\n  {desc}\n---"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content != content:
        filepath.write_text(new_content, encoding='utf-8')

def main():
    for filepath in SKILLS_DIR.glob("*.md"):
        process_file(filepath)

if __name__ == "__main__":
    main()
