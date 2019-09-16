cd ..
FILE=main.py
if [ -f "$FILE" ]; then
    echo "$FILE exist"
    echo "Running main.py"
    python main.py
else
    echo "run the bash script from the bin folder."
fi
