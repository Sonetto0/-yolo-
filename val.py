from ultralytics import YOLO


if __name__ == '__main__':
    # Load a model
    # model = YOLO("yolov8n.pt")  # load an official model
    model = YOLO(r"D:\shixun\sss\model\che_v1.pt")  # load a custom model

    # Validate the model
    metrics = model.val()  # no arguments needed, dataset and settings remembered
    print('map50:', metrics.box.map50)
    print('map75:', metrics.box.map75)
    print('map50-95:', metrics.box.map)

    # Validate the model with different confidence thresholds
    # for conf_threshold in [0.1, 0.25, 0.5, 0.75]:
    #     metrics = model.val(conf=conf_threshold)
    #     print(f"Confidence Threshold: {conf_threshold}")
    #     print(f"Precision: {metrics.box.mp}")
    #     print(f"Recall: {metrics.box.mr}")


    # total_fps = 0.0
    # num = 10
    # for _ in range(num):
    #     # 这里假设model.val()返回一个metrics对象，其中包含了fps信息
    #     metrics = model.val()
    #     fps = metrics.get_latency()
    #     total_fps += fps
    # # 计算平均fps
    # average_fps = 1000 / total_fps * num
    # # 打印结果
    # print(f'Average FPS over {num} runs: {average_fps:.2f}')