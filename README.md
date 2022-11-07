#B1팀 팀프로젝트 (넷플릭스 클론코딩)

## 프로젝트 이름

### 짭플릭스

## 프로젝트 소개

### 넷플릭스 클론코딩, 사용자의 취향에 맞춰서 영화 추천

## 팀 이름

### 싸지방

## 팀원 소개

박준석 

[devjunseok - Overview](https://github.com/devjunseok)

노우석 

[WooSeok-Nho - Overview](https://github.com/WooSeok-Nho/)

성창남 

[SungChangNam - Overview](https://github.com/SungChangNam)

양기철 

[hanmariyang - Overview](https://github.com/hanmariyang)

이태겸 

[poro625 - Overview](https://github.com/poro625)

## 개발 역할 분담

### 프론트엔드 - 양기철 성창남

### 최상위 템플릿

- [ ]  home.html (영화 목록, 영화 클릭하면 영화 상세 페이지로 이동(모달로 처리))
- [ ]  base.html (위에 navbar, 검색창, 글쓰기버튼, 홈버튼, 알림, 베이스 html)
- [ ]  footer.html (하단에 팀 소개)

### users 템플릿

- [ ]  login.html (로그인페이지)
- [ ]  signup.html (회원가입페이지)
- [ ]  profile_edit.html (회원정보 수정 페이지)
- [ ]  profile_edit_password.html(비밀번호 수정 페이지)
- [ ]  follow.html (회원정보 읽기, 팔로우,팔로워 페이지)

### contents 템플릿

- [ ]  upload.html (리뷰 업로드)
- [ ]  update.html (게시글 수정 페이지)
- [ ]  search.html (검색페이지)
- [ ]  recommend.html(추천 페이지)

### JavaScript

### 백엔드 - 팀원 모두

- 로그인 기능(users) - 박준석, 이태겸,
    - [ ]  회원가입 (email, 이름,비밀번호)
    - [ ]  로그인
    - [ ]  로그아웃
    - [ ]  내 프로필 편집(비밀번호 변경, 이메일 변경)
    - [ ]  회원탈퇴
    - [ ]  마이페이지
- 게시글 기능(contents) - 노우석, 양기철, 성창남
    - [ ]  리뷰삭제(본인의 글만)
    - [ ]  리뷰올리기+ 리뷰 수정(본인의 글만)
    - [ ]  좋아요
    - [ ]  검색
    - [ ]  영화 찜하기(ManyToMany Field 사용)
- 자동 장르 분류
    
    [The Movie Database API (themoviedb.org)](https://developers.themoviedb.org/3/configuration/get-api-configuration) API 사용
    
- 영상 추천 서비스 - 박준석, 이태겸, 노우석
    - [ ]  넷플릭스 데이터 크롤링
    - [ ]  영상 추천
- 추가로 시도해 볼 기능들
    - [ ]  팔로우, 팔로워
    - [ ]  태그
    - [ ]  별점
    - [ ]  이메일인증
    - [ ]  소셜로그인
    - [ ]  알림

## 개발 일정

- 11-02 (SA 작성 및 프로젝트 세팅)
- 11-03 (백엔드 API 구현)
- 11-04 (프론트-머신러닝 시작)
- 11-05 (프론트 - 머신러닝 구현)
- 11-06 (프론트 - 머신러닝 구현)
- 11-07 (프로젝트 마무리)
- 11-08 (발표 및 발표준비)
- 주말에는 계획된 일정 제외하고 남는 시간은 프로젝트 참여하기

## 사용하는 기술

- python (3.10.7)
- Django (4.1.1)
- HTML
- css
- JavaScript
- sqlite
- git
- yolov5
- PyTorch

## 와이어프레임

[https://www.figma.com/file/wsYCpFHXM7p0kYlyA5zzds/Jjapflix?node-id=0%3A1](https://www.figma.com/file/wsYCpFHXM7p0kYlyA5zzds/Jjapflix?node-id=0%3A1)

![image.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52dcda2d-3527-4da0-ac5d-bb06ee2dc624/image.png)

## DB erd

![20221102_234014.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4476258f-2a29-42ae-bd13-eb9c94948be4/20221102_234014.png)

## API 명세서

[프로젝트 API 설계하기](https://www.notion.so/cc193929825143c287af74705b5a5421)
