import os
import re
from pathlib import Path

SKILLS_DIR = Path(r"c:\Users\cerqu\Documents\Obsidian\Hermes\01_Global_Skills")

def clean_name(filename):
    # Remove emojis and other special characters
    # Keep only alphanumeric, hyphen, underscore
    name = re.sub(r'[^\w\s-]', '', filename.replace('.md', ''))
    # Replace spaces and underscores with hyphens
    name = re.sub(r'[\s_]+', '-', name).strip('-').lower()
    return name

def get_description(content):
    lines = content.splitlines()
    for line in lines:
        line = line.strip()
        if line and not line.startswith('---'):
            # Remove Markdown headers if present
            line = re.sub(r'^#+\s+', '', line)
            # Remove emojis if any to keep it clean (optional, but let's keep them)
            return line
    return "Skill file"

def process_file(filepath):
    if filepath.name == "🎯Skill_MetaAds_Intelligence_V5.md":
        return

    content = filepath.read_text(encoding='utf-8')
    if content.startswith('---'):
        return

    name = clean_name(filepath.name)
    description = get_description(content)

    frontmatter = f"""---
name: {name}
description: >
  {description}
---

"""
    filepath.write_text(frontmatter + content, encoding='utf-8')

def main():
    for filepath in SKILLS_DIR.glob("*.md"):
        process_file(filepath)

if __name__ == "__main__":
    main()
