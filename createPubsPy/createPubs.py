import os
import bibtexparser
import re

def parse_bib_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    return bib_database.entries

def filter_entries(entries, author_name):
    filtered_entries = []
    for entry in entries:
        authors = entry.get('author', '').replace('\n', ' ')
        if author_name.lower() in authors.lower():
            filtered_entries.append(entry)
    return filtered_entries

def extract_arxiv_url(entry):
    """Extracts and formats the arXiv URL from the BibTeX entry."""
    journal = entry.get('journal', '').lower()
    if 'arxiv' in journal:
        arxiv_id_match = re.search(r'arxiv[:\s]*([0-9]+\.[0-9]+)', journal)
        if arxiv_id_match:
            arxiv_id = arxiv_id_match.group(1)
            return f"https://arxiv.org/pdf/{arxiv_id}"
    return None

def format_authors(authors):
    """Formats author names as 'First Last'."""
    formatted_authors = []
    for author in authors.split(' and '):
        parts = [part.strip() for part in author.split(',')]
        if len(parts) == 2:
            formatted_authors.append(f"{parts[1]} {parts[0]}")
        else:
            formatted_authors.append(parts[0])
    return formatted_authors

def generate_md_content(entry, preprint_url=None):
    # Extract fields from the BibTeX entry
    title = entry.get('title', '').strip('{}')
    authors = format_authors(entry.get('author', ''))
    year = entry.get('year', '2024')
    date = f"{year}-12-12T00:00:00"
    publication_types = "1" if entry.get('booktitle') else "2"
    abstract = entry.get('abstract', 'Abstract not available.')
    publication = entry.get('booktitle') or entry.get('journal', '')
    url_pdf = entry.get('url', '')
    url_preprint = preprint_url if url_pdf else ''
    
    # Format the markdown content
    md_content = f"""---
title: "{title}"
date: {date}
authors: {authors}
publication_types: ["{publication_types}"]
abstract: "{abstract}"
featured: false
publication: "*{publication}*"
url_pdf: "{url_pdf}"
url_preprint: "{url_preprint}"
tags: []
---
"""
    return md_content

def create_folder_name(entry):
    # Create a folder name based on conference/journal name, year, and key paper topic from title
    year = entry.get('year', '2024')
    publication = entry.get('booktitle', entry.get('journal', '')).lower()
    publication_short = re.sub(r'[^a-z0-9]', '-', publication)[:10]  # Shorten and replace special characters
    title_keyword = re.sub(r'[^a-z0-9]', '-', entry.get('title', '').lower().split()[0])  # Use first keyword from the title
    return f"{publication_short}-{year}-{title_keyword}".strip('-')

def save_files(entry, preprint_url=None, output_dir="output"):
    # Generate folder name and create the folder
    folder_name = create_folder_name(entry)
    folder_path = os.path.join(output_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # Generate and save index.md
    md_content = generate_md_content(entry, preprint_url)
    with open(os.path.join(folder_path, 'index.md'), 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)
    
    # Create a BibDatabase object and add the entry
    bib_db = bibtexparser.bibdatabase.BibDatabase()
    bib_db.entries = [entry]
    
    # Save the BibTeX entry to cite.bib
    bibtex_str = bibtexparser.dumps(bib_db)
    with open(os.path.join(folder_path, 'cite.bib'), 'w', encoding='utf-8') as bib_file:
        bib_file.write(bibtex_str)

def merge_entries(acl_entries, scholar_entries):
    # Create a dictionary to prioritize ACL entries by title
    merged_entries = {}
    
    for entry in acl_entries:
        title = entry.get('title', '').strip('{}').lower()
        merged_entries[title] = (entry, None)  # (ACL entry, None for preprint URL initially)
    
    # Add Google Scholar entries only if they are not already in the ACL entries
    for entry in scholar_entries:
        title = entry.get('title', '').strip('{}').lower()
        preprint_url = extract_arxiv_url(entry)
        if title in merged_entries:
            # If an ACL entry exists, update it with the preprint URL if available
            acl_entry, _ = merged_entries[title]
            merged_entries[title] = (acl_entry, preprint_url)
        else:
            # Otherwise, add the Google Scholar entry with its preprint URL
            merged_entries[title] = (entry, preprint_url)
    
    return merged_entries.values()

def main():
    # Replace with the actual file paths
    acl_bib_file_path = 'anthology+abstracts.bib'
    scholar_bib_file_path = 'GScholarCitations.txt'
    output_dir = 'pubs/'
    author_name = 'Kanojia, Diptesh'
    
    # Parse both BibTeX files
    acl_entries = parse_bib_file(acl_bib_file_path)
    scholar_entries = parse_bib_file(scholar_bib_file_path)
    
    # Filter for entries where the author is Diptesh Kanojia
    acl_entries = filter_entries(acl_entries, author_name)
    scholar_entries = filter_entries(scholar_entries, author_name)
    
    # Merge the entries, prioritizing ACL entries
    merged_entries = merge_entries(acl_entries, scholar_entries)
    
    # Generate folders and files for each entry
    for entry, preprint_url in merged_entries:
        save_files(entry, preprint_url, output_dir=output_dir)
    
    print(f"Markdown and BibTeX files generated in {output_dir}")

if __name__ == '__main__':
    main()
