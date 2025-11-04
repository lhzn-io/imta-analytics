"""
Notebook utilities for consistent result display and formatting.

Provides functions for displaying analysis results with consistent formatting,
including the display_result() function for blue-background info boxes.
"""

from IPython.display import display, Markdown, HTML
from typing import Union, Optional


def display_result(content: str, title: Optional[str] = None, style: str = "info") -> None:
    """
    Display formatted result with colored background in Jupyter notebooks.
    
    Args:
        content: The main content to display (supports markdown)
        title: Optional title/header for the result box
        style: Display style - "info" (blue), "success" (green), "warning" (yellow), "error" (red)
    
    Example:
        >>> display_result("Data loaded successfully.", "✓ Success", "success")
        >>> display_result("Found 3 outliers in temperature data.", "⚠ Warning", "warning")
    """
    # Define color schemes for different styles
    colors = {
        "info": {
            "bg": "#d1ecf1",
            "border": "#bee5eb",
            "text": "#0c5460"
        },
        "success": {
            "bg": "#d4edda",
            "border": "#c3e6cb",
            "text": "#155724"
        },
        "warning": {
            "bg": "#fff3cd",
            "border": "#ffeaa7",
            "text": "#856404"
        },
        "error": {
            "bg": "#f8d7da",
            "border": "#f5c6cb",
            "text": "#721c24"
        }
    }
    
    color_scheme = colors.get(style, colors["info"])
    
    # Build HTML with title if provided
    title_html = ""
    if title:
        title_html = f'<strong>{title}</strong><br>'
    
    html = f"""
    <div style="
        background-color: {color_scheme['bg']};
        border: 1px solid {color_scheme['border']};
        border-left: 4px solid {color_scheme['border']};
        color: {color_scheme['text']};
        padding: 12px 16px;
        margin: 10px 0;
        border-radius: 4px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        font-size: 14px;
        line-height: 1.6;
    ">
        {title_html}
        {content}
    </div>
    """
    
    display(HTML(html))


def display_info(content: str, title: Optional[str] = None) -> None:
    """Display info message with blue background."""
    display_result(content, title, "info")


def display_success(content: str, title: Optional[str] = None) -> None:
    """Display success message with green background."""
    display_result(content, title, "success")


def display_warning(content: str, title: Optional[str] = None) -> None:
    """Display warning message with yellow background."""
    display_result(content, title, "warning")


def display_error(content: str, title: Optional[str] = None) -> None:
    """Display error message with red background."""
    display_result(content, title, "error")


def format_dict_as_list(data: dict, indent: int = 2) -> str:
    """
    Format dictionary as HTML list for display in result boxes.
    
    Args:
        data: Dictionary to format
        indent: Indentation level (spaces per level)
    
    Returns:
        HTML formatted string
    """
    items = []
    for key, value in data.items():
        items.append(f"<li><strong>{key}:</strong> {value}</li>")
    
    return f"<ul style='margin: 5px 0; padding-left: 20px;'>{''.join(items)}</ul>"


def format_stats_table(data: dict) -> str:
    """
    Format statistics dictionary as HTML table.
    
    Args:
        data: Dictionary of statistics (key: label, value: statistic)
    
    Returns:
        HTML formatted table string
    """
    rows = []
    for key, value in data.items():
        rows.append(f"<tr><td><strong>{key}</strong></td><td>{value}</td></tr>")
    
    table = f"""
    <table style='width: 100%; border-collapse: collapse;'>
        {''.join(rows)}
    </table>
    """
    
    return table
