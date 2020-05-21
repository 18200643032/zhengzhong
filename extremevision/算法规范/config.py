class Config_file():
    """docstring for ClassName"""
    config = {
        "gpu_id":{"gpu_id":1},
        "draw_roi_draw_res":{"draw_roi_area":True,"draw_result":True},
        "draw_roi_not_res_path":{"draw_roi_area":True,"draw_result":False},
        "draw_not_roi_draw_res":{"draw_roi_area":False,"draw_result":True},
        "draw_not":{"draw_roi_area":False,"draw_result":False},
        "words_true":{"draw_warning_text":True},
        "words_false":{"draw_warning_text":False},
        "roi_save_true":{"roi":["POLYGON((0.706060606060606 0.6175,0.703030303030303 0.9825,0.9878787878787879 0.99,0.9878787878787879 0.6025))"]}, #右下方正方形
        "roi_save_polygon":{"roi":["POLYGON((0.3515151515151515 0.0675,0.05454545454545454 0.4925,0.24545454545454545 0.93,0.8909090909090909 0.93,0.9181818181818182 0.4125))"]},#多变形
        "roi_save_null":{"roi":[""]} #传入空
}
    # #初始化配置参数复制
    # config_file_path = '/zhengzhong/config/'
    # #默认配置文件
    algo_config_primay_json = {
        "gpu_id": 0,
        "draw_roi_area": True,
        "roi_color": [255, 255, 0, 0.4],
        "roi": ["POLYGON((0 0,0 1,1 1,1 0))"],
        "roi_line_thickness": 3,
        "roi_fill": False,
        "draw_result": True,
        "draw_confidence": True,
        "thresh": 0.5,
    }