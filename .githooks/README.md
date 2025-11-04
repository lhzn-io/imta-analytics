# Git Hooks for IMTA Analytics

This directory contains git hooks for the IMTA Analytics project.

## Installation

Run the install script to set up the hooks:

```bash
.githooks/install-hooks.sh
```

Or use the Makefile target:

```bash
make install-hooks
```

## Pre-commit Hook

The pre-commit hook automatically runs fast unit tests before each commit to catch issues early.

### What it does

- Runs `make test-fast` (unit tests only, ~5-10 seconds)
- Activates the `imta-analytics` conda environment
- Prevents commits if tests fail
- Provides helpful error messages

### Bypassing the hook

If you need to commit despite failing tests (not recommended):

```bash
git commit --no-verify
```

## Hook Configuration

### Verify hook is installed

```bash
make check-hooks
```

### Reinstall hooks

```bash
.githooks/install-hooks.sh
```

### Remove hooks

```bash
rm .git/hooks/pre-commit
```

## Testing Workflow

### Fast tests (pre-commit)
```bash
make test-fast          # Unit tests only (~5-10s)
```

### Standard tests
```bash
make test               # Unit + integration tests
```

### All tests with coverage
```bash
make test-coverage      # Full suite with coverage report
```

## Troubleshooting

### Hook not running

1. Check if hook is installed: `ls -l .git/hooks/pre-commit`
2. Verify hook is executable: `chmod +x .git/hooks/pre-commit`
3. Reinstall: `.githooks/install-hooks.sh`

### Tests fail in hook but pass manually

1. Ensure conda environment is activated
2. Check that `pytest` and `pytest-cov` are installed
3. Verify package is installed: `pip install -e .`

### Hook takes too long

The hook runs only unit tests (~5-10s). If it's slower:

1. Check for slow tests in `tests/unit/`
2. Move slow tests to `tests/integration/`
3. Verify test fixtures are using `tmp_path` (automatic cleanup)

## Best Practices

1. **Run tests locally before committing**: `make test-fast`
2. **Don't bypass hooks routinely**: Fix failing tests instead
3. **Keep unit tests fast**: Mock external dependencies, avoid I/O
4. **Run full test suite periodically**: `make test` or `make test-coverage`
