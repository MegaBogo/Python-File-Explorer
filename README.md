# 파일 / 디렉토리만 보여주는 탐색기

## 기능
- 파일인 경우는 파일 내용을 보여주자
- 디렉토리인 경우는 해당 디렉토리로 이동시켜주고
  리스트를 보여주자

## 조건
- Ptyhon 내장모듈만 사용하자

## 찾아보기
Python 내장모듈에 파일/디렉토리/목록/경로등을 제공하는 모듈이 있는가?!

있었다!
바로 os모듈!
Operating System의 약어로 현재 경로를 가져오기, 디렉토리 목록 가져오기등 
운영체제에서 제공되는 다양한 기능을 파이썬에서 사용할 수 있게 해준 모듈이였다!

## 작업 흐름

main.py을 실행하면 현재 디렉토리 목록을 보여주고
file들을 files 에 담기

키보드 명령어를 받아 exit이면 종료
cd ..하면 뒤로 이동가기

###1. os모듈에서 디렉토리 목록을 보여주는 함수는 무엇인가?
- os.listdir(dirname)
: dirname에 있는 디렉토리 목록을 보여준다

- os.walk(dirname)
: dirname에 있는 시작 디렉토리부터 하위 디렉토리를 차례대로 보여준다

현재 디렉토리만 보여주는 기능을 원하기때문에 os.listdir(dirname)으로 작업했다.

그외
```python
for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    ext = os.path.splitext(full_filename)[-1]
    if(ext == ''):
        ext = 'directory'
```




<img width="600" height="300" src="intro-img.gif"></img>
