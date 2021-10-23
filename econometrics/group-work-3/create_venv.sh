VENV_NAME="group-work-3"
VENV_DIR="$HOME/venv/$VENV_NAME"

mkdir -p $HOME/venv

echo "$VENV_NAME : $VENV_DIR"
#rm -rf $VENV_DIR 
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate
pip install -r requirements.txt
