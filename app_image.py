


### 서브 함수 있는 곳

# app8.py와 연결
# 메뉴별로 분리해서 파일 만들기


# ------------------------------------------
import streamlit as st
from datetime import datetime
from app_utils import save_uploaded_file
# -------------------------------------------




def run_app_image() :
        # st.title('이미지 대시보드') -> 타이틀도 바꿀 수 있음. 대신 위에있는 타이틀 지워야함.
        st.subheader('이미지 파일 업로드')

        img_file = st.file_uploader('이미지를 업로드 하세요', type = ['png', 'jpg', 'jpeg'])
        # 파일을 업로드 받아서
        if img_file is not None: # 이미지파일에 아무것도 없지 않을때
            # print(type(img_file))
            # print(img_file.name) # 유저가 올린 파일의 파일명
            # print(img_file.size) # 파일 사이즈
            # print(img_file.type) # 파일 타입



        ## 그런데 여기서 유저가 올린 파일은 중복이름이 있을수 있음
        ## 유저가 올린 파일을
        ## 서버에서 유니크하게(중복되지않게) 처리하기 위해서
        ## 파일명을 현재시간 조합으로 해서 만든다.   
         
        # 현재 시간 알아내기(서버시간임)
            current_time = datetime.now() 
            # print(current_time) # 컴퓨터용 시간
            # print(current_time.isoformat()) # 사람용 시간으로 보여달라

            # 파일명에 ': '은 들어갈 수 없음.
            # ':' 을 '_' 로 바꾸기
            # print(current_time.isoformat().replace(':', '_'))

            # 파일 명 만들기
            # print(current_time.isoformat().replace(':', '_') + '.jpg')

            # 이제 변수에 집어넣기
            filename = current_time.isoformat().replace(':', '_') + '.jpg'

            # '저장하기' 함수 (서버에 저장하기 위한 함수) -->> 맨 위로 돌아가기
            # filename을 img_file의 네임으로 덮어써라
            img_file.name = filename 

            # 위에서 정의한 저장하기 함수를 불러와서 파라미터 적용하기
            save_uploaded_file('image', img_file)




            ### 업로드한 파일 유저에게 보여주기
            # 이미지 파일 업로드 하라는 코드 밑에다가 써야함 -->> 주의
            st.image('image/' + filename) # 파일이름 되게 김. 파일이름변수 사용하면 간편

