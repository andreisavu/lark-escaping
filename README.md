# Lark Escaping Repository

This repository is dedicated to exploring string literal parsing and SQL encoding tests. It serves as a practical example of using the `Lark` parser for parsing string literals and `pypika` for constructing SQL queries.

## Features

- **String Literal Parsing**: Utilizes the `Lark` parser to interpret and transform string literals in various formats.
- **SQL Encoding Tests**: Leverages `pypika` to construct SQL queries, ensuring correct encoding and escaping of string literals.

## Configuration

The project is configured for Python 3.11, with continuous integration tests running on GitHub Actions as specified in `.github/workflows/python-app.yml`.

## Dependencies

For detailed versions of dependencies, refer to `pyproject.toml`. Key dependencies include:
- `lark`: For parsing string literals.
- `pypika`: For constructing SQL queries.

## Playground for Copilot Workspace

This repository also serves as a playground for experimenting with GitHub's Copilot Workspace, exploring its capabilities in code generation and assistance.

## Using Earthly for Building and Testing

This project supports building and testing with Earthly, a build automation tool that allows for repeatable and isolated builds. To use Earthly, ensure you have it installed on your system.

### Building the Project

To build the project with Earthly, run the following command:

```shell
earthly +build
```

This command will install all necessary dependencies and prepare the project for testing or deployment.

### Running Tests

To run tests using Earthly, execute the following command:

```shell
earthly +test
```

This will run all configured tests in an isolated environment, ensuring consistency across different machines and environments.
