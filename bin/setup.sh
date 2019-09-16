ver=$(python -c"import sys; print(sys.version_info.major)")
if [ $ver -eq 2 ]; then
    echo "python version 2"
    echo "update python to python 3"
elif [ $ver -eq 3 ]; then
    echo "python version 3"
    echo "install requirements"
    cd .. || retrun "run file from bin folder"
    cd functional_spec || exit
    python -m pip install -r requirements.txt

else
    echo "Unknown python version: $ver"
fi