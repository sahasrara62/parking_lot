
cd ..
FILE=functional_spec/tests/test_parking_lot.py
if [ -f "$FILE" ]; then
    echo "$FILE exist"
    echo "testing the custom test cases"
    python -m pytest -q functional_spec/tests/test_parking_lot.py
else
    echo "run the bash script from the bin folder."
fi
