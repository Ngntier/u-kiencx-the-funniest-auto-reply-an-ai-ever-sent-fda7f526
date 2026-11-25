import os

ENTRY = "Day off approved. I've delegated every decision to a Magic 8-Ball — honestly, the accuracy is comparable."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
