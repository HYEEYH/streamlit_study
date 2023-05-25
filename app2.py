# http://localhost:8502/
# 뒤 숫자 8502는 port 번호다.
# print 는 터미널에 프린트 하라는 것. 웹 페이지에 안바뀜.



# 텍스트를 표시하는 방법


import streamlit as st

def main():
    st.title('웹 대시보드')

    name = '홍길동'

    # print('제 이름은 {}입니다'.format(name)) -> 이건 터미널에 출력하라는 의미
    st.text('제 이름은 {}입니다'.format(name))
    st.header('이 영역은 헤더 영역입니다')
    st.subheader('이 영역은 서브 헤더 영역입니다')
    st.success('성공했을때 나타내고 싶은 문장')
    st.warning('경고하고싶을때 문장')
    st.info('알림을 주고 싶을때')
    st.error('문제가 발생했음을 알려주고 싶을때')

    st.help(range)

if __name__ == '__main__':
    main()




