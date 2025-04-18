# 🏋️‍♂️ 헬스장 고객 이탈 분석 프로젝트 ✨🔥💻

## 🐢 팀명: 팀 거북거북 

## 📌 프로젝트 개요
헬스장 고객 데이터를 활용하여 **이탈 예측 모델**을 구축하고,  
분석 결과를 **시각화 및 웹 애플리케이션**으로 구현한 프로젝트입니다.

> 💡 머신러닝으로 고객 이탈을 사전에 예측하고,  
> 이를 통해 헬스장 운영 효율을 높이는 것이 목표입니다!

---

## 🏆 프로젝트 목표 및 배경
이 프로젝트의 주요 목표는 **헬스장 고객의 이탈을 예측**하는 것입니다.  
고객 이탈을 사전에 예측할 수 있다면, 헬스장 운영자들은 **고객 유지 전략**을 개선하고,  
**맞춤형 마케팅 전략**을 수립할 수 있습니다. 또한, 이를 통해 헬스장의 **수익성**을 높이고,  
**고객 만족도**를 개선할 수 있는 가능성이 있습니다.

---

## 📋 문제 정의
이 프로젝트는 **고객 데이터**에서 이탈 여부를 예측하는 문제를 다룹니다.  
구체적으로, 고객이 **이탈할 가능성**이 있는지 여부를 예측하여, 이탈을 방지할 수 있는  
전략을 도출하는 것이 목표입니다.

---

## 📄 데이터 출처
이 프로젝트에서 사용한 데이터는 **Kaggle**에서 제공하는 **Gym Churn Dataset**입니다.  
이 데이터셋은 헬스장의 고객 데이터를 포함하고 있으며, 고객의 기본 정보, 운동 방문 기록,  
그리고 이탈 여부를 포함합니다.

[👉 Kaggle Gym Churn Dataset 바로가기](https://www.kaggle.com/datasets/adrianvinueza/gym-customers-features-and-churn)


---

## 🧪 모델 성능
이 프로젝트에서 사용한 **머신러닝 모델**은 여러 가지 분류 모델을 비교하여 최적의 모델을 선정했습니다.  
**WeightedEnsemble_L2** 모델이 가장 높은 성능을 보였으며, 테스트 데이터셋에서 **정확도 96.37%**를 기록했습니다.  
모델의 성능을 평가하기 위해 **정밀도**, **재현율**, **F1-score** 등을 고려하였고,  
**WeightedEnsemble_L2**는 모든 평가 지표에서 우수한 성과를 보였습니다.
**WeightedEnsemble_L2**를 **cross_validation** 을 통해 데이터를 **5분할할** 한 후 5번 평가하고 평균을 내었습니다.

---

## 👨‍👩‍👧‍👦 팀원 소개

<div align="center">
  
<table>
  <tr>
    <td align="center" width="25%">
      <img src="./img/tt1.png" width="120px" height="120px"><br><br>
      <b>박슬기</b><br>
    </td>
    <td align="center" width="25%">
      <img src="./img/tt3.png" width="120px" height="120px"><br><br>
      <b>손현성</b><br>
    </td>
    <td align="center" width="25%">
      <img src="./img/tt4.png" width="120px" height="120px"><br><br>
      <b>이준배</b><br>
    </td>
    <td align="center" width="25%">
      <img src="./img/tt2.png" width="120px" height="120px"><br><br>
      <b>지상원</b><br>
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

---

### ✅ ERD(Entity Relationship Diagram)

> mysql 테이블 간의 관계를 시각화한 ERD입니다.

<div align="center">
  <img src="./img/erd.png" width="70%" alt="ERD 다이어그램">
</div>

---


## 🎨 Figma 프로토타입

> 어플리케이션 UI를 기획하고 디자인한 **Figma 프로토타입**입니다.  
> 각 페이지의 구조와 동작 방식을 시각적으로 확인할 수 있습니다.

[👉 Figma 프로토타입 보러가기](https://www.figma.com/proto/LVZggQL8duOJTETngRxvPG/2nd_Project?node-id=0-1&t=5xUii5nCHc80R47s-1)


---


## 📸 UI 사전 구성 이미지(화면 설계서)


| ![ppt1](./img/ppt1.png) | ![ppt2](./img/ppt2.png) | ![ppt3](./img/ppt3.png) | ![ppt4](./img/ppt4.png) |
|--------------------------|--------------------------|--------------------------|--------------------------|
| **대시보드** | **이탈 고객 분석** | **고객 이탈 예측 리스트** | **고객 상세** |

| ![ppt5](./img/ppt5.png) | ![ppt6](./img/ppt6.png) | ![ppt7](./img/ppt7.png) | ![ppt8](./img/ppt8.png) |
|--------------------------|--------------------------|--------------------------|--------------------------|
| **고객 관리 매니저** | **이벤트 생성** | **이벤트 생성 팝업창** | **이벤트 문자 발송** |

| ![ppt9](./img/ppt9.png) | ![ppt10](./img/ppt10.png) | ![ppt11](./img/ppt11.png) | ![ppt12](./img/ppt12.png) |
|--------------------------|--------------------------|--------------------------|--------------------------|
| **발송 완료 메시지 팝업1** | **발송 완료 메시지 팝업2** | **이벤트 수정 팝업** | **퀘스트 시스템 매니저1** |

| <img src="./img/ppt13.png" width="170px"> |
|--------------------------------------------|
| **퀘스트 시스템 매니저2** |

---

## 📄 데이터 컬럼 설명 페이지

### ✅ 원본 데이터 컬럼

| 컬럼명 | 설명 | 타입 | 예시값 |
|--------|------|------|--------|
| `gender` | 성별 (여자 0 / 남자 1) | int | 1 |
| `Near_Location` | 헬스장과의 거리 (멀다 0 / 가깝다 1) | int | 1 |
| `Partner` | 회사 할인 여부 (개인 0 / 할인 1) | int | 0 |
| `Promo_friends` | 지인 소개 여부 (없음 0 / 있음 1) | int | 1 |
| `Phone` | 연락처 제공 여부 (미제공 0 / 제공 1) | int | 1 |
| `Contract_period` | 계약 기간 (월 단위) | int | 12 |
| `Group_visits` | 그룹 세션 참여 여부 (No 0 / Yes 1) | int | 1 |
| `Age` | 나이 | int | 29 |
| `Avg_additional_charges_total` | 총 추가 요금 평균 | float | 55.6 |
| `Month_to_end_contract` | 계약 종료까지 남은 개월 수 | float | 1.0 |
| `Lifetime` | 총 헬스장 이용 기간 (개월 수) | int | 9 |
| `Avg_class_frequency_total` | 평균 수업 참가 횟수 | float | 2.3 |
| `Avg_class_frequency_current_month` | 이달 평균 수업 참가 횟수 | float | 1.8 |

---

### 🧠 파생 변수 (Feature Engineering)

| 컬럼명 | 설명 | 타입 | 예시값 |
|--------|------|------|--------|
| `social_connected` | 사회적 연결 수준 (`Partner + Promo_friends + Group_visits`) | int | 2 |
| `avg_monthly_add_charge` | 평균 월별 추가 요금 (`추가요금 / (이용기간+1)`) | float | 5.05 |
| `class_freq_ratio` | 수업 참가 비율 변화 (`이번달 / 전체 평균`) | float | 0.78 |
| `class_freq_change` | 수업 참가 횟수 변화량 (`이번달 - 전체`) | float | -0.5 |
| `contract_ending_soon` | 계약 만료 임박 여부 (1개월 이하: 1, 그 외: 0) | int | 1 |
| `social_connected_ratio` | 사회적 연결 비율 (`합 / 3`) | float | 0.67 |

---


## 🧪 분석 과정 및 결과

### 1. 데이터 수집 및 전처리 📂🧹
- 피처 엔지니어링
- 스케일링 및 스플릿

<div align="center">
  <img src="./img/datafeaturing.png" width="60%" alt="데이터 전처리 이미지">
</div>

### 2. EDA(탐색적 데이터 분석) 📊🔍
- 고객 분포 피처 중요도
- 상관관계 시각화 (heatmap 등)

<div align="center">
  <img src="./img/feature_importance.png" width="60%" alt="피처 중요도">
</div>
<div align="center">
  <img src="./img/label01grap.png" width="60%" alt="이탈 분포">
</div>
<div align="center">
  <img src="./img/heatmap_pearson.png" width="60%" alt="피처 히트맵">
</div>

### 3. 머신러닝 모델링 🤖📈
- 모델 선택 및 학습
- 평가

<div align="center">
  <img src="./img/leaderboard.png" width="60%" alt="머신러닝 모델 선택">
</div>
<div align="center">
  <img src="./img/modelscore.png" width="60%" alt="머신러닝 평가가">
</div>
<div align="center">
  <img src="./산출물/학습결과/model_result.png" width="60%" alt="머신러닝 모델 비교">
</div>

### 4. 예측 🤖📈
- 예측 및 분류
- 결과 그래프

<div align="center">
  <img src="./img/pred.png" width="60%" alt="예측 코드">
</div>
<div align="center">
  <img src="./img/countplot.png" width="60%" alt="예측 코드">
</div>

### 5. Streamlit 웹 앱 구현 🌐🖥️
- 위험도별 고객 분류 및 카운트
- 각종 그래프 제공
- 이벤트 및 퀘스트 페이지지

| ![sl1](./img/sl1.png) | ![sl2](./img/sl2.png) |
|-----------------------|-----------------------|
| **대시 보드** | **분석 그래프 페이지** |

| ![sl3](./img/sl3.png) | ![sl4](./img/sl4.png) |
|-----------------------|-----------------------|
| **고객이탈 위험도 선택 페이지** | **이탈 위험 고객 분석 페이지** |

| ![sl5](./img/sl5.png) | ![sl6](./img/sl6.png) |
|-----------------------|-----------------------|
| **고객 관리 매니저 페이지** | **고객 퀘스트 시스템 페이지** |

| <img src="./img/sl7.png" width="380px">  |
|-----------------------|
| **고객 퀘스트 랭킹 페이지** |

---

## 🪞 한 줄 회고 🧠💬

> 🧹 **박슬기**: "진짜 개발하러 와서 기획만 한 것 같긴 하지만;; 팀원들 덕분에 예전에 배웠던 것들도 다시 기억해낼 수 있었습니다. 하나하나 완성되어나가는 결과물을 보고 있자니 기분이 좋네요. 부족한 저지만 함께 잘 협업해준 팀원들과, 항상 친절히 가르쳐주신 선생님께 진심으로 감사드립니다."  
> 🤖 **손현성**: "크고 작은 문제들이 있었지만 팀원들과 함께 고민해보고 해결하는 과정에서 많은것을 배울 수 있었고, 모두가 노력한 만큼 결과물이 잘 나와서 함께한 팀원들에게 감사드립니다."
> 💻 **이준배**: "여러가지를 해보면서 수업을 들으며 공부하는 것과는 다른 성장하는 재미를 느낀거 같습니다. 항상 열심히 해준 팀원들에게도 감사합니다. 결과물들을 보니 뿌듯합니다"  
> 📊 **지상원**: "비록 부족한 저였지만 팀원들의 힘으로 이렇게 좋은 성과를 낼 수 있었던거 같습니다. 열정을 쏟은 만큼 결과물 또한 잘 나온거 같아 매우 기쁩니다!"

---


