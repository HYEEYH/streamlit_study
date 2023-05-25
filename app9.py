


### 스트림릿에서 차트 그리기


# ------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------



def main():
    st.title('내 앱 대시보드')

    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)


    ### 꽃받침의 길이와 너비에 대해 차트 그리기 --------------------
    # sepal_length, sepal_width의 관계를 차트로


    ## 차트 1
    fig = plt.figure()  # 여기서부터 차트 영역이다
    plt.scatter(data = df, x = 'sepal_length', y = 'sepal_width')
    # plt.show()  # 이건 주피터노트북에서 그리라고 명령내리는거임
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal_width')
    st.pyplot(fig)



    ## 차트 2
    fig2 = plt.figure()  # 차트 영역 잡아주기
    sns.regplot(data = df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig2)

    

    ## 차트 3
    ## 관계를 더 정확하게 분석하는 방법
    # 상관관계분석
    correlation = df[ ['sepal_length', 'sepal_width'] ].corr()
    st.dataframe(correlation) # 상관관계나오는건 데이터프레임이다



    ## 차트 4
    # sepal_length 의 히스토그램을 그리기
    # bin 의 개수는 20개 (디폴트는 10개)
    fig3 = plt.figure()
    plt.hist(data = df, x = 'sepal_length', rwidth = 0.8, bins = 20)
    st.pyplot(fig3)



    ## 차트 5
    # 하나의 차트 영역에 하나는 bins=10, 하나는 bins=20 그리기
    # 서브플롯 이용
    fig3 = plt.figure()
    plt.subplot(1, 2, 1)
    plt.hist(data = df, x = 'sepal_length', rwidth = 0.8, bins = 10)

    plt.subplot(1, 2, 2)
    plt.hist(data = df, x = 'sepal_length', rwidth = 0.8, bins = 20)
    st.pyplot(fig3)

    # 전체 차트 영역 비율 조절
    fig3 = plt.figure(figsize = (10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(data = df, x = 'sepal_length', rwidth = 0.8, bins = 10)

    plt.subplot(1, 2, 2)
    plt.hist(data = df, x = 'sepal_length', rwidth = 0.8, bins = 20)
    st.pyplot(fig3)

    # ----------------------------------------------------------



    ### species 컬럼에는 종에 대한 정보가 들어있는데
    ### 각 종별로 몇 개씩의 대이터가 있는지
    ### 차트로 나타내기


    # 각 종별 몇개씩 데이터가 있는지 확인.
    st.dataframe( df['species'].value_counts() )

    # 차트로 나타내기
    fig4 = plt.figure()
    sns.countplot(data = df, x = 'species')
    st.pyplot(fig4)

    # ------------------------------------------------


    ### 데이터 프레임의 차트 그리는 코드로도 실행 가능

    fig5 = plt.figure()
    df['species'].value_counts().plot(kind = 'barh')
    st.pyplot(fig5)

    ## 주피터 노트북에서는 되는데 여기서는 안됨
    ## 데이터프레임 자체 plot 함수는 스트림릿에서는 안됨.
    ## 전체 데이터 그려라는 안되지만 컬럼 하나만 그려라 는 됨.
    # fig6 = plt.figure()   
    # df.plot()
    # st.pyplot(fig6)

    ## 전체 데이터 그려라는 안되지만, 컬럼 하나만 그려라 는 됨.
    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)
    # ---------------------------------------------




if __name__ == '__main__':
    main()
