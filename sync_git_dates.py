import os
import subprocess

# --- THE TWO FOLDERS ---
old_repo_dir = r"C:\Users\elliott.ploutz\Documents\GitHub\auxsophia.github.io"
new_content_dir = r"C:\Users\elliott.ploutz\Documents\GitHub\peli-pages\content"

print("Mapping files between the old and new repositories...")

old_file_map = {}
for folder in ['_pages', '_posts']:
    search_path = os.path.join(old_repo_dir, folder)
    if os.path.exists(search_path):
        for root, _, files in os.walk(search_path):
            for file in files:
                if file.endswith('.md'):
                    abs_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_path, old_repo_dir)
                    old_file_map[file] = rel_path

print(f"Found {len(old_file_map)} files in the old repository history.")
print("Starting history sync...\n")

for root, _, files in os.walk(new_content_dir):
    for file in files:
        if not file.endswith(".md"):
            continue

        new_filepath = os.path.join(root, file)

        if file not in old_file_map:
            continue

        old_rel_path = old_file_map[file]

        try:
            result = subprocess.run(
                ['git', 'log', '--follow', '--date=short', '--format=%ad', old_rel_path],
                capture_output=True, text=True, check=True,
                cwd=old_repo_dir
            )
            dates = result.stdout.strip().split('\n')
            
            if not dates or dates[0] == '':
                continue

            modified_date = dates[0]  
            created_date = dates[-1]  
            
        except Exception as e:
            print(f"Error reading history for {file}: {e}")
            continue

        # --- THE NEW, BULLETPROOF INJECTION LOGIC ---
        with open(new_filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines or not lines[0].startswith("---"):
            continue

        new_lines = []
        in_frontmatter = False

        for i, line in enumerate(lines):
            # 1. Catch the opening ---
            if i == 0 and line.startswith("---"):
                in_frontmatter = True
                new_lines.append(line)
                continue
            
            # 2. Catch the closing --- and inject dates right before it
            if in_frontmatter and line.startswith("---"):
                new_lines.append(f"date: {created_date}\n")
                new_lines.append(f"modified: {modified_date}\n")
                
                new_lines.append(line) # Add the closing --- back in
                in_frontmatter = False
                continue
            
            # 3. Clean up the mess: Delete any existing date/modified lines completely
            # This handles both inside the frontmatter AND the stray ones outside!
            if line.startswith("date:") or line.startswith("modified:"):
                continue 

            # 4. Keep all other lines safe
            new_lines.append(line)

        # Write the perfectly formatted lines back to the file
        with open(new_filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
            
        print(f"Success: {file} -> Created: {created_date} | Modified: {modified_date}")

print("\nAll files successfully bridged, cleaned, and updated!")