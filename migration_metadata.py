import os

content_dir = "content"

for root, _, files in os.walk(content_dir):
    for file in files:
        if not file.endswith(".md"):
            continue

        filepath = os.path.join(root, file)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Check if the file has YAML frontmatter
        if not lines or not lines[0].startswith("---"):
            continue

        new_lines = []
        in_frontmatter = True
        permalink_val = None
        has_slug = False

        for i, line in enumerate(lines):
            # Check for the closing dashed line of the frontmatter
            if i > 0 and line.startswith("---"):
                in_frontmatter = False

            if in_frontmatter:
                if line.startswith("slug:"):
                    has_slug = True
                if line.startswith("permalink:"):
                    # Extract the path and clean up slashes
                    raw_link = line.split(":", 1)[1].strip().strip("/")
                    permalink_val = raw_link
                    continue  # Remove the permalink line
                if line.startswith("layout:"):
                    continue  # Remove Jekyll layout tags

            new_lines.append(line)

        # If a permalink was found, inject the new Pelican routing tags
        if permalink_val:
            for j, line in enumerate(new_lines):
                if j > 0 and line.startswith("---"):
                    insert_idx = j
                    break

            new_lines.insert(insert_idx, f"url: {permalink_val}/\n")
            new_lines.insert(insert_idx + 1, f"save_as: {permalink_val}/index.html\n")
            
            # Auto-generate a slug from the permalink path if missing to prevent collisions
            if not has_slug:
                slug = permalink_val.split("/")[-1]
                new_lines.insert(insert_idx + 2, f"slug: {slug}\n")

            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print(f"Updated metadata for: {filepath}")

print("Migration complete!")