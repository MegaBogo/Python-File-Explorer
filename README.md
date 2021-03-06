# 파일 / 디렉토리만 보여주는 탐색기 [19.03.10]

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

<https://docs.python.org/3/library/os.html><br />

## 작업 흐름

실행하면 현재 디렉토리 목록을 보여주고
file들을 files 에 담기

키보드 명령어를 받아 exit이면 종료
cd ..하면 뒤로 이동가기

디렉토리 목록을 파일/디렉토리로 구분하여
파일인 경우는 파일 내용을 출력하고
디렉토리인 경우는 입력한 디렉토리로 경로 변경해주기!

## 가능한가?
### 1. 디렉토리 목록을 보여주는 함수는 무엇인가?
- os.listdir(dirname)
: dirname에 있는 디렉토리 목록을 보여준다

- os.walk(dirname)
: dirname에 있는 시작 디렉토리부터 하위 디렉토리를 차례대로 보여준다

현재 디렉토리만 보여주는 기능을 원하기때문에 os.listdir(dirname)으로 작업했다.

### 2. 파일명의 확장자만 추출할 수 있는게 있는가?
os.path.splitext(full_filename)
: 파일 이름과 확장자를 한 쌍이 되도록 해주는 함수!<br />
  os.path.splitext(full_filename)[-1]를 사용하면 파일의 확장자를 가져올 수 있다

### 3. 파일/디렉토리 여부를 알려주는가?
os모듈에서 파일 존재 / 디렉토리 존재 여부를 알려주는 함수가 존재했다.

1. 파일 존재 여부<br />
: os.path.isdir(path)

2. 디렉토리 존재 여부<br />
: os.path.isdir(path)

### 4. 디렉토리를 변경해주는 함수가 있는가?
os.chdir(path)
: path의 값으로 디렉토리를 변경해준다.


## 정리한 내용 토대로 작업한 결과물
<img src="intro-img2.gif"></img><br />
파일/디렉토리 구분은 끝났다.

이제 이미지를 binary해서 뿌려줄지(...) 아니면 아예 제외를 해야하는지에 대한 부분.<br />
그리고 cd ..에서 그치는게 아니라 좀 더 쉽게 쓸 수 있는 기능을 추가는 부분
그리고 FileExplorer을 재활용 할 수 있게 하는 작업등이 나에게 남은 숙제이다!








