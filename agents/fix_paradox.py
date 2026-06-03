import os
import re

agent_dir = "/home/blablabla/agent-forge/agents"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Remove Knowledge Verification Rule from State Mapping
    rule_pattern = re.compile(r"^[ \t]*- \*\*Rule \d+ \(Knowledge Verification\):\*\* At the end of every interaction.*?\n", re.MULTILINE)
    content = rule_pattern.sub('', content)

    # 2. Append Knowledge Verification to Write Operations if not already there
    write_op_pattern = re.compile(r"(^[ \t]*- \*\*Write Operations:\*\*.*?)(?:\n|$)", re.MULTILINE)
    
    def write_op_repl(match):
        line = match.group(1)
        if "After writing, you MUST explicitly print" not in line:
            line += " After writing, you MUST explicitly print the exact JSON payload you saved to the user to confirm how and where you created new knowledge."
        return line + "\n"

    content = write_op_pattern.sub(write_op_repl, content)

    # 3. Replace map_[agent_name].md with map_[agentname]_domain.md
    content = content.replace("map_[agent_name].md", "map_[agentname]_domain.md")
    
    # 4. Replace <workspace_root>/agent-forge with <workspace_root>/agent-forge
    content = content.replace("<workspace_root>/agent-forge", "<workspace_root>/agent-forge")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk(agent_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Done.")
