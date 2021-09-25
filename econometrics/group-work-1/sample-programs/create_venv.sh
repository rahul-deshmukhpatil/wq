VENV_NAME="group-work-1"
VENV_DIR="~/venv/$VENV_NAME"
#rm -rf $VENV_DIR 
python3 -m venv $VENV_DIR 
source $VENV_DIR/bin/activate
pip install -r requirements.txt
