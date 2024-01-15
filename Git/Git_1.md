## Remote Repository
> 리모트 저장소는 인터넷이나 네트워크 어딘가에 있는 저장소를 말한다. 

## Git & Github
```shell
git remote add origin remote_repo_url : 리모트 저장소와 연결 
origin : 추가하는 원격저장소의 닉네임

git remote -v : 연결된 리모트 저장소를 보여줌

git push -u origin master : 원격 저장소에 commit 목록을 업로드
-u : Upstream

git clone remote_repo_url : 원격저장소를 클론 받아옴
git init 되어 있는 곳에 하면 안됨
```
<br>

### fetch vs pull
- **fetch** : git fetch 명령은 리모트 저장소의 데이터를 모두 로컬로 가져오지만, 자동으로 merge하지 않는다. 
- **pull** : git pull 명령은 리모트 저장소 브랜치에서 데이터를 가져올 뿐만 아니라 자동으로 로컬 브랜치와 merge 시킬 수 있다.

### push 
- 프로젝트를 공유하고 싶을 때 Upstream 저장소에 push할 수 있다.

### pull vs clone 
- **pull** : 원격저장소와 이미 연결되어 있어서 받아오는 것 
- **clone** : 로컬에 git 저장소가 없는 상태에서 원격 저장소 전체를 복제하는 것 (git init 필요 x)

## gitignore
> git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일
---
- 프로젝트에 따라 공유하지 않아야 하는 것도 존재하기 때문
- 이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 *적용되지 않음*
    - .gitignore 파일 생성
    - 공유하지 않을 파일 .gitignore에 추가

#### [gitignore 설정서비스]('https://www.toptal.com/developers/gitignore/')

<br>

## github 활용
- TIL(today i learned)을 통해 내가 학습하는 것을 기록
- 개인, 팀 프로젝트 코드를 공유
- 오픈 소스 프로젝트에 기여

<br>

## README.md
- 프로젝트에 대한 설명, 사용방법, 문서화된 정보 등을 포함하는 역할
- Markdown 형식으로 작성되며, 프로젝트 사용자, 개발자, 혹은 기여자들에게 프로젝트에 대한 전반적인 이해와 활용 방법을 제공하는데 사용