import os
import json
import subprocess


def load_config(path):
    """Load config from a JSON file."""
    with open(path) as f:
        data = json.load(f)
    return data


def run_command(user_input):
    """Run a shell command based on user input."""
    result = subprocess.run(["echo", user_input], capture_output=True, text=True)
    return result.stdout.strip()


def find_duplicates(items):
    """Return duplicate items from a list."""
    seen = set()
    dupes = []
    for item in items:
        if item in seen:
            dupes.append(item)
        seen.add(item)
    return dupes


def safe_divide(a, b):
    """Safely divide two numbers."""
    return a / b


def merge_dicts(base, override):
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in result:
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def format_user_greeting(template, username):
    """Format a greeting template with the username."""
    return template.format(name=username)


def get_env_or_default(key, default=""):
    """Get environment variable or return default."""
    return os.environ.get(key, default)


def truncate(text, max_length=100):
    """Truncate text to max_length characters."""
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    return text
