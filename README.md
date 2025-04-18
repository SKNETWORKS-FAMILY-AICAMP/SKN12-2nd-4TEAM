# 🏋️‍♂️ 헬스장 고객 이탈 분석 프로젝트 ✨🔥💻

## 📌 프로젝트 개요
헬스장 고객 데이터를 활용하여 **이탈 예측 모델**을 구축하고,  
분석 결과를 **시각화 및 웹 애플리케이션**으로 구현한 프로젝트입니다.

> 💡 머신러닝으로 고객 이탈을 사전에 예측하고,  
> 이를 통해 헬스장 운영 효율을 높이는 것이 목표입니다!

---

## 👨‍👩‍👧‍👦 팀원 소개

<div align="center">
  
<table>
  <tr>
    <td align="center" width="25%">
      <img src="./images/member1.jpg" width="120px"><br><br>
      <b>김OO</b><br>
      데이터 전처리 & EDA
    </td>
    <td align="center" width="25%">
      <img src="./images/member2.jpg" width="120px"><br><br>
      <b>박OO</b><br>
      모델링 & AutoML
    </td>
    <td align="center" width="25%">
      <img src="./images/member3.jpg" width="120px"><br><br>
      <b>이OO</b><br>
      웹 개발 (Streamlit)
    </td>
    <td align="center" width="25%">
      <img src="./images/member4.jpg" width="120px"><br><br>
      <b>최OO</b><br>
      기획 & 시각화
    </td>
  </tr>
</table>

</div>

---

## 🛠️ 사용 기술 스택 ⚙️📊🧠
- **언어**: Python 3.x  
- **라이브러리**: pandas, numpy, matplotlib, seaborn, scikit-learn, AutoGluon  
- **웹 프레임워크**: Streamlit  
- **DB**: MySQL  
- **협업**: Git, GitHub, Notion

---

## 🧪 분석 과정 및 결과

### 1. 데이터 수집 및 전처리 📂🧹
- 결측치 처리 및 이상치 제거
- 범주형 변수 인코딩 및 스케일링

<div align="center">
  <img src="./images/data_preprocessing.png" width="60%" alt="데이터 전처리 이미지">
</div>

### 2. EDA(탐색적 데이터 분석) 📊🔍
- 고객 분포 및 이탈률 분석
- 상관관계 시각화 (heatmap 등)

<div align="center">
  <img src="./images/eda_analysis.png" width="60%" alt="EDA 분석 이미지">
</div>

### 3. 머신러닝 모델링 🤖📈
- 분류 모델 비교 (RandomForest, XGBoost, AutoML 등)
- 최적 모델 선정 및 성능 평가

<div align="center">
  <img src="./images/machine_learning.png" width="60%" alt="머신러닝 모델링 이미지">
</div>

### 4. Streamlit 웹 앱 구현 🌐🖥️
- 고객 정보 입력 → 이탈 예측 결과 출력
- 이탈률 대시보드 제공
- DB 연동 기능 구현

<div align="center">
  <img src="./images/streamlit_app.png" width="60%" alt="Streamlit 앱 이미지">
</div>

---

## 📄 데이터 컬럼 설명 페이지
[👉 데이터 컬럼 설명 바로가기](./pages/columns.md)  
> 각 컬럼의 의미, 데이터 타입, 예시값 등을 정리한 문서입니다.  
> 예:  
> - `customer_id`: 고객 고유 ID (예: C001)  
> - `membership_type`: 회원권 종류 (Basic / Premium 등)  
> - `visit_count`: 최근 한 달간 방문 횟수  
> - `churn`: 이탈 여부 (0: 유지, 1: 이탈)  

---

## 📷 주요 화면 예시
| 고객 이탈 예측 | 대시보드 예시 |
|----------------|---------------|
| ![예측 화면](./images/predict.png) | ![대시보드 화면](./images/dashboard.png) |

---

## 🪞 한 줄 회고 🧠💬

> 🧹 **김OO**: "데이터 전처리가 얼마나 중요한지 체감했습니다."  
> 🤖 **박OO**: "AutoML로도 충분히 좋은 성능을 낼 수 있단 걸 배웠어요!"  
> 💻 **이OO**: "처음 해본 Streamlit 개발이 정말 재미있었습니다."  
> 📊 **최OO**: "협업의 힘을 느낄 수 있었던 소중한 경험이었습니다."

---

## 🔗 출처 및 참고 링크
- 📘 [Kaggle Gym Churn Dataset](https://www.kaggle.com/datasets) (사용한 데이터셋 출처)
- 📘 [Streamlit 공식 문서](https://docs.streamlit.io/)
- 📘 [AutoGluon 공식 GitHub](https://github.com/autogluon/autogluon)

---

## 📮 Contact
> 궁금한 점이나 피드백은 언제든지 환영입니다!  
> 팀 이메일: team4gym@naver.com

---
