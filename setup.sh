sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git-lfs
git lfs install
git lfs track "models"
git clone https://github.com/EricLBuehler/ScienceGPT.git
cd ScienceGPT
git config --global credential.helper store