# Contribution Guidelines

All kinds of contributions are welcome! As a contributor, here are the guidelines we would like you to follow:
- [Style Guide](#style-guide)
    - [Linting](#linting)
    - [Formatting](#formatting)
    - [Import Sorting](#import-sorting)
- [Commit Message Guidelines](#commit-message-guidelines)
    - [Header](#commit-message-header)
    - [Body](#commit-message-body)
    - [Footer](#commit-message-footer)

## Style Guide

Our project has several style guidelines that you must follow. Before you start, please read the instructions below carefully.

<!-- We use the following tools for linting and formatting:
- [flake8](https://flake8.pycqa.org/): A wrapper around some linter tools.
- [isort](https://pycqa.github.io/isort/): A Python utility to sort imports.
- [black](https://black.readthedocs.io/): A formatter for Python files.
- [codespell]: A Python utility to fix common misspellings in text files.
- [mdformat]: Mdformat is an opinionated Markdown formatter that can be used to enforce a consistent style in Markdown files. -->

### Linting

We adopt [PEP8](https://peps.python.org/pep-0008/) as the preferred code style and use [flake8](https://flake8.pycqa.org/) for linting to ensure code consistency and readability.

Use the following command:
```
flake8
```

### Formatting

For code formatting, we use [black](https://black.readthedocs.io/en/stable/), a highly opinionated code formatter. Black ensures a consistent and uniform code style throughout the project. It automatically reformats code to adhere to the PEP 8 style guide.

Use the following command:

```
black .
```

### Import Sorting

To maintain consistent import ordering, we also use [isort](https://pycqa.github.io/isort/).

Use the following command:

```
isort .
```

## Commit Message Guidelines

Each commit message consists of a **header**, a **body**, and a **footer**.

```
<header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The `header` is mandatory and must conform to the [Commit Message Header](#commit-message-header) format.

The `body` is strongly recommended for all commits, and when included, it must conform to the [Commit Message Body](#commit-message-body) format.

The `footer` is optional. The [Commit Message Footer](#commit-message-footer) format describes what the footer is used for and the structure it must have.

### Commit Message Header

```
<type>: <short summary>
  │           │
  │           └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test
```

The `<type>` and `<summary>` fields are mandatory.

#### Type
Must be one of the following:
- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- test: Adding missing tests or correcting existing tests

#### Summary
Use the summary field to provide a succinct description of the change:

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize the first letter
- no dot (.) at the end

### Commit Message Body
Just as in the summary, use the imperative, present tense: "fix" not "fixed" nor "fixes".

Explain the motivation for the change in the commit message body. This commit message should explain why you are making the change. You can include a comparison of the previous behavior with the new behavior in order to illustrate the impact of the change.

### Commit Message Footer
Related github issue number referenced by `Ref #ISSUE-NO.`
