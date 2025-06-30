import os
import re

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.readlines()

            modified = False
            new_content = []
            has_import = any("from time import sleep" in line for line in content)

            for line in content:
                new_content.append(line)

                # Ищем строку с self.browser.get(<URL>)
                if re.search(r"self\.browser\.get\(['\"](.+?)['\"]\)", line):
                    print(f"Found 'self.browser.get' in {path}")
                    new_content.append("        sleep(6)\n")
                    modified = True

            if modified and not has_import:
                new_content.insert(0, "from time import sleep\n")

            if modified:
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(new_content)
                print(f"Updated: {path}")
