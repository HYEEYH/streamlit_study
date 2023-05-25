# 데이터 프레임 그리기


import streamlit as st
import pandas as pd

def main():
    st.title('앱 대시보드')

    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

    species = df['species'].unique()
    st.text('아이리스 꽃은' + species + '으로 되어 있다.')
    st.write( df.head() )


if __name__ == '__main__':
    main()
