# FastAPI Application

FastAPI 기반 REST API 서버

## 프로젝트 구조

```
FastAPI/
├── app/
│   ├── config/          # 데이터베이스 설정
│   ├── core/            # 핵심 설정 (config.py)
│   ├── endpoints/       # API 엔드포인트
│   ├── impl/            # 비즈니스 로직 구현
│   ├── middleware/      # 미들웨어
│   ├── models/          # SQLAlchemy 모델
│   ├── schemas/         # Pydantic 스키마
│   └── utils/           # 유틸리티 함수
├── app.py               # 메인 애플리케이션
├── requirements.txt     # 의존성 패키지
└── .env.example         # 환경 변수 예시
```

## 설치 방법

1. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. 의존성 설치

```bash
pip install -r requirements.txt
```

3. 환경 변수 설정

```bash
cp .env.example .env
# .env 파일을 편집하여 필요한 설정 변경
```

## 실행 방법

```bash
python app.py
```

또는

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## API 문서

서버 실행 후 다음 URL에서 API 문서 확인 가능:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 엔드포인트

### Health Check
- `GET /api/v1/health/` - 헬스 체크

### Users
- `POST /api/v1/users/` - 사용자 생성
- `GET /api/v1/users/` - 사용자 목록 조회
- `GET /api/v1/users/{user_id}` - 사용자 상세 조회
- `PUT /api/v1/users/{user_id}` - 사용자 수정
- `DELETE /api/v1/users/{user_id}` - 사용자 삭제

### Items
- `POST /api/v1/items/` - 아이템 생성
- `GET /api/v1/items/` - 아이템 목록 조회
- `GET /api/v1/items/{item_id}` - 아이템 상세 조회
- `GET /api/v1/items/owner/{owner_id}` - 특정 사용자의 아이템 조회
- `PUT /api/v1/items/{item_id}` - 아이템 수정
- `DELETE /api/v1/items/{item_id}` - 아이템 삭제
"# fastapi" 
