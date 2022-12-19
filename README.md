Reusable workflow for building docs with Sphinx
===============================================

Prerequisites:

*   One or more jobs that build and upload a source and binary distribution
    artifact.

Usage:

```yaml
jobs:
  dist:
    # Job that builds and uploads a source and binary distribution artifact.
  sphinx:
    name: Build documentation
    needs: dist
    uses: evalf/workflow-sphinx/.github/workflows/build.yaml@release/1
    with:
      # Sphinx source directory. (optional)
      source: docs
      # Name of the dist artifact. (uploaded by job 'dist', optional)
      dist: dist
      # Comma-separated list of extras to include when installing the target. (optional)
      extras: ''
      # Space-separated list of packages required to build the documentation. (optional)
      requirements: ''
      # Name of the docs artifact. (optional)
      artifact: docs
```
