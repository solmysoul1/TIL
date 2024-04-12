# git

<br>

## branch
> 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 git의 도구

1. 독립 공간을 형성, 원본이 안전하다.
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적으로 협업과 개발이 가능하다.
3. 쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있다. 

- Master(main)브랜치
    - 사용자가 사용하고 있는 버전, 세상에 공개되어있으므로 함부로 수정, 복원, 삭제해서는 안됨
 
### branch 명령어

```shell
git init 

git branch # 브랜치 목록 확인

git branch -r # 원격 저장소의 브랜치 목록 확인

git branch hotfix # hotfix 라는 브랜치 생성

git branch -d # 병합된 브랜치만 삭제

git branch -D # 강제 삭제 (병합되지 않은 브랜치도 삭제 가능)
```
#### git switch 
> HEAD(현재 브랜치를 가리키는 포인터)를 이동

```shell
git switch branch_name # 다른 브랜치로 이동

git switch -c branch_name # 브랜치를 새로 만듦과 동시에 해당 브랜치로 이동

git switch -c branch_name commit_id # 특정 커밋 기준으로 브랜치 생성과 동시에 이동
```
#### git switch 주의사항
- git switch 하기 전 working directory 에 기록 되어 있는 지 확인

<br>

## branch merging (브랜치 병합)

> 분기된 브랜치를 하나로 병합

- **merge 수행 전 일단 다른 브랜치를 합치려고 하는 메인 브랜치로 switch 해야함**

### 병합의 종류
1. Fast-Forward
- merge 과정 없이 단순히 브랜치의 포인터가 이동
2. 3-Way-Merge (Merge commit)
- 병합 시 각 브랜치의 커밋 두 개와 공통 조상 커밋 하나를 사용하여 병합하는 것
    - 두 브랜치에서 다른 파일 혹은 같은 파일의 다른 부분을 수정했을 때 수행 가능한 병합
3. Merge Conflict
- 병합하는 두 브랜치에서 같은 파일의 같은 부분을 수정한 경우