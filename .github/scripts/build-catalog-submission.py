#!/usr/bin/env python3
"""Build the catalog submission issue body from extension.yml and the template."""

import json
import os
import sys
import yaml


def load_extension(path="extension.yml"):
    with open(path) as f:
        return yaml.safe_load(f)


def build_substitutions(ext, env):
    e = ext.get("extension", {})
    req = ext.get("requires", {})
    prov = ext.get("provides", {})
    hooks = ext.get("hooks", {})
    tags = ext.get("tags", [])

    tools = req.get("tools", [])
    if tools:
        lines = [
            f"- {t['name']} {t.get('version', '')} "
            f"({'required' if t.get('required') else 'optional'})"
            for t in tools
        ]
        required_tools = "\n".join(lines)
    else:
        required_tools = "None"

    commands = prov.get("commands", [])
    commands_list = ", ".join(f"`/{c['name']}`" for c in commands)
    commands_usage = "\n".join(
        f"# /{c['name']} - {c.get('description', '')}" for c in commands
    )
    key_features = "\n".join(
        f"- {c.get('description', c['name'])}" for c in commands
    )

    return {
        "$EXT_ID":            e.get("id", ""),
        "$EXT_NAME":          e.get("name", ""),
        "$EXT_DESCRIPTION":   e.get("description", ""),
        "$EXT_AUTHOR":        e.get("author", ""),
        "$EXT_REPOSITORY":    e.get("repository", ""),
        "$EXT_DOCUMENTATION": e.get("documentation", ""),
        "$EXT_CHANGELOG":     e.get("changelog", ""),
        "$EXT_LICENSE":       e.get("license", ""),
        "$EXT_HOMEPAGE":      e.get("homepage", ""),
        "$SPECKIT_VERSION":   req.get("speckit_version", ""),
        "$REQUIRED_TOOLS":    required_tools,
        "$COMMANDS_COUNT":    str(len(commands)),
        "$HOOKS_COUNT":       str(len(hooks)),
        "$TAGS":              ", ".join(tags),
        "$TAGS_JSON":         json.dumps(tags),
        "$KEY_FEATURES":      key_features,
        "$COMMANDS_LIST":     commands_list,
        "$COMMANDS_USAGE":    commands_usage,
        "$VERSION":           env["VERSION"],
        "$TAG":               env["TAG"],
        "$DATE":              env["DATE"],
        "$DOWNLOAD_URL":      env["DOWNLOAD_URL"],
    }


def render(template_path, substitutions, output_path):
    with open(template_path) as f:
        content = f.read()
    for placeholder, value in substitutions.items():
        content = content.replace(placeholder, value)
    with open(output_path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    template = sys.argv[1] if len(sys.argv) > 1 else ".github/templates/catalog-submission.md"
    output = sys.argv[2] if len(sys.argv) > 2 else "/tmp/catalog-submission-final.md"

    ext = load_extension("extension.yml")
    subs = build_substitutions(ext, os.environ)
    render(template, subs, output)
    print(f"Written to {output}")
