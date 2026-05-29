# Contributing to Best-websites-a-programmer-should-visit

Thank you for considering contributing to this project! Please follow these guidelines to ensure your contributions are accepted smoothly.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature or fix
3. Make your changes
4. Ensure your changes follow the existing format
5. Submit a pull request

## Contribution Format

When adding a new website, please use the following format:

`* [Site name | A simple description](url) : a simple description of the site or slogan of the site.`

## CI/CD Guidelines

This project uses GitHub Actions for Continuous Integration and Continuous Deployment. 

### What the CI/CD Pipeline Does:
- **Linting**: Checks markdown files for formatting issues
- **Testing**: Verifies that required files (README.md, CONTRIBUTING.md) exist
- **Build**: Creates documentation artifacts in the `dist` directory
- **Deployment**: Automatically deploys to GitHub Pages when changes are merged to the `main` branch

### Requirements for Contributions:
- All contributions must pass the linting stage
- All contributions must pass the testing stage
- Ensure your changes do not break the build process

### Reporting Issues
If you encounter any issues with the CI/CD pipeline or have suggestions for improvement, please open an issue.

kindly.
