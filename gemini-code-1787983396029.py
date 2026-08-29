import streamlit as st

st.set_page_config(page_title="2회고사 대비 서·논술형 자동 채점 시스템", layout="wide")

st.title("📝 서·논술형 답안 자동 채점 시스템")
st.caption("2회고사 대비 모의 문항 1~3세트 연습 및 자동 채점")

tabs = st.tabs(["[세트 1] 학습 공간", "[세트 2] 정전기", "[세트 3] AI와 예술"])

# ==========================================
# [세트 1] 채점 로직 및 화면
# ==========================================
with tabs[0]:
    st.header("[세트 1] 사회적 촉진과 사회적 억제")
    
    st.subheader("[서·논술형 1] 표 요약 완성하기")
    s1_q1_1 = st.text_input("S1-1-1. (1) 빈칸 입력", key="s1_1_1")
    s1_q1_2 = st.text_input("S1-1-2. (2) 빈칸 입력", key="s1_1_2")
    s1_q1_3 = st.text_input("S1-1-3. (3) 빈칸 입력", key="s1_1_3")
    
    if st.button("세트 1-1 채점", key="btn_s1_1"):
        score = 0
        feedback = []
        
        # (1) 검증: 쉬운/친숙한 과제
        if any(k in s1_q1_1 for k in ["쉬운", "친숙한", "노력", "취미", "좋아하는"]):
            score += 1
            feedback.append("✅ (1) 정답입니다.")
        else:
            feedback.append("❌ (1) 오답: '비교적 쉬운 과제'나 '친숙한 과목'의 특성이 포함되어야 합니다.")
            
        # (2) 검증: 혼자 차분히 집중
        if any(k in s1_q1_2 for k in ["혼자", "차분", "집중", "연습"]):
            if any(k in s1_q1_2 for k in ["모임", "함께", "도서관"]):
                feedback.append("❌ (2) 오답 (오개념): 어려운 과제에 '함께 공부' 개념을 적용했습니다.")
            else:
                score += 1
                feedback.append("✅ (2) 정답입니다.")
        else:
            feedback.append("❌ (2) 오답: '혼자 차분하게 집중'한다는 내용이 필요합니다.")
            
        # (3) 검증: 사회적 억제
        if "사회적 억제" in s1_q1_3.replace(" ", ""):
            score += 1
            feedback.append("✅ (3) 정답입니다.")
        else:
            feedback.append("❌ (3) 오답: 정확한 용어 '사회적 억제'를 입력해야 합니다.")
            
        st.info(f"점수: {score}/3점\n\n" + "\n".join(feedback))

    st.divider()
    
    st.subheader("[서·논술형 2] 설명문 작성하기")
    st.write("주어진 첫 문장: *과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.*")
    s1_q2_method1 = st.selectbox("(1) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s1_m1")
    s1_q2_1 = st.text_area("(1) 문장 작성 (끝에 괄호 표기)", key="s1_q2_1")
    s1_q2_method2 = st.selectbox("(2) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s1_m2")
    s1_q2_2 = st.text_area("(2) 문장 작성 (끝에 괄호 표기)", key="s1_q2_2")
    
    if st.button("세트 1-2 채점", key="btn_s1_2"):
        score = 0
        feedback = []
        
        # 중복 방법 검증
        if s1_q2_method1 != "선택" and s1_q2_method1 == s1_q2_method2:
            st.error("❌ 서로 다른 2가지의 설명 방법을 사용해야 합니다. (동일 방법 중복 사용 불가)")
        else:
            # (1) 채점
            if s1_q2_method1 != "선택" and len(s1_q2_1) > 10:
                if (s1_q2_method1 == "예시" and any(k in s1_q2_1 for k in ["예를 들어", "예컨대", "카페", "도서관"])) or \
                   (s1_q2_method1 == "대조" and any(k in s1_q2_1 for k in ["반면", "달리", "차이"])) or \
                   (s1_q2_method1 == "정의" and any(k in s1_q2_1 for k in ["뜻한다", "의미한다", "말한다"])):
                    score += 2
                    feedback.append("✅ (1) 선택한 설명 방법의 특성과 지문 내용이 잘 반영되었습니다.")
                else:
                    feedback.append("❌ (1) 선택한 설명 방법의 특징적 표현이 부족하거나 지문 내용과 일치하지 않습니다.")
            else:
                feedback.append("❌ (1) 설명 방법을 선택하고 문장을 작성해 주세요.")
                
            # (2) 채점
            if s1_q2_method2 != "선택" and len(s1_q2_2) > 10:
                if (s1_q2_method2 == "대조" and any(k in s1_q2_2 for k in ["반면", "달리", "차이"])) or \
                   (s1_q2_method2 == "예시" and any(k in s1_q2_2 for k in ["예를 들어", "예컨대"])) or \
                   (s1_q2_method2 == "인과" and any(k in s1_q2_2 for k in ["때문에", "따라서", "결과"])):
                    score += 2
                    feedback.append("✅ (2) 선택한 설명 방법의 특성과 지문 내용이 잘 반영되었습니다.")
                else:
                    feedback.append("❌ (2) 선택한 설명 방법의 특징적 표현이 부족하거나 지문 내용과 일치하지 않습니다.")
            else:
                feedback.append("❌ (2) 설명 방법을 선택하고 문장을 작성해 주세요.")
                
            st.info(f"점수: {score}/4점\n\n" + "\n".join(feedback))

    st.divider()
    
    st.subheader("[서·논술형 3] 영상 기획안 작성하기")
    s1_q3_a = st.text_input("Ⓐ 시각 요소 연출", key="s1_3_a")
    s1_q3_a_eff = st.text_area("Ⓐ 시각 요소의 효과 (지문 근거 필수)", key="s1_3_a_eff")
    s1_q3_b = st.text_input("Ⓑ 청각 요소 연출", key="s1_3_b")
    s1_q3_b_eff = st.text_area("Ⓑ 청각 요소의 효과 (지문 근거 필수)", key="s1_3_b_eff")
    
    if st.button("세트 1-3 채점", key="btn_s1_3"):
        score = 0
        feedback = []
        
        # Ⓐ 시각 연출 및 효과
        if any(k in s1_q3_a for k in ["혼자", "방", "책상", "고민", "클로즈업", "정적"]):
            score += 1
            if any(k in s1_q3_a_eff for k in ["어려운", "복잡한", "집중", "차분"]):
                score += 2
                feedback.append("✅ Ⓐ 시각 요소 및 지문 근거 기반 효과 서술이 완벽합니다.")
            else:
                feedback.append("⚠️ Ⓐ 연출은 적절하나, 효과에 '지문 근거(어려운 과제=혼자 집중)'가 부족합니다. (1점)")
        else:
            feedback.append("❌ Ⓐ 연출이 '혼자 차분히 집중하는 상황'을 표현하지 못했습니다.")
            
        # Ⓑ 청각 연출 및 효과
        if any(k in s1_q3_b for k in ["조용한", "고요", "시계", "연필", "소음 배제", "클래식"]):
            score += 1
            if any(k in s1_q3_b_eff for k in ["외부 자극", "몰입", "집중", "차분"]):
                score += 2
                feedback.append("✅ Ⓑ 청각 요소 및 지문 근거 기반 효과 서술이 완벽합니다.")
            else:
                feedback.append("⚠️ Ⓑ 연출은 적절하나, 효과에 '지문 근거'가 부족합니다. (1점)")
        else:
            feedback.append("❌ Ⓑ 연출이 '고요하고 집중되는 청각 분위기'를 표현하지 못했습니다.")
            
        st.info(f"점수: {score}/6점\n\n" + "\n".join(feedback))


# ==========================================
# [세트 2] 채점 로직 및 화면
# ==========================================
with tabs[1]:
    st.header("[세트 2] 정전기의 특징")
    
    st.subheader("[서·논술형 1] 표 요약 완성하기")
    s2_q1_1 = st.text_input("S2-1-1. (1) 비유 표현", key="s2_1_1")
    s2_q1_2 = st.text_input("S2-1-2. (2) 전하의 상태", key="s2_1_2")
    s2_q1_3 = st.text_input("S2-1-3. (3) 위험성", key="s2_1_3")
    
    if st.button("세트 2-1 채점", key="btn_s2_1"):
        score = 0
        feedback = []
        
        # (1) 고여 있는 물
        if any(k in s2_q1_1 for k in ["고여", "높은 곳", "멈춰"]):
            score += 1
            feedback.append("✅ (1) 정답입니다.")
        else:
            feedback.append("❌ (1) 오답: '높은 곳에 고여 있는 물' 비유가 들어가야 합니다.")
            
        # (2) 전하 정지/이동 안함
        if any(k in s2_q1_2 for k in ["이동하지", "머물러", "정지"]):
            score += 1
            feedback.append("✅ (2) 정답입니다.")
        else:
            feedback.append("❌ (2) 오답: '전하가 이동하지 않고 머물러 있음'의 의미가 포함되어야 합니다.")
            
        # (3) 위험하지 않음
        if any(k in s2_q1_3 for k in ["위험하지", "피해가 없", "안전"]):
            score += 1
            feedback.append("✅ (3) 정답입니다.")
        else:
            feedback.append("❌ (3) 오답: '위험하지 않음'의 의미가 들어가야 합니다.")
            
        st.info(f"점수: {score}/3점\n\n" + "\n".join(feedback))

    st.divider()
    
    st.subheader("[서·논술형 2] 설명문 작성하기")
    s2_q2_m1 = st.selectbox("(1) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s2_m1")
    s2_q2_1 = st.text_area("(1) 문장 작성", key="s2_q2_1")
    s2_q2_m2 = st.selectbox("(2) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s2_m2")
    s2_q2_2 = st.text_area("(2) 문장 작성", key="s2_q2_2")
    
    if st.button("세트 2-2 채점", key="btn_s2_2"):
        score = 0
        feedback = []
        
        if s2_q2_m1 != "선택" and s2_q2_m1 == s2_q2_m2:
            st.error("❌ 서로 다른 설명 방법을 활용해야 합니다.")
        else:
            # (1) 채점
            if s2_q2_m1 == "정의" and any(k in s2_q2_1 for k in ["란", "뜻", "의미", "말한다"]):
                score += 2
                feedback.append("✅ (1) 정의의 설명 방법이 유효하게 사용되었습니다.")
            elif s2_q2_m1 != "선택" and len(s2_q2_1) > 10:
                score += 2
                feedback.append("✅ (1) 작성되었습니다.")
            else:
                feedback.append("❌ (1) 조건에 맞는 문장을 작성해 주세요.")
                
            # (2) 채점
            if s2_q2_m2 == "비교와 대조" and any(k in s2_q2_2 for k in ["달리", "반면", "와 달리", "차이"]):
                score += 2
                feedback.append("✅ (2) 비교와 대조의 설명 방법이 유효하게 사용되었습니다.")
            elif s2_q2_m2 != "선택" and len(s2_q2_2) > 10:
                score += 2
                feedback.append("✅ (2) 작성되었습니다.")
            else:
                feedback.append("❌ (2) 조건에 맞는 문장을 작성해 주세요.")
                
            st.info(f"점수: {score}/4점\n\n" + "\n".join(feedback))

    st.divider()
    
    st.subheader("[서·논술형 3] 영상 기획안 작성하기")
    s2_q3_a = st.text_input("Ⓐ 시각 요소 (고여 있는 물)", key="s2_3_a")
    s2_q3_a_eff = st.text_area("Ⓐ 시각 요소 효과 (지문 근거)", key="s2_3_a_eff")
    s2_q3_b = st.text_input("Ⓑ 청각 요소 (고요함/정적)", key="s2_3_b")
    s2_q3_b_eff = st.text_area("Ⓑ 청각 요소 효과 (지문 근거)", key="s2_3_b_eff")
    
    if st.button("세트 2-3 채점", key="btn_s2_3"):
        score = 0
        feedback = []
        
        if any(k in s2_q3_a for k in ["높은", "절벽", "고여", "멈춰"]):
            score += 1
            if any(k in s2_q3_a_eff for k in ["고여 있는 물", "이동하지", "머물러", "위험하지 않"]):
                score += 2
                feedback.append("✅ Ⓐ 시각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓐ 효과에 '지문 근거(고여 있는 물/위험하지 않음)' 부족 (1점)")
        else:
            feedback.append("❌ Ⓐ 연출 오답: 흐르지 않고 고여 있는 물 연출 필요")
            
        if any(k in s2_q3_b for k in ["고요", "정적", "소리 없는", "잔잔"]):
            score += 1
            if any(k in s2_q3_b_eff for k in ["정(靜)", "움직이지", "정지", "머물러"]):
                score += 2
                feedback.append("✅ Ⓑ 청각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓑ 효과에 '지문 근거(정의 의미/전하 정지)' 부족 (1점)")
        else:
            feedback.append("❌ Ⓑ 연출 오답: 정지 상태를 나타내는 고요한 연출 필요")
            
        st.info(f"점수: {score}/6점\n\n" + "\n".join(feedback))


# ==========================================
# [세트 3] 채점 로직 및 화면
# ==========================================
with tabs[2]:
    st.header("[세트 3] 인공지능과 예술")
    
    st.subheader("[서·논술형 1] 표 요약 완성하기")
    s3_q1_1 = st.text_input("S3-1-1. (1) 올림픽 비유", key="s3_1_1")
    s3_q1_2 = st.text_input("S3-1-2. (2) 예술 여부 판단 및 근거", key="s3_1_2")
    s3_q1_3 = st.text_input("S3-1-3. (3) 예술로서의 가치", key="s3_1_3")
    
    if st.button("세트 3-1 채점", key="btn_s3_1"):
        score = 0
        feedback = []
        
        # (1) 로봇/완벽한 피겨
        if any(k in s3_q1_1 for k in ["로봇", "피겨", "완벽"]):
            score += 1
            feedback.append("✅ (1) 정답입니다.")
        else:
            feedback.append("❌ (1) 오답: '로봇의 완벽한 피겨 연기' 내용이 들어가야 합니다.")
            
        # (2) 결론: 예술로 보기 어려움 + 근거
        if any(k in s3_q1_2 for k in ["어렵다", "아니다", "볼 수 없다"]) and any(k in s3_q1_2 for k in ["감정", "철학", "이야기"]):
            score += 1
            feedback.append("✅ (2) 근거 및 결론 방향이 정확합니다.")
        else:
            feedback.append("❌ (2) 오답: '감정/철학 부재' 근거와 '예술로 보기 어렵다'는 결론이 명확히 들어가야 합니다.")
            
        # (3) 가치: 미술계 변화, 범주 확장
        if any(k in s3_q1_3 for k in ["변화", "범주", "확장", "상징"]):
            score += 1
            feedback.append("✅ (3) 정답입니다.")
        else:
            feedback.append("❌ (3) 오답: '미술계 변화' 또는 '예술 범주 확장/상징적 가치' 표현이 필요합니다.")
            
        st.info(f"점수: {score}/3점\n\n" + "\n".join(feedback))

    st.divider()
    
    st.subheader("[서·논술형 2] 설명문 작성하기")
    s3_q2_m1 = st.selectbox("(1) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s3_m1")
    s3_q2_1 = st.text_area("(1) 문장 작성", key="s3_q2_1")
    s3_q2_m2 = st.selectbox("(2) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s3_m2")
    s3_q2_2 = st.text_area("(2) 문장 작성", key="s3_q2_2")
    
    if st.button("세트 3-2 채점", key="btn_s3_2"):
        score = 0
        feedback = []
        
        if s3_q2_m1 != "선택" and s3_q2_m1 == s3_q2_m2:
            st.error("❌ 서로 다른 설명 방법을 선택해야 합니다.")
        else:
            if s3_q2_m1 != "선택" and len(s3_q2_1) > 10:
                score += 2
                feedback.append("✅ (1) 문장 작성 완료")
            else:
                feedback.append("❌ (1) 문장을 작성해 주세요.")
                
            if s3_q2_m2 != "선택" and len(s3_q2_2) > 10:
                score += 2
                feedback.append("✅ (2) 문장 작성 완료")
            else:
                feedback.append("❌ (2) 문장을 작성해 주세요.")
                
            st.info(f"점수: {score}/4점\n\n" + "\n".join(feedback))

    st.divider()
    
    st.subheader("[서·논술형 3] 영상 기획안 작성하기")
    s3_q3_a = st.text_input("Ⓐ 시각 요소 (인간 예술의 모습)", key="s3_3_a")
    s3_q3_a_eff = st.text_area("Ⓐ 시각 요소 효과 (지문 근거)", key="s3_3_a_eff")
    s3_q3_b = st.text_input("Ⓑ 청각 요소 (감동적 소리)", key="s3_3_b")
    s3_q3_b_eff = st.text_area("Ⓑ 청각 요소 효과 (지문 근거)", key="s3_3_b_eff")
    
    if st.button("세트 3-3 채점", key="btn_s3_3"):
        score = 0
        feedback = []
        
        if any(k in s3_q3_a for k in ["선수", "눈물", "노력", "열정", "교감"]):
            score += 1
            if any(k in s3_q3_a_eff for k in ["감정", "철학", "경험", "울림", "노력"]):
                score += 2
                feedback.append("✅ Ⓐ 시각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓐ 효과에 '지문 근거(인간의 감정/노력이 주는 울림)' 부족 (1점)")
        else:
            feedback.append("❌ Ⓐ 연출 오답: 인간의 노력과 감동을 드러내는 연출 필요")
            
        if any(k in s3_q3_b for k in ["오케스트라", "바이올린", "서정", "환호", "울림"]):
            score += 1
            if any(k in s3_q3_b_eff for k in ["감동", "대조", "따뜻한", "열정"]):
                score += 2
                feedback.append("✅ Ⓑ 청각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓑ 효과에 '지문 근거' 부족 (1점)")
        else:
            feedback.append("❌ Ⓑ 연출 오답: 감동을 배가시키는 서정적 음향 연출 필요")
            
        st.info(f"점수: {score}/6점\n\n" + "\n".join(feedback))
        import streamlit as st

st.set_page_config(page_title="2회고사 대비 서·논술형 자동 채점 시스템", layout="wide")

st.title("📝 서·논술형 답안 자동 채점 시스템")
st.caption("2회고사 대비 모의 문항 1~3세트 연습 및 자동 채점")

# 틀린 문제를 기록할 세션 상태 초기화
if "incorrect_questions" not in st.session_state:
    st.session_state.incorrect_questions = {}

tabs = st.tabs(["[세트 1] 학습 공간", "[세트 2] 정전기", "[세트 3] AI와 예술", "📌 복습할 내용"])

# ==========================================
# [세트 1] 채점 로직 및 화면
# ==========================================
with tabs[0]:
    st.header("[세트 1] 사회적 촉진과 사회적 억제")
    
    st.subheader("[서·논술형 1] 표 요약 완성하기")
    s1_q1_1 = st.text_input("S1-1-1. (1) 빈칸 입력", key="s1_1_1")
    s1_q1_2 = st.text_input("S1-1-2. (2) 빈칸 입력", key="s1_1_2")
    s1_q1_3 = st.text_input("S1-1-3. (3) 빈칸 입력", key="s1_1_3")
    
    if st.button("세트 1-1 채점", key="btn_s1_1"):
        score = 0
        feedback = []
        
        # (1) 검증
        if any(k in s1_q1_1 for k in ["쉬운", "친숙한", "노력", "취미", "좋아하는"]):
            score += 1
            feedback.append("✅ (1) 정답입니다.")
        else:
            feedback.append("❌ (1) 오답: '비교적 쉬운 과제'나 '친숙한 과목'의 특성이 포함되어야 합니다.")
            
        # (2) 검증
        if any(k in s1_q1_2 for k in ["혼자", "차분", "집중", "연습"]):
            if any(k in s1_q1_2 for k in ["모임", "함께", "도서관"]):
                feedback.append("❌ (2) 오답 (오개념): 어려운 과제에 '함께 공부' 개념을 적용했습니다.")
            else:
                score += 1
                feedback.append("✅ (2) 정답입니다.")
        else:
            feedback.append("❌ (2) 오답: '혼자 차분하게 집중'한다는 내용이 필요합니다.")
            
        # (3) 검증
        if "사회적 억제" in s1_q1_3.replace(" ", ""):
            score += 1
            feedback.append("✅ (3) 정답입니다.")
        else:
            feedback.append("❌ (3) 오답: 정확한 용어 '사회적 억제'를 입력해야 합니다.")
            
        st.info(f"점수: {score}/3점\n\n" + "\n".join(feedback))

        # 오답 기록
        if score < 3:
            st.session_state.incorrect_questions["세트 1 - 문항 1"] = {
                "point": "사회적 촉진과 사회적 억제 개념 구분 및 과제 난이도에 따른 환경 차이",
                "my_answer": f"(1) {s1_q1_1} / (2) {s1_q1_2} / (3) {s1_q1_3}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 1 - 문항 1", None)

    st.divider()
    
    st.subheader("[서·논술형 2] 설명문 작성하기")
    st.write("주어진 첫 문장: *과제의 특성과 난이도에 따라 우리의 학습 효율을 높이는 방법은 다르게 적용되어야 한다.*")
    s1_q2_method1 = st.selectbox("(1) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s1_m1")
    s1_q2_1 = st.text_area("(1) 문장 작성 (끝에 괄호 표기)", key="s1_q2_1")
    s1_q2_method2 = st.selectbox("(2) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s1_m2")
    s1_q2_2 = st.text_area("(2) 문장 작성 (끝에 괄호 표기)", key="s1_q2_2")
    
    if st.button("세트 1-2 채점", key="btn_s1_2"):
        score = 0
        feedback = []
        
        if s1_q2_method1 != "선택" and s1_q2_method1 == s1_q2_method2:
            st.error("❌ 서로 다른 2가지의 설명 방법을 사용해야 합니다. (동일 방법 중복 사용 불가)")
            score = 0
            feedback.append("❌ 동일한 설명 방법을 중복 활용하여 감점 처리되었습니다.")
        else:
            if s1_q2_method1 != "선택" and len(s1_q2_1) > 10:
                if (s1_q2_method1 == "예시" and any(k in s1_q2_1 for k in ["예를 들어", "예컨대", "카페", "도서관"])) or \
                   (s1_q2_method1 == "대조" and any(k in s1_q2_1 for k in ["반면", "달리", "차이"])) or \
                   (s1_q2_method1 == "정의" and any(k in s1_q2_1 for k in ["뜻한다", "의미한다", "말한다"])):
                    score += 2
                    feedback.append("✅ (1) 선택한 설명 방법의 특성과 지문 내용이 잘 반영되었습니다.")
                else:
                    feedback.append("❌ (1) 선택한 설명 방법의 특징적 표현이 부족하거나 지문 내용과 일치하지 않습니다.")
            else:
                feedback.append("❌ (1) 설명 방법을 선택하고 문장을 작성해 주세요.")
                
            if s1_q2_method2 != "선택" and len(s1_q2_2) > 10:
                if (s1_q2_method2 == "대조" and any(k in s1_q2_2 for k in ["반면", "달리", "차이"])) or \
                   (s1_q2_method2 == "예시" and any(k in s1_q2_2 for k in ["예를 들어", "예컨대"])) or \
                   (s1_q2_method2 == "인과" and any(k in s1_q2_2 for k in ["때문에", "따라서", "결과"])):
                    score += 2
                    feedback.append("✅ (2) 선택한 설명 방법의 특성과 지문 내용이 잘 반영되었습니다.")
                else:
                    feedback.append("❌ (2) 선택한 설명 방법의 특징적 표현이 부족하거나 지문 내용과 일치하지 않습니다.")
            else:
                feedback.append("❌ (2) 설명 방법을 선택하고 문장을 작성해 주세요.")
                
        st.info(f"점수: {score}/4점\n\n" + "\n".join(feedback))

        if score < 4:
            st.session_state.incorrect_questions["세트 1 - 문항 2"] = {
                "point": "서로 다른 설명 방법 명칭 사용 및 각 설명 방법의 표현 특징 호응",
                "my_answer": f"(1) [{s1_q2_method1}] {s1_q2_1}\n(2) [{s1_q2_method2}] {s1_q2_2}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 1 - 문항 2", None)

    st.divider()
    
    st.subheader("[서·논술형 3] 영상 기획안 작성하기")
    s1_q3_a = st.text_input("Ⓐ 시각 요소 연출", key="s1_3_a")
    s1_q3_a_eff = st.text_area("Ⓐ 시각 요소의 효과 (지문 근거 필수)", key="s1_3_a_eff")
    s1_q3_b = st.text_input("Ⓑ 청각 요소 연출", key="s1_3_b")
    s1_q3_b_eff = st.text_area("Ⓑ 청각 요소의 효과 (지문 근거 필수)", key="s1_3_b_eff")
    
    if st.button("세트 1-3 채점", key="btn_s1_3"):
        score = 0
        feedback = []
        
        if any(k in s1_q3_a for k in ["혼자", "방", "책상", "고민", "클로즈업", "정적"]):
            score += 1
            if any(k in s1_q3_a_eff for k in ["어려운", "복잡한", "집중", "차분"]):
                score += 2
                feedback.append("✅ Ⓐ 시각 요소 및 지문 근거 기반 효과 서술이 완벽합니다.")
            else:
                feedback.append("⚠️ Ⓐ 연출은 적절하나, 효과에 '지문 근거(어려운 과제=혼자 집중)'가 부족합니다. (1점)")
        else:
            feedback.append("❌ Ⓐ 연출이 '혼자 차분히 집중하는 상황'을 표현하지 못했습니다.")
            
        if any(k in s1_q3_b for k in ["조용한", "고요", "시계", "연필", "소음 배제", "클래식"]):
            score += 1
            if any(k in s1_q3_b_eff for k in ["외부 자극", "몰입", "집중", "차분"]):
                score += 2
                feedback.append("✅ Ⓑ 청각 요소 및 지문 근거 기반 효과 서술이 완벽합니다.")
            else:
                feedback.append("⚠️ Ⓑ 연출은 적절하나, 효과에 '지문 근거'가 부족합니다. (1점)")
        else:
            feedback.append("❌ Ⓑ 연출이 '고요하고 집중되는 청각 분위기'를 표현하지 못했습니다.")
            
        st.info(f"점수: {score}/6점\n\n" + "\n".join(feedback))

        if score < 6:
            st.session_state.incorrect_questions["세트 1 - 문항 3"] = {
                "point": "복합양식성 시/청각 연출 계획과 본문 지문에 기반한 효과 근거 제시",
                "my_answer": f"Ⓐ 시각: {s1_q3_a} / 효과: {s1_q3_a_eff}\nⒷ 청각: {s1_q3_b} / 효과: {s1_q3_b_eff}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 1 - 문항 3", None)


# ==========================================
# [세트 2] 채점 로직 및 화면
# ==========================================
with tabs[1]:
    st.header("[세트 2] 정전기의 특징")
    
    st.subheader("[서·논술형 1] 표 요약 완성하기")
    s2_q1_1 = st.text_input("S2-1-1. (1) 비유 표현", key="s2_1_1")
    s2_q1_2 = st.text_input("S2-1-2. (2) 전하의 상태", key="s2_1_2")
    s2_q1_3 = st.text_input("S2-1-3. (3) 위험성", key="s2_1_3")
    
    if st.button("세트 2-1 채점", key="btn_s2_1"):
        score = 0
        feedback = []
        
        if any(k in s2_q1_1 for k in ["고여", "높은 곳", "멈춰"]):
            score += 1
            feedback.append("✅ (1) 정답입니다.")
        else:
            feedback.append("❌ (1) 오답: '높은 곳에 고여 있는 물' 비유가 들어가야 합니다.")
            
        if any(k in s2_q1_2 for k in ["이동하지", "머물러", "정지"]):
            score += 1
            feedback.append("✅ (2) 정답입니다.")
        else:
            feedback.append("❌ (2) 오답: '전하가 이동하지 않고 머물러 있음'의 의미가 포함되어야 합니다.")
            
        if any(k in s2_q1_3 for k in ["위험하지", "피해가 없", "안전"]):
            score += 1
            feedback.append("✅ (3) 정답입니다.")
        else:
            feedback.append("❌ (3) 오답: '위험하지 않음'의 의미가 들어가야 합니다.")
            
        st.info(f"점수: {score}/3점\n\n" + "\n".join(feedback))

        if score < 3:
            st.session_state.incorrect_questions["세트 2 - 문항 1"] = {
                "point": "정전기의 비유적 속성, 전하 상태 및 위험성 핵심 정보 추출",
                "my_answer": f"(1) {s2_q1_1} / (2) {s2_q1_2} / (3) {s2_q1_3}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 2 - 문항 1", None)

    st.divider()
    
    st.subheader("[서·논술형 2] 설명문 작성하기")
    s2_q2_m1 = st.selectbox("(1) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s2_m1")
    s2_q2_1 = st.text_area("(1) 문장 작성", key="s2_q2_1")
    s2_q2_m2 = st.selectbox("(2) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s2_m2")
    s2_q2_2 = st.text_area("(2) 문장 작성", key="s2_q2_2")
    
    if st.button("세트 2-2 채점", key="btn_s2_2"):
        score = 0
        feedback = []
        
        if s2_q2_m1 != "선택" and s2_q2_m1 == s2_q2_m2:
            st.error("❌ 서로 다른 설명 방법을 활용해야 합니다.")
            feedback.append("❌ 설명 방법 중복 활용")
        else:
            if s2_q2_m1 == "정의" and any(k in s2_q2_1 for k in ["란", "뜻", "의미", "말한다"]):
                score += 2
                feedback.append("✅ (1) 정의의 설명 방법이 유효하게 사용되었습니다.")
            elif s2_q2_m1 != "선택" and len(s2_q2_1) > 10:
                score += 2
                feedback.append("✅ (1) 작성되었습니다.")
            else:
                feedback.append("❌ (1) 조건에 맞는 문장을 작성해 주세요.")
                
            if s2_q2_m2 == "비교와 대조" and any(k in s2_q2_2 for k in ["달리", "반면", "와 달리", "차이"]):
                score += 2
                feedback.append("✅ (2) 비교와 대조의 설명 방법이 유효하게 사용되었습니다.")
            elif s2_q2_m2 != "선택" and len(s2_q2_2) > 10:
                score += 2
                feedback.append("✅ (2) 작성되었습니다.")
            else:
                feedback.append("❌ (2) 조건에 맞는 문장을 작성해 주세요.")
                
        st.info(f"점수: {score}/4점\n\n" + "\n".join(feedback))

        if score < 4:
            st.session_state.incorrect_questions["세트 2 - 문항 2"] = {
                "point": "정전기의 정의 및 일반 전기와의 대조적 특징을 논리적 흐름으로 연결하기",
                "my_answer": f"(1) [{s2_q2_m1}] {s2_q2_1}\n(2) [{s2_q2_m2}] {s2_q2_2}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 2 - 문항 2", None)

    st.divider()
    
    st.subheader("[서·논술형 3] 영상 기획안 작성하기")
    s2_q3_a = st.text_input("Ⓐ 시각 요소 (고여 있는 물)", key="s2_3_a")
    s2_q3_a_eff = st.text_area("Ⓐ 시각 요소 효과 (지문 근거)", key="s2_3_a_eff")
    s2_q3_b = st.text_input("Ⓑ 청각 요소 (고요함/정적)", key="s2_3_b")
    s2_q3_b_eff = st.text_area("Ⓑ 청각 요소 효과 (지문 근거)", key="s2_3_b_eff")
    
    if st.button("세트 2-3 채점", key="btn_s2_3"):
        score = 0
        feedback = []
        
        if any(k in s2_q3_a for k in ["높은", "절벽", "고여", "멈춰"]):
            score += 1
            if any(k in s2_q3_a_eff for k in ["고여 있는 물", "이동하지", "머물러", "위험하지 않"]):
                score += 2
                feedback.append("✅ Ⓐ 시각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓐ 효과에 '지문 근거(고여 있는 물/위험하지 않음)' 부족 (1점)")
        else:
            feedback.append("❌ Ⓐ 연출 오답: 흐르지 않고 고여 있는 물 연출 필요")
            
        if any(k in s2_q3_b for k in ["고요", "정적", "소리 없는", "잔잔"]):
            score += 1
            if any(k in s2_q3_b_eff for k in ["정(靜)", "움직이지", "정지", "머물러"]):
                score += 2
                feedback.append("✅ Ⓑ 청각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓑ 효과에 '지문 근거(정의 의미/전하 정지)' 부족 (1점)")
        else:
            feedback.append("❌ Ⓑ 연출 오답: 정지 상태를 나타내는 고요한 연출 필요")
            
        st.info(f"점수: {score}/6점\n\n" + "\n".join(feedback))

        if score < 6:
            st.session_state.incorrect_questions["세트 2 - 문항 3"] = {
                "point": "정전기의 비유(고여 있는 물) 및 '정(靜)' 상태를 표현한 연출 및 본문 근거 명시",
                "my_answer": f"Ⓐ 시각: {s2_q3_a} / 효과: {s2_q3_a_eff}\nⒷ 청각: {s2_q3_b} / 효과: {s2_q3_b_eff}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 2 - 문항 3", None)


# ==========================================
# [세트 3] 채점 로직 및 화면
# ==========================================
with tabs[2]:
    st.header("[세트 3] 인공지능과 예술")
    
    st.subheader("[서·논술형 1] 표 요약 완성하기")
    s3_q1_1 = st.text_input("S3-1-1. (1) 올림픽 비유", key="s3_1_1")
    s3_q1_2 = st.text_input("S3-1-2. (2) 예술 여부 판단 및 근거", key="s3_1_2")
    s3_q1_3 = st.text_input("S3-1-3. (3) 예술로서의 가치", key="s3_1_3")
    
    if st.button("세트 3-1 채점", key="btn_s3_1"):
        score = 0
        feedback = []
        
        if any(k in s3_q1_1 for k in ["로봇", "피겨", "완벽"]):
            score += 1
            feedback.append("✅ (1) 정답입니다.")
        else:
            feedback.append("❌ (1) 오답: '로봇의 완벽한 피겨 연기' 내용이 들어가야 합니다.")
            
        if any(k in s3_q1_2 for k in ["어렵다", "아니다", "볼 수 없다"]) and any(k in s3_q1_2 for k in ["감정", "철학", "이야기"]):
            score += 1
            feedback.append("✅ (2) 근거 및 결론 방향이 정확합니다.")
        else:
            feedback.append("❌ (2) 오답: '감정/철학 부재' 근거와 '예술로 보기 어렵다'는 결론이 명확히 들어가야 합니다.")
            
        if any(k in s3_q1_3 for k in ["변화", "범주", "확장", "상징"]):
            score += 1
            feedback.append("✅ (3) 정답입니다.")
        else:
            feedback.append("❌ (3) 오답: '미술계 변화' 또는 '예술 범주 확장/상징적 가치' 표현이 필요합니다.")
            
        st.info(f"점수: {score}/3점\n\n" + "\n".join(feedback))

        if score < 3:
            st.session_state.incorrect_questions["세트 3 - 문항 1"] = {
                "point": "인공지능 작품의 예술 불가 이유(감정/철학 부재) 및 상징적 가치 정리",
                "my_answer": f"(1) {s3_q1_1} / (2) {s3_q1_2} / (3) {s3_q1_3}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 3 - 문항 1", None)

    st.divider()
    
    st.subheader("[서·논술형 2] 설명문 작성하기")
    s3_q2_m1 = st.selectbox("(1) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s3_m1")
    s3_q2_1 = st.text_area("(1) 문장 작성", key="s3_q2_1")
    s3_q2_m2 = st.selectbox("(2) 사용한 설명 방법", ["선택", "정의", "예시", "인과", "분석", "비교와 대조", "분류와 구분"], key="s3_m2")
    s3_q2_2 = st.text_area("(2) 문장 작성", key="s3_q2_2")
    
    if st.button("세트 3-2 채점", key="btn_s3_2"):
        score = 0
        feedback = []
        
        if s3_q2_m1 != "선택" and s3_q2_m1 == s3_q2_m2:
            st.error("❌ 서로 다른 설명 방법을 선택해야 합니다.")
            feedback.append("❌ 설명 방법 중복 활용")
        else:
            if s3_q2_m1 != "선택" and len(s3_q2_1) > 10:
                score += 2
                feedback.append("✅ (1) 문장 작성 완료")
            else:
                feedback.append("❌ (1) 문장을 작성해 주세요.")
                
            if s3_q2_m2 != "선택" and len(s3_q2_2) > 10:
                score += 2
                feedback.append("✅ (2) 문장 작성 완료")
            else:
                feedback.append("❌ (2) 문장을 작성해 주세요.")
                
        st.info(f"점수: {score}/4점\n\n" + "\n".join(feedback))

        if score < 4:
            st.session_state.incorrect_questions["세트 3 - 문항 2"] = {
                "point": "인공지능 작품의 가치와 인간 예술과의 차이점을 다른 설명 방법 2개로 비교 작성하기",
                "my_answer": f"(1) [{s3_q2_m1}] {s3_q2_1}\n(2) [{s3_q2_m2}] {s3_q2_2}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 3 - 문항 2", None)

    st.divider()
    
    st.subheader("[서·논술형 3] 영상 기획안 작성하기")
    s3_q3_a = st.text_input("Ⓐ 시각 요소 (인간 예술의 모습)", key="s3_3_a")
    s3_q3_a_eff = st.text_area("Ⓐ 시각 요소 효과 (지문 근거)", key="s3_3_a_eff")
    s3_q3_b = st.text_input("Ⓑ 청각 요소 (감동적 소리)", key="s3_3_b")
    s3_q3_b_eff = st.text_area("Ⓑ 청각 요소 효과 (지문 근거)", key="s3_3_b_eff")
    
    if st.button("세트 3-3 채점", key="btn_s3_3"):
        score = 0
        feedback = []
        
        if any(k in s3_q3_a for k in ["선수", "눈물", "노력", "열정", "교감"]):
            score += 1
            if any(k in s3_q3_a_eff for k in ["감정", "철학", "경험", "울림", "노력"]):
                score += 2
                feedback.append("✅ Ⓐ 시각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓐ 효과에 '지문 근거(인간의 감정/노력이 주는 울림)' 부족 (1점)")
        else:
            feedback.append("❌ Ⓐ 연출 오답: 인간의 노력과 감동을 드러내는 연출 필요")
            
        if any(k in s3_q3_b for k in ["오케스트라", "바이올린", "서정", "환호", "울림"]):
            score += 1
            if any(k in s3_q3_b_eff for k in ["감동", "대조", "따뜻한", "열정"]):
                score += 2
                feedback.append("✅ Ⓑ 청각 요소 및 지문 근거 효과 완벽함")
            else:
                feedback.append("⚠️ Ⓑ 효과에 '지문 근거' 부족 (1점)")
        else:
            feedback.append("❌ Ⓑ 연출 오답: 감동을 배가시키는 서정적 음향 연출 필요")
            
        st.info(f"점수: {score}/6점\n\n" + "\n".join(feedback))

        if score < 6:
            st.session_state.incorrect_questions["세트 3 - 문항 3"] = {
                "point": "인간 예술의 특성(노력, 열정, 감정)을 담은 영상 연출 및 마음의 울림 관련 본문 근거 서술",
                "my_answer": f"Ⓐ 시각: {s3_q3_a} / 효과: {s3_q3_a_eff}\nⒷ 청각: {s3_q3_b} / 효과: {s3_q3_b_eff}",
                "feedback": "\n".join(feedback)
            }
        else:
            st.session_state.incorrect_questions.pop("세트 3 - 문항 3", None)


# ==========================================
# 📌 [복습할 내용] 탭
# ==========================================
with tabs[3]:
    st.header("📌 조건 미충족 문항 복습하기")
    st.write("제출된 문항 중 조건에 미달하거나 감점된 문항의 핵심 복습 포인트와 작성 답안을 검토하세요.")
    
    if not st.session_state.incorrect_questions:
        st.success("🎉 축하합니다! 모든 문제의 조건을 완벽하게 충족했거나 아직 채점을 진행하지 않았습니다.")
    else:
        for q_title, info in st.session_state.incorrect_questions.items():
            with st.expander(f"❌ {q_title} - 복습 필요", expanded=True):
                st.markdown(f"**💡 핵심 복습 포인트**\n> {info['point']}")
                st.markdown("**✏️ 내가 제출한 답안**")
                st.code(info['my_answer'])
                st.markdown("**🔍 채점 피드백 및 부족한 점**")
                st.warning(info['feedback'])
