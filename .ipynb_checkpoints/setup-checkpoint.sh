sudo apt-get install git-lfs
git clone https://github.com/EricLBuehler/ScienceGPT.git
cd ScienceGPT
git lfs install
git lfs track "*.pt"
git config --global credential.helper store
git config --global user.email "ericlbuehler@gmail.com"
git config --global user.name "EricLBuehler"