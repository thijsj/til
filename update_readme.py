#!/usr/bin/env python3

import pathlib
import argparse

base_path = pathlib.Path(__file__).resolve().parent

start_block = "<!--index start-->"
end_block = "<!--index end-->"


def find_docs():
    all_docs = {}
    for doc in base_path.glob("*/*.md"):
        parent_data = all_docs.setdefault(doc.parent.name, {"docs": []})
        if not parent_data.get("title"):
            parent_data["title"] = doc.parent.name.title()
        doc_lines = doc.read_text().splitlines()
        doc_data = {
            "link": doc.relative_to(base_path).as_posix(),
            "title": doc.stem,
        }
        parent_data["docs"].append(doc_data)
        for line in doc_lines:
            if line.startswith("# "):
                doc_data["title"] = line[2:].strip()
                break
    return all_docs


def update_readme(dry_run=False):
    readme_path = base_path / "README.md"
    lines = readme_path.read_text().splitlines()
    start_index = lines.index(start_block)
    end_index = lines.index(end_block)
    new_lines = lines[: start_index + 1]

    docs = find_docs()
    for parent in sorted(docs.values(), key=lambda x: x["title"]):
        new_lines.append(f"## {parent['title']}")
        for doc in sorted(parent["docs"], key=lambda x: x["title"]):
            new_lines.append(f"- [{doc['title']}]({doc['link']})")
        new_lines.append("")

    new_lines += lines[end_index:]

    if dry_run:
        print("\n".join(new_lines))
    else:
        tmp_path = readme_path.with_suffix(".tmp")
        tmp_path.write_text("\n".join(new_lines))
        tmp_path.replace(readme_path)
        print(f"Updated {readme_path} with the latest documentation links.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update README.md with the latest version."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without writing changes.",
        default=False,
    )
    args = parser.parse_args()
    update_readme(dry_run=args.dry_run)
