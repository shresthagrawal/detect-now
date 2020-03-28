# Clone The repo
`git clone https://github.com/shresthagrawal/covid19.git`
`cd covid19`

# Create a virtual env
`virtualenv venv`

`source venv/bin/activate`

# Clone 
`git clone https://github.com/tyiannak/pyAudioAnalysis.git`

# Install Dependencies
`pip3 install -r ./App/requirements.txt`

`pip3 install -r ./pyAudioAnalysis/requirements.txt`

`brew install ffmpeg`

# Install
`pip3 install -e pyAudioAnalysis`

# Using Test.py
`python3 App/app.py`

# Alternative
`chmod +x ./auto.sh`

`./auto.sh`

# Training on the original dataset
`python3 pyAudioAnalysis/pyAudioAnalysis/audioAnalysis.py trainClassifier -i data/cough/not_sick data/cough/sick --method randomforest -o model_new`

#Training on Uploads
`python3 pyAudioAnalysis/pyAudioAnalysis/audioAnalysis.py trainClassifier -i data/uploads/not_sick data/uploads/sick --method randomforest -o model/model_new`

# Training Dataset
[data-set](https://osf.io/4pt2s/)
