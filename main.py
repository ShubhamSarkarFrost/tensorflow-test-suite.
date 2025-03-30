import unittest
from utils.reporter import TestReportGenerator

def main():
    print("\n🔥 Running TensorFlow Test Suite...")

    # Initialize the report generator
    report_generator = TestReportGenerator(output_dir="test_reports")

    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    runner = unittest.TextTestRunner(verbosity=2)

    result = runner.run(suite)

    # Collect errors and failures
    for test_case, error_msg in result.errors:
        report_generator.add_result(str(test_case), "FAILED", details=error_msg)

    for test_case, fail_msg in result.failures:
        report_generator.add_result(str(test_case), "FAILED", details=fail_msg)

    # Collect passed tests
    if result.wasSuccessful():
        for test in suite:
            report_generator.add_result(str(test), "PASSED")

    # Generate new report
    report = report_generator.generate_report()

    print("\n✅ Test execution completed!")
    print(f"📄 JSON report: {report['json_path']}")
    print(f"📊 HTML report: {report['html_path']}")
    print(f"📈 Visual report: {report['pie_chart_path']}")

if __name__ == "__main__":
    main()
