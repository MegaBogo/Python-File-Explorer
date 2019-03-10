# 파일 / 디렉토리만 보여주는 탐색기

## 기능
- 파일인 경우는 파일 내용을 보여주자
- 디렉토리인 경우는 해당 디렉토리로 이동시켜주고
  리스트를 보여주자

## 조건
- Ptyhon 내장모듈만 사용하자

## 작업 흐름
main.py을 실행하면 현재 디렉토리 목록을 보여주고
file들을 files 에 담기

키보드 명령어를 받아 exit이면 종료
cd ..하면 뒤로 이동가기

그외에
```
for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    ext = os.path.splitext(full_filename)[-1]
    if(ext == ''):
        ext = 'directory'
```





<img width="600" height="300" src="intro-img.gif"></img>
