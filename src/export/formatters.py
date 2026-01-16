"""Export formatters for results"""

import json
import csv
from typing import List, Dict, Any


class ResultFormatter:
    """Formats classification results for export"""
    
    @staticmethod
    def to_json(results: List[Dict[str, Any]], output_path: str) -> None:
        """Export results to JSON"""
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
    
    @staticmethod
    def to_csv(results: List[Dict[str, Any]], output_path: str) -> None:
        """Export results to CSV"""
        if not results:
            return
        
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    
    @staticmethod
    def to_xml(results: List[Dict[str, Any]], output_path: str) -> None:
        """Export results to XML"""
        xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<results>\n'
        for result in results:
            xml_content += '  <result>\n'
            for key, value in result.items():
                xml_content += f'    <{key}>{value}</{key}>\n'
            xml_content += '  </result>\n'
        xml_content += '</results>'
        
        with open(output_path, 'w') as f:
            f.write(xml_content)
