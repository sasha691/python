call venv/scripts/activate

pip install -r requirements.txt
set TF_ENABLE_ONEDNN_OPTS=0
python __main__.py