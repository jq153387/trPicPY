from PIL import Image
import os

# 源目錄和目標目錄
source_directory = "./your_source_directory"
output_directory = "./new_cover"

# 確保目標目錄存在，如果不存在則創建
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 獲取源目錄下所有文件
file_list = os.listdir(source_directory)

# 循環處理每個文件
for filename in file_list:
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):  # 僅處理圖片文件
        input_path = os.path.join(source_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # 打開圖像
        img = Image.open(input_path)

        # 計算縮放比例
        target_width = 1920
        target_height = 1230
        scale = max(target_width / img.width, target_height / img.height)

        # 計算新的寬度和高度
        new_width = int(img.width * scale)
        new_height = int(img.height * scale)

        # 調整圖像大小
        img_resized = img.resize((new_width, new_height))

        # 創建新的圖像並居中
        new_img = Image.new("RGB", (target_width, target_height), "white")
        offset = ((target_width - img_resized.width) // 2, (target_height - img_resized.height) // 2)
        new_img.paste(img_resized, offset)

        # 裁剪超出畫布的部分
        new_img = new_img.crop((0, 0, target_width, target_height))

        # 保存圖像
        new_img.save(output_path)

        print(f"處理完成: {filename}")

print("所有圖片處理完成。")