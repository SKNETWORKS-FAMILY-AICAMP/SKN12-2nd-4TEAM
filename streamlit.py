import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import matplotlib.font_manager as fm
import seaborn as sns
import time
from streamlit.components.v1 import html
import os
import base64



# ─── 페이지 설정 ─────────────────────────
st.set_page_config(page_title="고객 관리 매니저", layout="wide")
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# ─── DB 함수 ────────────────────────────
def get_connection():
    return mysql.connector.connect(
        host='127.0.0.1', port=3306,
        user='root', password='',
        database='quest_db', charset='utf8mb4'
    )
def fetch_customer_data(risk_level="전체"):
    """
    risk_level: '전체', '안전', '주의', '위험'
    predict_result 테이블의 predict_proba 컬럼 (0,1,2) 으로 필터링
    """
    conn = get_connection()
    try:
        # 1) 쿼리 생성
        query  = "SELECT * FROM predict_result"
        params = []
        if   risk_level == "안전":
            query += " WHERE predict_proba = %s"
            params = [0]
        elif risk_level == "주의":
            query += " WHERE predict_proba = %s"
            params = [1]
        elif risk_level == "위험":
            query += " WHERE predict_proba = %s"
            params = [2]
        # 전체일 땐 WHERE 절 없음

        # 2) SQL 실행
        df = pd.read_sql(query, conn, params=params)

        # 3) 컬럼명을 한글로 매핑
        kor_columns = [
            '성별',
            '거리',
            '파트너 여부',
            '프로모션 친구 여부',
            '전화번호',
            '계약 기간',
            '그룹 방문 여부',
            '나이',
            '추가 요금 총합',
            '계약 만료까지 남은 월',
            '총 이용 개월',
            '전체 수업 평균 횟수',
            '현재 월 수업 평균 횟수',
            '소셜 연결 여부',
            '월 평균 추가 요금',
            '수업 빈도 비율',
            '수업 빈도 변화',
            '계약 만료 임박 여부',
            '소셜 연결 비율',
            '이탈',          # 나중에 제거
            '예측 이탈',
            '이탈 레벨'
        ]
        if len(kor_columns) == len(df.columns):
            df.columns = kor_columns
        else:
            st.warning(f"컬럼 수 불일치: 기대 {len(kor_columns)} vs 실제 {len(df.columns)}")

        # 4) '이탈', '예측 이탈' 컬럼 제거
        df = df.drop(columns=['이탈', '예측 이탈'], errors='ignore')

        return df

    finally:
        conn.close()


def load_categories():
    conn = get_connection()
    df = pd.read_sql("SELECT id, title, description, risk_level FROM categories", conn)
    conn.close()
    return df

def load_predict_data_from_db():
    conn = get_connection()
    # predict_proba 별로 카운트
    df = pd.read_sql(
        """
        SELECT predict_proba, COUNT(*) AS cnt
        FROM predict_result
        GROUP BY predict_proba
        """,
        conn
    )
    conn.close()


    counts = {str(int(row.predict_proba)): int(row.cnt) for row in df.itertuples()}
    total = sum(counts.values())
    return counts, total

# ─── 콜백 함수 ─────────────────────────
def on_confirm(rid, title):
    # 실제 발송 로직...
    st.session_state.confirm_id = None
    placeholder = st.empty()
    placeholder.success(f"✅ ‘{title}’ 퀘스트가 발송되었습니다!")
    time.sleep(2)
    placeholder.empty()

# ─── 상수 정의 ─────────────────────────
PREDICT_LABELS = {"0": "안전", "1": "주의", "2": "위험"}
PREDICT_COLORS = {"0": "#9BD770", "1": "#F6A84F", "2": "#F44336"}
RISK_LABELS    = {'0': '안전', '1': '주의', '2': '위험', '3': '전체'}
RISK_COLORS    = {'0': '#9BD770', '1': '#F6A84F', '2': '#F44336', '3': '#B0BEC5'}

# ─── 세션 초기화 ────────────────────────
if 'menu' not in st.session_state:
    st.session_state.menu = 'DashBoard'
    st.session_state.risk_filter = '3'
    st.session_state.popup_open  = False
    st.session_state.selected    = ''
    st.session_state.target_cnt  = 0
    
if 'show_confirm' not in st.session_state:
    st.session_state.show_confirm     = False
    st.session_state.sel_title        = ""
    st.session_state.sel_target_count = 0
    
if 'confirm_id' not in st.session_state:
    st.session_state.confirm_id = None
    
if 'sent_ids' not in st.session_state:
    st.session_state.sent_ids = []
    
if 'menu' not in st.session_state:
    st.session_state.menu = "📊 DashBoard"
    
if 'risk_level' not in st.session_state:
    st.session_state.risk_level = "전체"
# ─── 사이드바 메뉴 ──────────────────────
with st.sidebar:
    st.markdown("## 메뉴")
    for label in [
        "DashBoard",
        "Churn Analytics",
        "Customer List",
        "Customer Management",
        "Customer Quest System"
    ]:
        if st.button(label):
            st.session_state.menu = label.replace("🔷 ", "")           
###################################################################################################
###################################################################################################
###################################################################################################
# ─── DashBoard ───────────────────────────
###################################################################################################
###################################################################################################
###################################################################################################
if st.session_state.menu == "DashBoard":
    # 1) 페이지 타이틀을 가운데 정렬
    st.markdown(
        "<h1 style='text-align:center; margin-bottom:0;'>이탈 위험 고객 관리</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("<hr style='margin-top:0;'>", unsafe_allow_html=True)

    # 2) 데이터 로드 & 필터링
    counts, total = load_predict_data_from_db()


    # 3) 카드 안에 총 유저·파일명 입력박스
    c1, c2 = st.columns([2,1])
    with c1:
        st.text_input("Total users", f"{total:,}", disabled=True)
    with c2:
        st.text_input("사용 데이터 이름", "predict_result.csv", disabled=True)

    st.markdown("<div style='height:1px; margin:16px 0; background:#eee;'></div>", unsafe_allow_html=True)

    # 4) 차트 영역
    if counts:
        labels = [PREDICT_LABELS[k] for k in ["0","1","2"]]
        vals   = [counts.get(k,0) for k in ["0","1","2"]]
        colors = [PREDICT_COLORS[k] for k in ["0","1","2"]]

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(labels, vals, color=colors, edgecolor="none")
        for bar, v in zip(ax.patches, vals):
            ax.text(
                bar.get_x() + bar.get_width()/2,
                v + max(vals) * 0.02,
                f"{v:,}",
                ha="center",
                va="bottom",
                fontsize=12,
            )
        ax.set_ylabel("")
        ax.set_xlabel("")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.grid(axis="y", color="#eee", linestyle="--", linewidth=1)
        ax.set_axisbelow(True)
        st.pyplot(fig)

    # 7) 카드 컨테이너 닫기
    st.markdown("</div>", unsafe_allow_html=True)
###################################################################################################
###################################################################################################
###################################################################################################
# ─── Churn Analytics & Customer List ────
###################################################################################################
###################################################################################################
###################################################################################################
elif st.session_state.menu == 'Churn Analytics':
    # 1) 중앙 정렬된 제목 + 구분선
    st.markdown(
        "<h1 style='text-align:center; margin-bottom:0;'>📉 이탈 위험 고객 분석</h1>"
        "<hr style='margin-top:0; margin-bottom:24px;'>",
        unsafe_allow_html=True
    )

    # 2) 드롭다운(선택 기준)과 요약정보 카드를 위한 컨테이너 시작 (생략)
    

    # 3) 선택 기준 + 데이터 개수 입력창처럼 표현
    col1, col2 = st.columns([2, 1])
    # 옵션 리스트 만들기
    eng_to_kor = {
        'gender': '성별', 'Near_Location': '근거리 거주 여부', 'Partner': '파트너 여부',
        'Promo_friends': '홍보 친구 수', 'Phone': '전화번호', 'Contract_period': '계약 기간',
        'Group_visits': '그룹 방문 횟수', 'Age': '나이',
        'Avg_additional_charges_total': '총 추가 요금 평균',
        'Month_to_end_contract': '계약 종료까지 개월 수', 'Lifetime': '이용 기간',
        'Avg_class_frequency_total': '총 수업 평균 빈도',
        'Avg_class_frequency_current_month': '이번 달 수업 평균 빈도'
    }
    # 컬럼 분류
    binary_label_map = {
        'gender': {0: '여자', 1: '남자'},
        'Near_Location': {0: '멀다', 1: '가깝다'},
        'Partner': {0: '개인', 1: '회사 할인'},
        'Promo_friends': {0: '없음', 1: '지인소개'},
        'Phone': {0: '미제공', 1: '제공'},
        'Group_visits': {0: 'No', 1: 'Yes'},
    }
    @st.cache_data
    def load_data():
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM predict_result", conn)
        conn.close()
        return df
    categorical_cols = [c for c in binary_label_map if c in eng_to_kor]
    duration_cols    = [c for c in ['Contract_period','Month_to_end_contract','Lifetime'] if c in eng_to_kor]
    usage_cols       = [c for c in ['Age','Avg_additional_charges_total','Avg_class_frequency_total','Avg_class_frequency_current_month'] if c in eng_to_kor]
    all_columns = [('📌 범주형', c) for c in categorical_cols] + \
                  [('⏳ 기간', c) for c in duration_cols] + \
                  [('💰 사용량', c) for c in usage_cols]
    column_options = [f"{grp} - {eng_to_kor[col]}" for grp, col in all_columns]
    column_map     = {opt: col for (grp, col), opt in zip(all_columns, column_options)}

    # 실제 selectbox
    selected_opt = st.selectbox("", column_options, label_visibility="collapsed")
    selected_col = column_map[selected_opt]
    selected_kor = eng_to_kor[selected_col]
    with col1:
        st.text_input("기준", selected_kor, disabled=True)
    with col2:
        # 예시로 전체 건수 표시 (Churn 예측 df.size)
        df_all = load_data()  # predict_result 전체
        st.text_input("전체 건수", f"{len(df_all):,}", disabled=True)

    st.markdown("<div style='height:1px; margin:16px 0; background:#eee;'></div>", unsafe_allow_html=True)

    # 4) 차트 그리기
    fig, ax = plt.subplots(figsize=(8, 4))
    group_labels = {0:'안전',1:'주의',2:'위험',3:'전체'}
    group_colors = {0:'#9BD770',1:'#F6A84F',2:'#F44336',3:'#B0BEC5'}

    if selected_col in categorical_cols:
        # 범주형: 도수분포
        grouped = df_all.groupby('predict_proba')[selected_col].value_counts().unstack(fill_value=0)
        overall = df_all[selected_col].value_counts().to_frame().T
        overall.index = [3]
        grouped = pd.concat([grouped, overall])
        grouped.columns = [binary_label_map[selected_col][v] for v in grouped.columns]
        grouped.index   = [group_labels[i] for i in grouped.index]
        grouped.plot(kind='bar', ax=ax, color=['#4A90E2','#F97F51'])
        for cont in ax.containers:
            ax.bar_label(cont, fmt='%d', label_type='edge')
        ax.set_ylabel("고객 수")
        ax.legend(title=selected_kor)
    else:
        # 수치형: 평균 비교
        means = df_all.groupby('predict_proba')[selected_col].mean()
        means.loc[3] = df_all[selected_col].mean()
        means = means.sort_index()
        means.index = [group_labels[i] for i in means.index]
        bars = ax.bar(
            means.index,
            means.values,
            color=[group_colors[i] for i in means.index.map({v:k for k,v in group_labels.items()})]
        )
        for bar in bars:
            ax.text(
                bar.get_x() + bar.get_width()/2,
                bar.get_height(),
                f"{bar.get_height():.2f}",
                ha='center', va='bottom'
            )
        ax.set_ylabel("평균값")

    # 차트 스타일 통일
    ax.set_xlabel("")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", color="#eee", linestyle="--", linewidth=1)
    ax.set_axisbelow(True)
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

    # 2) 상관관계 히트맵
    st.subheader("요인별 상관관계도")
    exclude = ['Churn','target','predict','predict_proba']
    num_df = df_all.select_dtypes(include='number').drop(columns=exclude, errors='ignore')
    num_df = num_df[[c for c in num_df.columns if c in eng_to_kor]]
    num_df.columns = [eng_to_kor[c] for c in num_df.columns]

    fig2, ax2 = plt.subplots(figsize=(10,8))
    sns.heatmap(num_df.corr(), annot=True, fmt=".2f", cmap="Blues", square=True, ax=ax2)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig2)

    st.info("색이 진할수록 서로 강한 상관관계를 지닌 것으로 분석됩니다.")
###################################################################################################
###################################################################################################
###################################################################################################
# ─── Customer List ────
###################################################################################################
###################################################################################################
###################################################################################################
elif st.session_state.menu == 'Customer List':
    st.header("👥 고객 리스트")
    st.subheader("고객 이탈 예측 위험도 선택")

    # 1) 위험도 필터 버튼
    spacer, col_all, col_safe, col_warn, col_danger = st.columns([6, 1, 1, 1, 1])

    with col_all:
        if st.button("전체"):
            st.session_state.risk_level = "전체"
    with col_safe:
        if st.button("안전"):
            st.session_state.risk_level = "안전"
    with col_warn:
        if st.button("주의"):
            st.session_state.risk_level = "주의"
    with col_danger:
        if st.button("위험"):
            st.session_state.risk_level = "위험"

    # 2) DB에서 데이터 조회
    df = fetch_customer_data(st.session_state.risk_level)
    customer_count = len(df)

    # 3) 요약 정보
    st.markdown(f"""
        <h3 style="font-size:20px">
          ✅ 선택된 위험도: <strong>{st.session_state.risk_level}</strong>  
          | 선택된 고객 수: <strong>{customer_count}명</strong>
        </h3>
    """, unsafe_allow_html=True)

    # 4) 결과 테이블 표시
    if not df.empty:
        st.dataframe(df)
    else:
        st.warning("⚠️ 해당 조건에 맞는 고객 데이터가 없습니다.")


###################################################################################################
###################################################################################################
###################################################################################################
# ─── Customer Management ─────────────────────────────
###################################################################################################
###################################################################################################
###################################################################################################
elif st.session_state.menu == 'Customer Management':
    st.header("👥 고객 관리 매니저")
    df = load_categories()
    df['label'] = df['risk_level'].map(RISK_LABELS)
    df['color'] = df['risk_level'].map(RISK_COLORS)

    # ── 필터: 오른쪽 정렬을 위해 spacer 추가 ─────────────────────
    spacer, col_all, col_safe, col_warn, col_danger = st.columns([6, 1, 1, 1, 1])
    if col_all.button("전체", key="filter_3"):
        st.session_state.risk_filter = '3'
    if col_safe.button("안전", key="filter_0"):
        st.session_state.risk_filter = '0'
    if col_warn.button("주의", key="filter_1"):
        st.session_state.risk_filter = '1'
    if col_danger.button("위험", key="filter_2"):
        st.session_state.risk_filter = '2'

    # 선택된 필터가 '전체'(3)가 아니면 리스크 레벨로 필터링
    if st.session_state.risk_filter != '3':
        df = df[df['risk_level'] == st.session_state.risk_filter]

    
    # 리스트
    st.markdown("### 전체 회원")
    for _, row in df.iterrows():
        # 만약 이 row 가 confirm 중이면 모달만 보여주고 루프 탈출
        if st.session_state.confirm_id == row['id']:
            placeholder = st.empty()
            placeholder.info(f"🚨 ‘{row['title']}’ 퀘스트를 발송하시겠습니까?")
            c1, c2 = st.columns(2)
            with c1:
                st.button(
                    "✅ 발송",
                    key=f"do_confirm_{row['id']}",
                    on_click=lambda rid=row['id'], title=row['title']: on_confirm(rid, title)
                )
            with c2:
                st.button(
                    "❌ 취소",
                    key=f"do_cancel_{row['id']}",
                    on_click=lambda: st.session_state.update(confirm_id=None)
                )
            break

        # 평소 expander + 발송 버튼
        with st.expander(f"📌 {row['title']} ({row['label']})"):
            st.markdown(f"<span style='color:{row['color']};'>{row['description']}</span>",
                        unsafe_allow_html=True)
            st.button(
                "📩 문자 발송",
                key=f"send_{row['id']}",
                on_click=lambda rid=row['id']: st.session_state.update(confirm_id=rid)
            )

###################################################################################################
###################################################################################################
###################################################################################################
# ─── Customer Quest System ─────────────────────────────
###################################################################################################
###################################################################################################
###################################################################################################
elif st.session_state.menu == 'Customer Quest System':
    st.header("🧩 고객 퀘스트 시스템")

    # ─── CSS: full-width quest rows + 필터 컬럼 ─────────────────────
    st.markdown("""
    <style>
    main .block-container {
      max-width: 100% !important;
      padding-left: 1rem;
      padding-right: 1rem;
    }
    .quest-row {
      border: 1px solid #4b4b4b;
      border-radius: 8px;
      padding: 12px 16px;
      margin-bottom: 12px;
    }
    .quest-row .row-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .quest-row .cell {
      font-size: 16px;
      overflow: hidden;
      white-space: nowrap;
    }
    .quest-row .cell.name     { flex: 2; text-align: left;  font-size:18px; }
    .quest-row .cell.text     { flex: 1.2; }
    .quest-row .cell.progress { flex: 5;   }
    .quest-row .cell.score    { flex: 1;   }
    .quest-row .cell.status,
    .quest-row .cell.star     { flex: 0 0 30px; }
    .quest-row .cell.filter   { flex: 1.5; text-align: right; }

    .quest-row progress {
      width: 100%;
      height: 1rem;
      accent-color: #9BD770;
    }
    </style>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["퀘스트 관리", "랭킹"])

    # ─── TAB1: 퀘스트 관리 with 필터 이모지 ─────────────────────────
    with tab1:
        st.subheader("퀘스트 관리")

        # 1) 오른쪽 상단 필터 버튼 (투명 버튼 대신 이모지)
        cols = st.columns([6, 1, 1, 1, 1])
        if 'quest_filter' not in st.session_state:
            st.session_state.quest_filter = "전체"
        if cols[1].button("전체"): st.session_state.quest_filter = "전체"
        if cols[2].button("안전"): st.session_state.quest_filter = "안전"
        if cols[3].button("주의"): st.session_state.quest_filter = "주의"
        if cols[4].button("위험"): st.session_state.quest_filter = "위험"

        # 2) 퀘스트 목록 및 필터 매핑
        quests = [
            {"name":"출석체크",      "cur":300, "tgt":4000, "score":10,  "lvl":"안전"},
            {"name":"오운완 업로드", "cur":750,  "tgt":4000, "score":10,  "lvl":"주의"},
            {"name":"PT 체험",      "cur":10,  "tgt":1890, "score":50,  "lvl":"주의"},
            {"name":"3일 연속 방문", "cur":35,   "tgt":100,  "score":10,  "lvl":"안전"},
            {"name":"복귀 미션",     "cur":20, "tgt":213,  "score":500, "lvl":"위험"},
            {"name":"주 3회 출석",   "cur":400,  "tgt":2354, "score":70,  "lvl":"위험"},
        ]
        mapping = {
            "전체": [0,1,2,3,4,5],
            "안전": [0,1,2],
            "주의": [0,1,3,5],
            "위험": [0,1,4,5],
        }
        emojis = ["🔵","🟢","🟡","🟠"]
        grey   = "⚪"

        # 3) 리스트 렌더링
        for i in mapping[st.session_state.quest_filter]:
            q = quests[i]
            # status = "🟢" if q["lvl"]=="안전" else "🟠" if q["lvl"]=="주의" else "🔴"  # 제거
            # star   = "⭐" if q["score"]>=70 else ""                                 # 제거
            circles = "".join(
                emojis[j] if i in mapping[label] else grey
                for j,label in enumerate(["전체","안전","주의","위험"])
            )
            st.markdown(f"""
            <div class="quest-row">
              <div class="row-inner">
                <div class="cell name">{q['name']}</div>
                <div class="cell text">{q['cur']} / {q['tgt']}</div>
                <div class="cell progress">
                  <progress value="{q['cur']}" max="{q['tgt']}"></progress>
                </div>
                <div class="cell score">🏅 {q['score']}</div>
                <div class="cell filter">{circles}</div>  <!-- 필터 이모지만 남김 -->
              </div>
            </div>
            """, unsafe_allow_html=True)


    # ─── TAB2: 랭킹 ─────────────────────────────────────────
    with tab2:
        def get_base64_image(image_path):
            if not os.path.exists(image_path):
                print(f"이미지 파일 없음: {image_path}")
                return ""
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    
        # base64 이미지 딕셔너리 정의 (이미지를 base64로 변환)
        base_path = os.path.join(os.getcwd(), "img", "streamlit_img")
        crown_images_base64 = {
            1: get_base64_image(os.path.join(base_path, "금관.png")),
            2: get_base64_image(os.path.join(base_path, "은관.png")),
            3: get_base64_image(os.path.join(base_path, "동관.png")),
        }
    
        st.subheader("📊 랭킹")
    
        data = [
            {"rank": 1, "name": "이규영", "attendance": 330, "quests": 320, "score": 3540},
            {"rank": 2, "name": "김도윤", "attendance": 342, "quests": 300, "score": 3360},
            {"rank": 3, "name": "권성호", "attendance": 326, "quests": 289, "score": 3120},
            {"rank": 4, "name": "지상원", "attendance": 311, "quests": 264, "score": 2980},
            {"rank": 5, "name": "이준배", "attendance": 309, "quests": 261, "score": 2970},
            {"rank": 6, "name": "송현석", "attendance": 298, "quests": 249, "score": 2840},
            {"rank": 7, "name": "박슬기", "attendance": 281, "quests": 240, "score": 2670},
        ]
    
        for user in data:
            c1, c2, c3, c4, c5, c6, c7 = st.columns([0.8, 1.5, 2, 1.5, 1.2, 2, 0.5])
    
            with c1:
                crown_img_html = ""
                if user["rank"] in crown_images_base64 and crown_images_base64[user["rank"]]:
                    img_base64 = crown_images_base64[user["rank"]]
                    # 왕관 크기 1.5배로 증가, 가운데 정렬을 위해 display: block과 margin을 사용
                    crown_img_html = f'<img src="data:image/png;base64,{img_base64}" height="54" style="display:block; margin: 0 auto;">'
    
                st.markdown(
                    f"""
                    <div style='display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 6px;'>
                        <span style='font-size: 20px; font-weight: bold;'>{user['rank']}</span>
                        {crown_img_html}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with c2:
                st.markdown(f"**{user['name']}**")
            with c3:
                st.markdown(f"**출석율 {user['attendance']} / 365  ({round(user['attendance']/365*100, 2)}%)**")
            with c4:
                st.progress(user['attendance'] / 365)
            with c5:
                st.markdown(f"🏆 **{user['score']}**")
            with c6:
                st.markdown(f"**🎯 퀘스트 달성수: {user['quests']}**")
            with c7:
                st.markdown("🟢")
            st.markdown("---")