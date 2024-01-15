# Git
> 분산 버전 관리 시스템 <br> 코드의 변경 이력을 기록하고 협업을 원활하게 하는 도구 
##### 버전관리 : 변화를 기록하고 추적하는 것
<br>
## 중앙 vs 분산

- 중앙집중식 : 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드 
    - 기본 버전 관리는 불필요한 메모리의 소모가 있다. 
- 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리
    - 중앙서버에 의존하지 않고도 동시에 다양한 작업을 수행할 수 있음
    - 개발자들 간의 작업 충돌을 줄여주고 개발 생산성을 향상시킴
    - 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음
    - 변화한 부분만 저장해 메모리의 소모가 적으며 조회 시간이 적게 걸린다. 
    - 개발되어 온 과정을 파악할 수 있다.
    - 이전 버전과의 변경 사항을 비교할 수 있다.

<br>

# git의 3가지 영역
- Working Directory
    - 현재 작업 중인 위치
- Staging Area
    - Working Directory에서 변경된 파일 중, 다음 버전에 포함 시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository
    - 버전 commit 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록됨

<br>

# Git의 동작

```python
git init : 로컬 저장소 설정 (초기화), git 의 버전관리를 시작할 디렉토리에서 진행, 경로확인필수
```
```python
git add : Staging Area 에 추가
```
```python
git add . : 모든 파일을 스테이징
```
```python
git add *.txt* : 확장자가 txt인 파일만 스테이징
```
```python
git rm --cached <파일> : Staging Area에서 제거 
```
```python
git commit -m "commit message" : 해당 시점의 버전을 생성하고 변경이력을 남김
```
```python
git status : 현재상태
```
```python
git log : commit 기록
```
```python
git log --oneline : git log를 간략하게 보여줌
```
```python
git log --online --graph : git log를 그래프로 보여줌
```

### [git 공식문서]('https://git-scm.com/book/ko/v2')
