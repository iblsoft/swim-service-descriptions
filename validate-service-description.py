#!/usr/bin/env python3
"""
SWIM Service Description Validator

This script validates SWIM service description JSON documents against the
DESCRIPTION-V2 JSON schema.
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate, ValidationError, SchemaError
except ImportError:
    print("Error: jsonschema library not found. Install it with: pip install jsonschema")
    sys.exit(1)


def load_json_file(file_path):
    """Load and parse a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {file_path}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        sys.exit(1)


def validate_service_description(json_doc_path, schema_path):
    """
    Validate a SWIM service description JSON document against the schema.
    
    Args:
        json_doc_path: Path to the JSON document to validate
        schema_path: Path to the JSON schema file
        
    Returns:
        True if validation succeeds, False otherwise
    """
    # Load the JSON document
    print(f"Loading JSON document: {json_doc_path}")
    json_doc = load_json_file(json_doc_path)
    
    # Load the schema
    print(f"Loading schema: {schema_path}")
    schema = load_json_file(schema_path)
    
    # Validate
    try:
        print("Validating...")
        validate(instance=json_doc, schema=schema)
        print("✓ Validation successful! The document is valid.")
        return True
    except ValidationError as e:
        print("✗ Validation failed!")
        print(f"Error: {e.message}")
        if e.path:
            print(f"Path: {' -> '.join(str(p) for p in e.path)}")
        if e.schema_path:
            print(f"Schema path: {' -> '.join(str(p) for p in e.schema_path)}")
        return False
    except SchemaError as e:
        print(f"✗ Schema error: {e.message}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error during validation: {e}")
        return False


def main():
    """Main entry point for the validator."""
    parser = argparse.ArgumentParser(
        description='Validate SWIM Service Description JSON documents against the DESCRIPTION-V2 schema.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s service.json
  %(prog)s service.json --schema custom-schema.json
        """
    )
    
    parser.add_argument(
        'json_document',
        help='Path to the JSON document to validate'
    )
    
    parser.add_argument(
        '-s', '--schema',
        default=None,
        help='Path to the schema file (default: service-metadata-schema/description/DESCRIPTION-V2.json)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Determine schema path
    if args.schema:
        schema_path = Path(args.schema)
    else:
        # Try to find schema in the submodule location
        script_dir = Path(__file__).parent
        submodule_schema = script_dir / 'service-metadata-schema' / 'description' / 'DESCRIPTION-V2.json'
        
        if submodule_schema.exists():
            schema_path = submodule_schema
            if args.verbose:
                print(f"Using schema from submodule: {schema_path}")
        else:
            print("Error: Schema file not found!")
            print("Please ensure the submodule is initialized:")
            print(f"  git submodule update --init --recursive")
            print(f"Expected schema location: {submodule_schema}")
            print("Or specify a schema path with --schema option")
            sys.exit(1)
    
    if not schema_path.exists():
        print(f"Error: Schema file not found: {schema_path}")
        sys.exit(1)
    
    # Validate the document
    success = validate_service_description(args.json_document, schema_path)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
