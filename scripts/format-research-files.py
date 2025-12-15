#!/usr/bin/env python3
"""
Add YAML frontmatter to research markdown files
"""

import os
import re
from pathlib import Path
from datetime import datetime

def extract_metadata_from_content(content, filepath):
    """Extract metadata from markdown content"""
    metadata = {}

    # Extract title (first H1)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    else:
        # Use filename as title
        metadata['title'] = Path(filepath).stem.replace('-', ' ').title()

    # Extract dates from filename (e.g., product-2024-12-10.md)
    filename = Path(filepath).stem
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if date_match:
        metadata['created'] = date_match.group(1)
        metadata['updated'] = date_match.group(1)
    else:
        today = datetime.now().strftime('%Y-%m-%d')
        metadata['created'] = today
        metadata['updated'] = today

    # Determine category based on path
    filepath_str = str(filepath)
    if 'stories' in filepath_str:
        metadata['category'] = 'Research'
        metadata['type'] = 'Success Story'
        metadata['tags'] = ['success-story']
    elif 'patterns' in filepath_str:
        metadata['category'] = 'Research'
        metadata['type'] = 'Pattern'
        metadata['tags'] = ['pattern']
    elif 'ideas' in filepath_str:
        metadata['category'] = 'Research'
        if 'feasibility' in filename:
            metadata['type'] = 'Feasibility Analysis'
            metadata['tags'] = ['feasibility', 'idea']
        else:
            metadata['type'] = 'Business Idea'
            metadata['tags'] = ['idea']
    elif 'reports' in filepath_str:
        metadata['category'] = 'Research'
        metadata['type'] = 'Analysis Report'
        metadata['tags'] = ['analysis', 'report']

    return metadata

def has_frontmatter(content):
    """Check if content already has YAML frontmatter"""
    return content.strip().startswith('---')

def create_frontmatter(metadata):
    """Create YAML frontmatter from metadata"""
    lines = ['---']

    # Title
    lines.append(f"title: {metadata.get('title', 'Untitled')}")

    # Dates
    lines.append(f"created: {metadata.get('created', '')}")
    lines.append(f"updated: {metadata.get('updated', '')}")

    # Tags
    tags = metadata.get('tags', [])
    if tags:
        tags_str = ', '.join(tags)
        lines.append(f"tags: [{tags_str}]")

    # Category and type
    if 'category' in metadata:
        lines.append(f"category: {metadata['category']}")
    if 'type' in metadata:
        lines.append(f"type: {metadata['type']}")

    lines.append('---')
    lines.append('')  # Blank line after frontmatter

    return '\n'.join(lines)

def add_frontmatter_to_file(filepath):
    """Add frontmatter to a markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has frontmatter
        if has_frontmatter(content):
            print(f"⏭️  Skip (has frontmatter): {filepath}")
            return False

        # Extract metadata
        metadata = extract_metadata_from_content(content, filepath)

        # Create frontmatter
        frontmatter = create_frontmatter(metadata)

        # Combine frontmatter + original content
        new_content = frontmatter + content

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Added frontmatter: {filepath}")
        return True

    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    """Main function"""
    research_dir = Path(__file__).parent.parent / 'research'

    if not research_dir.exists():
        print(f"❌ Research directory not found: {research_dir}")
        return

    # Find all markdown files
    md_files = list(research_dir.rglob('*.md'))

    print(f"\n📝 Found {len(md_files)} markdown files in research/\n")

    processed = 0
    skipped = 0
    errors = 0

    for md_file in sorted(md_files):
        result = add_frontmatter_to_file(md_file)
        if result is True:
            processed += 1
        elif result is False:
            skipped += 1
        else:
            errors += 1

    print(f"\n📊 Summary:")
    print(f"   ✅ Processed: {processed}")
    print(f"   ⏭️  Skipped: {skipped}")
    print(f"   ❌ Errors: {errors}")
    print(f"   📄 Total: {len(md_files)}\n")

if __name__ == '__main__':
    main()
