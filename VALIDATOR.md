# SWIM Service Description Validator

The repository includes a Python validator script to validate service descriptions against the official JSON schema.

## Setup

1. Create a Python virtual environment (recommended):

**On Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**On Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required Python package:
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install jsonschema
```

3. If you cloned the repository, initialize the submodule:
```bash
git submodule update --init --recursive
```

## Usage

Validate a service description file:

**With activated virtual environment:**
```bash
python validate-service-description.py "METAR (IWXXM)_METEOFRANCE.json"
```

**Or with direct path to Python in virtual environment (Windows):**
```bash
.\.venv\Scripts\python.exe validate-service-description.py "METAR (IWXXM)_METEOFRANCE.json"
```

**Or with direct path to Python in virtual environment (Linux/Mac):**
```bash
./.venv/bin/python validate-service-description.py "METAR (IWXXM)_METEOFRANCE.json"
```

Use a custom schema file:
```bash
python validate-service-description.py service.json --schema path/to/schema.json
```

Enable verbose output:
```bash
python validate-service-description.py service.json --verbose
```

The validator will:
- ✓ Exit with code 0 if validation succeeds
- ✗ Exit with code 1 if validation fails, with detailed error messages

## Schema Location

The validator uses the schema from the git submodule:
- `service-metadata-schema/description/DESCRIPTION-V2.json` (from git submodule)
- Custom path can be specified with `--schema` option

Make sure to initialize the submodule after cloning:
```bash
git submodule update --init --recursive
```
