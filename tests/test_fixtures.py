import pytest
from pathlib import Path
import json
from mdcitefix.core import fix_markdown, FixOptions, FixReport

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def collect_fixture_cases():
    """フィクスチャディレクトリから全テストケースを収集"""
    cases = []
    for test_dir in sorted(FIXTURES_DIR.iterdir()):
        if not test_dir.is_dir() or test_dir.name.startswith('.') or test_dir.name == '__pycache__':
            continue
        input_file = test_dir / "input.md"
        expected_file = test_dir / "expected.md"
        if input_file.exists() and expected_file.exists():
            # Use directory name as test ID (format: NN__category__case_name)
            test_id = test_dir.name
            cases.append((test_id, test_dir))
    return cases


@pytest.mark.parametrize("test_id,test_dir", collect_fixture_cases())
def test_fixture(test_id, test_dir):
    """パラメータ化されたフィクスチャテスト"""
    # 入力と期待出力を読み込み
    input_md = (test_dir / "input.md").read_text(encoding="utf-8")
    expected_md = (test_dir / "expected.md").read_text(encoding="utf-8")

    # オプション設定を読み込み（あれば）
    config_file = test_dir / "config.json"
    if config_file.exists():
        config = json.loads(config_file.read_text(encoding="utf-8"))
        options = FixOptions(**config)
    else:
        options = FixOptions()

    # 実行
    actual_md, report = fix_markdown(input_md, options)

    # 検証
    assert actual_md == expected_md, (
        f"Output mismatch in {test_id}\n"
        f"Expected:\n{expected_md}\n"
        f"Actual:\n{actual_md}\n"
        f"Report: {report.to_json()}"
    )

    # メタデータがあればレポートも検証
    metadata_file = test_dir / "metadata.json"
    if metadata_file.exists():
        metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
        if "expected_report" in metadata:
            _verify_report(report, metadata["expected_report"], test_id)


def _verify_report(actual: FixReport, expected: dict, test_id: str):
    """レポート内容の検証"""
    if "missing_count" in expected:
        assert len(actual.missing) == expected["missing_count"], (
            f"{test_id}: Expected {expected['missing_count']} missing refs, "
            f"got {len(actual.missing)}: {actual.missing}"
        )
    if "merged_count" in expected:
        assert len(actual.merged) == expected["merged_count"], (
            f"{test_id}: Expected {expected['merged_count']} merged refs, "
            f"got {len(actual.merged)}: {actual.merged}"
        )
    if "warnings_count" in expected:
        assert len(actual.warnings) == expected["warnings_count"], (
            f"{test_id}: Expected {expected['warnings_count']} warnings, "
            f"got {len(actual.warnings)}: {actual.warnings}"
        )
    if "unused_count" in expected:
        assert len(actual.unused) == expected["unused_count"], (
            f"{test_id}: Expected {expected['unused_count']} unused refs, "
            f"got {len(actual.unused)}: {actual.unused}"
        )
