from docling.document_converter import DocumentConverter

source = "https://lp.aros.com.br/"

converter = DocumentConverter()
result = converter.convert(source)

print(result.document.export_to_markdown())