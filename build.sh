# Building
python3 -m build

# Pushing (requires user input)
python3 -m twine upload --repository pypi dist/*

# Remove excess files
rm -r dist/*
rm -r src/*.egg-info
