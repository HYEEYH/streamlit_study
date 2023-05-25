

### 메인 함수 있는 곳



# --------------------------------------------

import streamlit as st


# 다른 파이썬 파일 임포트
from app_image import run_app_image 
from app_csv import run_app_csv
from app_about import run_app_about
# ----------------------------------------------


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
        run_app_image()
            


    elif choice == menu[1] :  # ------------------------------------
        run_app_csv()

             

    else : # -------------------------------------------------------
        run_app_about()



if __name__ == '__main__': 
    main()

