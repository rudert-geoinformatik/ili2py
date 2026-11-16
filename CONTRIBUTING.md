# Contributing

Thank you for considering reading this guide!
Contributions are welcome :)


* [Types of Contributions](#Types-of-Contributions)
* [Contributor Setup](#Setting-Up-the-Code-for-Local-Development)
* [Contributor Guidelines](#Contributor-Guidelines)
* [Contributor Testing](#Testing)
* [Core Committer Guide](#Core-Committer-Guide)


## Types of Contributions

You can contribute in many ways:

### Report Bugs

Report bugs at [https://github.com/rudert-geoinformatik/ili2py/issues](https://github.com/rudert-geoinformatik/ili2py/issues).
W
Stambling upon a Bug means encountering different behaviour than the expected/advertised one. When you are reporting a bug, please include the following infromation by filling in [the template](https://github.com/rudert-geoinformatik/ili2py/.github/blob/master/.github/ISSUE_TEMPLATE/bug_report.md).

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* If you can, provide detailed steps to reproduce the bug.
* If you don't have steps to reproduce the bug, just note your observations in as much detail as you can. Questions to start a discussion about the issue are welcome.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is open to whoever wants to implement it. See [Contributor Setup](#Setting-Up-the-Code-for-Local-Development) to get started.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "please-help" is open to whoever wants to implement it.

Please do not combine multiple feature enhancements into a single pull request.

See [Contributor Setup](#Setting-Up-the-Code-for-Local-Development) to get started.

### Write Documentation

ili2py could always use more documentation, whether as part of the official ili2py docs, in docstrings, etc.

If you want to review your changes on the documentation locally, you can do:

```bash
make doc-serve
```

This will compile the documentation (into html) and start watching the files for changes, recompiling as you save.
You can open it in your browser at http://127.0.0.1:8000 !

### Submit Feedback

The best way to send feedback is to file an issue at [https://github.com/rudert-geoinformatik/ili2py/issues](https://github.com/rudert-geoinformatik/ili2py/issues).

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Setting Up the Code for Local Development

Here's how to set up `ili2py` for local development.

1. Fork the `ili2py` repo on GitHub.
2. Clone your fork locally:

```bash
git clone git@github.com:rudert-geoinformatik/ili2py.git
```

3. Install your local copy with [uv](https://docs.astral.sh/uv/). This creates `.venv` with the package (editable) and the `dev` and `test` dependency groups:

```bash
cd ili2py
make install-test
uv run pre-commit install
```

4. Create a branch for local development:

```bash
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

1. When you're done making changes, check that your changes pass the tests locally:

```bash
make test
make lint
make check
```

`make format` applies the ruff fixes and formatting. If you want to produce a built tar.gz and wheel distributions:

```bash
make build
```

1. Ensure that your feature or commit is fully covered by tests. Check the coverage report that is shown on the console when you run `make test-coverage`.

1. Commit your changes and push your branch to GitHub:

```bash
git add -p
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

8. Submit a pull request through the GitHub website.

## Contributor Guidelines

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. The pull request should be contained: if it's too big consider splitting it into smaller pull requests.
3. If the pull request adds functionality, the docs should be updated.
4. The pull request must pass all CI/CD jobs before being ready for review.
5. If one CI/CD job is failing for unrelated reasons you may want to create another PR to fix that first.

### Coding Standards

* Single Responsibility of Units
* Modularity
* Composition over Inheritance


## Testing

Tests run with pytest, see the [pytest usage docs](https://docs.pytest.org/en/stable/how-to/usage.html) for selecting tests.

To run all tests:

```bash
make test
```

To only run test cases matching the string 'smoke_test':

```bash
uv run --group test pytest -k 'smoke_test'
```

To run the tests with another python version (e.g. 3.13):

```bash
uv run --isolated --python 3.13 --group test pytest
```

### End-to-end tests

The end-to-end tests (marker `e2e`) generate python classes from an IMD, read and write the XTF test data with them and check the written XTF with [ilivalidator](https://github.com/claeis/ilivalidator). They are not part of `make test`. Requirements:

* a Java runtime (JRE), `java` has to be on the `PATH`
* network access: ilivalidator is downloaded from downloads.interlis.ch and the models are looked up on http://models.interlis.ch

To run them:

```bash
make test-e2e
```

ilivalidator is downloaded and unpacked to `build/ilivalidator-<version>` on the first run. The version and the number of parallel pytest workers can be overridden:

```bash
make test-e2e ILIVALIDATOR_VERSION=1.15.0 E2E_WORKERS=8
```

Without `ILIVALIDATOR_JAR` (set by `make test-e2e`) or `java` the tests are skipped.

To run them for some models only, `model` is handed to pytest as `-k` expression:

```bash
make test-e2e model="Fruchtfolgeflaechen or Hazard_Mapping"
```

### Reading and writing with the rendered classes

The tests of reading and writing XTF with the rendered classes are grouped in sections, so they can be run on their own:

* `make test-rendered-read`: the rendered classes read the XTF of a model, with the geometry as dataclasses and compact
* `make test-rendered-write`: the XTF written with compact geometry is the same as the one written by xsdata alone

Both take `model` as well. They run on a fast selection of INTERLIS 2.3 and 2.4 models and need neither java nor network.

To run the unit tests and the end-to-end tests together:

```bash
make tests
```


## Core Committer Guide

### Vision and Scope

Core committers, use this section to:

* Guide your instinct and decisions as a core committer
* Limit the codebase from growing infinitely

#### API Accessible

* Modular API striving for statelessness
* Easy to use without having to think too hard
* Flexible for more complex use cases
* Easily extensible

#### Extensible

* Modular Design
* Aim for statelessness


#### Fast and Focused

ili2py is designed to do one thing, and do that one thing very well.

* Cover the important use cases and as little as possible beyond that :)


#### Inclusive

* Cross-platform and cross-version support

#### Stable

* Aim for high test coverage and covering corner cases
* No pull requests will be accepted that drop test coverage on any platform
* Stable APIs that tool builders can rely on


### Process: Pull Requests

How to prioritize pull requests, from most to least important:

* Fixes for broken tests. Broken means broken on any supported platform or Python version.
* Extra tests to cover corner cases.
* Minor edits to docs.
* Bug fixes.
* Major edits to docs.
* Features.

#### Pull Requests Review Guidelines
- Think carefully about the long-term implications of the change. How will it affect existing projects that are dependent on this? If this is complicated, do we really want to maintain it forever?
- Take the time to get things right, PRs almost always require additional improvements to meet the bar for quality. **Be very strict about quality.**
- When you merge a pull request take care of closing/updating every related issue explaining how they were affected by those changes. Also, remember to add the author to `AUTHORS.md`.

### Process: Issues

If an issue is a bug that needs an urgent fix, mark it for the next patch release.
Then either fix it or mark as please-help.

For other issues: encourage friendly discussion, moderate debate, offer your thoughts.

### Process: Roadmap

The roadmap located [here](https://github.com/rudert-geoinformatik/ili2py/milestones?direction=desc&sort=due_date&state=open)

Due dates are flexible.

### Process: Release

* Follow semantic versioning. Look at: [http://semver.org](http://semver.org). We stay on `0.x` while the API is still changing.
* The git tag is the only source of the version. setuptools-scm derives it at build time, nobody writes a version into the code.
* Untagged builds get a dev version like `0.1.1.dev3+g1a2b3c4`.

Releasing:

1. Make sure everything for the release is merged to `master`. There is no changelog to update: the release notes are generated from the merged pull requests, so give pull requests meaningful titles.
2. Tag and push:

```bash
git tag -a vX.Y.Z -m "vX.Y.Z"
git push origin vX.Y.Z
```

Alternatively create the release with a new tag in the GitHub UI.

3. CI builds and tests, creates the GitHub release with generated release notes, binaries, wheel and sdist and publishes the package to PyPI as `interlis2py`.
