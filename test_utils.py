import os
import json
import tempfile
from utils import (
    load_config,
    run_command,
    find_duplicates,
    safe_divide,
    merge_dicts,
    format_user_greeting,
    get_env_or_default,
    truncate,
)


def test_load_config():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({"key": "value"}, f)
        f.flush()
        result = load_config(f.name)
    assert result == {"key": "value"}
    os.unlink(f.name)


def test_run_command():
    result = run_command("hello")
    assert result == "hello"


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 3]) == [2, 3]


def test_find_duplicates_none():
    assert find_duplicates([1, 2, 3]) == []


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0


def test_merge_dicts():
    base = {"a": 1, "b": {"c": 2}}
    override = {"b": {"d": 3}}
    result = merge_dicts(base, override)
    assert result == {"a": 1, "b": {"c": 2, "d": 3}}


def test_format_user_greeting():
    assert format_user_greeting("Hello, {name}!", "Alice") == "Hello, Alice!"


def test_get_env_or_default():
    os.environ["TEST_KEY"] = "test_value"
    assert get_env_or_default("TEST_KEY") == "test_value"
    del os.environ["TEST_KEY"]


def test_get_env_or_default_missing():
    assert get_env_or_default("NONEXISTENT_KEY", "fallback") == "fallback"


def test_truncate():
    assert truncate("hello", 10) == "hello"


def test_truncate_long():
    assert truncate("a" * 200, 100) == "a" * 97 + "..."
