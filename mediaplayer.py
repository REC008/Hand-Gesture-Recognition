import cv2 
import mediapipe as mp
import pyautogui
import time

def count_fingers(lst):
    finger_count = 0  # Renamed cnt to finger_count

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        finger_count += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        finger_count += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        finger_count += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        finger_count += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        finger_count += 1

    return finger_count

cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

start_init = False
prev = -1
start_time = 0  # Initialize start_time

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]
        cnt = count_fingers(hand_keyPoints)

        if prev != cnt:  # Updated condition
            if not start_init:
                start_time = time.time()
                start_init = True
            elif (end_time - start_time) > 0.2:
                if cnt == 1:
                    pyautogui.press("right")
                elif cnt == 2:
                    pyautogui.press("left")
                elif cnt == 3:
                    pyautogui.press("up")
                elif cnt == 4:
                    pyautogui.press("down")
                elif cnt == 5:
                    pyautogui.press("space")

                prev = cnt
                start_init = False

        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:  # Press Esc to exit
        cv2.destroyAllWindows()
        cap.release()
        break
