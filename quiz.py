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
