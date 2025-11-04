#!/bin/bash

# Script to install git hooks for the imta-analytics project
# This sets up pre-commit hooks that prevent commits with failing tests

echo "Setting up git hooks for imta-analytics..."

# Get the repository root
REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"
GITHOOKS_DIR="$REPO_ROOT/.githooks"

# Check if .githooks directory exists
if [ ! -d "$GITHOOKS_DIR" ]; then
    echo "Error: .githooks directory not found!"
    exit 1
fi

# Install pre-commit hook
if [ -f "$GITHOOKS_DIR/pre-commit" ]; then
    echo "Installing pre-commit hook..."
    cp "$GITHOOKS_DIR/pre-commit" "$HOOKS_DIR/pre-commit"
    chmod +x "$HOOKS_DIR/pre-commit"
    echo "✅ Pre-commit hook installed successfully!"
else
    echo "Warning: pre-commit hook not found in .githooks/"
fi

echo ""
echo "Git hooks setup complete!"
echo ""
echo "The pre-commit hook will now:"
echo "  - Run 'make test-fast' before each commit (unit tests only)"
echo "  - Typical commit time: ~5-10 seconds"
echo "  - Prevent commits if fast tests fail"
echo "  - Allow bypass with 'git commit --no-verify' if needed"
echo ""
echo "💡 Hook Management:"
echo "  - Check status: make check-hooks"
echo "  - Run fast tests: make test-fast"
echo "  - Run all tests: make test"
echo "  - Reinstall hooks: .githooks/install-hooks.sh"
