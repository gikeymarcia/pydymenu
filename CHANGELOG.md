All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.2.0] - 2021-07-05

### Added

- Rofi support with `pydymenu.rofi()`
- Added preview support for `fzf` with `pydymenu.fzf(options, preview="figlet 
  {}")`

### Changed

- No longer return `str` when `multi=False`. Instead, I always return a list of 
  strings.  When multi select is disallowed the `len(return_val) == 1 and 
  type(return_val) is list`

## [0.1.0-alpha] - 2021-06-09

### Added

- Initial release with working `pydymenu.fzf()`

### Changed

- Transmuted abstract wish into executable code (thanks brain)

### Fixed

- Scratched deep urge to create

## [Unreleased]
