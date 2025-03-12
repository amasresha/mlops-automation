```markdown
# MLOps Automation

A simple MLOps pipeline demonstrating Continuous Integration and Continuous Deployment (CI/CD) for a machine learning application.

```

 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Train the model:
  ```bash
  python app.py
  ```

- Run tests:
  ```bash
  python test_app.py
  ```

## CI/CD Automation

Use the `makefile` for linting, testing, and formatting:

- **Lint the code**:
  ```bash
  make lint
  ```

- **Run tests**:
  ```bash
  make test
  ```

- **Format the code**:
  ```bash
  make format
  ```

## License

Feel free to use it in any way.
