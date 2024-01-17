
Run these commands to install dependencies: 
    pip install git+https://github.com/huggingface/diffusers.git transformers accelerate xformers wandb
    huggingface-cli login
    wandb login

    pip install datasets 
    pip3 install torch torchvision torchaudio

I found that uninstall and reinstalling torchvision helped with errors...


--- 
Steps for pushing the model to the hub. 

* this did not work yet, I keep getting network errors...



    1  wget https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh
    2  chmod +x script.deb.sh
    3  ./script.deb.sh 
    4  apt-get install git-lfs
    5  git lfs install
    6  huggingface-cli login
    7  cd controlnet-densepose-sd2-1-base/
    8  ls
    9  git lfs install
   17  huggingface-cli login