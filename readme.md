
Run these commands to install dependencies: 
    pip install git+https://github.com/huggingface/diffusers.git transformers accelerate xformers wandb
    huggingface-cli login
    wandb login

    pip install datasets 
    pip3 install torch torchvision torchaudio

I found that uninstall and reinstalling torchvision helped with errors...