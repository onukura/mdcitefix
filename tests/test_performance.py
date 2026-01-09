import pytest
import time
from pathlib import Path
from mdcitefix.core import fix_markdown, FixOptions

FIXTURES_DIR = Path(__file__).parent / "fixtures"

# パフォーマンステストはデフォルトでスキップ
# pytest -m performance で実行
pytestmark = pytest.mark.performance


@pytest.mark.parametrize("test_name,max_time_ms", [
    ("19__performance__medium_500_refs", 100),
    ("20__performance__large_1000_refs", 500),
])
def test_performance_benchmark(test_name, max_time_ms):
    """パフォーマンスベンチマーク"""
    test_dir = FIXTURES_DIR / test_name
    input_file = test_dir / "input.md"

    # テストケースがまだ存在しない場合はスキップ
    if not input_file.exists():
        pytest.skip(f"Performance test fixture {test_name} not yet created")

    input_md = input_file.read_text(encoding="utf-8")

    # ウォームアップ
    fix_markdown(input_md)

    # 実測定（3回の平均）
    times = []
    for _ in range(3):
        start = time.perf_counter()
        fix_markdown(input_md)
        end = time.perf_counter()
        times.append((end - start) * 1000)

    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)

    print(f"\n{test_name}:")
    print(f"  Average: {avg_time:.2f}ms")
    print(f"  Min: {min_time:.2f}ms")
    print(f"  Max: {max_time:.2f}ms")
    print(f"  Target: {max_time_ms}ms")

    assert avg_time < max_time_ms, (
        f"Performance degradation: {avg_time:.2f}ms > {max_time_ms}ms target"
    )
