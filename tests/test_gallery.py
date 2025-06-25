import os
import re
from pathlib import Path


def extract_local_images(html: str):
    pattern = re.compile(r"['\"]([^'\"]+\.(?:jpg|jpeg|png|gif))['\"]", re.IGNORECASE)
    images = set()
    for match in pattern.finditer(html):
        path = match.group(1)
        if '://' not in path:
            images.add(path)
    return sorted(images)


def test_gallery_images_exist():
    repo_root = Path(__file__).resolve().parents[1]
    index_file = repo_root / 'index.html'
    html = index_file.read_text(encoding='utf-8')
    images = extract_local_images(html)
    assert images, 'No images found in index.html'
    for img in images:
        assert (repo_root / img).is_file(), f"Missing image file: {img}"
