## Cleaned-Webvid
Use strategy to achieve cleaned webvid-10m dataset for video generation modeling. 

1. Get watermark with blackground.

![black](https://github.com/feizc/Cleaned-Webvid/assets/37614046/5e3cbe2f-cdea-45b6-9737-ba4e032c1fe6) 

2. Expand the area using erosion and dilation algorithms.

![black_binary](https://github.com/feizc/Cleaned-Webvid/assets/37614046/ee529021-6608-48e8-8e24-b8cddec97a4b) 

3. Inpainting image with OpenCV.

![image](https://github.com/feizc/Cleaned-Webvid/assets/37614046/f4c562c7-969c-4e50-a9ab-cc721fe03aa3)
![dst](https://github.com/feizc/Cleaned-Webvid/assets/37614046/8b14a5db-2a67-420d-90ec-23c2e3fa0c6b)

Repeat the watermark removing for each frame in video. 

