from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)

def test_bake_project_with_defaults(cookies):
    expected_folders = ["tests", "docs", "my_new_python_project", ".gitignore"]
    result = cookies.bake()

    assert result.project_path.is_dir()
    assert result.exit_code == 0
    assert result.exception is None

    found_folders = [folder.name for folder in list(result.project_path.glob("*"))]
    logger.info(f"Found the following folders: {found_folders}")

    for folder in expected_folders:
        assert folder in found_folders
