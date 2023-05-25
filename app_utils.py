


### 서브 함수 있는 곳



### 유틸 함수, 공통사용 함수 있는 부분


# --------------------------------------
import streamlit as st
from datetime import datetime
import os
import pandas as pd
# --------------------------------------




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