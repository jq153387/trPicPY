# 圖片批量處理腳本

這個 Python 腳本用於將指定目錄中的圖片文件進行批量處理。每個圖片都會按照指定的目標大小進行縮放、居中和裁剪，然後保存到新的目錄中。

## 使用方法

安裝 Pillow 庫（如果未安裝）：

```bash
pip install Pillow
```

修改腳本中的源目錄和目標目錄：

```   
source_directory = "./your_source_directory"
output_directory = "./new_cover"
```

在終端中運行腳本：

```
python your_script.py

```

## 注意事項

- 本腳本僅處理指定目錄中的圖片文件（.jpg、.jpeg、.png、.gif、.webp）。
- 建議備份源目錄中的圖片，以免因處理而造成損失。
- 處理後的圖片將保存在新的目標目錄中。
  
腳本運行後，你將看到處理完成的提示信息。



# Image Batch Processing Script

This Python script is designed to batch process image files in a specified directory. Each image will be resized, centered, and cropped to the specified target dimensions, then saved to a new directory.

## Usage

Install the Pillow library (if not already installed):

```bash
pip install Pillow
```

Modify the script with your source and output directories:

```
source_directory = "./your_source_directory"
output_directory = "./new_cover"
```

Run the script in the terminal:

```
python your_script.py
```

## Notes

- This script only processes image files (.jpg, .jpeg, .png, .gif, .webp) in the specified directory.
- It is recommended to back up images in the source directory to avoid potential loss during processing.
- Processed images will be saved in the new output directory.

After running the script, you will see completion messages in the terminal.



