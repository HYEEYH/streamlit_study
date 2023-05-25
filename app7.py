

import streamlit as st
from datetime import datetime
import os
import pandas as pd



### 서버에 저장하기 함수--------------------------------------
# 디렉토리 이름과, 파일을 주면
# 해당 디렉토리에 파일을 저장해 주는 함수
def save_uploaded_file(directory, file) :
    # 1. 저장할 디렉토리가 있는지 확인하고
    # 2. 없으면 디렉토리(폴더)를 먼저 만든다.

    # 디렉토리가 있는지 확인하는 코드
    if not os.path.exists(directory) :  # 이 디렉토리가 없다면
        os.makedirs(directory)
    # 3. 디렉토리가 있으니, 파일 저장하기
    # file.name -> 밑에 변수로 지정되어 있음
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success('파일 저장 완료') #스트림릿에 띄워라

# ------------------------------------------------------------



def main():
    st.title('내 앱 대시보드')
    


    ### 누르면 왼쪽에 메뉴 나오게 하기
    menu = ['이미지업로드', 'csv업로드', 'About']
    # ('메뉴'-> 유저에게 보여지는거, menu -> 여기서 가져와라)
    # st.sidebar.selectbox('메뉴', menu)  # 화면에 보여주기만 하는것


    ## 선택한 메뉴 페이지로 이동하기
    choice = st.sidebar.selectbox('메뉴', menu)
    # print(choice)
    # if choice == '이미지업로드': # 라고 해도 되지만 메뉴 이름 자동변환위해
    
    if choice == menu[0] :
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


            



    elif choice == menu[1] :  # ------------------------------------
        st.subheader('CSV 파일 업로드')

        ### CSV 파일 업로드하기
        # 업로드 확장자 제한하기 : type = ['csv', 'tsv',...]
        csv_file = st.file_uploader('CSV 파일 업로드', type = ['csv'])
        if csv_file is not None : # 파일이 있을때만 처리할꺼야
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':', '_') + '.csv'
            # 새로운 파일명 만듦

            # csv_file.name 유저가 올린 파일 이름을/ filename 우리가 올린
            csv_file.name = filename

            # 이제 서버에 저장하기
            save_uploaded_file('csv', csv_file)


            # 유저가 올린 파일 데이터프레임형식으로 보여주기
            df = pd.read_csv('csv/' + filename)
            st.dataframe(df)


             


    else : # -------------------------------------------------------
        st.subheader('이 대시보드 설명')



if __name__ == '__main__':  # -----------------------------------
    main()

