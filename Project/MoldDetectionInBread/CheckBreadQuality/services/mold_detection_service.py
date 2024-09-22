import cv2
import numpy as np
import os

from common.utils import EXPORT_FOLDER
from models.view_model import ViewModel

class MoldDetectionService():
    def __init__(self):
        pass

    def return_view(self, filename, moldDetectionResult):
        view = ViewModel()
        view.link_preview_hsv_img = 'static/export/%s' % ('hsv_img' + filename)
        view.link_preview_img_with_outline_rgb = 'static/export/%s' % ('img_with_outline_rgb' + filename)
        view.link_preview_result_combined_rgb = 'static/export/%s' % ('result_combined_rgb' + filename)
        view.link_preview_img_with_mold_rgb = 'static/export/%s' % ('img_with_mold_rgb' + filename)
        view.mold_detection_result = moldDetectionResult

        return view

    def detect(self, filename, imgpath):
        # Đọc ảnh và thay đổi kích thước
        img = cv2.imread(imgpath)

        img_resized = cv2.resize(img, (300, 300))

        # Chuyển đổi sang không gian màu HSV
        hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)

        # Định nghĩa khoảng màu cho vàng óng hoặc cam vàng (bánh mì)
        lower_yellow_orange = np.array([15, 50, 50])  # Điều chỉnh ngưỡng để bao gồm cả màu vàng nhạt
        upper_yellow_orange = np.array([35, 255, 255])

        # Định nghĩa khoảng màu cho mốc
        lower_mold = np.array([30, 40, 40])
        upper_mold = np.array([90, 255, 255])

        # Tạo mặt nạ cho màu bánh mì
        mask_bread = cv2.inRange(hsv, lower_yellow_orange, upper_yellow_orange)

        # Tạo mặt nạ cho mốc
        mask_mold = cv2.inRange(hsv, lower_mold, upper_mold)

        # Áp dụng mask lên ảnh gốc để thấy rõ các vùng bánh mì
        result_bread = cv2.bitwise_and(img_resized, img_resized, mask=mask_bread)

        # Tìm các contours từ mask bánh mì
        contours_bread, _ = cv2.findContours(mask_bread, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Tạo một bản sao của ảnh gốc để vẽ outline bánh mì
        img_with_outline = img_resized.copy()
        for contour in contours_bread:
            if cv2.contourArea(contour) > 1000:  # Chỉ vẽ các contour có diện tích lớn hơn 1000
                cv2.drawContours(img_with_outline, [contour], -1, (0, 255, 0), 2)

        # Tạo mask cho vùng bên trong outline bánh mì
        bread_mask = np.zeros_like(mask_bread)
        cv2.drawContours(bread_mask, [contour for contour in contours_bread if cv2.contourArea(contour) > 1000], -1, 255, thickness=cv2.FILLED)

        # Kết hợp các mặt nạ để chỉ phát hiện mốc bên trong vùng màu bánh mì
        combined_mask = cv2.bitwise_and(bread_mask, mask_mold)

        # Áp dụng mask lên ảnh gốc để thấy rõ các vùng bị mốc
        result_combined = cv2.bitwise_and(img_resized, img_resized, mask=combined_mask)

        # Tìm các contours từ mask kết hợp
        contours_mold, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Tạo một bản sao của ảnh gốc để vẽ các vùng mốc
        img_with_mold = img_resized.copy()

        # Vẽ các contour của mốc trên ảnh gốc
        moldDetectionResult = ''
        if len(contours_mold) > 15:
            moldDetectionResult = "Moldy bread"
            for contour in contours_mold:
                if cv2.contourArea(contour) > 0:
                    # Vẽ contour bao quanh vùng mốc
                    cv2.drawContours(img_with_mold, [contour], -1, (0, 0, 255), 2)
        else:
            moldDetectionResult = "Bread is not moldy"

        # Chuyển đổi ảnh từ BGR sang RGB cho matplotlib
        img_resized_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        img_with_outline_rgb = cv2.cvtColor(img_with_outline, cv2.COLOR_BGR2RGB)
        result_combined_rgb = cv2.cvtColor(result_combined, cv2.COLOR_BGR2RGB)
        img_with_mold_rgb = cv2.cvtColor(img_with_mold, cv2.COLOR_BGR2RGB)
                    
        export_path = os.path.join(EXPORT_FOLDER, 'hsv_img' + filename)
        cv2.imwrite(export_path, hsv)

        # img_with_outline_rgb = cv2.cvtColor(img_with_outline, cv2.COLOR_BGR2RGB)
        img_with_outline_rgb = img_with_outline
        export_path = os.path.join(EXPORT_FOLDER, 'img_with_outline_rgb' + filename)
        cv2.imwrite(export_path, img_with_outline_rgb)

        # result_combined_rgb = cv2.cvtColor(result_combined, cv2.COLOR_BGR2RGB)
        result_combined_rgb = result_combined
        export_path = os.path.join(EXPORT_FOLDER, 'result_combined_rgb' + filename)
        cv2.imwrite(export_path, result_combined_rgb)

        # img_with_mold_rgb = cv2.cvtColor(img_with_mold, cv2.COLOR_BGR2RGB)
        img_with_mold_rgb = img_with_mold
        export_path = os.path.join(EXPORT_FOLDER, 'img_with_mold_rgb' + filename)
        cv2.imwrite(export_path, img_with_mold_rgb)

        return self.return_view(filename, moldDetectionResult)