pip install -r requirements.txt

if [[ $1 == 'dev' ]]; then
    pip install -r requirements.dev.txt
fi
