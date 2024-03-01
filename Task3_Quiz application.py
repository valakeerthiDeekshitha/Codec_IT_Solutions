class Quiz:
    def __init__(self):
        self.questions = {
            'General Knowledge': [
                {
                    'question': 'What is the capital of France?',
                    'options': ['London', 'Paris', 'Berlin', 'Madrid'],
                    'answer': 'Paris'
                },
                {
                    'question': 'What is the largest planet in the solar system?',
                    'options': ['Jupiter', 'Saturn', 'Mars', 'Earth'],
                    'answer': 'Jupiter'
                }
            ],
            'Science': [
                {
                    'question': 'What is the powerhouse of the cell?',
                    'options': ['Nucleus', 'Mitochondria', 'Chloroplast', 'Ribosome'],
                    'answer': 'Mitochondria'
                },
                {
                    'question': 'What is the chemical symbol for water?',
                    'options': ['Wo', 'Wa', 'Wt', 'H2O'],
                    'answer': 'H2O'
                }
            ]
        }
        self.score = 0

    def display_categories(self):
        print("Available quiz categories:")
        for category in self.questions.keys():
            print("- " + category)

    def display_questions(self, category):
        if category in self.questions:
            print(f"\n{category} Quiz:")
            for i, q in enumerate(self.questions[category]):
                print(f"\n{i + 1}. {q['question']}")
                for j, option in enumerate(q['options']):
                    print(f"   {j + 1}. {option}")
                answer = input("Your answer: ")
                if q['options'][int(answer) - 1] == q['answer']:
                    self.score += 1
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is: {q['answer']}")
            print(f"\nYour score for {category} quiz: {self.score}/{len(self.questions[category])}")
        else:
            print("Invalid category.")

    def take_quiz(self):
        self.display_categories()
        category = input("\nChoose a quiz category: ")
        self.display_questions(category)


quiz = Quiz()
quiz.take_quiz()
