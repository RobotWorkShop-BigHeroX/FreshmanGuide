import json
import os
import sys

REQUIRED_TOP_FIELDS = ["siteTitle", "orgName", "defaultDocId", "categories"]
REQUIRED_DOC_FIELDS = ["id", "year", "title", "badge", "releaseTag", "publishDate", "updatedAt", "markdownPath", "pdfPath"]

def validate_catalog():
    catalog_path = "catalog.json"
    assert os.path.exists(catalog_path), f"{catalog_path} not found"
  
    with open(catalog_path, "r", encoding="utf-8") as f:
        data = json.load(f)
  
    for field in REQUIRED_TOP_FIELDS:
        assert field in data, f"Missing top-level field: {field}"
  
    total_docs = 0
    doc_ids = set()
  
    for cat in data["categories"]:
        assert "name" in cat, "Category missing name"
        assert "items" in cat, "Category missing items"
      
        for item in cat["items"]:
            for field in REQUIRED_DOC_FIELDS:
                assert field in item, f"Doc item missing field {field}: {item}"
          
            doc_id = item["id"]
            assert doc_id not in doc_ids, f"Duplicate doc ID: {doc_id}"
            doc_ids.add(doc_id)
          
            # 校验物理 Markdown 文件存在
            md_path = item["markdownPath"]
            assert os.path.exists(md_path), f"Markdown file not found: {md_path}"
            assert os.path.getsize(md_path) > 100, f"Markdown file suspiciously small: {md_path}"
          
            # 校验物理 PDF 文件存在
            pdf_path = item["pdfPath"]
            assert os.path.exists(pdf_path), f"PDF file not found: {pdf_path}"
            actual_size = os.path.getsize(pdf_path)
            assert actual_size > 100000, f"PDF file suspiciously small: {pdf_path}"
          
            # 校验 attachmentUrl（如果配置）
            if "attachmentUrl" in item and item["attachmentUrl"]:
                url = item["attachmentUrl"]
                assert url.startswith("https://github.com/RobotWorkShop-BigHeroX/FreshmanGuide/releases/download/"), f"Invalid release asset download URL format: {url}"
          
            total_docs += 1
  
    assert data["defaultDocId"] in doc_ids, f"defaultDocId '{data['defaultDocId']}' not found in registered items"
    print(f"Catalog validation passed: {total_docs} documents verified.")

if __name__ == "__main__":
    validate_catalog()
