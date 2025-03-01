if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
. .venv/bin/activate
sha256sum -c req-SHA256SUMS
if [ $? == "0" ]; then
    echo "requirements.txt sin cambios"
else 
    echo "requirements.txt con cambio, actualizando ..."
    sha256sum requirements.txt > req-SHA256SUMS
    pip install -r requirements.txt
fi
flask --app app run --host=0.0.0.0 --debug --port ${FLASK_PORT:-5000}