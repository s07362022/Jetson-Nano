import pyrealsense2 as rs
import numpy as np
import cv2
import time
from datetime import datetime
import pandas as pd 
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

pipeline.start(config)
 
align_to = rs.stream.color
align = rs.align(align_to)
#yolo
CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("F:\\program1\\yolov4\\darknet-master\\build\\darknet\\x64\\data\\coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
net = cv2.dnn.readNet("F:\\program1\\Jetson\\yolov4.weights", "F:\\program1\\yolov4\\darknet-master\\build\\darknet\\x64\\cfg\\yolov4.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)
counts = 0

try:
    while cv2.waitKey(1) < 1:
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)   
        depth_frame = aligned_frames.get_depth_frame() 
        color_frame = aligned_frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        #print(type(color_image))<class 'numpy.ndarray'>
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        frame=color_image
        height, width, channels = color_image.shape 
        start = time.time()
        classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        end = time.time()

        start_drawing = time.time()
        for (classid, score, box) in zip(classes, scores, boxes):
            color = COLORS[int(classid) % len(COLORS)]
            label = "%s : %f" % (class_names[classid[0]], score)
            #cv2.rectangle(frame, box, color, 2)
            x,y,w,h = box[0],box[1],box[2],box[3]
            cv2.rectangle(frame, (x,y), (x+w,y+h), color, 1)
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            text_depth = "depth is "+str(np.round(depth_frame.get_distance(int(x+(1/2)*w), int(y+(1/2)*h)),3))+"m"
            frame=cv2.putText(frame,text_depth,(x,y-30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2,cv2.LINE_AA)

            # 輸入檔案寫在這裡, x= 寬框中心,y=長寬中心,w=寬度,h=長度
            # label = class 物件名稱
            # depth_len = 距離 深度

            # txt版本
            # f = open('./txt_file/%s.txt'%(counts),'w') #
            # f.write("%s %s %s %s %s"%(label, x , y, w, h))
            # f.close()
            # print("save label class")
            result  = list()
            depth_len =np.round(depth_frame.get_distance(int(x+(1/2)*w), int(y+(1/2)*h)),3)
            counts +=1
            if depth_len<=5:    
                location = ''
                if (x <= width // 3 * 1):
                    location ='left'
                elif x >= width // 3 * 2:
                    location = 'right'
                else:
                    location = 'middle'  

                result.append([counts,location,datetime.now()])

                if counts % 10 == 0:
                    df = pd.DataFrame(result,columns=['index','location','updatetime']).to_csv('backup.csv',encoding='cp950') #csv檔案
                
                if len(result) >= 1800:
                    result = list()


        end_drawing = time.time()
        images = np.hstack((frame, depth_colormap))
        
        fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
        cv2.putText(frame, fps_label, (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)


        key = cv2.waitKey(1)
        
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
 
except:
    pass


        
 
 
finally:
    pipeline.stop()
