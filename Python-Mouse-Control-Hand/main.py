import mediapipe as mp
import cv2
import win32api
import pyautogui
 
print("Stating Mouse control program using hand\nPress 'q' to exit program")

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click = 0

Is_hand_first_time_in = True
distance_x, distance_y = 0, 0

video = cv2.VideoCapture(0)
 
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands: 
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageHeight, imageWidth, _ = image.shape
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
 
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark: 
                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        
                    point = str(point)
     
                    if point == 'HandLandmark.INDEX_FINGER_TIP':
                        # if hand in first time then get distance
                        try:
                            if(Is_hand_first_time_in):
                                mx, my = win32api.GetCursorPos()  # mouse
                                hx, hy = pixelCoordinatesLandmark[0], pixelCoordinatesLandmark[1]  # hand
                                
                                distance_x = mx - hx
                                distance_y = my - hy
                                                                
                            Is_hand_first_time_in = False
                        except:
                            pass
                        
                        try:
                            indexTip_x = int(pixelCoordinatesLandmark[0] + distance_x)
                            indexTip_y = int(pixelCoordinatesLandmark[1] + distance_y)
                            
                            win32api.SetCursorPos((indexTip_x, indexTip_y))
                            
                            # multiple by 4,5 to increase speed, if u want
                            # win32api.SetCursorPos((indexTip_x*4,indexTip_y*5))
                        except:
                            pass
     
                    elif point == 'HandLandmark.THUMB_TIP':
                        try:
                            thumbTip_x = pixelCoordinatesLandmark[0] + distance_x
                            thumbTip_y = pixelCoordinatesLandmark[1] + distance_y
                        except:
                            pass                        
     
                    try:
                        # pyautogui.moveTo(indexTip_x,indexTip_y)
                        Distance_x = indexTip_x - thumbTip_x  # x = (x1 - x2)
                        Distance_y = indexTip_y - thumbTip_y  # y = (y1 - y2)
                        
                        
                        #CLick issue due to distance paramer in Index_tip
                        
                        # if thumb & index tip (x,y) distance < 10 then click
                        if abs(Distance_x) < 10 and abs(Distance_y) < 10:
                            click += 1
                            if(click % 5) == 0:  # to avoid multi click, click after 5
                                print("single click")
                                pyautogui.click()                            
                    except:
                        pass
        else:
            Is_hand_first_time_in = True
        
        cv2.namedWindow('Hand Tracking', cv2.WINDOW_NORMAL)
        cv2.imshow('Hand Tracking', image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            # press 'q' to exit program

video.release()
