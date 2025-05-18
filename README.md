# 📝 DRF 기반 블로그 프로젝트

Django REST Framework와 Bootstrap을 활용한 API 기반 블로그 프로젝트입니다.  
회원 기능, 게시글 작성/수정/삭제, 댓글, 검색 기능 등을 구현했으며,  
프론트엔드는 Django 템플릿 + JavaScript `fetch()` 방식으로 직접 연동했습니다.
(ENG Version below)
---

## 💡 주요 기능

- ✅ 게시글 CRUD (REST API)
- ✅ 댓글 기능 (API 기반)
- ✅ 검색 기능 (제목/내용 기준)
- ✅ 로그인 / 로그아웃 / 회원가입
- ✅ 사용자 인증에 따른 권한 분리
- ✅ 작성자만 글/댓글 수정/삭제 가능
- ✅ Bootstrap 기반 UI
- ✅ GitHub 연동 및 프로젝트 정리 완료


---

## 🛠 사용 기술

| 구분 | 기술 |
|------|------|
| 백엔드 | Django 5.2.1, Django REST Framework |
| 프론트엔드 | HTML5, CSS3, Bootstrap 5, JavaScript |
| 인증 | Django 세션 기반 인증 |
| 개발환경 | Python 3.12, VSCode, macOS |

---

## 🚀 실행 방법 (로컬)

```bash
git clone https://github.com/KangMirae/drf-blog.git
cd drf-blog
python -m venv venv
source venv/bin/activate      # 윈도우: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## 📁 디렉토리 구조 요약

drf-blog/
├── blog/                   # 게시글/댓글/뷰/API
├── drf_blog/               # 설정 및 URL
├── templates/              # HTML 템플릿들
├── static/ (선택)          # 정적 파일
├── venv/                   # 가상환경 (제외)
└── requirements.txt

---

## ✨ 향후 개선 아이디어

* 이미지 업로드 기능
* 댓글 수정/삭제
* 태그 / 카테고리 분류
* 프론트엔드 React로 분리

---

## 📬 만든 사람
by @KangMirae

(ENG)-------------------------------------------------------------


# 📝 DRF-based Blog Project

This is an API-based blog project built with Django REST Framework and Bootstrap.  
It includes features such as user authentication, CRUD for posts, comment support, search functionality, and more.  
The frontend uses Django templates along with `fetch()` in JavaScript to interact with the REST API.

---

## 💡 Key Features

- ✅ Full CRUD for blog posts via REST API
- ✅ API-based comment system
- ✅ Search functionality (by title/content)
- ✅ User authentication (signup/login/logout)
- ✅ Authorization: only authors can edit/delete their content
- ✅ Bootstrap-based responsive UI
- ✅ GitHub integrated & documented

---

## 🛠 Tech Stack

| Layer | Tech |
|-------|------|
| Backend | Django 5.2.1, Django REST Framework |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Auth | Django Session Authentication |
| Environment | Python 3.12, VSCode, macOS |

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/KangMirae/drf-blog.git
cd drf-blog
python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## 📁 Project Structure Overview

drf-blog/
├── blog/                   # Core app: posts, comments, views, API
├── drf_blog/               # Project configuration and routing
├── templates/              # HTML templates
├── static/ (optional)      # Static files
├── venv/                   # Virtual environment (excluded from version control)
└── requirements.txt

---

## ✨ Future Improvements

* Image uploads
* Comment editing/deleting
* Tags / Category support
* Refactor frontend into React SPA

---

## 📬 Author
by @KangMirae
