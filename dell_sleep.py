import os
import re


directory = "/Users/nikitahudakov/PycharmProjects/AutotestSE_Desktop"


for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            new_lines = [line for line in lines if not re.search(r"\bsleep\(6\)", line)]

            if new_lines != lines:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)

