
#

import streamlit as st
import pandas as pd

def main():
    st.title('앱 대시보드')

    df = pd.read_csv('data/iris.csv')



    ### 버튼 누르면 데이터프레임 보이도록 편집
    # 조건문 써서 눌르면 -> 보여주기
    # 버튼 클릭하는것 = True
    # st.button('데이터보기')
    if st.button('데이터보기'):  # 버튼을 클릭했다면
        st.dataframe(df)




    ###  버튼 두개 만들기
    # 대문자 버튼을 누르면 대문자로 표시하고
    # 소문자 버튼을 누르면 소문자로 나오게 하기
    name = 'Mike'

    if st.button('대문자'):
        st.text( name.lower() )

    if st.button('소문자'):
        st.text( name.upper() )


    st.dataframe(df)




    # petal_length 컬럼을 정렬하고싶다면
    # 오름차순정렬, 내림차순 정렬 두 가지 옵션 선택 가능하도록

    status = st.radio('정렬을 선택하세요', ['오름차순', '내림차순'])
    # print(status)   # -> 결과가 터미널에 나타남. 웹페이지에서 선택해도 터미널에 나타남
    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length', ascending = False))






    ### 체크박스 만들기

    # st.checkbox('데이터프레임 보이기') # 체크박스에 표시하는 순간 True가 됨.
    if st.checkbox('데이터프레임 보이기'):
        st.dataframe( df.head(3) )
    else :               # 안쓰면 화면에 안나오는거. 써도 되고 안써도 되고
        st.write('데이터가 없습니다')





    ### 여러개 중에 1개를 선택 (드롭다운목록 같은거)
    language = ['Python', 'Java', 'C', 'Go', 'PHP']
    # st.selectbox('선호하는 언어를 선택!', language)

    selected_lang = st.selectbox('선호하는 언어를 선택!', language)
    if selected_lang == 'Python':
        st.text('파이썬이 최고지')
    elif selected_lang == 'Java':
        st.text('클래스가 좀 어려워')





    ### 멀티 셀렉트
    # 데이터 프레임의 컬럼 이름을 보여주고
    # 유저가 컬럼을 선택하면
    # 해당 컬럼만 가져와서 데이터프레임을 보여주고싶다

    # df.columns   
    # 리스트 비스무리한 애들은 파이썬이 알아서 리스트비스무리한걸로 처리해줌
    column_list = st.multiselect('컬럼을 선택하세요', df.columns)
    print(column_list)

    # 선택한 컬럼으로 데이터프레임 보여주기
    # 원하는 컬럼 선택한거에 엑세스  ->  df[column_list]
    # 웹페이지에 보여줘라            -> st.
    # 근데 그거 데이터프레임임.      ->  .dataframe
    st.dataframe(df[column_list])




    ### 슬라이더
    age = st.slider('나이', min_value = 10, max_value = 110, 
                    step = 1, value = 50 )
    st.text('나이는 ' + str(age) + ' 입니다')





    ### 
    with st.expender('hello') : # 익스펜더를 부르면
        st.text('안녕하세요')   # 텍스트가 나오게 해달라





if __name__ == '__main__':
    main()
