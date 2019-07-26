from .util import configure_settings
configure_settings()

import pytest

from django.core.files.storage import FileSystemStorage
from django.test.utils import override_settings

from yarn.finders import get_files
from yarn.finders import YarnFinder
from yarn.finders import yarn_add


@pytest.yield_fixture
def yarn_dir(tmpdir):
    package_json = tmpdir.join('package.json')
    package_json.write('''{
    "name": "test",
    "dependencies": {"mocha": "*"}
    }''')
    with override_settings(YARN_ROOT_PATH=str(tmpdir)):
        yarn_add()
        yield tmpdir


def test_get_files(yarn_dir):
    storage = FileSystemStorage(location=str(yarn_dir))
    files = get_files(storage, match_patterns='*')
    assert any([True for _ in files])

def test_finder_list_all(yarn_dir):
    f = YarnFinder()
    assert any([True for _ in f.list()])

def test_finder_find(yarn_dir):
    f = YarnFinder()
    file = f.find('mocha/mocha.js')
    assert file

def test_finder_in_subdirectory(yarn_dir):
    with override_settings(YARN_STATIC_FILES_PREFIX='lib'):
        f = YarnFinder()
        assert f.find('lib/mocha/mocha.js')

def test_finder_with_patterns_in_subdirectory(yarn_dir):
    with override_settings(YARN_STATIC_FILES_PREFIX='lib', YARN_FILE_PATTERNS={'mocha': ['*']}):
        f = YarnFinder()
        assert f.find('lib/mocha/mocha.js')

def test_finder_with_patterns_in_directory_component(npm_dir):
    with override_settings(YARN_STATIC_FILES_PREFIX='lib', YARN_FILE_PATTERNS={'mocha': ['*/*js']}):
        f = YarnFinder()
        assert f.find('lib/mocha/lib/test.js')

def test_no_matching_paths_returns_empty_list(npm_dir):
    with override_settings(YARN_FILE_PATTERNS={'foo': ['bar']}):
        f = YarnFinder()
        assert f.find('mocha/mocha.js') == []

def test_finder_cache(yarn_dir):
    with override_settings(YARN_FINDER_USE_CACHE=True):
        f = YarnFinder()
        f.list()
        assert f.cached_list is not None
        assert f.list() is f.cached_list

def test_finder_no_cache(yarn_dir):
    with override_settings(YARN_FINDER_USE_CACHE=False):
        f = YarnFinder()
        f.list()
        assert f.cached_list is None
        assert f.list() is not f.cached_list
