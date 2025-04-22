import re
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='attr')
def attr(field_widget_html, css):
    """
    Adds HTML attributes to a Django form field widget's HTML.

    Usage: {{ form.my_field.as_widget|attr:"class:form-control,placeholder:Enter text here,required" }}

    Parses comma-separated attribute definitions.
    - "key:value" sets the attribute 'key' to 'value'.
    - "attribute" sets a boolean attribute (like 'required').
    - "class:value" will append 'value' to existing classes if present.
    """
    attrs = {}
    definitions = css.split(',')

    # Parse attribute definitions
    for d in definitions:
        d = d.strip()
        if ':' in d:
            key, val = d.split(':', 1)
            attrs[key.strip()] = val.strip()
        elif d: # Handle boolean attributes like 'required'
            attrs[d.strip()] = True

    # Render the widget with the new attributes
    # Note: This simple implementation directly modifies the HTML string.
    # A more robust approach might involve parsing the HTML or using widget attrs.

    # Find the opening tag (e.g., <input ... >)
    tag_match = re.match(r'<(\w+)([^>]*)>', field_widget_html)
    if not tag_match:
        return field_widget_html # Return original if tag not found

    tag_name = tag_match.group(1)
    existing_attrs_str = tag_match.group(2)
    closing_part = field_widget_html[tag_match.end():] # Part after the opening tag

    # Extract existing attributes into a dict
    existing_attrs = {}
    for match in re.finditer(r'([\w-]+)(?:="([^"]*)")?', existing_attrs_str):
        key = match.group(1)
        # Use value or True for boolean attributes
        value = match.group(2) if match.group(2) is not None else True
        existing_attrs[key.lower()] = value


    # Merge and update attributes
    final_attrs = existing_attrs.copy()
    for key, value in attrs.items():
        key_lower = key.lower()
        if key_lower == 'class' and 'class' in final_attrs:
            # Append class value, ensuring no duplicate spaces
            current_classes = final_attrs['class'].split() if isinstance(final_attrs['class'], str) else []
            new_classes = value.split()
            all_classes = current_classes + [cls for cls in new_classes if cls not in current_classes]
            final_attrs['class'] = ' '.join(all_classes)

        elif key_lower == 'class':
             final_attrs['class'] = value # Set class if it doesn't exist
        else:
            final_attrs[key_lower] = value # Overwrite or add other attributes


    # Build the new attributes string
    attrs_parts = []
    for key, value in final_attrs.items():
        if value is True: # Boolean attribute (e.g., required)
            attrs_parts.append(conditional_escape(key))
        else:
            # Ensure value is escaped properly
            attrs_parts.append(f'{conditional_escape(key)}="{conditional_escape(value)}"')

    new_attrs_str = (' ' + ' '.join(attrs_parts)) if attrs_parts else ''

    # Reconstruct the HTML
    new_html = f'<{tag_name}{new_attrs_str}>{closing_part}'

    return mark_safe(new_html)


@register.filter(name='add_error_class')
def add_error_class(field_widget_html, errors):
    """
    Adds the 'is-invalid' class to a widget's HTML if errors exist for the field.

    Usage: {{ form.my_field.as_widget|add_error_class:form.my_field.errors }}
    """
    if errors:
        # Use the attr filter to add the class cleanly
        return attr(field_widget_html, 'class:is-invalid')
    return field_widget_html

# Optional: Add a filter to render widget directly (if not using as_widget)
# Example: {{ form.my_field|add_class:"form-control" }}
@register.filter(name='add_class')
def add_class(field, css_class):
    """Adds a CSS class to a Django form field's widget."""
    return field.as_widget(attrs={'class': css_class})