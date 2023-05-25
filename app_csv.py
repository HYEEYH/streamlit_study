


### 서브 함수 있는 곳


# app8.py와 연결
# 메뉴별로 분리해서 파일 만들기

# ------------------------------------------
import streamlit as st
import pandas as pd
from datetime import datetime

from app_utils import save_uploaded_file

#-------------------------------------------


def run_app_csv() :
        
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
