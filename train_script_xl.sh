accelerate launch train_controlnet_sdxl.py \
 --pretrained_model_name_or_path="stabilityai/stable-diffusion-xl-base-1.0" \
 --output_dir="model_out" \
 --dataset_name=jschoormans/densepose_1024 \
 --conditioning_image_column=conditioning_image \
 --image_column=file_name \
 --caption_column=caption \
 --resolution=512 \
 --learning_rate=1e-5 \
 --validation_image "validation_images/000988787_densepose.jpg" "validation_images/002021752_densepose.jpg" "validation_images/002162699_densepose.jpg" \
 --validation_prompt "High-quality close-up dslr photo of man doing yoga" "Girl smiling, professional dslr photograph, dark background, studio lights, high quality" "Portrait of a runner" \
 --train_batch_size=1 \
 --num_train_epochs=3 \
 --tracker_project_name="controlnet" \
 --enable_xformers_memory_efficient_attention \
 --checkpointing_steps=5000 \
 --validation_steps=1000 \
 --report_to wandb \
 --push_to_hub \
 --gradient_accumulation_steps=4 \
 --gradient_checkpointing \
 --use_8bit_adam \
 --set_grads_to_none



