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
