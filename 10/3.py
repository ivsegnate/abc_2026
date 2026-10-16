import csv
import json
from abc import ABC, abstractmethod
from datetime import datetime
import io
import xml.etree.ElementTree as ET


class DataExporter(ABC):

    @abstractmethod
    def export(self, data: list[dict]) -> None:
        pass

    @abstractmethod
    def get_format_name(self) -> str:
        pass

    def validate_data(self, data: list) -> bool:
        return bool(data)


class JSONExporter(DataExporter):

    def get_format_name(self) -> str:
        return "JSON"

    def export(self, data: list[dict]) -> None:
        if not self.validate_data(data):
            raise ValueError("Данные для экспорта пусты.")

        modified_data = []
        current_time = datetime.now().isoformat()

        for record in data:
            new_record = record.copy()
            new_record["export_timestamp"] = current_time
            modified_data.append(new_record)

        print(json.dumps(modified_data, ensure_ascii=False, indent=2))


class CSVExporter(DataExporter):

    def get_format_name(self) -> str:
        return "CSV"

    def export(self, data: list[dict]) -> None:
        if not self.validate_data(data):
            raise ValueError("Данные для экспорта пусты.")

        output = io.StringIO()
        headers = list(data[0].keys())

        writer = csv.DictWriter(output, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)

        print(output.getvalue().strip())


class XMLExporter(DataExporter):

    def get_format_name(self) -> str:
        return "XML"

    def export(self, data: list[dict]) -> None:
        if not self.validate_data(data):
            raise ValueError("Данные для экспорта пусты.")

        root = ET.Element("report")

        for record in data:
            item = ET.SubElement(root, "item")
            for key, value in record.items():
                child = ET.SubElement(item, key)
                child.text = str(value)

        xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
        print(xml_str)


if __name__ == "__main__":
    sales_data = [
        {"product": "Laptop", "price": 1000, "quantity": 2},
        {"product": "Mouse", "price": 50, "quantity": 10},
    ]

    exporters = [JSONExporter(), CSVExporter(), XMLExporter()]

    for exporter in exporters:
        print(f"Формат: {exporter.get_format_name()}")
        exporter.export(sales_data)
        print()
