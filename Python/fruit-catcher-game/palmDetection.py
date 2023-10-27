import cv2
import mediapipe as mp


def is_palm_closed(hand_landmarks):
    thumb = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]

    thumb_to_index_dist = abs(thumb.x - index_finger.x) + abs(thumb.y - index_finger.y)
    thumb_to_middle_dist = abs(thumb.x - middle_finger.x) + abs(thumb.y - middle_finger.y)
    thumb_to_ring_dist = abs(thumb.x - ring_finger.x) + abs(thumb.y - ring_finger.y)
    thumb_to_pinky_dist = abs(thumb.x - pinky_finger.x) + abs(thumb.y - pinky_finger.y)

    threshold = 0.1
    if (
        thumb_to_index_dist < threshold and
        thumb_to_middle_dist < threshold and
        thumb_to_ring_dist < threshold and
        thumb_to_pinky_dist < threshold
    ):
        return True
    else:
        return False
    
def player_position(x,y):
    return [int(x*1280),int(y*720)]


mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            is_closed = is_palm_closed(hand_landmarks)

            x = min(lm.x for lm in hand_landmarks.landmark)
            y = min(lm.y for lm in hand_landmarks.landmark)
            w = max(lm.x for lm in hand_landmarks.landmark) - x
            h = max(lm.y for lm in hand_landmarks.landmark) - y

            cv2.rectangle(image, (int(x * image.shape[1]), int(y * image.shape[0])),
                          (int((x + w) * image.shape[1]), int((y + h) * image.shape[0])),
                          (0, 255, 0), 2)
            cv2.putText(image, "Palm Closed: {}".format(is_closed), (int(x * image.shape[1]), int(y * image.shape[0]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
