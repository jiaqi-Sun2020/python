import cv2
import os
from tqdm import tqdm
import torch
# import numpy as np
# from LapDepth.model import LDRN
# import glob
# import torch.backends.cudnn as cudnn
# from PIL import Image
# from torchvision import transforms
# import torch.nn.functional as F
# import matplotlib.pyplot as plt
import argparse


#========================================================================lap

from yolo.detect_yolo_distance import detect








in_path = "./in"

pictures_path = os.listdir(in_path)
# print(pictures_path)
last_shape = None
for i,picture_path  in tqdm(enumerate(pictures_path)):
    read_path = in_path +"/" + picture_path
    img = cv2.imread(read_path)
    img_shape = img.shape
    if last_shape != None:
        assert img_shape == last_shape , "error img-shape"
    last_shape = img_shape


# #==============================================================================================================================================================
# parser = argparse.ArgumentParser(description='Laplacian Depth Residual Network training on KITTI',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument('--model_dir',type=str, default = r'./LapDepth/LDRN_KITTI_ResNext101_pretrained_data.pkl')
# parser.add_argument('--img_dir', type=str, default = None)
# parser.add_argument('--img_folder_dir', type=str, default= "./in")
#
# # Dataloader setting
# parser.add_argument('--seed', default=0, type=int, help='seed for random functions, and network initialization')
#
# # Model setting
# parser.add_argument('--encoder', type=str, default = "ResNext101")
# parser.add_argument('--pretrained', type=str, default = "KITTI")
# parser.add_argument('--norm', type=str, default = "BN")
# parser.add_argument('--n_Group', type=int, default = 32)
# parser.add_argument('--reduction', type=int, default = 16)
# parser.add_argument('--act', type=str, default = "ReLU")
# parser.add_argument('--max_depth', default=80.0, type=float, metavar='MaxVal', help='max value of depth')
# parser.add_argument('--lv6', action='store_true', help='use lv6 Laplacian decoder')
#
# # GPU setting
# parser.add_argument('--cuda', action='store_true')
# parser.add_argument('--gpu_num', type=str, default = "0", help='force available gpu index')
# parser.add_argument('--rank', type=int,   help='node rank for distributed training', default=0)
#
# args = parser.parse_args()
#
#
# # --model_dir
# # LDRN_KITTI_ResNext101_pretrained_data.pkl
# # --img_folder_dir
# # ./example
# # --pretrained
# # KITTI
# # --cuda
# # --gpu_num
# # 0
#
#
#
# assert (args.img_dir is not None) or (args.img_folder_dir is not None), "Expected name of input image file or folder"
#
# if args.cuda and torch.cuda.is_available():
#     os.environ["CUDA_VISIBLE_DEVICES"]= args.gpu_num
#     cudnn.benchmark = True
#     print('=> on CUDA')
# else:
#     print('=> on CPU')
#
# if args.pretrained == 'KITTI':
#     args.max_depth = 80.0
# elif args.pretrained == 'NYU':
#     args.max_depth = 10.0
#
# print('=> loading model..')
# Model = LDRN(args)
# if args.cuda and torch.cuda.is_available():
#     Model = Model.cuda()
# Model = torch.nn.DataParallel(Model)
# assert (args.model_dir != ''), "Expected pretrained model directory"
# Model.load_state_dict(torch.load(args.model_dir))
# Model.eval()
#
# if args.img_dir is not None:
#     if args.img_dir[-1] == '/':
#         args.img_dir = args.img_dir[:-1]
#     img_list = [args.img_dir]
#     result_filelist = ['./out_' + args.img_dir.split('/')[-1]]
# elif args.img_folder_dir is not None:
#     if args.img_folder_dir[-1] == '/':
#         args.img_folder_dir = args.img_folder_dir[:-1]
#     png_img_list = glob.glob(args.img_folder_dir + '/*.png')
#     jpg_img_list = glob.glob(args.img_folder_dir + '/*.jpg')
#     img_list = png_img_list + jpg_img_list
#     img_list = sorted(img_list)
#     result_folder = './out/1laplace_' + args.img_folder_dir.split('/')[-1]
#     if not os.path.exists(result_folder):
#         os.makedirs(result_folder)
#     result_filelist = []
#     for file in img_list:
#         result_filename = './out/1laplace_' + file.split('/')[-1]
#         result_filelist.append(result_filename)
#
# print("=> process..")
# normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#
# for i, img_file in tqdm(enumerate(img_list)):
#     img = Image.open(img_file)
#     img = np.asarray(img, dtype=np.float32)/255.0
#     if img.ndim == 2:
#         img = np.expand_dims(img,2)
#         img = np.repeat(img,3,2)
#     img = img.transpose((2, 0, 1))
#     img = torch.from_numpy(img).float()
#     img = normalize(img)
#     if args.cuda and torch.cuda.is_available():
#         img = img.cuda()
#
#     _, org_h, org_w = img.shape
#
#     # new height and width setting which can be divided by 16
#     img = img.unsqueeze(0)
#
#     if args.pretrained == 'KITTI':
#         new_h = 352
#         new_w = org_w * (352.0/org_h)
#         new_w = int((new_w//16)*16)
#         img = F.interpolate(img, (new_h, new_w), mode='bilinear')
#     elif args.pretrained == 'NYU':
#         new_h = 432
#         new_w = org_w * (432.0/org_h)
#         new_w = int((new_w//16)*16)
#         img = F.interpolate(img, (new_h, new_w), mode='bilinear')
#
#     # depth prediction
#     #with torch.no_grad():
#     #    _, out = Model(img)
#
#     img_flip = torch.flip(img,[3])
#     with torch.no_grad():
#         _, out = Model(img)
#         _, out_flip = Model(img_flip)
#         out_flip = torch.flip(out_flip,[3])
#         out = 0.5*(out + out_flip)
#
#     if new_h > org_h:
#         out = F.interpolate(out, (org_h, org_w), mode='bilinear')
#     out = out[0,0]
#
#     if args.pretrained == 'KITTI':
#         out = out[int(out.shape[0]*0.18):,:]
#         out = out*256.0
#     elif args.pretrained == 'NYU':
#         out = out*1000.0
#     out = out.cpu().detach().numpy().astype(np.uint16)
#     out = (out/out.max())*255.0
#     result_filename = result_filelist[i]
#     plt.imsave(result_filename ,np.log10(out), cmap='plasma_r')
#     if (i+1)%10 == 0:
#         print("=>",i+1,"th image is processed..")
#
# print("=> laplace_Done.")
#
#
# #===============================完成laplac,接下来是

#
pictures_path = os.listdir(in_path)
read_lap_path = "./out/1laplace_in/"
save_lap_path = "./out/2laplace_change/"
# print(pictures_path)
# print(img_shape)
for i,lap_pic_path in tqdm(enumerate(pictures_path)):

    readpath =read_lap_path+lap_pic_path
    savepath = save_lap_path+lap_pic_path
    # print(readpath)

    img = cv2.imread(readpath)
    #img = cv2.resize(img, (1640, 470))

    img = cv2.resize(img, (img_shape[1], img_shape[0]-120))  #高度-减去120
    cv2.imwrite(savepath, img)

#裁剪完laplace的图片了   放在了  /out/2laplace_change/文件夹中



# #===============================完成laplac的剪切,接下来是对照片的

# --source
# ./in/
# --weights
# ./yolo/weights/yolov5s.pt
# --conf
# 0.45

parser1 = argparse.ArgumentParser()
parser1.add_argument('--weights', nargs='+', type=str, default='./yolov5s.pt', help='model.pt path(s)')
parser1.add_argument('--source', type=str, default='./in/', help='source')  # file/folder, 0 for webcam
parser1.add_argument('--output', type=str, default='out/3yolo_distance', help='output folder')  # output folder
parser1.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
parser1.add_argument('--conf-thres', type=float, default=0.45, help='object confidence threshold')
parser1.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
parser1.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser1.add_argument('--view-img', action='store_true', help='display results')
parser1.add_argument('--save-txt', action='store_true', help='save results to *.txt')
parser1.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
parser1.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
parser1.add_argument('--augment', action='store_true', help='augmented inference')
parser1.add_argument('--update', action='store_true', help='update all models')
opt = parser1.parse_args()


with torch.no_grad():

        detect(opt)






