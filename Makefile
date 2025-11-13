# Makefile for imta-analytics

# Use bash instead of sh for conda activation
SHELL := /bin/bash

# Define conda environment activation command
CONDA_BASE := $(shell conda info --base 2>/dev/null || echo "$$HOME/.miniconda3")
CONDA_ACTIVATE = source $(CONDA_BASE)/etc/profile.d/conda.sh && conda activate imta-analytics
PYTEST = $(CONDA_ACTIVATE) && python -m pytest

.PHONY: help pubs-md tech-md refs-md clean-md clean-tech-md clean docs
.PHONY: test test-fast test-coverage test-unit test-integration
.PHONY: install-hooks check-hooks

help:
	@echo "Available targets:"
	@echo ""
	@echo "Testing:"
	@echo "  test          - Run unit and integration tests"
	@echo "  test-fast     - Run unit tests only (fast, for pre-commit)"
	@echo "  test-unit     - Run unit tests only"
	@echo "  test-integration - Run integration tests only"
	@echo "  test-coverage - Run tests with coverage report"
	@echo ""
	@echo "Git Hooks:"
	@echo "  install-hooks - Install git pre-commit hooks"
	@echo "  check-hooks   - Check if git hooks are installed"
	@echo ""
	@echo "Documentation:"
	@echo "  docs          - Generate PDF documentation from markdown"
	@echo "  pubs-md       - Convert PDFs in refs/publications to markdown using markitdown"
	@echo "  tech-md       - Convert PDFs in refs/technical to markdown using markitdown"
	@echo "  refs-md       - Convert all PDFs in refs/ subdirectories to markdown"
	@echo "  clean-md      - Remove all generated markdown files"
	@echo "  clean-tech-md - Remove generated markdown from refs/technical"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean         - Remove all build artifacts, caches, and temporary files"

# Generate markdown files from PDFs in refs/publications using markitdown
pubs-md:
	@echo "Generating markdown files from PDFs in refs/publications..."
	@cd refs/publications && \
	missing_count=0; \
	for pdf in *.pdf; do \
		md="$${pdf%.pdf}.md"; \
		if [ ! -f "$$md" ]; then \
			echo "Converting: $$pdf"; \
			uvx --with markitdown[all] markitdown "$$pdf" --output "$$md" || { echo "Failed to convert $$pdf"; exit 1; }; \
			missing_count=$$((missing_count + 1)); \
		fi; \
	done; \
	if [ $$missing_count -eq 0 ]; then \
		echo "✅ All PDFs already have markdown files"; \
	else \
		echo "✅ Converted $$missing_count PDF(s) to markdown"; \
	fi; \
	echo ""; \
	echo "Summary:"; \
	echo "  PDF files: $$(ls -1 *.pdf 2>/dev/null | wc -l)"; \
	echo "  MD files:  $$(ls -1 *.md 2>/dev/null | grep -v '^README.md$$' | wc -l)"

# Generate markdown files from PDFs in refs/technical using markitdown
tech-md:
	@echo "Generating markdown files from PDFs in refs/technical..."
	@cd refs/technical && \
	missing_count=0; \
	for pdf in *.pdf; do \
		md="$${pdf%.pdf}.md"; \
		if [ ! -f "$$md" ]; then \
			echo "Converting: $$pdf"; \
			uvx --with markitdown[all] markitdown "$$pdf" --output "$$md" || { echo "Failed to convert $$pdf"; exit 1; }; \
			missing_count=$$((missing_count + 1)); \
		fi; \
	done; \
	if [ $$missing_count -eq 0 ]; then \
		echo "✅ All PDFs already have markdown files"; \
	else \
		echo "✅ Converted $$missing_count PDF(s) to markdown"; \
	fi; \
	echo ""; \
	echo "Summary:"; \
	echo "  PDF files: $$(ls -1 *.pdf 2>/dev/null | wc -l)"; \
	echo "  MD files:  $$(ls -1 *.md 2>/dev/null | grep -v '^README.md$$' | wc -l)"

# Convert all PDFs in refs/ subdirectories to markdown
refs-md: pubs-md tech-md
	@echo ""
	@echo "✅ All reference PDFs converted to markdown"

# Remove all generated markdown files (excluding README.md)
clean-md: clean-tech-md
	@echo "Removing generated markdown files..."
	@cd refs/publications && \
	for pdf in *.pdf; do \
		md="$${pdf%.pdf}.md"; \
		if [ -f "$$md" ]; then \
			rm "$$md"; \
			echo "Removed: $$md"; \
		fi; \
	done
	@echo "✅ All generated markdown files cleaned"

# Remove generated markdown from refs/technical
clean-tech-md:
	@echo "Removing generated markdown files from refs/technical..."
	@cd refs/technical && \
	for pdf in *.pdf; do \
		md="$${pdf%.pdf}.md"; \
		if [ -f "$$md" ]; then \
			rm "$$md"; \
			echo "Removed: $$md"; \
		fi; \
	done
	@echo "✅ Technical markdown files cleaned"

# Remove all build artifacts, caches, and temporary files
clean:
	@echo "Cleaning up build artifacts and temporary files..."
	@# Python caches
	@find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name '*.pyc' -delete 2>/dev/null || true
	@find . -type f -name '*.pyo' -delete 2>/dev/null || true
	@find . -type f -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
	@# Build directories
	@rm -rf build/ dist/ .eggs/ 2>/dev/null || true
	@# Test and coverage
	@rm -rf .pytest_cache/ .coverage htmlcov/ .tox/ 2>/dev/null || true
	@# Type checking
	@rm -rf .mypy_cache/ .pytype/ 2>/dev/null || true
	@# IDE files
	@find . -type f -name '.DS_Store' -delete 2>/dev/null || true
	@# Windows Zone.Identifier artifacts
	@find . -type f -name '*Zone.Identifier' -delete 2>/dev/null || true
	@echo "✅ Cleaned up all build artifacts and temporary files"

# Utility target to activate conda environment
activate-env:
	@echo "Activating imta-analytics conda environment..."

# Testing targets
test: activate-env
	@echo "Running standard tests (unit + integration)..."
	@$(PYTEST) tests/ -v

test-fast: activate-env
	@echo "Running fast tests (unit tests only)..."
	@# Check hook configuration unless we're in CI or being called by the hook itself
	@if [ -z "$$CI" ] && [ -z "$$GIT_HOOK" ] && [ -d ".git" ]; then \
		echo "🔍 Verifying pre-commit hook configuration..."; \
		if [ -f ".git/hooks/pre-commit" ]; then \
			if ! grep -q "make test-fast" ".git/hooks/pre-commit"; then \
				echo ""; \
				echo "⚠️  WARNING: Pre-commit hook is NOT configured for fast tests!"; \
				echo "   Current hook may run ALL tests (slow commits)"; \
				echo ""; \
				echo "   To fix, reinstall hooks with: make install-hooks"; \
				echo ""; \
			fi; \
		else \
			echo ""; \
			echo "⚠️  WARNING: No pre-commit hook installed!"; \
			echo "   Tests will NOT run automatically before commits"; \
			echo ""; \
			echo "   To install hooks: make install-hooks"; \
			echo ""; \
		fi; \
	fi
	@$(PYTEST) tests/unit/ -v

test-unit: activate-env
	@echo "Running unit tests..."
	@$(PYTEST) tests/unit/ -v

test-integration: activate-env
	@echo "Running integration tests..."
	@$(PYTEST) tests/integration/ -v

test-coverage: activate-env
	@echo "Running tests with coverage..."
	@$(CONDA_ACTIVATE) && python -m coverage run -m pytest tests/ -v && \
		python -m coverage report -m && \
		python -m coverage html
	@echo ""
	@echo "Coverage report generated in htmlcov/index.html"

# Git hooks management
install-hooks:
	@echo "Installing git hooks..."
	@.githooks/install-hooks.sh

check-hooks:
	@echo "Checking git hooks installation..."
	@if [ -f ".git/hooks/pre-commit" ]; then \
		echo "✅ Pre-commit hook is installed"; \
		echo "   Location: .git/hooks/pre-commit"; \
		if grep -q "make test-fast" ".git/hooks/pre-commit"; then \
			echo "   Configuration: Running 'make test-fast' (unit tests only)"; \
		else \
			echo "   ⚠️  Configuration: NOT using 'make test-fast'"; \
		fi; \
	else \
		echo "❌ Pre-commit hook is NOT installed"; \
		echo "   Run 'make install-hooks' to install"; \
	fi

# Documentation generation (markdown to PDF)
docs:
	@echo "Generating PDF documentation from markdown files with YAML frontmatter..."
	@tmpfile=$$(mktemp); \
	find docs refs -name "*.md" -type f -print0 | while IFS= read -r -d '' md_file; do \
		if head -1 "$$md_file" | grep -q "^---$$"; then \
			pdf_file="$${md_file%.md}.pdf"; \
			echo "Converting: $$md_file"; \
			if pandoc "$$md_file" \
				-o "$$pdf_file" \
				--pdf-engine=xelatex \
				-V geometry:"top=1.2in,bottom=1.2in,left=1.3in,right=1.3in" \
				-V fontsize=11pt \
				-V linestretch=1.4 \
				-V documentclass=article \
				-V mainfont:"Liberation Serif" \
				-V monofont:"Liberation Mono" \
				-V sansfont:"Liberation Sans" \
				--toc \
				--toc-depth=2 \
				-V colorlinks=true \
				-V linkcolor=blue \
				-V urlcolor=blue \
				-V toccolor=black 2>/dev/null; then \
				echo "1" >> "$$tmpfile"; \
			else \
				echo "  ⚠️  Failed to convert $$md_file"; \
			fi; \
		fi; \
	done; \
	if [ -f "$$tmpfile" ]; then \
		count=$$(wc -l < "$$tmpfile"); \
		rm "$$tmpfile"; \
		echo ""; \
		echo "✅ Converted $$count markdown file(s) to PDF"; \
	else \
		echo "No markdown files with YAML frontmatter found."; \
		echo "Add frontmatter to markdown files to enable PDF generation:"; \
		echo "---"; \
		echo "title: \"Document Title\""; \
		echo "subtitle: \"Optional Subtitle\""; \
		echo "author: \"Your Name\""; \
		echo "date: \"YYYY-MM-DD\""; \
		echo "---"; \
	fi
