import cv2             
import mediapipe as mp
import pyautogui
import time

def count_fingers(lst): # lst will store value of hand_keyPoints
    cnt = 0

    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2   # X and Y values are normalized between 0-1 hence we will multiply by 100 to scale them up  

    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
        cnt += 1

    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
        cnt += 1

    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
        cnt += 1

    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
        cnt += 1

    # Thumb will be raised in X axis | Here we will use a more manual approach by using 6

    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
        cnt += 1


    return cnt 

cap = cv2.VideoCapture(0)           # read frames from 0th webcam



# defining Variables
drawing = mp.solutions.drawing_utils     # to draw keypoints on frame
hands = mp.solutions.hands               # to detect hands
hand_obj = hands.Hands(max_num_hands=1)  # detected hand is stored in hand_obj


start_init = False 

prev = -1

while True:
    end_time = time.time()
    _, frm = cap.read()                     # reading frames and storing them in frm
    frm = cv2.flip(frm, 1)                  # flip camera


    # passing frm in hand_obj but in RGB format
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    # res can be null also incase no hands are detected

    if res.multi_hand_landmarks:    #means if hands are detected : it will return LIST of detected hands

        hand_keyPoints = res.multi_hand_landmarks[0]   # we will detect only 1 hand Fisrt element of LIST

        cnt = count_fingers(hand_keyPoints)

        if not(prev==cnt):
            if not(start_init):
                start_time = time.time()
                start_init = True

            elif (end_time-start_time) > 0.2: # we will give 0.2 seconds to user to raise fingers
                if (cnt == 1):
                    pyautogui.press("right")
                
                elif (cnt == 2):
                    pyautogui.press("left")

                elif (cnt == 3):
                    pyautogui.press("up")

                elif (cnt == 4):
                    pyautogui.press("down")

                elif (cnt == 5):
                    pyautogui.press("space")

                prev = cnt
                start_init = False   # reset time


        


        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)    # connecting dots by drawing the landmarks on detected hands 

    cv2.imshow("window", frm)           # show frames to user


    
    # if user presses the ESC key for 1 millisecond
    if cv2.waitKey(10) == 27:
        cv2.destroyAllWindows()         # close camera window
        cap.release()                   # release camera
        break                           # break this while Loop