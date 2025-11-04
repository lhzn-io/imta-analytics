# Makefile for imta-analytics

.PHONY: help pubs-md tech-md refs-md clean-md clean-tech-md clean

help:
	@echo "Available targets:"
	@echo ""
	@echo "Documentation:"
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
