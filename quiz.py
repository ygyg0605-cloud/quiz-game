class Quiz:
    """개별 퀴즈를 표현하는 클래스"""
    
    def __init__(self, question, choices, answer, hint=None):
        """
        Args:
            question (str): 문제
            choices (list): 선택지 4개 ['①번', '②번', '③번', '④번']
            answer (int): 정답 (1~4)
            hint (str): 힌트 (선택사항)
        """
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
    
    def display(self):
        """퀴즈를 화면에 출력"""
        print(f"\n📝 {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")
    
    def is_correct(self, user_answer):
        """사용자 정답 확인"""
        return user_answer == self.answer
    
    def to_dict(self):
        """JSON 저장용 딕셔너리로 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }
    
    @staticmethod
    def from_dict(data):
        """딕셔너리에서 Quiz 객체 생성"""
        return Quiz(
            data["question"],
            data["choices"],
            data["answer"],
            data.get("hint")
        )

# 기본 퀴즈 데이터 (예: 파이썬 주제)
DEFAULT_QUIZZES = [
    Quiz(
        "Python에서 리스트와 튜플의 가장 큰 차이는?",
        ["리스트는 변경 가능, 튜플은 불변", "튜플이 더 빠르다", "리스트만 반복문 사용 가능", "차이가 없다"],
        1,
        "변경 가능성(mutability)을 생각해보세요"
    ),
    Quiz(
        "다음 중 딕셔너리의 키로 사용할 수 없는 것은?",
        ["문자열", "숫자", "리스트", "튜플"],
        3,
        "변경 불가능한 타입만 키가 될 수 있습니다"
    ),
    Quiz(
        "for 루프에서 break의 역할은?",
        ["루프를 건너뛴다", "루프를 즉시 종료한다", "함수를 종료한다", "조건을 다시 확인한다"],
        2,
        "루프 탈출을 생각해보세요"
    ),
    Quiz(
        "클래스에서 __init__ 메서드의 역할은?",
        ["객체를 삭제한다", "객체를 초기화한다", "메서드를 정의한다", "상속을 처리한다"],
        2,
        "객체 생성 시 가장 먼저 실행되는 메서드입니다"
    ),
    Quiz(
        "JSON 파일의 주요 장점은?",
        ["매우 빠르다", "사람이 읽기 쉽고 언어 간 호환성이 좋다", "보안이 뛰어나다", "용량이 작다"],
        2,
        "데이터 교환 형식으로 널리 사용됩니다"
    ),
]
