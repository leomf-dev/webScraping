from pathlib import Path
import json
from lxml import html

HTML_FILE = Path(__file__).resolve().parent / "descargas_sunat" / "resultado_ruc.html"


def normalize_text(text: str) -> str:
    return " ".join(text.split()).strip().rstrip(":")


def parse_value(node):
    if node is None:
        return None

    table_rows = node.xpath(".//tr")
    if table_rows:
        values = []
        for tr in table_rows:
            text = normalize_text(" ".join(tr.xpath(".//text()")))
            if text:
                values.append(text)
        return values

    paragraphs = node.xpath(".//p[contains(@class,'list-group-item-text')]//text()")
    if paragraphs:
        return normalize_text(" ".join(paragraphs))

    return normalize_text(" ".join(node.xpath(".//text()")))


def extract_data(html_content: str) -> dict:
    tree = html.fromstring(html_content)
    data = {}

    item_nodes = tree.xpath("//div[contains(@class,'list-group-item')]")
    for item in item_nodes:
        row_nodes = item.xpath(".//div[contains(@class,'row')]")
        if not row_nodes:
            continue

        for row in row_nodes:
            cols = row.xpath("./div")
            for idx in range(0, len(cols), 2):
                label_node = cols[idx]
                value_node = cols[idx + 1] if idx + 1 < len(cols) else None

                label = normalize_text(" ".join(label_node.xpath(".//h4//text()")))
                if not label:
                    label = normalize_text(" ".join(label_node.xpath(".//text()")))
                if not label:
                    continue

                value = parse_value(value_node)
                if value is None:
                    continue

                existing = data.get(label)
                if existing is None:
                    data[label] = value
                else:
                    # Si existen múltiples valores para la misma etiqueta, agruparlos
                    if isinstance(existing, list):
                        if isinstance(value, list):
                            existing.extend(value)
                        else:
                            existing.append(value)
                        data[label] = existing
                    else:
                        data[label] = [existing, value]

    footer_text = tree.xpath("//div[contains(@class,'panel-footer')]//small/text()")
    if footer_text:
        data["Fecha consulta"] = normalize_text(footer_text[0])

    return data


def main():
    if not HTML_FILE.exists():
        raise FileNotFoundError(f"No se encontró el archivo HTML en {HTML_FILE}")

    html_content = HTML_FILE.read_text(encoding="utf-8")
    extracted = extract_data(html_content)
    print(json.dumps(extracted, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
