from api.openai_client import OpenAIProvider
from api.tavily_client import TavilyProvider

class RecommendationGenerator:
    def __init__(self):
        self.openai_client = OpenAIProvider()

    def generate_recommendations(self, user_course, user_interest, past_module_names = None):
        recc_prompt = '''You will be given a student's area of interest, the current course the student is enrolled in and MAYBE the past module names that the user has completed. Your task is to suggest or recommend similar courses for the student. Generate 10 module names along with their summary. The past module names might or might not be given. If it's not given or not understandable ignore it completely. However, if it is clearly given then give more priority to the past module names while generating the recommendations. The output should be in json format where each key corresponds to the recommended course name and the value is a short description about the recommeded course.
        Student's Current Course: {user_course}
        Student's Interests: {user_interest}
        Student's Past Module Names: {past_module_names}

        Example output:
        ```json
        course name here : course summary here
        ```
        '''
        
        output = self.openai_client.generate_json_response(recc_prompt.format(user_course = user_course, user_interest=user_interest, past_module_names=past_module_names))
        return output