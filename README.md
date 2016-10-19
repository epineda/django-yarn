# django-yarn

Want to use npm/yarn modules in your django project without vendoring them? django-yarn serves as a wrapper around the yarn command-line program as well as a staticfiles finder.

## Installation

1. `$ pip install django-yarn`
2. Install npm, then install yarn (`npm install -g yarn`). If you use a private registry, make sure your `.yarnrc` is set up to connect to it
3. Have a `package.json` at the root of your project, listing your dependencies
4. Add `yarn.finders.YarnFinder` to `STATICFILES_FINDERS`
5. Configure your `settings.py`
6. `$ yarn add` with the command line, or with Python: `from yarn.finder import yarn_add; yarn_add()`
7. `$ ./manage.py collectstatic` will copy all selected node_modules files into your `STATIC_ROOT`.

## Configuration

 * `YARN_ROOT_PATH`: *absolute* path to the yarn "root" directory - this is where yarn will look for your `package.json`, put your `node_modules` folder and look for a `.yarnrc` file
 * `YARN_EXECUTABLE_PATH`: (optional) defaults to wherever `yarn` is on your PATH.  If you specify this, you can override the path to the `yarn` executable.  This is also an *absolute path*.
 * `YARN_STATIC_FILES_PREFIX`: (optional) Your yarn files will end up under this path inside static.  I usually use something like 'js/lib' (so your files will be in /static/js/lib/react.js for example) but you can leave it blank and they will just end up in the root.
 * `YARN_FILE_PATTERNS`: (optional) By default, django-yarn will expose all files in `node_modules` to Django as staticfiles.  You may not want *all* of them to be exposed.  You can pick specific files by adding some additional configuration:

    ```python
    YARN_FILE_PATTERNS = {
        'react': ['react.js'],
        'express': ['lib/*.js', 'index.js']
    }
    ```

    Keys are the names of the npm/yarn modules, and values are lists containing strings.  The strings match against glob patterns.

 * `YARN_FINDER_USE_CACHE`: (default True) A boolean that enables cache in the finder. If enabled, the file list will be computed only once, when the server is started.

## yarn add

If you want to run `yarn add` programmatically, you can do:

```python
from yarn.finders import yarn_add
yarn_add()
```

## Changelog

* V1.0.0 - Initial release based on django-npm v1.0.0.
