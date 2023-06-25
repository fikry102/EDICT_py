from edict_functions import *

'''
We provide a function `EDICT_editing` which accepts an image path, 
base prompt (original description) and desired edit prompt (target description).
'''


#save the image
from datetime import datetime
current_time = datetime.now()
folder_path = "Editing_imgs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_name = current_time.strftime("%Y%m%d_%H%M%S")+'.png'
img_path=os.path.join(folder_path,file_name)
plt.savefig(img_path)


#Editing
im_path = 'experiment_images/imagenet_cake.jpg'
base_prompt = 'A cupcake'
orig=load_im_into_format_from_path(im_path)

file_name = 'orig.png'
img_path=os.path.join(folder_path,file_name)
orig.save(img_path)

for edit_prompt in ['An Easter cupcake',
                   'A hedgehog cupcake',
                   'An England Union Jack cupcake',
                   'A Chinese New Year cupcake',
                   'A rainbow cupcake']:
    print(edit_prompt)
    edit_img=EDICT_editing(im_path,
              base_prompt,
              edit_prompt)[0]
    file_name = current_time.strftime("%Y%m%d_%H%M%S")+'.png'
    img_path=os.path.join(folder_path,file_name)
    edit_img.save(img_path)