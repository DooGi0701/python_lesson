## 1.0 Git project 시작하기
- `git init`
  - 내 프로젝트를 git이 관리한다
  - 한번 더 쓰면 초기화 됨
- `git add [경로]`:
- commit할 파일을 정한다.
  ```shell
  git add . #모든 폴더와 파일을 추가한다.
  git add images/ #특정 폴더만 추가한다.
  git add main.py #특정 파일만 추가한다.
  ```
- `git commit -m "제목"`: 작업한 이력을 기록한다.