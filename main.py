# /Users/kimjaeyeon/Downloads/sql_test/한국도로공사_휴게소 만족도 점수_20171231..csv

import pandas as pd
import chardet
from io import StringIO
import streamlit as st

st.title('MAC 인코딩 이슈 해결')
st.title('여러 CSV 파일 처리하기')

encoding_type = 'euc-kr'

uploaded_files = st.file_uploader("여러 파일을 선택해주세요", accept_multiple_files=True)
file_path = st.text_input('원하는 파일 경로를 적어주세요. : (/Users/Downloads/)')


def file_to_dataframe(uploaded_file):
        # 파일의 인코딩 타입을 확인합니다.
        raw_data = uploaded_file.read(100000)  # 샘플로 파일의 처음부터 일정량만 읽습니다.
        result = chardet.detect(raw_data)
        uploaded_file.seek(0)  # 파일 읽기 포인터를 다시 처음으로 이동시킵니다.
        # print(uploaded_file.name)
        if result['encoding'] == 'EUC-KR':
            print("encoding 이슈 euc-kr", uploaded_file.name, result)
            dataframe = pd.read_csv(uploaded_file, encoding = encoding_type, encoding_errors='ignore')   
            return dataframe
        else:
            print("encoding 이슈 utf-8", uploaded_file.name, result)
            dataframe = pd.read_csv(uploaded_file, encoding = "utf-8", encoding_errors='ignore')
            return dataframe

if uploaded_files:
    if st.button("변경 요청하기"):
        for uploaded_file in uploaded_files:
            
            df = file_to_dataframe(uploaded_file)
            file_name = uploaded_file.name
            full_file_path = file_path + file_name

            with st.spinner('변경 작업 진행중....'):
                try:
                    print(full_file_path)
                    test2 = df.to_csv(full_file_path, encoding = "utf-8", index=False)
                    st.success('정상적으로 변환되었습니다!!', icon="✅")
                    
                except Exception as e:
                    st.error(f"에러가 발생했습니다: {e}")
# /Users/kimjaeyeon/Downloads/sql_test/sql_test2/


