# CLI
> Command Line Interface

###### 명령어를 통해 사용자와 컴퓨터가 상호작용하는 방식
##### CLI 명령은 완전하고 즉각적이다. (복구x)

<br>
<br>

# CLI vs GUI
- GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 성능을 상대적으로 더 많이 소모
- 수 많은 서버 / 개발 시스템이 CLI를 통한 조작 환경을 제공

<br>
<br>

# CLI 문법
```python
cd(change directory)
```
##### 디렉토리 변경 

```python
cd .
```
##### 현재 작업 중인 디렉토리를 확인

```python
cd ..
```
##### 현재의 상위 디렉토리 (부모폴더)

- 예
```python
cd ../cli
```
##### 현재 위치의 부모 위치에 있는 cli 폴더로 이동

<br>

---

<br>


```python
mkdir(make directory)
```
##### 폴더생성
```python
ls(list)
```
##### 현재 작업중인 폴더 안의 파일 목록
```python
ls -a
```
##### 숨겨진 파일까지 보여줌

<br>

---

<br>

```python
start (mac=open)
```
##### 폴더/파일 열기
```python
rm(remove)
```
##### 파일삭제 - 휴지통 x 영구삭제

```python
rm -r
```
##### 디렉토리 삭제

<br>
<br>

## CLI에서 가장 중요한 것은 나의 위치(경로)이다. 
- **절대경로** : Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것(pwd)
- **상대경로** : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것(cd)

