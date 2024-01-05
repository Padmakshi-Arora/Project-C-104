import cv2

img = []

cv2.imread("solar-system.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (30,310),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,0)
            )

cv2.putText(img,
            "Venus",
            (40,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,255)
            )

cv2.putText(img,
            "Earth",
            (50,330),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,255)
            )

cv2.putText(img,
            "Mars",
            (60,340),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (70,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,0)
            )

cv2.putText(img,
            "Saturn",
            (80,360),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,255)
            )

cv2.putText(img,
            "Uranus",
            (90,370),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,255)
            )

cv2.putText(img,
            "Neptune",
            (100,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imwrite("Solar_systemwithname.jpg", img)
