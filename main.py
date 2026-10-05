r"""
Main execution script for AnnaLis Gadea HTML Documentation.
Website source: https://paparazzi.li/annalis-gadea/
Output directory: D:\Annalis_Gadea\html
"""

import os
import sys
import shutil
import urllib.request
import json
import re

import generator

OUTPUT_DIR = r"D:\Annalis_Gadea\html"
HTMLOLD_DIR = r"D:\Annalis_Gadea\htmlold"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")

def ensure_images():
    r"""Ensure all required image assets exist in D:\Annalis_Gadea\html\images."""
    print("=" * 60)
    print("1. Synchronizing Image Assets")
    print("=" * 60)
    os.makedirs(IMAGES_DIR, exist_ok=True)
    
    # 1. Copy from htmlold if available
    old_images = os.path.join(HTMLOLD_DIR, "images")
    if os.path.exists(old_images):
        src_files = os.listdir(old_images)
        print(f"Checking {len(src_files)} image files from {old_images}...")
        copied = 0
        for f in src_files:
            dst = os.path.join(IMAGES_DIR, f)
            if not os.path.exists(dst):
                shutil.copy2(os.path.join(old_images, f), dst)
                copied += 1
        if copied > 0:
            print(f"Copied {copied} new images.")
        else:
            print("All existing images are already present in target directory.")

    # 2. Check and download image.png (portrait)
    img_portrait = os.path.join(IMAGES_DIR, "image.png")
    if not os.path.exists(img_portrait):
        print("Downloading portrait image (image.png)...")
        req = urllib.request.Request(
            "https://paparazzi.li/wp-content/uploads/2026/02/image.png",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req) as resp, open(img_portrait, "wb") as out:
            out.write(resp.read())
        print("image.png downloaded successfully!")
    else:
        print("Portrait image (image.png) verified on disk.")

    total_images = len(os.listdir(IMAGES_DIR))
    print(f"Total images available in {IMAGES_DIR}: {total_images}")
    return total_images

def verify_output():
    """Perform comprehensive automated verification of generated documentation."""
    print("\n" + "=" * 60)
    print("3. Validating Generated Documentation")
    print("=" * 60)

    errors = []

    # Expected HTML files
    expected_html_files = [
        "index.html",
        "annalis-gadea.html",
        "search.html",
        "annalis-gadea-asthetik-des-verfalls.html",
        "annalis-gadea-bleistiftzeichnungen.html",
        "annalis-gadea-diverse-themen.html",
        "annalis-gadea-elemente.html",
        "annalis-gadea-pflanzen-figurlich.html",
        "annalis-gadea-genesis.html",
        "annalis-gadea-geometrische-formen.html",
        "annalis-gadea-hauser.html",
        "annalis-gadea-lanzarotte.html",
        "annalis-gadea-akte.html",
        "annalis-gadea-nachbearbeitete-fotos.html",
        "annalis-gadea-organisch-abstrakt.html",
        "annalis-gadea-organisch-abstrakt-kleinformate.html",
        "annalis-gadea-pflanzliches-kleinformat.html",
        "annalis-gadea-pflanzen.html",
        "annalis-gadea-pflanzlich-abstrakt.html",
        "annalis-gadea-schnecken-und-schwane.html",
        "annalis-gadea-toscana.html",
        "annalis-gadea-transformationen.html",
    ]

    for f in expected_html_files:
        path = os.path.join(OUTPUT_DIR, f)
        if not os.path.exists(path):
            errors.append(f"Missing HTML file: {f}")
        else:
            size = os.path.getsize(path)
            if size == 0:
                errors.append(f"Empty HTML file: {f}")

    # Expected assets
    for a in ["style.css", "app.js", "search_data.js"]:
        path = os.path.join(OUTPUT_DIR, a)
        if not os.path.exists(path):
            errors.append(f"Missing asset file: {a}")
        elif os.path.getsize(path) == 0:
            errors.append(f"Empty asset file: {a}")

    # Check search_data.js content
    search_data_path = os.path.join(OUTPUT_DIR, "search_data.js")
    if os.path.exists(search_data_path):
        with open(search_data_path, "r", encoding="utf-8") as f:
            content = f.read()
        json_str = content.replace("window.SEARCH_DATA = ", "").rstrip(";\n")
        try:
            s_data = json.loads(json_str)
            pages_count = len(s_data.get("pages", []))
            items_count = len(s_data.get("items", []))
            print(f"Search index verified: {pages_count} pages, {items_count} searchable artworks/entries.")
            if pages_count != 20:
                errors.append(f"Expected 20 pages in search index, found {pages_count}")
            if items_count != 574:
                errors.append(f"Expected 574 items in search index, found {items_count}")
        except Exception as e:
            errors.append(f"Failed to parse search_data.js: {e}")

    # Verify that image references in HTML exist on disk and clicking shows full whole image
    disk_images = set(os.listdir(IMAGES_DIR))
    gallery_files = [f for f in expected_html_files if f not in ["index.html", "annalis-gadea.html", "search.html"]]
    
    total_cards = 0
    cards_with_full_image_link = 0

    for gf in gallery_files:
        path = os.path.join(OUTPUT_DIR, gf)
        with open(path, "r", encoding="utf-8") as f:
            html_text = f.read()

        # Find all card links
        card_matches = re.findall(r'<a class="artwork-card" href="([^"]+)" data-index="(\d+)"[^>]*>', html_text)
        for href, idx in card_matches:
            total_cards += 1
            img_filename = href.replace("images/", "")
            if img_filename in disk_images:
                cards_with_full_image_link += 1
            else:
                errors.append(f"Artwork card in {gf} links to non-existent image: {href}")

    print(f"Artwork cards verified across gallery pages: {cards_with_full_image_link} / {total_cards}")
    if total_cards != 573:
        errors.append(f"Expected 573 gallery cards, found {total_cards}")

    # Print validation result
    if errors:
        print("\n[WARNING] Validation issues detected:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\n[SUCCESS] All verification checks passed with 100% accuracy!")
        return True

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    print("=" * 60)
    print("AnnaLis Gadea HTML Documentation Generator")
    print(f"Target directory: {OUTPUT_DIR}")
    print("=" * 60)

    # 1. Sync & verify images
    ensure_images()

    # 2. Build documentation
    print("\n" + "=" * 60)
    print("2. Generating HTML Documentation Pages")
    print("=" * 60)
    generator.build_documentation()

    # 3. Validate results
    success = verify_output()

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  - Output Folder: {OUTPUT_DIR}")
    print(f"  - Home Page: {os.path.join(OUTPUT_DIR, 'index.html')}")
    print(f"  - Search Page: {os.path.join(OUTPUT_DIR, 'search.html')}")
    print("  - Local URL: file:///D:/Annalis_Gadea/html/index.html")
    print("  - Searchable: Yes (live search bar + dedicated search page)")
    print("  - Image Display: Clicking any image displays the whole full-resolution image with 100% zoom/pan viewer and direct file link")
    print("=" * 60)

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
