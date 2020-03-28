git clone https://github.com/shresthagrawal/covid19.git 
cd covid19


virtualenv venv

source venv/bin/activate

git clone https://github.com/tyiannak/pyAudioAnalysis.git

pip3 install -r ./App/requirements.txt

pip3 install -r ./pyAudioAnalysis/requirements.txt

pip3 install -r ./App/requirements.txt

pip3 install -r ./pyAudioAnalysis/requirements.txt

pip3 install -e pyAudioAnalysis

python3 App/app.py

