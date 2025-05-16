from ultralytics import YOLO


def main():
    """
    model = YOLO("yolov8l.yaml")

    model.train(data="config.yaml", epochs=100, patience=10, cache=True, save=True, save_period=1, device=0, cos_lr=True)
    """

    class_dictionary = {
        0: 'sun',
        1: 'football',
        2: 'sports_ball',
        3: 'bird',
        4: 'cloud',
        5: 'pet',
        6: 'butterfly',
        7: 'flower',
        8: 'stickman',
        9: 'house',
        10: 'person',
        11: 'door',
        12: 'window',
        13: 'tree',
        14: 'vehicle',
        15: 'fish',
        16: 'star',
        17: 'heart'
    }

    model = YOLO('cdp_best.pt')

    #model.val(data='config.yaml', save_json=True, save_txt=True)

    result = model.predict(source=r"C:\\Users\\Petar\\Desktop\\cdp\\data\\data\\images\\val\\61.jpg", save=True)

    for i, box in enumerate(result[0].boxes):
        print(f"Detected class #{i}: {class_dictionary[int(box.cls)]}\nxywhn: {box.xywhn}")

if __name__ == '__main__':
    main()
