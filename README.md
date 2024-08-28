# PYINSTALLER-APPIMAGE
To create the executable file using pyinstaller command line in linux system
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
pyinstaller --onedir main.py

pyinstaller --onedir \
    --exclude-module matplotlib \
    --exclude-module torch.utils.tensorboard \
    --add-data '/home/inx-soft-026/.local/lib/python3.10/site-packages/cv2:cv2' \
    --add-data '/home/inx-soft-026/.local/lib/python3.10/site-packages/numpy:numpy' \
    --add-data '/home/inx-soft-026/.local/lib/python3.10/site-packages/torch:torch' \
    main.py

