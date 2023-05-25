

import streamlit as st

# 사진 영상 처리하는 라이브러리 불러오기
from PIL import Image


def main():
    st.title('내 앱 대시보드')



    ### 사진과 영상을 보여주기

    ## 사진(이미지)
    img = Image.open('data/image_03.jpg')
    # print(img)
    
    st.image(img)
    # 화면에 꽉차게 그림을 보여주고싶을때
    st.image( img , use_column_width= True)

    # 이미지 URL로 불러와서 보여주기(인터넷에서 이미지 주소 복사해오기)
    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')


    ## 영상
    # 'rb' : 모드. 읽기모드여서 r (쓰기모드는 w) / 동영상은 타입이 바이널이어서 b
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)




if __name__ == '__main__':
    main()