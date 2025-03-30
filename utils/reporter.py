import json
import os
import glob
from datetime import datetime
import matplotlib.pyplot as plt



class TestReportGenerator:
    """
    A class to generate test reports for TensorFlow models
    """

    def __init__(self, output_dir="test_reports"):
        self.output_dir = output_dir
        self.results = []

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Clean old reports before starting a new run
        self.clean_old_reports()

    def clean_old_reports(self):
        """Delete old report files before generating new ones."""
        print("\n🧹 Cleaning up old reports...")

        # Remove all old .json, .html, and .png files
        report_patterns = [
            os.path.join(self.output_dir, "*.json"),
            os.path.join(self.output_dir, "*.html"),
            os.path.join(self.output_dir, "*.png")
        ]

        for pattern in report_patterns:
            for file in glob.glob(pattern):
                os.remove(file)
                print(f"🗑️ Deleted: {file}")

    def add_result(self, test_name, status, details=""):
        """Add a test result to the report."""
        self.results.append({
            "test_name": test_name,
            "status": status,
            "details": details,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def generate_report(self):
        """Generate all reports (JSON, HTML, PNG)."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # JSON report
        json_path = os.path.join(self.output_dir, f"test_report_{timestamp}.json")
        with open(json_path, "w") as f:
            json.dump(self.results, f, indent=4)

        # HTML report
        html_path = os.path.join(self.output_dir, f"test_report_{timestamp}.html")
        self._generate_html_report(html_path)

        # Visualization (pie chart)
        pie_chart_path = os.path.join(self.output_dir, f"test_results_pie_{timestamp}.png")
        self._generate_visual_report(pie_chart_path)

        return {
            "json_path": json_path,
            "html_path": html_path,
            "pie_chart_path": pie_chart_path
        }

    def _generate_html_report(self, output_path):
        """Generate an HTML report."""
        html_content = """
        <html>
        <head>
            <title>Test Report</title>
            <style>
                body { font-family: Arial, sans-serif; }
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid #ddd; padding: 8px; }
                th { background-color: #f2f2f2; }
                .pass { color: green; }
                .fail { color: red; }
            </style>
        </head>
        <body>
        <h1>Test Report</h1>
        <table>
        <tr><th>Test Name</th><th>Status</th><th>Details</th><th>Timestamp</th></tr>
        """

        for result in self.results:
            status_class = "pass" if result['status'] == "PASSED" else "fail"
            html_content += f"""
            <tr>
                <td>{result['test_name']}</td>
                <td class="{status_class}">{result['status']}</td>
                <td>{result['details']}</td>
                <td>{result['timestamp']}</td>
            </tr>
            """

        html_content += "</table></body></html>"

        with open(output_path, "w") as f:
            f.write(html_content)

    def _generate_visual_report(self, output_path):
        """Generate a pie chart visualization."""
        statuses = [r['status'] for r in self.results]
        passed = statuses.count("PASSED")
        failed = statuses.count("FAILED")

        labels = ['PASSED', 'FAILED']
        sizes = [passed, failed]
        colors = ['#4CAF50', '#FF5733']

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
        plt.title("Test Results")
        plt.savefig(output_path)
        plt.close()
