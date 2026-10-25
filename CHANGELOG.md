# Changelog

## Unreleased

### Added

- Nix builds, tests, docs, and direnv development shell.
- Ruff linting, treefmt formatting, and Nix-based GitHub CI.

### Changed

- Moved setuptools configuration to `pyproject.toml`.
- Switched docs to Furo.
- Converted README and docs to Markdown with MyST.

### Removed

- Python 2 compatibility; use `0.3.3` for Python 2.

## [0.3.3] - 2016-09-05

### Changed

- Ported examples to Python 3.

### Fixed

- Dictionary traversal on Python 3.
- Missing `LICENSE` in source distributions.
- README formatting on PyPI.

## [0.3.2] - 2016-06-28

### Changed

- Release metadata only.

## [0.3.1] - 2015-10-03

### Added

- MIT license file.

### Fixed

- Unicode labels on Python 2.

## [0.3] - 2015-02-27

### Added

- Configurable `LeftAligned` renderer; retained `draw_tree()`.
- Dictionary and attribute-based traversal.
- Unicode box styles and Sphinx API docs.

[0.3]: https://pypi.org/project/asciitree/0.3/
[0.3.1]: https://pypi.org/project/asciitree/0.3.1/
[0.3.2]: https://pypi.org/project/asciitree/0.3.2/
[0.3.3]: https://pypi.org/project/asciitree/0.3.3/
