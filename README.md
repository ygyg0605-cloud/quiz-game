# 🎮 Python 퀴즈 게임

## 📌 프로젝트 개요
Python 기초 문법을 학습하기 위한 터미널 기반 퀴즈 게임입니다.
퀴즈를 풀고, 새로운 퀴즈를 추가하며, 최고 점수를 기록할 수 있습니다.

## 🎯 퀴즈 주제: Python 기초
### 선정 이유
- Python 초보자가 자주 헷갈리는 개념들을 다룸
- 변수, 자료구조, 제어문, 클래스 등 핵심 개념 포함
- 실무에서 자주 사용되는 JSON 파일 저장 경험

## 🚀 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/ygyg0605-cloud/quiz-game.git
cd quiz-game
## 추가 정부

dbsrl02051922@c6r2s6 git.dir % git commit -m "Initial commit"
[main (root-commit) ba6e0f1] Initial commit
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 txt1
 create mode 100644 txt2
 create mode 100644 txt3
dbsrl02051922@c6r2s6 git.dir % vi txt1
dbsrl02051922@c6r2s6 git.dir % clear

dbsrl02051922@c6r2s6 git.dir % cd ..
dbsrl02051922@c6r2s6 ~ % ls
Desktop		Documents	Downloads	Library		Movies		Music		OrbStack	Pictures	Public		git.dir
dbsrl02051922@c6r2s6 ~ % rmd git.dir
zsh: command not found: rmd
dbsrl02051922@c6r2s6 ~ % rm git.dir
rm: git.dir: is a directory
dbsrl02051922@c6r2s6 ~ % rm -r git.dir
override r--r--r-- dbsrl02051922/dbsrl02051922 for git.dir/.git/objects/ba/6e0f1ad310f7108bf41281c2f605837dc02a44? y 
override r--r--r-- dbsrl02051922/dbsrl02051922 for git.dir/.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391? Yest
override r--r--r-- dbsrl02051922/dbsrl02051922 for git.dir/.git/objects/77/13ec96c3df2d8990afcd30d70df54a5fb1dda1? Yes
dbsrl02051922@c6r2s6 ~ % ls
Desktop		Documents	Downloads	Library		Movies		Music		OrbStack	Pictures	Public
dbsrl02051922@c6r2s6 ~ % mkdir quiz-game
dbsrl02051922@c6r2s6 ~ % cd quiz-game
dbsrl02051922@c6r2s6 quiz-game % nano .gitignore
dbsrl02051922@c6r2s6 quiz-game % git init 
Initialized empty Git repository in /Users/dbsrl02051922/quiz-game/.git/
dbsrl02051922@c6r2s6 quiz-game % git add .
dbsrl02051922@c6r2s6 quiz-game % git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   .gitignore

dbsrl02051922@c6r2s6 quiz-game % git commit -m "Init: 프로젝트 초기 설정"
[main (root-commit) fcd970f] Init: 프로젝트 초기 설정
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 5 insertions(+)
 create mode 100644 .gitignore
dbsrl02051922@c6r2s6 quiz-game % git remote add origin https://github.com/ygyg0605/quiz-game.git
dbsrl02051922@c6r2s6 quiz-game % git branch -M main
dbsrl02051922@c6r2s6 quiz-game % git push -u origin main\
> 
Username for 'https://github.com': ygyg0605
Password for 'https://ygyg0605@github.com': 
remote: Repository not found.
fatal: repository 'https://github.com/ygyg0605/quiz-game.git/' not found
dbsrl02051922@c6r2s6 quiz-game % git remote add origin https://github.com/ygyg0605-cloud/quiz-game.git
error: remote origin already exists.
dbsrl02051922@c6r2s6 quiz-game % git remote rm origin
dbsrl02051922@c6r2s6 quiz-game % git remote add origin https://github.com/ygyg0605-cloud/quiz-game.git
dbsrl02051922@c6r2s6 quiz-game % git branch -M main                                                   
dbsrl02051922@c6r2s6 quiz-game % git push -u origin main                                              
Username for 'https://github.com': ygyg0605
Password for 'https://ygyg0605@github.com': 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 292 bytes | 292.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/ygyg0605-cloud/quiz-game.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
dbsrl02051922@c6r2s6 quiz-game % nano quiz.py
dbsrl02051922@c6r2s6 quiz-game % git add quiz.py
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Feat: Quiz 클래스 구현"
[main 15eaae5] Feat: Quiz 클래스 구현
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 44 insertions(+)
 create mode 100644 quiz.py
dbsrl02051922@c6r2s6 quiz-game % nano quiz.py
dbsrl02051922@c6r2s6 quiz-game % nano quiz.py
dbsrl02051922@c6r2s6 quiz-game % git add quiz.py                       
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Feat: 기본 퀴즈 데이터 5개 작성 (Python 주제)"
[main 6db3377] Feat: 기본 퀴즈 데이터 5개 작성 (Python 주제)
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 34 insertions(+)
dbsrl02051922@c6r2s6 quiz-game % nano quiz_game.py
dbsrl02051922@c6r2s6 quiz-game % git add quiz.py                                              
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Feat: QuizGame 클래스 구현 (메뉴/풀기/추가/목록/점수)"
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	quiz_game.py

nothing added to commit but untracked files present (use "git add" to track)
dbsrl02051922@c6r2s6 quiz-game % git add quiz_game.py                                                 
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Feat: QuizGame 클래스 구현 (메뉴/풀기/추가/목록/점수)"
[main 2bf4fdc] Feat: QuizGame 클래스 구현 (메뉴/풀기/추가/목록/점수)
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 207 insertions(+)
 create mode 100644 quiz_game.py
dbsrl02051922@c6r2s6 quiz-game % nano main.py
dbsrl02051922@c6r2s6 quiz-game % python main.py

========================================
🎮 퀴즈 게임에 오신 것을 환영합니다!
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 종료
========================================

선택 (1-5): 1

📚 총 5개의 퀴즈를 풀어보세요!

📝 Python에서 리스트와 튜플의 가장 큰 차이는?
  1. 리스트는 변경 가능, 튜플은 불변
  2. 튜플이 더 빠르다
  3. 리스트만 반복문 사용 가능
  4. 차이가 없다
정답 (1-4): 1
✅ 정답입니다!

📝 다음 중 딕셔너리의 키로 사용할 수 없는 것은?
  1. 문자열
  2. 숫자
  3. 리스트
  4. 튜플
정답 (1-4): 4
❌ 오답입니다. 정답은 3번입니다.

📝 for 루프에서 break의 역할은?
  1. 루프를 건너뛴다
  2. 루프를 즉시 종료한다
  3. 함수를 종료한다
  4. 조건을 다시 확인한다
정답 (1-4): 2
✅ 정답입니다!

📝 클래스에서 __init__ 메서드의 역할은?
  1. 객체를 삭제한다
  2. 객체를 초기화한다
  3. 메서드를 정의한다
  4. 상속을 처리한다
정답 (1-4): 2
✅ 정답입니다!

📝 JSON 파일의 주요 장점은?
  1. 매우 빠르다
  2. 사람이 읽기 쉽고 언어 간 호환성이 좋다
  3. 보안이 뛰어나다
  4. 용량이 작다
정답 (1-4): 1
❌ 오답입니다. 정답은 2번입니다.

========================================
🎉 게임 종료!
점수: 3/5 (60.0%)
========================================
🏆 새로운 최고 점수입니다!

========================================
🎮 퀴즈 게임에 오신 것을 환영합니다!
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 종료
========================================

선택 (1-5): 4

🏆 최고 점수: 3점

========================================
🎮 퀴즈 게임에 오신 것을 환영합니다!
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 종료
========================================

선택 (1-5): 5
💾 데이터가 저장되었습니다.
dbsrl02051922@c6r2s6 quiz-game % git add main.py
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Feat: main.py 진입점 작성"
[main bd85c72] Feat: main.py 진입점 작성
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 9 insertions(+)
 create mode 100644 main.py
dbsrl02051922@c6r2s6 quiz-game % git checkout -b feature/random-quiz
Switched to a new branch 'feature/random-quiz'
dbsrl02051922@c6r2s6 quiz-game % nano quiz_game.py
dbsrl02051922@c6r2s6 quiz-game % python main.py
✅ 저장된 데이터를 불러왔습니다.

========================================
🎮 퀴즈 게임에 오신 것을 환영합니다!
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 종료
========================================

선택 (1-5): 1

📚 총 5개의 퀴즈를 풀어보세요!

📝 Python에서 리스트와 튜플의 가장 큰 차이는?
  1. 리스트는 변경 가능, 튜플은 불변
  2. 튜플이 더 빠르다
  3. 리스트만 반복문 사용 가능
  4. 차이가 없다
정답 (1-4): 1
✅ 정답입니니니니니다!

📝 다음 중 딕셔너리의 키로 사용할 수 없는 것은?
  1. 문자열
  2. 숫자
  3. 리스트
  4. 튜플
정답 (1-4): 3
✅ 정답입니니니니니다!

📝 for 루프에서 break의 역할은?
  1. 루프를 건너뛴다
  2. 루프를 즉시 종료한다
  3. 함수를 종료한다
  4. 조건을 다시 확인한다
정답 (1-4): 2
✅ 정답입니니니니니다!

📝 클래스에서 __init__ 메서드의 역할은?
  1. 객체를 삭제한다
  2. 객체를 초기화한다
  3. 메서드를 정의한다
  4. 상속을 처리한다
정답 (1-4): 2
✅ 정답입니니니니니다!

📝 JSON 파일의 주요 장점은?
  1. 매우 빠르다
  2. 사람이 읽기 쉽고 언어 간 호환성이 좋다
  3. 보안이 뛰어나다
  4. 용량이 작다
정답 (1-4): 2
✅ 정답입니니니니니다!

========================================
🎉 게임 종료!
점수: 5/5 (100.0%)
========================================
🏆 새로운 최고 점수입니다!

========================================
🎮 퀴즈 게임에 오신 것을 환영합니다!
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 종료
========================================

선택 (1-5): 5
💾 데이터가 저장되었습니다.
dbsrl02051922@c6r2s6 quiz-game % git add quiz_game.py
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Feat: 퀴즈 정답 표현 변경"
[feature/random-quiz 528f147] Feat: 퀴즈 정답 표현 변경
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
dbsrl02051922@c6r2s6 quiz-game % git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)
dbsrl02051922@c6r2s6 quiz-game % nano quiz_game.py                        
dbsrl02051922@c6r2s6 quiz-game % git branch
  feature/random-quiz
* main
dbsrl02051922@c6r2s6 quiz-game % git branch list
dbsrl02051922@c6r2s6 quiz-game % git branchlist
git: 'branchlist' is not a git command. See 'git --help'.
dbsrl02051922@c6r2s6 quiz-game % git list
git: 'list' is not a git command. See 'git --help'.

The most similar commands are
	bisect
	rev-list
dbsrl02051922@c6r2s6 quiz-game % git rev-list
usage: git rev-list [<options>] <commit>... [--] [<path>...]

  limiting output:
    --max-count=<n>
    --max-age=<epoch>
    --min-age=<epoch>
    --sparse
    --no-merges
    --min-parents=<n>
    --no-min-parents
    --max-parents=<n>
    --no-max-parents
    --remove-empty
    --all
    --branches
    --tags
    --remotes
    --stdin
    --exclude-hidden=[fetch|receive|uploadpack]
    --quiet
  ordering output:
    --topo-order
    --date-order
    --reverse
  formatting output:
    --parents
    --children
    --objects | --objects-edge
    --disk-usage[=human]
    --unpacked
    --header | --pretty
    --[no-]object-names
    --abbrev=<n> | --no-abbrev
    --abbrev-commit
    --left-right
    --count
    -z
  special purpose:
    --bisect
    --bisect-vars
    --bisect-all
dbsrl02051922@c6r2s6 quiz-game % git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   restore    Restore working tree files
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   diff       Show changes between commits, commit and working tree, etc
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   backfill   Download missing objects in a partial clone
   branch     List, create, or delete branches
   commit     Record changes to the repository
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   reset      Set `HEAD` or the index to a known state
   switch     Switch branches
   tag        Create, list, delete or verify tags

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
dbsrl02051922@c6r2s6 quiz-game % git merge feature/random-quiz
Updating bd85c72..528f147
Fast-forward
 quiz_game.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
dbsrl02051922@c6r2s6 quiz-game % nano quiz_game.py            
dbsrl02051922@c6r2s6 quiz-game % git branch -d feature/random-quiz
Deleted branch feature/random-quiz (was 528f147).
dbsrl02051922@c6r2s6 quiz-game % git branch
  list
* main
dbsrl02051922@c6r2s6 quiz-game % git add RAEDME.md
fatal: pathspec 'RAEDME.md' did not match any files
dbsrl02051922@c6r2s6 quiz-game % nano README.md
dbsrl02051922@c6r2s6 quiz-game % git add RAEDME.md
fatal: pathspec 'RAEDME.md' did not match any files
dbsrl02051922@c6r2s6 quiz-game % git add README.md
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Docs: README.md 작성 완료"
[main 92edb1c] Docs: README.md 작성 완료
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 18 insertions(+)
 create mode 100644 README.md
dbsrl02051922@c6r2s6 quiz-game % git push origin main
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 6 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (18/18), 5.31 KiB | 5.31 MiB/s, done.
Total 18 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (6/6), done.
To https://github.com/ygyg0605-cloud/quiz-game.git
   fcd970f..92edb1c  main -> main
dbsrl02051922@c6r2s6 quiz-game % cd ..
dbsrl02051922@c6r2s6 ~ % cd quiz-game         
dbsrl02051922@c6r2s6 quiz-game % nano README.md                           
dbsrl02051922@c6r2s6 quiz-game % git add RAEDME.md                        
fatal: pathspec 'RAEDME.md' did not match any files
dbsrl02051922@c6r2s6 quiz-game % git add README.md
dbsrl02051922@c6r2s6 quiz-game % git commit -m "Docs: README.md 작성 완료"
[main 91c0aa3] Docs: README.md 작성 완료
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+), 1 deletion(-)
dbsrl02051922@c6r2s6 quiz-game % git push origin main                     
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 360 bytes | 360.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/ygyg0605-cloud/quiz-game.git
   92edb1c..91c0aa3  main -> main
dbsrl02051922@c6r2s6 quiz-game % cd ..                                    
dbsrl02051922@c6r2s6 ~ % git clone https://github.com/ygyg0605-cloud/quiz-game.git quiz-game-clone
Cloning into 'quiz-game-clone'...
remote: Enumerating objects: 24, done.
remote: Counting objects: 100% (24/24), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 24 (delta 8), reused 24 (delta 8), pack-reused 0 (from 0)
Receiving objects: 100% (24/24), 5.84 KiB | 5.84 MiB/s, done.
Resolving deltas: 100% (8/8), done.
dbsrl02051922@c6r2s6 ~ % cd quiz-game-clone
dbsrl02051922@c6r2s6 quiz-game-clone % ls
README.md	main.py		quiz.py		quiz_game.py
dbsrl02051922@c6r2s6 quiz-game-clone % cat quiz_game.py
import json
import os
from quiz import Quiz, DEFAULT_QUIZZES

class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""
    
    STATE_FILE = "state.json"
    
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_state()
    
    def load_state(self):
        """state.json에서 데이터 불러오기"""
        try:
            if os.path.exists(self.STATE_FILE):
                with open(self.STATE_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                    self.best_score = data.get("best_score", 0)
                    print("✅ 저장된 데이터를 불러왔습니다.")
            else:
                self._use_default_quizzes()
        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self._use_default_quizzes()
    
    def _use_default_quizzes(self):
        """기본 퀴즈 데이터 사용"""
        self.quizzes = DEFAULT_QUIZZES.copy()
        self.best_score = 0
    
    def save_state(self):
        """state.json에 데이터 저장"""
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(self.STATE_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("💾 데이터가 저장되었습니다.")
        except IOError as e:
            print(f"❌ 저장 실패: {e}")
    
    def display_menu(self):
        """메인 메뉴 표시"""
        print("\n" + "="*40)
        print("🎮 퀴즈 게임에 오신 것을 환영합니다!")
        print("="*40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("="*40)
    
    def get_menu_choice(self):
        """메뉴 선택 입력받기"""
        while True:
            try:
                choice = input("\n선택 (1-5): ").strip()
                if not choice:
                    print("❌ 입력이 비어있습니다. 다시 입력하세요.")
                    continue
                choice = int(choice)
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("❌ 1~5 사이의 숫자를 입력하세요.")
            except ValueError:
                print("❌ 숫자를 입력하세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n\n프로그램을 종료합니다...")
                self.save_state()
                exit()
    
    def play_quiz(self):
        """퀴즈 풀기"""
        if not self.quizzes:
            print("❌ 등록된 퀴즈가 없습니다.")
            return
        
        score = 0
        total = len(self.quizzes)
        
        print(f"\n📚 총 {total}개의 퀴즈를 풀어보세요!")
        
        for idx, quiz in enumerate(self.quizzes, 1):
            quiz.display()
            
            while True:
                try:
                    answer = input(f"정답 (1-4): ").strip()
                    if not answer:
                        print("❌ 입력이 비어있습니다.")
                        continue
                    answer = int(answer)
                    if 1 <= answer <= 4:
                        break
                    else:
                        print("❌ 1~4 사이의 숫자를 입력하세요.")
                except ValueError:
                    print("❌ 숫자를 입력하세요.")
                except (KeyboardInterrupt, EOFError):
                    print("\n\n게임을 중단합니다...")
                    self.save_state()
                    exit()
            
            if quiz.is_correct(answer):
                print("✅ 정답입니니니니니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")
        
        # 결과 표시
        percentage = (score / total) * 100
        print(f"\n{'='*40}")
        print(f"🎉 게임 종료!")
        print(f"점수: {score}/{total} ({percentage:.1f}%)")
        print(f"{'='*40}")
        
        # 최고 점수 갱신
        if score > self.best_score:
            self.best_score = score
            print(f"🏆 새로운 최고 점수입니다!")
    
    def add_quiz(self):
        """퀴즈 추가"""
        print("\n📝 새로운 퀴즈를 추가합니다.")
        
        try:
            question = input("문제: ").strip()
            if not question:
                print("❌ 문제를 입력하세요.")
                return
            
            choices = []
            for i in range(1, 5):
                choice = input(f"선택지 {i}: ").strip()
                if not choice:
                    print("❌ 모든 선택지를 입력하세요.")
                    return
                choices.append(choice)
            
            while True:
                try:
                    answer = input("정답 번호 (1-4): ").strip()
                    if not answer:
                        print("❌ 입력이 비어있습니다.")
                        continue
                    answer = int(answer)
                    if 1 <= answer <= 4:
                        break
                    else:
                        print("❌ 1~4 사이의 숫자를 입력하세요.")
                except ValueError:
                    print("❌ 숫자를 입력하세요.")
            
            new_quiz = Quiz(question, choices, answer)
            self.quizzes.append(new_quiz)
            print("✅ 퀴즈가 추가되었습니다.")
            self.save_state()
        
        except (KeyboardInterrupt, EOFError):
            print("\n\n입력을 취소합니다...")
            self.save_state()
            exit()
    
    def show_quizzes(self):
        """퀴즈 목록 보기"""
        if not self.quizzes:
            print("❌ 등록된 퀴즈가 없습니다.")
            return
        
        print(f"\n📚 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("="*50)
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"{idx}. {quiz.question}")
        print("="*50)
    
    def show_best_score(self):
        """최고 점수 확인"""
        if self.best_score == 0:
            print("❌ 아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점")
    
    def run(self):
        """게임 실행"""
        while True:
            self.display_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quizzes()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                self.save_state()
                break
dbsrl02051922@c6r2s6 quiz-game-clone % echo "## 추가 정부" >> README.md
dbsrl02051922@c6r2s6 quiz-game-clone % git add README.md
dbsrl02051922@c6r2s6 quiz-game-clone % git commit -m "Docs: README에 추가 정보 작성"
[main 23e4eea] Docs: README에 추가 정보 작성
 Committer: ygyg0605 <dbsrl02051922@c6r2s6.codyssey.kr>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
dbsrl02051922@c6r2s6 quiz-game-clone % git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 6 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 353 bytes | 353.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/ygyg0605-cloud/quiz-game.git
   91c0aa3..23e4eea  main -> main
dbsrl02051922@c6r2s6 quiz-game-clone % cd ../quiz-game
dbsrl02051922@c6r2s6 quiz-game % git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 333 bytes | 111.00 KiB/s, done.
From https://github.com/ygyg0605-cloud/quiz-game
 * branch            main       -> FETCH_HEAD
   91c0aa3..23e4eea  main       -> origin/main
Updating 91c0aa3..23e4eea
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
dbsrl02051922@c6r2s6 quiz-game % git log --online
fatal: unrecognized argument: --online
dbsrl02051922@c6r2s6 quiz-game % git log --oneline
23e4eea (HEAD -> main, origin/main) Docs: README에 추가 정보 작성
91c0aa3 Docs: README.md 작성 완료
92edb1c Docs: README.md 작성 완료
528f147 Feat: 퀴즈 정답 표현 변경
bd85c72 (list) Feat: main.py 진입점 작성
2bf4fdc Feat: QuizGame 클래스 구현 (메뉴/풀기/추가/목록/점수)
6db3377 Feat: 기본 퀴즈 데이터 5개 작성 (Python 주제)
15eaae5 Feat: Quiz 클래스 구현
fcd970f Init: 프로젝트 초기 설정
dbsrl02051922@c6r2s6 quiz-game % git branch       
  list
* main
dbsrl02051922@c6r2s6 quiz-game % git go 23e4eea
git: 'go' is not a git command. See 'git --help'.

The most similar command is
	log
dbsrl02051922@c6r2s6 quiz-game % git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   restore    Restore working tree files
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   diff       Show changes between commits, commit and working tree, etc
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   backfill   Download missing objects in a partial clone
   branch     List, create, or delete branches
   commit     Record changes to the repository
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   reset      Set `HEAD` or the index to a known state
   switch     Switch branches
   tag        Create, list, delete or verify tags

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
dbsrl02051922@c6r2s6 quiz-game % git clone https://github.com/ygyg0605-cloud/quiz-game.git
cd quiz-game
Cloning into 'quiz-game'...
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 27 (delta 10), reused 25 (delta 8), pack-reused 0 (from 0)
Receiving objects: 100% (27/27), 6.11 KiB | 6.11 MiB/s, done.
Resolving deltas: 100% (10/10), done.
dbsrl02051922@c6r2s6 quiz-game % python main.py

========================================
🎮 퀴즈 게임에 오신 것을 환영합니다!
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 종료
========================================

선택 (1-5): 1

📚 총 5개의 퀴즈를 풀어보세요!

📝 Python에서 리스트와 튜플의 가장 큰 차이는?
  1. 리스트는 변경 가능, 튜플은 불변
  2. 튜플이 더 빠르다
  3. 리스트만 반복문 사용 가능
  4. 차이가 없다
정답 (1-4): 2
❌ 오답입니다. 정답은 1번입니다.

📝 다음 중 딕셔너리의 키로 사용할 수 없는 것은?
  1. 문자열
  2. 숫자
  3. 리스트
  4. 튜플
정답 (1-4): 3
✅ 정답입니니니니니다!

📝 for 루프에서 break의 역할은?
  1. 루프를 건너뛴다
  2. 루프를 즉시 종료한다
  3. 함수를 종료한다
  4. 조건을 다시 확인한다
정답 (1-4): 2
✅ 정답입니니니니니다!

📝 클래스에서 __init__ 메서드의 역할은?
  1. 객체를 삭제한다
  2. 객체를 초기화한다
  3. 메서드를 정의한다
  4. 상속을 처리한다
정답 (1-4): 2
✅ 정답입니니니니니다!

📝 JSON 파일의 주요 장점은?
  1. 매우 빠르다
  2. 사람이 읽기 쉽고 언어 간 호환성이 좋다
  3. 보안이 뛰어나다
  4. 용량이 작다
정답 (1-4): 2
✅ 정답입니니니니니다!

========================================
🎉 게임 종료!
점수: 4/5 (80.0%)
========================================
🏆 새로운 최고 점수입니다!

========================================
🎮 퀴즈 게임에 오신 것을 환영합니다!
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 최고 점수 확인
5. 종료
========================================

선택 (1-5): 
