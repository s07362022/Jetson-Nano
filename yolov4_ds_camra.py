import cv2
import time

CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("E:\\workspace\\project_\\yolo_data\\name.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

#vc = cv2.VideoCapture("E:\\workspace\\project_\\yolo_data\\K94A0001_new.mp4")
cap = cv2.VideoCapture(0)

net = cv2.dnn.readNet("E:\\workspace\\project_\\yolo_data\\yolov4-tiny-3l_best.weights", "E:\\workspace\\project_\\yolo_data\\yolov4-tiny-3l.cfg")
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

## smoke process
from level_3 import tem, convert_temp,mask_img,leavel
def cut_img(image, classes, confs, boxes):
    cut_img_list = []
    for (classid, conf, box) in zip(classes, confs, boxes):
        x, y, w, h = box
        if x - 20 < 0:
            x = 21
        if y - 20 < 0:
            y = 21
        #cut_img = image[y - 30:y + h + 30, x - 18:x + w + 25]
        cut_img = image[y - 20: y + h + 30, x - 10: x + w + 10]
        cut_img_list.append(cut_img)
    return cut_img_list[0]

kelvin_table = {
    1000: (255,56,0),
    1500: (255,109,0),
    2000: (255,137,18),
    2500: (255,161,72),
    3000: (255,180,107),
    3500: (255,196,137),
    4000: (255,209,163),
    4500: (255,219,186),
    5000: (255,228,206),
    5500: (255,236,224),
    6000: (255,243,239),
    6500: (255,249,253),
    7000: (245,243,255),
    7500: (235,238,255),
    8000: (227,233,255),
    8500: (220,229,255),
    9000: (214,225,255),
    9500: (208,222,255),
    10000: (204,219,255)}
leavel_list = []
font = cv2.FONT_HERSHEY_PLAIN
smoke_count = 0
## smoke process

while (True):
    ret, frame = cap.read()
    #(grabbed, frame) = vc.read()
    if not ret:
        exit()

    start = time.time()
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    end = time.time()

    # start_drawing = time.time()
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid[0]], score)
        # smoke process
        if classes[0][0] == 0:
            cut = cut_img(frame, classes, scores, boxes)
            smoke_count +=1
            if smoke_count % 10 ==0:
                smoke_img = cv2.resize(cut,(400,400))
                mask = tem(smoke_img)
                
                ori,black  = mask_img(mask,smoke_img)
                cv2.imshow("ori",mask)
                global smoke_level_re
                smoke_level_re = leavel(black,ori)
                leavel_list.append(smoke_level_re)
                print("判斷黑煙等級: {} ".format(smoke_level_re))
                smoke_level_str="Detected Smoke Leveal: "+str(smoke_level_re)
                
                    
                
    
        #cv2.imshow("black",ori)    
        try:
            cv2.putText(frame,smoke_level_str,(50, 50 -5), font, 2, [0,25,220], 1)
        except:
            pass
        # smoke process
        #cv2.rectangle(frame, box, color, 2)
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(frame, (x,y), (x+w,y+h), color, 1)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    # end_drawing = time.time()
    
    #fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
    #cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    try:
        cv2.imshow("smoke", cut)
    except:
        pass
    cv2.imshow("detections", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
