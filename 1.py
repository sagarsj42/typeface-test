def bounding_boxes(file_name):
    img = cv2.imread(file_name)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bb = list()
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w == 1 and h == 1:
            continue
        bb.append([x, y, w, h])
    
    return bb

