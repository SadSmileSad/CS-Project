import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.75, min_tracking_confidence=0.5)

def process_frame(f):
    frame = cv2.flip(f, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Change BGR to RGB for proper processing

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks: 
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    return frame


cap = cv2.VideoCapture(0)

cap.open(0)

while cap.isOpened():
    if cv2.waitKey(1) == 27:  
        break

    success, frame = cap.read()
    if not success:
        print("Not success")
        break

    frame = process_frame(frame)

    cv2.imshow("my window", frame)

cap.release()
cv2.destroyAllWindows()