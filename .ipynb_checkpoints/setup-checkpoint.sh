sudo apt-get install git-lfs
git clone https://github.com/EricLBuehler/ScienceGPT.git
cd ScienceGPT
git lfs install
git lfs track "models"
git config --global credential.helper store