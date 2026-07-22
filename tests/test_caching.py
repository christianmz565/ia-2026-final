"""Unit tests for the caching module and step execution logic."""

import tempfile
import unittest
from pathlib import Path

from src.caching import is_cached, run_cached_step


class TestCaching(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_is_cached_file(self) -> None:
        file_path = self.path / "test.txt"
        self.assertFalse(is_cached(file_path))

        # Empty file should not count as cached
        file_path.touch()
        self.assertFalse(is_cached(file_path))

        # Non-empty file should count as cached
        file_path.write_text("content")
        self.assertTrue(is_cached(file_path))

    def test_is_cached_dir(self) -> None:
        dir_path = self.path / "test_dir"
        self.assertFalse(is_cached(dir_path))

        dir_path.mkdir()
        # Empty directory should not count as cached
        self.assertFalse(is_cached(dir_path))

        # Non-empty directory should count as cached
        (dir_path / "item.txt").write_text("hello")
        self.assertTrue(is_cached(dir_path))

    def test_run_cached_step_execution_and_skip(self) -> None:
        target_file = self.path / "result.txt"
        execution_count = 0

        def _step_fn() -> Path:
            nonlocal execution_count
            execution_count += 1
            target_file.write_text("step output")
            return target_file

        # First run: should execute function
        res1 = run_cached_step("test_step", target_file, _step_fn)
        self.assertEqual(execution_count, 1)
        self.assertEqual(res1, target_file)

        # Second run: should skip execution (cached)
        res2 = run_cached_step("test_step", target_file, _step_fn)
        self.assertEqual(execution_count, 1)
        self.assertEqual(res2, target_file)

        # Third run with force=True: should re-execute function
        res3 = run_cached_step("test_step", target_file, _step_fn, force=True)
        self.assertEqual(execution_count, 2)
        self.assertEqual(res3, target_file)


if __name__ == "__main__":
    unittest.main()
