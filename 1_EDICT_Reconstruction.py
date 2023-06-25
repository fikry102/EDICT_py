from edict_functions import *

'''
Given an image (`x0`), we can invert it into latents `(xt,yt)` and reconstruct it with EDICT passes in different directions.

`run_baseline=True` is the DDIM-C baseline method from our paper, to run DDIM-UC `prompt` should be the empty string `''`

'''

#Reconstruction
im = load_im_into_format_from_path('experiment_images/church.jpg')
prompt = 'A church'
run_baseline = False

latents = coupled_stablediffusion(prompt,
                               reverse=True,
                                init_image=im,
                                run_baseline=run_baseline,
                               )
if run_baseline:
    latents = latents[0]
recon = coupled_stablediffusion(prompt,
                               reverse=False,
                                fixed_starting_latent=latents,
                                run_baseline=run_baseline,
                               )
recon = recon[0]

fig, (ax0, ax1) = plt.subplots(1,2)
ax0.imshow(im)
ax0.set_title("Original")
ax1.imshow(recon)
ax1.set_title("Recon")
plt.tight_layout()
# plt.show()

#save the image
from datetime import datetime
current_time = datetime.now()
folder_path = "Reconstruction_imgs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file_name = current_time.strftime("%Y%m%d_%H%M%S")+'.png'
img_path=os.path.join(folder_path,file_name)
plt.savefig(img_path)
