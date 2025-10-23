# Makefile for imta-analytics

.PHONY: help pubs-md clean-md

help:
	@echo "Available targets:"
	@echo ""
	@echo "Documentation:"
	@echo "  pubs-md      - Convert PDFs in refs/publications to markdown using markitdown"
	@echo "  clean-md     - Remove all generated markdown files"

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

# Remove all generated markdown files (excluding README.md)
clean-md:
	@echo "Removing generated markdown files..."
	@cd refs/publications && \
	for pdf in *.pdf; do \
		md="$${pdf%.pdf}.md"; \
		if [ -f "$$md" ]; then \
			rm "$$md"; \
			echo "Removed: $$md"; \
		fi; \
	done
	@echo "✅ Generated markdown files cleaned"
