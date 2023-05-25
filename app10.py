


# ----------------------------------
import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

# ----------------------------------



def main():
    st.title('내 앱 대시보드')
    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)
    st.write( df1.shape )

    ### 멀티셀렉트를 이용해 언어를 선택하게 하고 그거와 관련된 차트 그려보기
    
    # 컬럼에 뭐 있는지 확인
    # print( df1.columns )
    # 슬라이싱 이용해서 week 빼기
    print( df1.columns[ 1: ] )

    # 변수에 저장
    lang_list = df1.columns[ 1: ]

    # 유저에게 언어 선택 받기
    choice_list = st.multiselect('언어를 선택하세요', lang_list)
    
    # 프린트해서 확인
    print(choice_list)

    #@@
    # 유저가 아무것도 선택 안했을때 처리하기
    if len(choice_list) > 0 :  # 데이터가 있다면

        # 유저가 선택한 리스트만 가져와 변수에 넣고 표 보여주기
        choice_df = df1[ choice_list ]
        st.dataframe(choice_df)



        ## 스트림릿이 제공하는 라인차트
        # 각 행의 데이터를 y, 행 정보를 x축
        st.line_chart(choice_df)


        ## 스트림릿이 제공하는 영역차트
        #
        st.area_chart(choice_df)


    ### 아무것도 선택 안했을때 차트영역등이 빈공간으로 나오지 않게 하기
    # 조건문이 필요
    # 위치가 중요
    #@@ 위치에 집어넣으면 됨.






    ### 아이리스 데이터 ---------------------------------------
    df2 = pd.read_csv('data/iris.csv')

    ## 스트림릿이 제공하는 바 차트
    df3 = df2[ ['sepal_length', 'sepal_width'] ]
    st.bar_chart(df3)

    ## Altair 이용
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length', y = 'petal_width', color = 'species')
    
    st.altair_chart(chart)




    ### 로케이션 데이터 ----------------------------------------

    ## 스트림릿의 map차트
    df4 = pd.read_csv('data/location.csv', index_col = 0)
    print(df4)

    # zoom = 5 : 숫자가 작을수록 멀리서 보는것. 숫자만 적어도 됨.
    st.map(df4, zoom = 5)



    ### 프로그램 언어 데이터
    df5 = pd.read_csv('data/prog_languages_data.csv', index_col = 0)
    st.dataframe(df5)


    # plotly 의 pie 차트 ( 파이차트 - 비율을 보고 싶을때)
    fig1 = px.pie(df5, 'lang', 'Sum', title=' 각언어별 비율') # 차트 영역 만들기
    # df5 : 가져올 데이터, 'lang': 어떤거에대해 그릴꺼냐, 'Sum': 수치 뭘로할까
    st.plotly_chart(fig1)


    # plotly 의 bar 차트
    # fig2 = px.bar()
    df6 = df5.sort_values('Sum', ascending = False)
    fig2 = px.bar(df6, x = 'lang', y = 'Sum')
    st.plotly_chart(fig2)





if __name__ == '__main__':
    main()
