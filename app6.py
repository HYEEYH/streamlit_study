

### 유저에게 키보드로 입력받는 UI


import streamlit as st

def main():
    st.title('내 앱 대시보드')



    ### 텍스트 입력받기
    # 파이썬에서는 숫자 입력하든 문자 입력하든 전부 문자열로 입력함
    # 하지만 st.은 앞에  text 붙여서 문자라고 지정할 수 있음
    name = st.text_input('이름을 입력하세요!', max_chars = 10)
    st.text('입력하신 이름은 ' + name)


    # 텍스트를 여러줄 입력받고싶을때
    # 영역조절하고싶을때 : height = 10 -> 10줄까지입력가능
    message = st.text_area(' 메세지를 입력하세요 ', height = 10)
    st.text(message)




    ### 숫자 입력하기
    # 디폴트가 실수로 나옴.
    # 정수로만 나오게 하고 싶을때 : 1, 100 -> min_value, max_value임
    number = st.number_input('숫자를 입력하세요', 1, 100)
    st.text(number * 3)

    # 실수로 나오게 하고싶을때
    number2 = st.number_input('숫자를 입력하세요', 1.0, 100.0)
    st.text(number2 * 3)





    ### 날짜 입력받기
    # 디폴트는 현재날짜
    my_date = st.date_input('약속 날짜 입력')
    # print(my_date)
    # print( type(my_date))
    st.text(my_date)




    ### 시간
    my_time = st.time_input('시간 선택', )
    # print( type(my_time))
    st.text(my_time)




    ### 비밀번호 처리 방법
    # 실제로 웹 대시보드에서는 사용하지 않는 기능
    password = st.text_input('비밀번호 입력', type = 'password')
    st.text(password)




    ### 색 입력
    color = st.color_picker('색을 선택하세요')
    st.text(color)

    





if __name__ == '__main__':
    main()
