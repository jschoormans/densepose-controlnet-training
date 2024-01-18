from huggingface_hub import HfApi
api = HfApi()

api.upload_folder(
    folder_path="controlnet-densepose-sd2-1-base",
    repo_id="jschoormans/controlnet-densepose-sd2-1-base",
    repo_type="model",
)