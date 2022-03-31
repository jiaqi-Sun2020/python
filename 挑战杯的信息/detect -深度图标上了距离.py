import argparse
import os
import shutil
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords,
    xyxy2xywh, plot_one_box, strip_optimizer, set_logging)
from utils.torch_utils import select_device, load_classifier, time_synchronized

#===========================================================================
import numpy as np

def xyxy2numpy(xyxy):
    list_ = []
    for n in xyxy:
        n = n.cpu().numpy()
        list_.append(n)
    return list_

K = 8/(1.01**104)  #指数为1.2防止过大造成溢出  (默认为255-151的灰度值为800毫米)
def get_min_distance(xyxy,img):
    xyxy = xyxy2numpy(xyxy)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    h = int(xyxy[3])-int(xyxy[1])  #y2-y1
    w = int(xyxy[2])-int(xyxy[0])  #x2-x1
    distance =0
    #print(xyxy)
    roi = img[int(xyxy[1]+h/4):int(xyxy[3]-h/4),int(xyxy[0]+w/4):int(xyxy[2]-w/4)]
    max_ = np.max(roi)
    # print(roi.shape)
    # print(max_)
    # if(max_>200):
    #     y=999
    # else:
    if True:
        y = K * (1.01 ** (255 - max_))
    # print(y)
    # print(20*"=======")
    return y+distance
base_path = "laplace_change_size"+"/"
def get_lap_img(path):
    lap_path = base_path + path.split("\\")[-1]
    img = cv2.imread(lap_path)   #读取laplace的照片
    #print(lap_path,img.shape)    #1640,470的照片我应该在获取的yolo框中   y坐标加120
    return img


#===========================================================================




def detect(save_img=False):
    out, source, weights, view_img, save_txt, imgsz = \
        opt.output, opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size
    webcam = source.isnumeric() or source.startswith(('rtsp://', 'rtmp://', 'http://')) or source.endswith('.txt')

    # Initialize
    set_logging()
    device = select_device(opt.device)
    if os.path.exists(out):
        shutil.rmtree(out)  # delete output folder
    os.makedirs(out)  # make new output folder
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model'])  # load weights
        modelc.to(device).eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    if webcam:
        view_img = True
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz)
    else:
        save_img = True
        dataset = LoadImages(source, img_size=imgsz)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

    # Run inference
    t0 = time.time()
    img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
    _ = model(img.half() if half else img) if device.type != 'cpu' else None  # run once
    for path, img, im0s, vid_cap in dataset:
        # ===========================================================================
        # ===========================================================================

        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=opt.augment)[0]

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t2 = time_synchronized()

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
            else:
                p, s, im0 = path, '', im0s

            save_path = str(Path(out) / Path(p).name)
            txt_path = str(Path(out) / Path(p).stem) + ('_%g' % dataset.frame if dataset.mode == 'video' else '')
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if det is not None and len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += '%g %ss, ' % (n, names[int(c)])  # add to string

                # Write results
                # ==============================
                # im0 = cv2.imread(r"lap_change.png")
                im0 = get_lap_img(path)
                # ==============================
                for *xyxy, conf, cls in reversed(det):
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * 5 + '\n') % (cls, *xywh))  # label format

                    if save_img or view_img:  # Add bbox to image
                        # label = '%s %.2f' % (names[int(cls)], conf)             #此处是更改标签名称的
                        # plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)

                        #================================================
                        xyxy[1] = xyxy[1]-120
                        xyxy[3] = xyxy[3]-120
                        if 1200<xyxy[0]<1210 and 70<xyxy[1]<80 and 1404<xyxy[2]<1414 and 201<xyxy[3]<211:     #[1205, 75, 1409, 206]
                             continue

                        if names[int(cls)]=="kites":
                            continue

                        if xyxy[3]<0 or xyxy[1]<0 :
                            # xyxy[1] = xyxy[1] +120
                            # xyxy[3] = xyxy[3] + 120
                            continue


                        distance =get_min_distance(xyxy,im0)
                        #print(distance)
                        label = '%s %.2f m' % (names[int(cls)], distance)  # 此处是更改标签名称的
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)
                        # if True:
                        #     label = '%s %.2f' % (names[int(cls)], conf)             #此处是更改标签名称的
                        #     #label = 'people %.2f' % (conf)
                        #     xyxy[1]= xyxy[1] -120
                        #     xyxy[3] = xyxy[3] -100
                        #     print(20*"=")
                        #     print(xyxy)
                        #     print(20 * "=")
                        #     #plot_one_box(xyxy, img, label=label, color=colors[int(cls)], line_thickness=3)
                        #     plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)
                        # ================================================



            # Print time (inference + NMS)
            print('%sDone. (%.3fs)' % (s, t2 - t1))

            # Stream results
            if view_img:
                cv2.imshow(p, im0)
                if cv2.waitKey(1) == ord('q'):  # q to quit
                    raise StopIteration

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'images':
                    cv2.imwrite(save_path, im0)
                else:
                    if vid_path != save_path:  # new video
                        vid_path = save_path
                        if isinstance(vid_writer, cv2.VideoWriter):
                            vid_writer.release()  # release previous video writer

                        fourcc = 'mp4v'  # output video codec
                        fps = vid_cap.get(cv2.CAP_PROP_FPS)
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))
                    vid_writer.write(im0)

    if save_txt or save_img:
        print('Results saved to %s' % Path(out))

    print('Done. (%.3fs)' % (time.time() - t0))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov5s.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.4, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    opt = parser.parse_args()
    print(opt)

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                detect()
                strip_optimizer(opt.weights)
        else:
            detect()
