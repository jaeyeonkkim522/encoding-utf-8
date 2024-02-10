import pandas as pd
import chardet
import streamlit as st
from streamlit_extras.buy_me_a_coffee import button


def main():
    button(username = 'jaeyeon', floating=True, width = 221)

    st.title('KO-utf-8 변환기')
    st.title('맥북에서 한글 csv파일 utf-8 자동 변환')

    encoding_type = 'euc-kr'

    uploaded_files = st.file_uploader("Upload your csv file", type = ['csv'], accept_multiple_files=True)
    # file_path = st.text_input('원하는 파일 경로를 적어주세요.  (/Users/Downloads/)')


    def file_to_dataframe(uploaded_file):
            # 파일의 인코딩 타입을 확인합니다.
            raw_data = uploaded_file.read(100000)  # 샘플로 파일의 처음부터 일정량만 읽습니다.
            result = chardet.detect(raw_data)
            uploaded_file.seek(0)  # 파일 읽기 포인터를 다시 처음으로 이동시킵니다.
            # print(uploaded_file.name)
            if result['encoding'] == 'EUC-KR':
                dataframe = pd.read_csv(uploaded_file, encoding = encoding_type, encoding_errors='ignore')   
                return dataframe
            else:
                dataframe = pd.read_csv(uploaded_file, encoding = "utf-8", encoding_errors='ignore')
                return dataframe
            
        
    if uploaded_files:
        if st.button("변경 요청하기"):
            for uploaded_file in uploaded_files:
                
                df = file_to_dataframe(uploaded_file)
                file_name = uploaded_file.name
                # full_file_path = file_path + file_name

                with st.spinner('변경 작업 진행중....'):
                    try:
                        st.download_button(
                            label='CSV로 다운로드',
                            data=df.to_csv(encoding = "utf-8"), 
                            file_name=file_name, 
                            mime='text/csv'
                        )
                        #test2 = df.to_csv(encoding = "utf-8", index=False)
                        
                        st.success('정상적으로 변환되었습니다!!', icon="✅")
                        
                    except Exception as e:
                        st.error(f"에러가 발생했습니다: {e}")
    # /Users/kimjaeyeon/Downloads/sql_test/sql_test2/
