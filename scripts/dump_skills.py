import os
from pathlib import Path

SKILLS_DIR = Path(r"c:\Users\cerqu\Documents\Obsidian\Hermes\01_Global_Skills")
DUMP_FILE = Path(r"c:\Users\cerqu\Documents\Obsidian\Hermes\data\skills_dump.txt")

def main():
    dump_content = ""
    for filepath in SKILLS_DIR.glob("*.md"):
        if filepath.name == "🎯Skill_MetaAds_Intelligence_V5.md":
            continue
        
        # Read first 15 lines
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = [next(f) for x in range(25)]
        except StopIteration:
            pass
        
        content = "".join(lines)
        dump_content += f"====================\n{filepath.name}\n====================\n{content}\n\n"
        
    DUMP_FILE.write_text(dump_content, encoding='utf-8')

if __name__ == "__main__":
    main()
