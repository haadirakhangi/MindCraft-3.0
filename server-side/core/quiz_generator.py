from api.gemini_client import GeminiProvider
from api.tavily_client import TavilyProvider

class QuizGenerator:
    def __init__(self):
        self.gemini_client = GeminiProvider()
        self.tavily_client = TavilyProvider()

    def generate_quiz(self, sub_modules):
        quiz_prompt = """As an educational chatbot named ISSAC, your task is to create a set of 10 theoretical quiz questions \
    with multiple-choice options that should cover all the sub-modules. The questions should be theoretical-based and difficult to \
    efficiently test the theoretical knowledge of the student. \
    Ensure that the output is a valid JSON format, with a single 'quizData' which is a list of dictionaries structured as follows:
    ```
    "question": "The question here",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "correct_option": "The correct option string here."
    "explanation": "Explanation for Question 1"

    ...[and so on]
    ```

    Create a set of 10 quiz questions following the above-mentioned format.
    ```
    Sub Modules : {sub_modules}
    ```
    """
        
        output = self.gemini_client.generate_json_response(quiz_prompt.format(sub_modules = sub_modules))
        return output
    
    def generate_quiz_from_web(self, sub_modules):
        search_result = self.tavily_client.search_context(','.join(sub_modules[:4]))

        quiz_prompt_for_web = """As an educational chatbot named ISAAC, your task is to create a set of 10 theoretical quiz questions \
    with multiple-choice options that should cover all the sub-modules. You will be given information from the internet related to the sub-modules. \
    Use this information to create the quiz questions. The questions should be theoretical-based and difficult to \
    efficiently test the theoretical knowledge of the student. \

    Sub Modules : {sub_modules}

    Search Result = {search_result}


    Ensure that the output is a valid JSON format, with a single 'quizData' which is a list of dictionaries structured as follows:
    ```
    "question": "The question here",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "correct_option": "The correct option string here."
    "explanation": "Explanation for Question 1"

    ...[and so on]
    ```

    Create a set of 10 quiz questions following the above-mentioned format.

    """
        
        output = self.gemini_client.generate_json_response(quiz_prompt_for_web.format(sub_modules = sub_modules, search_result = search_result))
        return output
    
    def generate_applied_quiz(self, sub_modules):
        quiz_prompt = """As an educational chatbot named ISSAC, your task is to create a set of 10 creative and application-based quiz questions with multiple-choice options that should be based on the sub-modules as well as any related sub-topic. Create questions in a scenario-based manner like the ones in a word problem or applied problems (starting with 'suppose...', 'imagine...', 'if...' or 'let's say...') to efficiently test the understanding of concepts and principles to solve real-world or hypothetical situations based on the sub modules. The questions should be descriptive and lengthy to give a complete scenario to the student. Ensure that the output is a valid JSON format, with a single 'quizData' which is a list of dictionaries structured as follows:
    ```
    "question": "The question here",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "correct_option": "The correct option string here."
    "explanation": "Explanation for Question 1"

    ...[and so on]
    ```

    Create a set of 10 quiz questions that are in the described manner and follow the above-mentioned format.

    Sub Modules : {sub_modules}
    """
        
        output = self.gemini_client.generate_json_response(quiz_prompt.format(sub_modules = sub_modules))
        return output

    def generate_applied_quiz_from_web(self, sub_modules):
        search_result = self.tavily_client.search_context(','.join(sub_modules[:4]))
        quiz_prompt_for_web = """
        As an educational chatbot named ISAAC, your task is to create a diverse set of 10 creative and application-based quiz questions with multiple-choice options that should be based on the sub-modules. You will be given information from the internet related to the sub-modules.
    Use this information to create the quiz questions.

    Sub Modules : {sub_modules}

    Search Result = ```{search_result}```


    Create questions in a scenario-based manner like the ones in a word problem or applied problems
    to efficiently test the understanding of concepts and principles to solve real-world or hypothetical situations based on the sub modules. The questions should be descriptive and should provide hypothetical scenarios to give a complete scenario to the student. Ensure that the output is a valid JSON format, with a single 'quizData' which is a list of dictionaries structured as follows:
    ```
    "question": "The question here",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "correct_option": "The correct option string here."
    "explanation": "Explanation for Question 1"

    ...[and so on]
    ```

    Create a set of 10 questions that follow the described manner and the above-mentioned format.
    """

        output = self.gemini_client.generate_json_response(quiz_prompt_for_web.format(sub_modules = sub_modules, search_result = search_result))
        return output

    def generate_conversation_quiz(self, sub_modules):
        quiz_prompt = """You are an educational examiner and your task is to ask various conceptual questions to a student(asking them to explain or elaborate their answers) based on the specified list of topics. Imagine as if you are talking to the student while asking the questions. Ensure that the output is a valid JSON format, with the keys being the question number and values being the questions.

    Create a set of 1 concept-based quiz questions in the above-mentioned format.
    ```
    Sub Modules : {sub_modules}
    ```
    """

        output = self.gemini_client.generate_json_response(quiz_prompt.format(sub_modules = sub_modules))
        output_list = list(output.values())
        return output_list

    def generate_conversation_quiz_from_web(self, sub_modules):
        search_result = self.tavily_client.search_context(','.join(sub_modules[:4]), search_depth="advanced", max_tokens=4000)
        quiz_prompt = """You are an educational examiner and your task is to ask various conceptual questions to a student (asking them to explain or elaborate their answers) based on the specified list of topics. Imagine as if you are talking to the student while asking the questions. You will be given information from the internet related to the sub-modules. Use this information to create the questions.

    Sub Modules : ```{sub_modules}```

    Search Result = ```{search_result}```

    Ensure that the output is a valid JSON format, with the keys being the question number and values being the questions.

    Create a set of 1 concept-based quiz questions in the above-mentioned format.

    """
        
        output = self.gemini_client.generate_json_response(quiz_prompt.format(sub_modules = sub_modules, search_result = search_result))
        output_list = list(output.values())
        return output_list
